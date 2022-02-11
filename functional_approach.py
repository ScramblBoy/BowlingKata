def is_valid_sequence(sequence):
    if len(sequence) == 22:
        if sequence[-4] == 10:  # checks if last regular frame is a strike
            if sequence[-2] == 10:  # checks if first roll after last frame is also a strike
                return sequence[-1] in range(0, 11) and are_all_frames_valid(sequence[:-2])
            else:
                return are_all_frames_valid(sequence)
        else:
            return False
    elif len(sequence) == 21:
        return sequence[-3] + sequence[-2] == 10 and sequence[-1] in range(0, 11) and are_all_frames_valid(
            sequence[:-1])
    elif len(sequence) == 20:
        return are_all_frames_valid(sequence)
    else:
        return False


def are_all_frames_valid(sequence):
    for idx in range(0, len(sequence), 2):
        if sum(sequence[idx:idx + 2]) not in range(0, 11):
            return False
    return True


def calculate_score(sequence):
    framescores = []
    if is_valid_sequence(sequence):
        for counter in range(0, 20, 2):
            if sequence[counter] == 10:
                if sequence[counter + 2] == 10:
                    if counter == 18:
                        framescores.append(10 + sequence[-2] + sequence[-1])
                    else:
                        framescores.append(20 + sequence[counter + 4])
                else:
                    framescores.append(10 + sum(sequence[counter + 2:counter + 4]))
            elif sum(sequence[counter:counter + 2]) == 10:
                framescores.append(10 + sequence[counter + 2])
            else:
                framescores.append(sum(sequence[counter:counter + 2]))
        return sum(framescores)
    else:
        print("invalid sequence!")
        return
