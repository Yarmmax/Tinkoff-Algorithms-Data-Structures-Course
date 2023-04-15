def ab_pruning(states, alpha, beta, player, steps):
    if steps == 0:
        return 2 if player == 1 else 1
    if states.is_winning():
        return 1 if player == 1 else 2
    if player == 1:
        for move in states.moves():
            alpha = max(alpha, ab_pruning(states + move, alpha, beta, 2, steps-1))
            if beta <= alpha:
                return alpha
        return alpha
    else:
        for move in states.moves():
            beta = min(beta, ab_pruning(states + move, alpha, beta, 1, steps-1))
            if beta <= alpha:
                return beta
        return beta


states