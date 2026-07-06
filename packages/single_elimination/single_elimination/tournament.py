"""
This defines a single elimination 'Tournament' object.
"""
import math
import itertools

from single_elimination.match import Match
from single_elimination.participant import Participant

class Tournament:
    """
    This is a single-elimination tournament where each match is between 2 competitors.
    It takes in a list of competitors, which can be strings or any type of Python object,
    but they should be unique. They should be ordered by a seed, with the first entry being the most
    skilled and the last being the least. They can also be randomized before creating the instance.
    Optional options dict fields:
    """
    def __init__(self, competitors_list, options={}):
        assert len(competitors_list) > 1
        self.__matches = []
        next_higher_power_of_two = int(math.pow(2, math.ceil(math.log2(len(competitors_list)))))
        winners_number_of_byes = next_higher_power_of_two - len(competitors_list)
        incoming_participants = list(map(Participant, competitors_list))
        incoming_participants.extend([None] * winners_number_of_byes)

        while len(incoming_participants) > 1:
            half_length = int(len(incoming_participants)/2)
            first = incoming_participants[0:half_length]
            last = incoming_participants[half_length:]
            last.reverse()
            next_round_participants = []
            for participant_pair in zip(first, last):
                if participant_pair[1] is None:
                    next_round_participants.append(participant_pair[0])
                elif participant_pair[0] is None:
                    next_round_participants.append(participant_pair[1])
                else:
                    match = Match(participant_pair[0], participant_pair[1])
                    next_round_participants.append(match.get_winner_participant())
                    self.__matches.append(match)
            incoming_participants = next_round_participants
        self.__winner = incoming_participants[0]

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
        returns a list of Matches that they are currently playing in.
        """
        matches = []
        for match in self.get_active_matches():
            competitors = [participant.get_competitor() for participant in match.get_participants()]
            if competitor in competitors:
                matches.append(match)
        return matches

    def get_winners(self):
        """
        Returns None if the winner has not been decided yet,
        and returns a list containing the single victor otherwise.
        """
        if len(self.get_active_matches()) > 0:
            return None
        return [self.__winner.get_competitor()]

    def add_win(self, match, competitor):
        """
        Set the victor of a match, given the competitor string/object and match.
        """
        match.set_winner(competitor)
