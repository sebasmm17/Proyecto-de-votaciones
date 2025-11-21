from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),

    # VOTERS
    path("voters/", views.voter_list, name="voter_list"),
    path("voters/create/", views.voter_create, name="voter_create"),
    path("voters/<int:id>/", views.voter_detail, name="voter_detail"),
    path("voters/<int:id>/delete/", views.voter_delete, name="voter_delete"),

    # CANDIDATES
    path("candidates/", views.candidate_list, name="candidate_list"),
    path("candidates/create/", views.candidate_create, name="candidate_create"),
    path("candidates/<int:id>/", views.candidate_detail, name="candidate_detail"),
    path("candidates/<int:id>/delete/", views.candidate_delete, name="candidate_delete"),

    # VOTING
    path("vote/", views.vote, name="vote"),
    path("results/", views.results, name="vote_results"),
]