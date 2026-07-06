from single_elimination import Tournament as SingleEliminationTournament

def printMatches(matches):
    print("Active Matches:")
    for match in matches:
        if match.is_ready_to_start():
            print("\t{} vs {}".format(*[p.get_competitor()
                                        for p in match.get_participants()]))


def add_win(tourney, competitor):
    m = tourney.get_active_matches_for_competitor(competitor)[0]
    tourney.add_win(m, competitor)


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
        SingleEliminationTournament([])
        raise Exception('Expected error')
    except AssertionError:
        pass

    # 1 competitor
    try:
        SingleEliminationTournament([1])
        raise Exception('Expected error')
    except AssertionError:
        pass

    # 2 competitors
    tourney = SingleEliminationTournament(rangeBase1(2))
    checkActiveMatches(tourney, [[1, 2]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 3 competitors
    tourney = SingleEliminationTournament(rangeBase1(3))
    checkActiveMatches(tourney, [[2, 3]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[2, 1]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 4 competitors
    tourney = SingleEliminationTournament(rangeBase1(4))
    checkActiveMatches(tourney, [[1, 4], [2, 3]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[4, 1]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [[1, 2]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 5 competitors
    tourney = SingleEliminationTournament(rangeBase1(5))
    checkActiveMatches(tourney, [[2, 3], [4, 5]])
    add_win(tourney, 4)
    checkActiveMatches(tourney, [[4, 1], [2, 3]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[4, 1]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [[1, 2]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 6 competitors
    tourney = SingleEliminationTournament(rangeBase1(6))
    checkActiveMatches(tourney, [[4, 5], [3, 6]])
    add_win(tourney, 4)
    checkActiveMatches(tourney, [[3, 6], [4, 1]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [[3, 6]])
    add_win(tourney, 3)
    checkActiveMatches(tourney, [[2,3]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[1,2]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 7 competitors
    tourney = SingleEliminationTournament(rangeBase1(7))
    checkActiveMatches(tourney, [[4, 5], [3, 6], [2, 7]])
    add_win(tourney, 4)
    checkActiveMatches(tourney, [[3, 6], [2, 7], [1, 4]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [[3, 6], [2, 7]])
    add_win(tourney, 3)
    checkActiveMatches(tourney, [[2, 7]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[2, 3]])
    add_win(tourney, 2)
    checkActiveMatches(tourney, [[1, 2]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [])

    # 8 competitors
    tourney = SingleEliminationTournament(rangeBase1(8))
    checkActiveMatches(tourney, [[1, 8], [2, 7], [3, 6], [4, 5]])
    add_win(tourney, 3)
    checkActiveMatches(tourney, [[1, 8], [2, 7], [4, 5]])
    add_win(tourney, 7)
    checkActiveMatches(tourney, [[1, 8], [4, 5], [3, 7]])
    add_win(tourney, 5)
    checkActiveMatches(tourney, [[1, 8], [3, 7]])
    add_win(tourney, 1)
    checkActiveMatches(tourney, [[3, 7], [1, 5]])
    add_win(tourney, 5)
    checkActiveMatches(tourney, [[3, 7]])
    add_win(tourney, 3)
    checkActiveMatches(tourney, [[3, 5]])
    add_win(tourney, 3)
    checkActiveMatches(tourney, [])
    if tourney.get_winners() != [3]:
        raise Exception("Incorrect winner")

    print("Starting performance test")

    n = 20000
    tourney = SingleEliminationTournament(range(n))
    matches = tourney.get_active_matches()
    while len(matches) > 0:
        for match in matches:
            tourney.add_win(match, match.get_participants()[0].get_competitor())
        matches = tourney.get_active_matches()

    print("Single elimination tests passed")
