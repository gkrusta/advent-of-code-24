def iscorrect(record):
    n = len(record)

    for i in range(1, n):
        diff = record[i] - record[i - 1]
        if not (1 <= abs(diff) <= 3) or (diff > 0 and record[0] > record[1]) or (diff < 0 and record[0] < record[1]):
            return False
    return True


def almostcorrect(record):
    for i in range(len(record)):
        new_report = record[:i] + record[i + 1:]
        if iscorrect(new_report):
            return True
    return False


def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    res = 0

    for line in lines:
        record = list(map(int, line.split()))
        if iscorrect(record) or almostcorrect(record):
            res += 1
    
    print("\nSum:", res)


main()