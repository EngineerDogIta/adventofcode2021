"""
# PART 1

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which,
when decoded properly, can tell you many useful things about the conditions of the submarine.
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers
(called the gamma rate and the epsilon rate).
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit
in the corresponding position of all numbers in the diagnostic report.

For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits.
Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively,
and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit,
the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal.
Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
then multiply them together. What is the power consumption of the submarine?
(Be sure to represent your answer in decimal, not binary.)

"""

if __name__ == '__main__':
    with open('input.txt', 'r', encoding='UTF-8') as f:
        rows = [str(x) for x in f.read().splitlines()]
    
    most_common_bits = []
    least_common_bits = []

    for i in range(len(rows[0])):
        # get only the first character of each row
        stripped_bits = [int(row[i]) for row in rows]
        most_common_bits.append(str(max(set(stripped_bits), key=stripped_bits.count)))
        print(f'Most common {i} bit: {most_common_bits[i]}')
        least_common_bits.append(str(min(set(stripped_bits), key=stripped_bits.count)))
        print(f'Least common {i} bit: {least_common_bits[i]}')


    gamma_rate = "".join(most_common_bits)
    print(f'Gamma rate: {gamma_rate}')
    gamma_rate_dec = int(gamma_rate, 2)
    print(f'Gamma rate: {gamma_rate_dec}')

    epsilon_rate = "".join(least_common_bits)
    print(f'Epsilon rate: {epsilon_rate}')
    epsilon_rate_dec = int(epsilon_rate, 2)
    print(f'Epsilon rate: {epsilon_rate_dec}')

    power_consumption = gamma_rate_dec * epsilon_rate_dec
    # power consumption of the submarine
    print(f'Power consumption: {power_consumption}')

