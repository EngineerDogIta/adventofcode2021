
def find_most_common_bit(list_binaries, index):
    """Find the most common bit in the index in parameter."""
    bits = [int(binary[index]) for binary in list_binaries]
    if(bits.count(0) == bits.count(1)): # if they have the same amount of 0 and 1
        most_common_bit = "1"
    else:
        if(bits.count(0) > bits.count(1)):
            most_common_bit = "0"
        else:
            most_common_bit = "1"
    return most_common_bit

def find_least_common_bit(list_binaries, index):
    """Find the least common bit in the index in parameter."""
    bits = [int(binary[index]) for binary in list_binaries]
    if(bits.count(0) == bits.count(1)): # if they have the same amount of 0 and 1
        least_common_bit = "0"
    else:
        if(bits.count(0) > bits.count(1)):
            least_common_bit = "1"
        else:
            least_common_bit = "0"
    return least_common_bit

if __name__ == "__main__":
    with open("input.txt", "r", encoding="UTF-8") as f:
        rows = [str(x) for x in f.read().splitlines()]

    # Next, you should verify the life support rating,
    # which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    # clone all items from rows into oxygen_generator_rating_list
    oxygen_generator_rating_list = rows[:]
    co2_scrubber_rating_list = rows[:]

    # For each char in row, get the max or min value
    for i_char_at in range(len(rows[0])):
        most_bit = find_most_common_bit(oxygen_generator_rating_list, i_char_at)
        print("Most common bit at index {} is {}".format(i_char_at, most_bit))
        oxygen_generator_rating_list = [b for b in oxygen_generator_rating_list if b[i_char_at] == most_bit]
        if(len(oxygen_generator_rating_list) == 1):
            oxygen_generator_rating = int(oxygen_generator_rating_list[0], 2)
    
    for i_char_at in range(len(rows[0])):
        least_bit = find_least_common_bit(co2_scrubber_rating_list, i_char_at)
        print("Least common bit at index {} is {}".format(i_char_at, least_bit))
        co2_scrubber_rating_list = [b for b in co2_scrubber_rating_list if b[i_char_at] == least_bit]
        if(len(co2_scrubber_rating_list) == 1):
            co2_scrubber_rating = int(co2_scrubber_rating_list[0], 2)

    # get only the first character of each row
    print(f'CO2 scrubber rating: {co2_scrubber_rating}')

    # What is the life support rating of the submarine?
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f'Life support rating: {life_support_rating}')
