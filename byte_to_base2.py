
input_num = input("Enter the base2 number: ")
input_num = input_num[::-1]

output_num = 0

for pos, digit in enumerate(input_num):
    output_num += int(digit)  (2 ** pos)

print(f'Output in bytes = {output_num}')