import os
from collections import Counter

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()
        
    data_lines = [x.split(' | ') for x in data]

    total = 0

    # data_lines = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'.split(' | ')]
    for line in data_lines:
        output_decoded = []
        all_combinations = [{xx for xx in x} for x in line[0].split(' ')] # 10 combinations_digits
        assert(len(all_combinations) == 10)

        output_encoded = [{xx for xx in x} for x in line[1].split(' ')] # 4 digits
        assert(len(output_encoded) == 4)
        """
            0:6      1:2      2:5      3:5      4:4
         aaaa    ....    aaaa    aaaa    ....
        b    c  .    c  .    c  .    c  b    c
        b    c  .    c  .    c  .    c  b    c
         ....    ....    dddd    dddd    dddd
        e    f  .    f  e    .  .    f  .    f
        e    f  .    f  e    .  .    f  .    f
         gggg    ....    gggg    gggg    ....
        
          5:5      6:6      7:3      8:7      9:6
         aaaa    aaaa    aaaa    aaaa    aaaa
        b    .  b    .  .    c  b    c  b    c
        b    .  b    .  .    c  b    c  b    c
         dddd    dddd    ....    dddd    dddd
        .    f  e    f  .    f  e    f  .    f
        .    f  e    f  .    f  e    f  .    f
         gggg    gggg    ....    gggg    gggg
        """
        digits = dict()
        here_069 = []
        here_235 = []
        count_chars = Counter()
        for x in all_combinations:
            """
             dddd
            e    a
            e    a
             ffff
            g    b
            g    b
             cccc
            """
            if len(x) == 2: # digit is 1
                digits[1] = x
            elif len(x) == 4: # digit is 4
                digits[4] = x
            elif len(x) == 3: # digit is 7
                digits[7] = x
            elif len(x) == 7: # digit is 8
                digits[8] = x
            elif len(x) == 6:
                # digit can be 0,6,9
                here_069.append(x)
            elif len(x) == 5:
                # digit can be 2,3,5
                here_235.append(x)
            count_chars.update(x)
        remaining_combinations = [*here_069, *here_235]

        counter_069 = Counter(''.join([''.join(x) for x in here_069]))
        counter_235 = Counter(''.join([''.join(x) for x in here_235]))

        segment_b = Counter(''.join([''.join(x) for x in all_combinations])).most_common(1)[0][0]
        segment_g = (counter_069 + counter_235).most_common()[-1][0]
        segment_d = list(Counter(digits[7]) - Counter(digits[1]))[0]
        segment_e = (counter_069 - counter_235).most_common(1)[0][0]
        segment_a = list(digits[1] - {segment_b})[0]
        
        digits[9] = [x for x in here_069 if not(segment_g in x)][0]
        digits[6] = [x for x in here_069 if x != digits[9] and not(segment_a in x)][0]
        digits[0] = [x for x in here_069 if x != digits[9] and segment_a in x][0]

        digits[2] = [x for x in here_235 if not(segment_b in x) and not(segment_e in x)][0]
        digits[5] = [x for x in here_235 if not(segment_a in x) and not(segment_g in x)][0]
        digits[3] = [x for x in here_235 if not(segment_e in x) and not(segment_g in x)][0]


        # print(f'digits: {str(digits)}')
        
        for encoded_num in output_encoded:
            for x in range(0,10):
                if x in digits.keys() and digits[x] == encoded_num:
                    output_decoded.append(str(x))
                    break
        output_decoded_str = ''.join(output_decoded)
        # print(f'output_decoded: {output_decoded_str}')
        total += int(output_decoded_str)
    
    print(f' total = {total}')
    