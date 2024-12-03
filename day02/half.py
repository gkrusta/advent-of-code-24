def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    res = 0

    for line in lines:
        i = 0
        ascending = True
        record = line.split()
        record = list(map(int, record))

        if (len(record) >= 2):
            if  record[0] > record[1]:
                ascending = False
            for i in range(len(record)):
                if i == len(record) - 1:
                    res += 1
                    break
                if record[i] > record[i + 1] and ascending:
                    break
                elif record[i] < record[i + 1] and not ascending:
                    break
                if abs(record[i] - record[i + 1]) == 0 or abs(record[i] - record[i + 1]) > 3:
                    break
    
    print("\nSum:", res)
    file.close()

main()