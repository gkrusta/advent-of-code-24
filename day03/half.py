import re

def main():
    file = open("input.txt", "r")
    memory_list = file.readlines()
    memory_str = ''.join(memory_list)
    res = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.findall(pattern, memory_str)
    print("matches:", matches)
    
    res = sum(int(x) * int(y) for x, y in matches)
    print("\nSum:", res)
    file.close()

main()