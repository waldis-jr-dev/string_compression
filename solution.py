def compression_algorithm(string):
    compressed_string = ""
    el_num = 0
    while el_num < len(string):
        sequence_counter = []
        sequence_len = 1
        while True:
            is_out = False
            try:
                sequence, next_sequence = "", ""
                for num in range(sequence_len):
                    sequence += string[el_num+num]
                    next_sequence += string[el_num+num+sequence_len]
            except IndexError:
                is_out = True
                sequence_len = 1
                break
            if sequence == next_sequence:
                if sequence not in sequence_counter:
                    sequence_counter.append(sequence)
                    sequence_counter.append(2)
                else:
                    sequence_counter[1] += 1
                el_num += sequence_len
            elif sequence not in sequence_counter:
                sequence_len += 1
            else:
                break
        if not is_out or len(sequence_counter) > 1:
            compressed_string += f" {sequence_counter[1]}{sequence_counter[0]}"
            if len(string) - (el_num + sequence_len) <= len(sequence_counter[0]):
                el_num += len(sequence_counter[0]) - 1
        else:
            compressed_string += f" {string[el_num]}"
        el_num += sequence_len
    return compressed_string.strip()


def compress_string(string):
    normal_result = compression_algorithm(string)
    reversed_result = ""
    for seq in compression_algorithm(string[::-1]).split()[::-1]:
        reversed_result += " "
        to_add = ""
        for el in seq:
            if el.isdigit():
                reversed_result += el
            if el.isalpha():
                to_add += el
        reversed_result += to_add[::-1]
    reversed_result = reversed_result.strip()
    return min(normal_result, reversed_result, key=len)


if __name__ == '__main__':
    test = "AAAAAAAAAABABABCCDXDFSXDFSXDFSX"
    # test = "AAAAAAAAAABABABCCD"
    print(compress_string(test))
