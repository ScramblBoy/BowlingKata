def is_valid_sequence(sequence):
    if len(sequence) == 22:
        if sequence[-4] == 10:
            return are_all_frames_valid(sequence)
        else:
            return False
    elif len(sequence) == 21:
        if sequence[-3] + sequence[-2] == 10:
            if sequence[-1] in range(0, 11):
                return are_all_frames_valid(sequence[:-1])
            else:
                return False
        else:
            return False
    elif len(sequence) == 20:
        return are_all_frames_valid(sequence)
    else:
        return False


def are_all_frames_valid(sequence):
    for idx in range(0, len(sequence), 2):
        if sum(sequence[idx:idx + 2]) not in range(0, 11):
            return False
    return True


if __name__ == '__main__':
    print("hello world")
