#!/usr/bin/python

import random
import sys

def decrease_values(list, index, value):
    for i in xrange(index, len(list)):
        list[i] = min(list[i], value)

def reachable(point):
    result = []

    for i in xrange(len(point)):
        for j in xrange(point[i]):
            if i == 0 and j == 0:
                continue
            next = list(point)
            decrease_values(next, i, j)
            result.append(tuple(next))

    return result

def SG(memo, point):
    if point not in memo:
        losing = True

        for r in reachable(point):
            losing = losing and SG(memo, r)

        memo[point] = not losing

    return memo[point]

def make_terminal_point(rows_count):
    result = [0] * rows_count
    result[0] = 1
    return tuple(result)

def make_initial_point(rows_count, cols_count):
    return tuple([cols_count] * rows_count)

def make_initial_memo(rows_count):
    return {make_terminal_point(rows_count): False}

def all_losing_points(memo):
    return [point for point in memo if not memo[point]]

def read_tuple():
    return tuple(map(int,
                     sys.stdin.readline()
                     .strip()
                     .replace("'", "")
                     .split(",")))

def main():
    random.seed()

    print "Enter rows and cols number. E.g. '4, 7' for the original task."
    input = read_tuple()
    rows_count = input[0]
    cols_count = input[1]

    memo = make_initial_memo(rows_count)
    SG(memo, make_initial_point(rows_count, cols_count))
    losing_points = all_losing_points(memo)

    while True:
        print "Enter position (" + \
            str([cols_count] * 4).replace("[", "").replace("]","") + \
            " would be a fair starting point)"

        input = read_tuple()
        reachable_from_input = reachable(input)

        # Bug? I don't know why this doesn't work and don't have time right
        # now to investigate:
        # answers = [position for position in reachable_from_input
        #            if not memo[position]]

        answers = [position for position in reachable_from_input
                   if position in losing_points]

        if not reachable_from_input:
            print "There are no positions reachable from a given one :("
        else:
            if not answers:
                print "There are no adequate moves from a given position - " + \
                      " I am returning a random one:"
                print random.choice(reachable_from_input)
            else:
                print "The best move from here is:"
                print random.choice(answers)

if __name__ == "__main__":
    main()
