from django.shortcuts import render, redirect
from .models import Voter,Candidate,Vote

# Create your views here.
def index(request):
    return render(request, "index.html")

# --- Lista de los votantes---
def voter_list(request):
    voters = Voter.objects.all()
    return render(request, "voters/list.html", {"voters": voters})

# --- Registrar votante ---
def voter_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if Candidate.objects.filter(name=name).exists():
            return render(request, "voters/create.html", {"error": "Este nombre ya es candidato."})

        if Voter.objects.filter(email=email).exists():
            return render(request, "voters/create.html", {"error": "El correo ya existe."})

        Voter.objects.create(name=name, email=email)
        return redirect("voter_list")

    return render(request, "voters/create.html")

# --- Detalles de los votantes---
def voter_detail(request, id):
    voter = Voter.objects.get(id=id)
    return render(request, "voters/detail.html", {"voter": voter})

# --- Eliminar votante---
def voter_delete(request, id):
    voter = Voter.objects.get(id=id)
    voter.delete()
    return redirect("voter_list")


# --- Lista de candidatos---
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, "candidates/list.html", {"candidates": candidates})

# --- Registrar candidato ---
def candidate_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        party = request.POST.get("party")

        if Voter.objects.filter(name=name).exists():
            return render(request, "candidates/create.html", {"error": "Este nombre ya es un votante."})

        Candidate.objects.create(name=name, party=party)
        return redirect("candidate_list")

    return render(request, "candidates/create.html")

# --- Detalles del candidato ---
def candidate_detail(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, "candidates/detail.html", {"candidate": candidate})

# --- Eliminar candidato ---
def candidate_delete(request, id):
    candidate = Candidate.objects.get(id=id)
    candidate.delete()
    return redirect("candidate_list")

# --- Registrar un voto ---
def vote(request):
    voters = Voter.objects.filter(has_voted=False)
    candidates = Candidate.objects.all()

    if request.method == "POST":
        voter_id = request.POST.get("voter")
        candidate_id = request.POST.get("candidate")

        voter = Voter.objects.get(id=voter_id)
        candidate = Candidate.objects.get(id=candidate_id)

        if voter.has_voted:
            return render(request, "vote.html", {
                "error": "Este votante ya votó.",
                "voters": voters,
                "candidates": candidates,
            })

        Vote.objects.create(voter_id=voter, candidate_id=candidate)

        voter.has_voted = True
        voter.save()

        candidate.votes += 1
        candidate.save()

        return redirect("/")

    return render(request, "vote.html", {
        "voters": voters,
        "candidates": candidates,
    })


# --- Resultados ---

def results(request):


    total_votes = Vote.objects.count()

    voters_who_voted = Voter.objects.filter(has_voted=True).count()
    voters_who_did_not_vote = Voter.objects.filter(has_voted=False).count()
    total = voters_who_voted + voters_who_did_not_vote


    candidates = []
    for c in Candidate.objects.all():
        votes_for_candidate = Vote.objects.filter(candidate_id=c).count()
        percentage = (votes_for_candidate / total_votes * 100) if total_votes > 0 else 0

        candidates.append({
            "candidate": c,
            "votes": votes_for_candidate,
            "percentage": round(percentage, 2)
        })

    return render(request, "vote_results.html", {
        "total_votes": total_votes,
        "voters_who_voted": voters_who_voted,
        "total":total,
        "candidates": candidates
    })