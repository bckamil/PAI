# Generated by Django 3.0.5 on 2020-06-14 14:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0004_remove_tournament_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=64)),
                ('ranking', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('tournament_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
