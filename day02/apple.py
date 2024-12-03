def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    res = 0

    for line in lines:
        print(" line:", line)
        fail_counter = 0
        record = line.split()
        record = list(map(int, record))

        if len(record) >= 2:
            i = 0
            while i < len(record) - 1:
                ascending = record[0] < record[1]
                print("\nfail:", fail_counter)
                print(" number:", record[i])

                if fail_counter > 1:
                    break
                if (record[i] > record[i + 1] and ascending) or \
                   (record[i] < record[i + 1] and not ascending) or \
                   abs(record[i] - record[i + 1]) == 0 or \
                   abs(record[i] - record[i + 1]) > 3:

                    temp_remove_i = record[:i] + record[i + 1:]
                    fail_count_i = count_failures(temp_remove_i)
                    print("fail count 1: ", fail_count_i)
                    temp_remove_i_plus_1 = record[:i + 1] + record[i + 2:]
                    fail_count_i_plus_1 = count_failures(temp_remove_i_plus_1)
                    print("fail_count_i_plus_1: ", fail_count_i_plus_1)
                    # Decide which element to remove
                    if fail_count_i <= fail_count_i_plus_1:
                        record.pop(i)  # Remove current element
                        if i > 0:
                            i -= 1
                    else:
                        record.pop(i + 1)  # Remove the next element
                    print("record: ", record)

                    fail_counter += 1  # Increment failure counter
                    if fail_counter > 1:  # Stop if too many failures
                        break
                else:
                    i += 1  # Move to the next position

            if fail_counter <= 1:  # If the record is safe, increment result
                res += 1

    print("\nSum:", res)
    file.close()


def count_failures(record):
    fail_counter = 0
    if len(record) < 2:
        return fail_counter

    ascending = record[0] < record[1]
    for i in range(len(record) - 1):
        if (record[i] > record[i + 1] and ascending) or \
           (record[i] < record[i + 1] and not ascending) or \
           abs(record[i] - record[i + 1]) == 0 or \
           abs(record[i] - record[i + 1]) > 3:
            fail_counter += 1
    return fail_counter


main()
