import re

def main():
    file = open("input.txt", "r")
    memory_list = file.readlines()
    memory_str = ''.join(memory_list)
    res = 0
    enabled = True
    mull_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_patter = r"don't\(\)"
    pattern = rf'{mull_pattern}|{do_pattern}|{dont_patter}'

    for match in re.finditer(pattern, memory_str):
        print("matches:", match.group(1))
        if enabled and match.group(1) and match.group(2):
            res += int(match.group(1)) * int(match.group(2))
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
    
    print("\nSum:", res)
    file.close()

main()