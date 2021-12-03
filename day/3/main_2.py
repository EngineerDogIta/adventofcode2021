""""
# PART 2
Next, you should verify the life support rating, 
which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report 
- finding them is the tricky part. 
Both values are located using a similar process that involves filtering out values until only one remains. 
Before searching for either rating value, 
start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers.

Then:
Keep only numbers selected by the bit criteria for the type of rating value for which you are searching.
Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
and keep only numbers with that bit in that position.
If 0 and 1 are equally common, keep values with a 1 in the position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
and keep only numbers with that bit in that position. If 0 and 1 are equally common,
keep values with a 0 in the position being considered.
For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

Start with all 12 numbers and consider only the first bit of each number.
There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position:
11110, 10110, 10111, 10101, 11100, 10000, and 11001.
Then, consider the second bit of the 7 remaining numbers:
there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position:
10110, 10111, 10101, and 10000.
In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
In the fifth position, there are an equal number of 0 bits and 1 bits (one each).
So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
Then, to determine the CO2 scrubber rating value from the same example above:

Start again with all 12 numbers and consider only the first bit of each number.
There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position:
00100, 01111, 00111, 00010, and 01010.
Then, consider the second bit of the 5 remaining numbers:
there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
In the third position, there are an equal number of 0 bits and 1 bits (one each).
So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating,
then multiply them together. What is the life support rating of the submarine?
(Be sure to represent your answer in decimal, not binary.)
"""

if __name__ == "__main__":
    with open("input.txt", "r", encoding="UTF-8") as f:
        rows = [str(x) for x in f.read().splitlines()]

    # Next, you should verify the life support rating,
    # which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    # get only the first character of each row
    list_of_criteria_oxygen = list(rows)
    for i in range(len(list_of_criteria_oxygen[0])):
        bits = [int(row[i]) for row in list_of_criteria_oxygen] # get all the bits in the row in the position i
        if(bits.count(0) == bits.count(1)): # if they have the same amount of 0 and 1
            most_common_bit = "1"
        else:
            most_common_bit = str(max(bits.count(0), bits.count(1)))
        print(f'Most common {i} bit: {most_common_bit}')
        
        list_of_criteria_oxygen = [row for row in list_of_criteria_oxygen if int(row[i]) == int(most_common_bit)]

        if len(list_of_criteria_oxygen) == 1:
            oxygen_generator_rating = int(list_of_criteria_oxygen[0], 2)
            break

    print(f'Oxygen generator rating: {oxygen_generator_rating}')

    list_of_criteria_co2 = list(rows)
    for i in range(len(list_of_criteria_co2[0])):
        bits = [int(row[i]) for row in list_of_criteria_co2] # get all the bits in the row in the position i
        if(bits.count(0) == bits.count(1)): # if they have the same amount of 0 and 1
            least_common_bit = "0"
        else:
            least_common_bit = str(min(bits.count(0), bits.count(1)))
        print(f'Least common {i} bit: {least_common_bit}')
        
        list_of_criteria_co2 = [row for row in list_of_criteria_co2 if int(row[i]) == int(least_common_bit)]

        if len(list_of_criteria_co2) == 1:
            co2_scrubber_rating = int(list_of_criteria_co2[0], 2)
            break
 
    print(f'CO2 scrubber rating: {co2_scrubber_rating}')

    # What is the life support rating of the submarine?
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f'Life support rating: {life_support_rating}')
