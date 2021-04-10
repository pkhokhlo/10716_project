def rock_paper_scissors(p1_action, p2_action):
    #actions: 0 (rock), 1 (paper), 2 (scissors)
    #scores: 0 (lose), 0.5 (tie), 1 (win)
    #output: [p1_score, p_2score]

    if p1_action == p2_action:
        #tie
        return [0.5, 0.5]
    elif (p1_action == 0 and p2_action == 2) or (p1_action == 1 and p2_action == 0) or (p1_action == 2 and p2_action == 1):
        #player 1 wins
        return [1.0, 0.0]
    else:
        #player 2 wins
        return [0.0, 1.0]

def chicken_or_dare(p1_action, p2_action):
    #actions: 0 (dare), 1 (chicken)
    #scores: (D,D)->(0, 0), (D,C)->(7,2), (C,D)->(2,7), (C,C)->(6,6)
    #output: [p1_score, p2_score]

    if p1_action == 0 and p2_action == 0:
        return [0.0, 0.0]
    elif p1_action == 0 and p2_action == 1:
        return [1.0, 2.0/7.0]
    elif p1_action == 1 and p2_action == 0:
        return [2.0/7.0, 1.0]
    else:
        return [6.0/7.0, 6.0/7.0]
