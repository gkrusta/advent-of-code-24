def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    left_list = []
    right_list = []

    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()
    diff = [abs(a - b) for a, b in zip(left_list, right_list)]
    res = sum(diff)

    print("Left List:", left_list)
    print("Right List:", right_list)
    print("\nSum:", res)
    file.close()

main()