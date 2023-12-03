calibration = []


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


def split_matrix(matrix):
    for i in range(len(matrix)):
        calibration.append(matrix[i][0])


sum_all = 0
first_digit = ""
last_digit = ""
last_number = ""
read_file("input.txt")

for i in range(len(calibration)):
    for j in calibration[i]:
        if j.isdigit() == True:
            first_digit = j
            last_digit = j
            break

    for k in calibration[i]:
        if k.isdigit() == True:
            last_digit = k
    last_number = first_digit + last_digit
    # print(
    # f"The string {calibration[i]} their first digit is: {first_digit} and last digit is: {last_digit}, in total: {last_number}"
    # )
    if last_number != "":
        sum_all += int(last_number)
    # first_digit, last_digit, last_number = "", "", ""

print(f"The answer is: {sum_all}")
