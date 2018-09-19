#!/usr/bin/env python


def create_next_state(previous_states, number_of_each_color):
    previous_state = previous_states[-1]
    num_colors = len(previous_state)
    num_already_selected = len(previous_states)
    next_state = [0.0] * num_colors
    for c in range(num_colors):
        num_left_already_selected_colors = (c + 1) * number_of_each_color - num_already_selected
        num_left_new_colors = (num_colors - c - 1) * number_of_each_color
        next_state[c] += previous_state[c] * (num_left_already_selected_colors / float(num_left_already_selected_colors + num_left_new_colors))
        if c + 1 < num_colors:
            next_state[c + 1] += previous_state[c] * (num_left_new_colors / float(num_left_already_selected_colors + num_left_new_colors))
    return next_state


def print_states(states):
    for state in states:
        print ' '.join('{:.9f}'.format(val) for val in state)


def expected_colors(number_of_colors, number_of_each_color, number_selected):
    first_state = [1.0] + [0.0] * (number_of_colors - 1)
    states = [first_state]
    while len(states) < number_selected:
        states.append(create_next_state(states, number_of_each_color))
    print_states(states)
    return sum((c + 1) * states[-1][c] for c in range(number_of_colors))


def main():
    # print '{:.10}'.format(expected_colors(2, 2, 3))[:-1]
    print '{:.9f}'.format(expected_colors(7, 10, 20))


if __name__ == '__main__':
    main()
