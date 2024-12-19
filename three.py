import re
sum = 0
do = True

def calc_params(valid_instructions) -> None:
    global sum
    for instruction in valid_instructions:
        x, y = map(int, re.findall(pattern=r"\d+", string=instruction))
        sum += x*y

with open('three.csv') as input:
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    filtered = re.findall(pattern=pattern, string=input.read())
    for instruction in filtered:
        if do and instruction.startswith('mul'):
            x, y = map(int, re.findall(pattern=r"\d+", string=instruction))
            sum += x*y 
        elif instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False

    # valid_instructions = re.findall(pattern=pattern, string=input.read())
    # mul_params = ()
    # calc_params(valid_instructions)


print(sum)








