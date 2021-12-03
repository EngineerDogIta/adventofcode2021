

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

