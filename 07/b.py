CARDS = "J23456789TQKA"


def get_card_counts(hand):
    return {c: hand.count(c) for c in CARDS}


def num_equal(hand):
    counts = get_card_counts(hand)
    return tuple(sorted([c for c in counts.values() if c > 0], reverse=True))


def tie_break_score(h):
    """
    Returns a tie breaker score for a hand.
    """
    BASE = 100
    b = 1
    score = 0
    for c in h[::-1]:
        score += CARDS.index(c) * b
        b *= BASE

    return score


def rank_score(hand):
    # If there are jokers, turn them into whatever other card there is the most of
    counts = get_card_counts(hand)
    counts["J"] = 0
    if "J" in hand:
        hand = hand.replace("J", max(counts, key=counts.get))

    # Five of a kind
    if num_equal(hand) == (5,):
        return 6

    # Four of a kind
    if num_equal(hand) == (4, 1):
        return 5

    # Full house
    if num_equal(hand) == (3, 2):
        return 4

    # Three of a kind
    if num_equal(hand) == (3, 1, 1):
        return 3

    # Two pair
    if num_equal(hand) == (2, 2, 1):
        return 2

    # One pair
    if num_equal(hand) == (2, 1, 1, 1):
        return 1

    return 0


def full_score(hand):
    return (rank_score(hand), tie_break_score(hand))


def main():
    filename = "input.txt"

    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    hands = [line[0] for line in lines]
    bids = [int(line[1]) for line in lines]

    # Sort bids by hand score
    scores = [full_score(hand) for hand in hands]
    sorted_bids = [bid for _, bid in sorted(zip(scores, bids), reverse=True)]

    ans = 0
    for i, b in enumerate(sorted_bids):
        ans += b * (len(sorted_bids) - i)

    print(ans)


if __name__ == "__main__":
    main()
