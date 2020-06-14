import datetime

from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import filters, generics, status, views, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from tournaments.models import Application, Match, Tournament
from tournaments.permissions import ObjectOwnerUpdate
from tournaments.serializers import (ApplicationSerializer, MatchSerializer,
                                     TournamentDetailsSerializer,
                                     TournamentSerializer, UserSerializer)
from tournaments.tokens import account_activation_token


class TournamentListCreateView(generics.ListCreateAPIView):
    queryset = Tournament.objects.filter(datetime__gte=datetime.datetime.now())
    serializer_class = TournamentDetailsSerializer
    permissios = (IsAuthenticatedOrReadOnly,)
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TournamentDetailsView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Tournament.objects.all()
    serializer_class = TournamentDetailsSerializer


class TournamentUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permissions = (ObjectOwnerUpdate,)


class UserTournamentsListView(generics.ListAPIView):
    serializer_class = TournamentSerializer
    permissions = (IsAuthenticated,)

    def get_queryset(self):
        applications = Application.objects.values_list(
            'tournament_application')

        return Tournament.objects.filter(pk__in=applications).order_by('-datetime')


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    permissions = (IsAuthenticated,)
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            tournament = serializer.validated_data['tournament_application']
            applications = Application.objects.filter(
                tournament_application=tournament
            )
            if len(applications) <= tournament.limit:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)

                return Response(serializer.data, status=201, headers=headers)
            else:
                return Response({'msg': 'Tournament is full'}, status=status.HTTP_400_BAD_REQUEST)


class MatchWinnerView(views.APIView):
    def put(self, request, pk, format=None):
        match = get_object_or_404(Match, pk=pk)
        winner = get_object_or_404(User, pk=request.data['winner'])

        if not match.accept:
            if match.winner:
                if match.winner == winner:
                    match.accept = True
                    next_match = match.next_match
                    if next_match.player_1 is None:
                        next_match.player_1 = winner
                    else:
                        next_match.player_2 = winner
                        next_match.save()
                else:
                    match.winner = None
            else:
                match.winner = winner

            match.winner_set_by = request.user
            match.save()
            serializer = MatchSerializer(match)

            return Response(serializer.data)

        return Response({}, status=400)


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = (IsAuthenticated,)

    def get_object(self):
        self.kwargs['pk'] = self.request.user.pk

        return super(UserViewSet, self).get_object()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return Response(
            {'msg': 'Thank you for your email confirmation. Now you can login your account.'},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'msg': 'Activation link is invalid!'},
            status=status.HTTP_400_BAD_REQUEST
        )
