from src.style import Style
import sys
import csv

style_codes = { style_code[0] : style_code[1] for style_code in list(csv.reader(open('res/style-codes.csv', 'r'))) }

if len(sys.argv) < 2:
    print('Usage: python3 main.py <file> [output_file]')
    exit(1)

file_name = sys.argv[1]

input_file = open(file_name, 'r')
if len(sys.argv) == 3:
    output_file = open(sys.argv[2], 'w')
else:
    if file_name.__contains__('/'):
        output_file = open(f'{file_name[:file_name.rindex("/") + 1]}styled-{file_name[file_name.rindex("/") + 1:]}', 'w')
    else:
        output_file = open(f'styled-{file_name}', 'w')

input_text = input_file.read()

stack = []
output = ''

while input_text.__contains__('<console'):
    index = input_text.index('<console')
    if index != 0:
        output += str(Style(input_text[:index], list(stack), style_codes))
    input_text = input_text[index:]
    index = input_text.index('>')
    styles_text = input_text[9:index].split('.')
    styles = [style.strip().upper() for style in styles_text if style.strip() != '']
    input_text = input_text[index+1:]
    stack.append(styles)
    while input_text.__contains__('</console>') and input_text.find('</console>') < (input_text.find('<console') if input_text.__contains__('<console') else len(input_text)):
        index = input_text.index('</console>')
        output += str(Style(input_text[:index], list(stack), style_codes))
        input_text = input_text[index+10:]
        stack.pop()

output += input_text

i = 0
while i < len(output):
    if output[i] == '!':
        if output[i-1] == '<' or output[i-2:i] == '</':
            output = output[:i] + output[i+1:]
            while output[i] == '!':
                i += 1
    i += 1

output_file.write(output)

input_file.close()
output_file.close()