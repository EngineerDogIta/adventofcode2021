import os
from collections import Counter

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as f:
        data = f.read().splitlines()
        
    data_lines = [x.split(' | ') for x in data]

    count_digits = Counter()

    for line in data_lines:
        output_decoded = []
        combinations = [{xx for xx in x} for x in line[0].split(' ')] # 10 combinations_digits
        assert(len(combinations) == 10)

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
        for x in combinations:
            if len(x) == 2: # digit is 1
                digits[1] = x
            elif len(x) == 4: # digit is 4
                digits[4] = x
            elif len(x) == 3: # digit is 7
                digits[7] = x
            elif len(x) == 7: # digit is 8
                digits[8] = x

        # print(f'digits: {str(digits)}')
        
        for encoded_num in output_encoded:
            for x in range(0,10):
                if x in digits.keys() and digits[x] == encoded_num:
                    output_decoded.append(x)
                    break
        # print(output_decoded)
        # assert(len(output_decoded) == 4)
        count_digits.update(output_decoded)
    
    print(f' 1 = {count_digits[1]}, 4 = {count_digits[4]}, 7 = {count_digits[7]}')
    print(f' 1, 4, 7, 8 = {(count_digits[1]+count_digits[4]+count_digits[7]+count_digits[8])}')
    