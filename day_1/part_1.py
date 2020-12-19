""" Part 1 solution """

with open('input.txt') as inputs:
    print(type(inputs), inputs)
    numbers = set()
    for number in inputs:
        numbers.add(int(number))

for num in numbers: # O(n^2)
    rem = 2020 - num

    for j in numbers: # O(n)
        second_rem = rem - j
        if second_rem in numbers: # O(1)
            print(second_rem * j * num )
            break


