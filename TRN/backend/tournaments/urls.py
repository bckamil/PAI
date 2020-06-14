from django.urls import path

from tournaments.views import (ApplicationCreateView, CreateUserView,
                               MatchWinnerView, TournamentDetailsView,
                               TournamentListCreateView, TournamentUpdateView,
                               UserTournamentsListView, UserViewSet, activate)

urlpatterns = [
    path('api/tournaments/', TournamentListCreateView.as_view(), name='tournaments'),
    path('api/tournaments/<int:id>',
         TournamentDetailsView.as_view(), name='tournament-details'),
    path('api/tournaments/<int:id>/update',
         TournamentUpdateView.as_view(), name='tournament-update'),
    path('api/tournaments/join/',
         ApplicationCreateView.as_view(), name='tournament-join'),
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/user/me/', UserViewSet.as_view({'get': 'retrieve'}), name='me'),
    path('api/tournamens/user/', UserTournamentsListView.as_view(),
         name='tournaments-user'),
    path('api/match/winner/<int:pk>',
         MatchWinnerView.as_view(), name='match-winner'),
    path('api/user/confirm/<str:uidb64>/<str:token>', activate, name='activate-account')
]
