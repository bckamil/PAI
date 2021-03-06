# Generated by Django 3.0.5 on 2020-05-21 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournament',
            name='participants',
            field=models.ManyToManyField(related_name='user_tournament', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SponsorLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.BooleanField(blank=True, default=None, null=True)),
                ('tournament_level', models.IntegerField()),
                ('next_match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Match')),
                ('player_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_2', to=settings.AUTH_USER_MODEL)),
                ('player_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='player_1', to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
