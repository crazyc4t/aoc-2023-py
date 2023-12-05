calibration = []
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum_all = 0
first_digit = ""
last_digit = ""
last_number = ""
number_keys = list(numbers.keys())


def read_file(file):
    lines = []
    fread = open(file, "r")
    while True:
        text = fread.readline()
        if len(text) == 0:
            break
        else:
            lines.append(text.split())
    split_matrix(lines)
    fread.close()


def split_matrix(matrix):
    for i in range(len(matrix)):
        calibration.append(matrix[i][0])


def check_numbers(line):
    indexes = {}
    for key in number_keys:
        if line.find(key) != -1:
            indexes[line.find(key)] = numbers[key]
    indexes_keys = list(indexes.keys())
    indexes_keys.sort()
    return indexes, indexes_keys


def replace_numbers(line):
    indexes, indexes_keys = check_numbers(line)
    current_line = line
    for i in indexes_keys:
        current_line = current_line[:i] + str(indexes[i]) + current_line[i + 1 :]
    return current_line


def return_replaced(line):
    i = 0
    t = replace_numbers(line)
    while i < len(line) // 2:
        t = replace_numbers(t)
        i += 1
    return t


read_file("input.txt")

for i in range(len(calibration)):
    current_string = return_replaced(calibration[i])
    for j in current_string:
        if j.isdigit() == True:
            first_digit = j
            last_digit = j
            break

    for k in current_string:
        if k.isdigit() == True:
            last_digit = k
    last_number = first_digit + last_digit
    print(f"The current line is {calibration[i]}")
    print(f"The two digits are: {last_number}")
    if last_number != "":
        sum_all += int(last_number)

print(f"The total calibration value is: {sum_all}")
