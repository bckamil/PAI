import datetime

import pytz
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from tournaments.models import Application, Match, Tournament
from tournaments.tokens import account_activation_token

utc = pytz.UTC


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('user',)


class MatchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class MatchSerializer(serializers.ModelSerializer):
    player_1 = MatchUserSerializer()
    player_2 = MatchUserSerializer()
    winner = MatchUserSerializer()

    class Meta:
        model = Match
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

    def validate(self, data):
        now = utc.localize(datetime.datetime.now())
        if data['datetime'] <= now:
            raise serializers.ValidationError("Start datetime must be greater than now")
        if data['deadline'] <= now:
            raise serializers.ValidationError("Deadline must be greater than now")
        if data['datetime'] > data['deadline']:
            raise serializers.ValidationError("Start date must occur after deadline")
        return data


class TournamentDetailsSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True, read_only=True, source='match_set')
    applications = ApplicationSerializer(many=True, read_only=True, source='application_set')

    class Meta:
        model = Tournament
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=False
        )

        mail_subject = 'Activate your blog account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': 'http://localhost:8080',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            mail_subject, message, to=[validated_data['email']]
        )
        email.send()

        user.set_password(validated_data['password'])
        user.save()

        return user


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)


class NewPasswordSerializer(serializers.Serializer):
    password_1 = serializers.CharField(required=True)
    password_2 = serializers.CharField(required=True)
