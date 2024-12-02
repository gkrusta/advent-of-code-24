from collections import Counter

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    left_list = []
    right_list = []
    score = 0

    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    frequency_table = Counter(right_list)
    print("frequency:", frequency_table)

    for num in left_list:
        if num in frequency_table:
            score += num * frequency_table[num]
    
    print("\nSum:", score)
    file.close()

main()