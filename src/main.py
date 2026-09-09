from src.style import Style
from src import values
import sys

def get_input_output(args):
    if len(args) < 2:
        print('Usage: stylet <file> [output_file]')
        exit(1)

    if args[1] == '-h' or args[1] == '--help':
        print('Usage: stylet <file> [output_file]')
        print('If output_file is not specified, the output will be to stdout')
        print('To style for the terminal, use the following syntax:')
        print('\t<console.<style1>.<style2>...> ... </console>')
        print('Example:')
        print('\t<console.bold.color-red.bg-green> This is bold red text in green bg </console>')
        exit(0)
        
    file_name = args[1]
    input_file = open(file_name, 'r')

    if len(args) == 3:
        output_file = open(args[2], 'w')
    else:
        output_file = sys.stdout
    return input_file, output_file

def get_style_codes():
    return values.style_codes

def filter_exclaimation(output):
    i = 0
    while i < len(output):
        if output[i] == '!':
            if output[i-1] == '<' or output[i-2:i] == '</':
                output = output[:i] + output[i+1:]
                while output[i] == '!':
                    i += 1
        i += 1
    return output

def get_styles(input_text):
    styles_text = input_text.split('.')
    return [style.strip().upper() for style in styles_text if style.strip() != '']

def write_output(output_file, output):
    output_file.write(filter_exclaimation(output))

def main(args = None):
    if args is None:
        args = sys.argv

    style_codes = get_style_codes()
    input_file, output_file = get_input_output(args)
    input_text = input_file.read()
    styles_stack = []

    while '<console' in input_text:
        index = input_text.index('<console')

        if index != 0:
            write_output(output_file, str(Style(input_text[:index], list(styles_stack), style_codes)))

        input_text = input_text[index:]
        
        index = input_text.index('>')

        styles = get_styles(input_text[9:index])
        styles_stack.append(styles)
        
        input_text = input_text[index+1:]
        
        while '</console' in input_text and input_text.find('</console') < (input_text.find('<console') if '<console' in input_text else len(input_text)):
            index = input_text.index('</console')
            
            write_output(output_file, str(Style(input_text[:index], list(styles_stack), style_codes)))
            
            input_text = input_text[index:]
            input_text = input_text[input_text.index('>') + 1:]
            styles_stack.pop()

    write_output(output_file, input_text)
    input_file.close()
    output_file.close()
