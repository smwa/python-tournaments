from round_robin_tournament import Tournament as RoundRobinTournament

def printMatches(matches):
    print("Active Matches:")
    for match in matches:
        if match.is_ready_to_start():
            print("\t{} vs {}".format(*[p.get_competitor()
                                        for p in match.get_participants()]))

def checkActiveMatches(tourney, competitorPairs):
    matches = tourney.get_active_matches()
    if len(competitorPairs) != len(matches):
        printMatches(matches)
        print(competitorPairs)
        raise Exception("Invalid number of competitors: {} vs {}".format(
            len(matches), len(competitorPairs)))
    for match in matches:
        inMatches = False
        for competitorPair in competitorPairs:
            participants = match.get_participants()
            if competitorPair[0] == participants[0].get_competitor():
                if competitorPair[1] == participants[1].get_competitor():
                    inMatches = True
            elif competitorPair[0] == participants[1].get_competitor():
                if competitorPair[1] == participants[0].get_competitor():
                    inMatches = True
        if not inMatches:
            printMatches(matches)
            print(competitorPairs)
            raise Exception("Wrong matches")

def rangeBase1(length):
    return [i + 1 for i in range(length)]

if __name__ == '__main__':

    # 0 competitors
    try:
        RoundRobinTournament([])
        raise Exception('Expected error')
    except AssertionError:
        pass

    # 1 competitor
    try:
        RoundRobinTournament([1])
        raise Exception('Expected error')
    except AssertionError:
        pass

    # 2 competitors
    tourney = RoundRobinTournament(rangeBase1(2))
    checkActiveMatches(tourney, [[1, 2]])
    tourney.add_win(tourney.get_active_matches_for_competitor(1)[0], 1)
    checkActiveMatches(tourney, [])

    # 3 competitors
    tourney = RoundRobinTournament(rangeBase1(3))
    checkActiveMatches(tourney, [[1, 2], [1, 3], [2, 3]])
    tourney.add_win(tourney.get_active_matches_for_competitor(2)[0], 2)
    checkActiveMatches(tourney, [[1, 3], [2, 3]])
    tourney.add_win(tourney.get_active_matches_for_competitor(1)[0], 1)
    checkActiveMatches(tourney, [[2, 3]])
    tourney.add_win(tourney.get_active_matches_for_competitor(2)[0], 2)
    checkActiveMatches(tourney, [])

    # 4 competitors
    tourney = RoundRobinTournament(rangeBase1(4))
    checkActiveMatches(tourney, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(4)[0], 4)
    checkActiveMatches(tourney, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(3)[0], 3)
    checkActiveMatches(tourney, [[1, 2], [2, 3], [2, 4], [3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(1)[0], 1)
    checkActiveMatches(tourney, [[2, 3], [2, 4], [3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(2)[0], 2)
    checkActiveMatches(tourney, [[2, 4], [3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(2)[0], 2)
    checkActiveMatches(tourney, [[3, 4]])
    tourney.add_win(tourney.get_active_matches_for_competitor(3)[0], 3)
    checkActiveMatches(tourney, [])
    if tourney.get_winners() != [2]:
        raise Exception("Incorrect winner")

    print("Starting performance test")

    n = 2048
    tourney = RoundRobinTournament(range(n))
    matches = tourney.get_active_matches()
    while len(matches) > 0:
        for match in matches:
            tourney.add_win(match, match.get_participants()[0].get_competitor())
        matches = tourney.get_active_matches()

    print("Round robin tests passed")
