from jovian.pythondsa import evaluate_test_cases

# We need to write a program to find the position of a given number in a list of
# numbers arranged in decreasing order. we also need to minimize the number of
# times we access elements from the list.

# Input:
#        cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
#        query: A number, whose position in the array is to be determined. E.g. 7

# Output:
#        position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)


def test_location(cards, query, mid):
    mid_num = cards[mid]

    if mid_num == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'

    elif mid_num < query:
        return 'left'

    elif mid_num > query:
        return 'right'


def locate_card(cards, query):
    start = 0
    end = len(cards)-1

    while start <= end:
        mid = start + (end-start)//2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid

        elif result == 'right':
            start = mid+1

        elif result == 'left':
            end = mid-1

    return -1


    # TEST CASES
tests = []
tests.append(
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3})
tests.append(
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6})
tests.append({"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0})
tests.append(
    {"input": {"cards": [3, -1, -9, -127], "query": -127}, "output": 3})
tests.append({"input": {"cards": [6], "query": 6}, "output": 0})
tests.append({"input": {"cards": [9, 7, 5, 2, -9], "query": 4}, "output": -1})
tests.append({"input": {"cards": [], "query": 7}, "output": -1})
tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 3},
        "output": 7,
    }
)
tests.append(
    {
        "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 6},
        "output": 2,
    }
)

print(evaluate_test_cases(locate_card, tests))
