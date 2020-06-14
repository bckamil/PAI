import copy
import datetime
import math
import random

from tournaments.models import Application, Match, Tournament


def draw_ladder():
    now = datetime.datetime.now().replace(second=0, microsecond=0)
    tournaments = Tournament.objects.filter(deadline=now)
    for tournament in tournaments:
        tournament_ladder(tournament)


def tournament_ladder(tournament):
    applications = Application.objects.filter(tournament_application=tournament)
    applications = [x for x in applications]
    random.shuffle(applications)
    full_levels = int(math.sqrt(len(applications)))
    levels = full_levels + 1
    
    last_level_users_number = (len(applications) - (2 ** full_levels)) * 2
    last_level_users = applications[0:last_level_users_number]

    full_levels_users = applications[last_level_users_number:]
    full_levels_number = (len(applications) - last_level_users_number) / 2
    if not full_levels_number % 1 == 0 and full_levels != 0:
        full_levels_number += 1

    last_level = []
    this_level = []
    for i in range(full_levels):
        level = i + 1
        for x in range(2 ** i):
            next_match = None
            if len(last_level) > 0:
                next_match = last_level[x // 4]
            match = add_match(tournament, level, next_match)
            this_level.append(match)
        last_level = copy.deepcopy(this_level)
        this_level = []

    for i in range(last_level_users_number // 2):
        if len(last_level) > 0:
            next_match = last_level[i // 4]
        match = add_match(tournament, levels, next_match)

    last_level_matches = Match.objects.filter(tournament=tournament, tournament_level=levels)
    for index, match in enumerate(last_level_matches):
        i = index + 1
        players = last_level_users[i*2-2:i*2]
        set_players(match, players)

    full_level_matches = Match.objects.filter(tournament=tournament, tournament_level=full_levels)
    matches_next_in_full_level = Match.objects.filter(next_match__in=full_level_matches).values_list('next_match')
    full_level_matches_to_set = full_level_matches.exclude(id__in=matches_next_in_full_level)
    for index, match in enumerate(full_level_matches_to_set):
        i = index + 1
        players = full_levels_users[i*2-2:i*2]
        if len(players) == 1:
            players.append(None)
        set_players(match, players)


def add_match(tournament, level, next_match):
    match = Match.objects.create(
        tournament_level=level,
        tournament=tournament,
        next_match=next_match
    )

    return match


def set_players(match, players):
    match.player_1 = players[0].user
    match.player_2 = players[1].user
    match.save()
