"""
This defines a round robin 'Tournament' object.
"""
import math
import itertools

from round_robin_tournament.match import Match
from round_robin_tournament.participant import Participant

class Tournament:
    """
    This is a round-robin tournament where each match is between 2 competitors.
    It takes in a list of competitors, which can be strings or any type of Python object,
    but they should be unique. They should be ordered by a seed, with the first entry being the most
    skilled and the last being the least. They can also be randomized before creating the instance.
    Optional options dict fields:
    winners_to_take: How many players will be counted as winners once the games have been played.
    """
    def __init__(self, competitors_list, options={}):
        assert len(competitors_list) > 1
        self.__wins = {}
        self.__winners_to_take = 1
        if 'winners_to_take' in options:
            self.__winners_to_take = options['winners_to_take']
        self.__matches = []
        participants = list(map(Participant, competitors_list))

        for x in range(len(participants)):
            for y in range(x + 1, len(participants)):
                self.__matches.append(Match(participants[x], participants[y]))

    def __iter__(self):
        return iter(self.__matches)

    def get_active_matches(self):
        """
        Returns a list of all matches that are ready to be played.
        """
        return [match for match in self.get_matches() if match.is_ready_to_start()]

    def get_matches(self):
        """
        Returns a list of all matches for the tournament.
        """
        return self.__matches

    def get_active_matches_for_competitor(self, competitor):
        """
        Given the string or object of the competitor that was supplied
        when creating the tournament instance,
        returns a list of Match's that they are currently playing in.
        """
        return [match for match in self.get_active_matches() if competitor in _get_match_competitors(match)]

    def get_winners(self):
        """
        Returns None if the winner has not been decided yet,
        and returns a list containing the single victor otherwise.
        """
        if len(self.get_active_matches()) > 0:
            return None
        winners_asc = [x[0] for x in sorted(self.__wins.items(), key=lambda kv: kv[1])]
        winners_asc.reverse()
        return winners_asc[0:self.__winners_to_take]

    def add_win(self, match, competitor):
        """
        Set the victor of a match, given the competitor string/object and match.
        """
        match.set_winner(competitor)
        if competitor not in self.__wins:
            self.__wins[competitor] = 0
        self.__wins[competitor] += 1

def _get_match_competitors(match):
    return [participant.get_competitor() for participant in match.get_participants()]
