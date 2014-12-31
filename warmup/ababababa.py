__author__ = 'julio'
test_cases = input()
for i in xrange(test_cases):
    sequence = raw_input()
    steps = 0
    for index, letter in enumerate(sequence):
        try:
            next_letter = sequence[index+1]
        except IndexError:
            next_letter = None
        if next_letter:
            if next_letter == letter:
                steps += 1
        else:
            print steps

