# Round Robin Tournament
This is a python package to manage the matches for a round robin tournament.

For usage, see the test files.

Create an issue if you have any suggested features, changes, or documentation. Pull requests welcome.

Install with `pip install round_robin_tournament`

Example usage:
```
from round_robin_tournament import Tournament

players = ['Robin', 'Jaynee', 'Michelle']

tournament = Tournament(players)

matches = tournament.get_active_matches()

while len(matches) > 0:
  print("{} matches left".format(len(matches)))
  match = matches[0]
  participants = match.get_participants()
  first_participant = participants[0]
  first_participant_name = first_participant.get_competitor()
  second_participant = participants[1]
  second_participant_name = second_participant.get_competitor()
  print("{} vs {}".format(first_participant_name, second_participant_name))
  tournament.add_win(match, first_participant_name)
  matches = tournament.get_active_matches()

print(tournament.get_winners())
```
