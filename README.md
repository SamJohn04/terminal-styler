# Terminal Styler

CLI tool for transpiling your code, adding foreground and background colours, as well as styles such as bold, underline, and more to your terminal output.

## Prerequisites

- Python
- Support for ANSI codes in your terminal

## Installation

To install the program, you may use pip or any package manager of your choice as the program is available on PyPI. To install using pip, execute the following command:

> ```pip install terminal-styler```

## Execution

To run the program, execute the following command from the root directory of the project:

> ```stylet <input-file> [<output-file>]```

If no output file is specified, the output file will be `stdout`

## Input File

The input file should be a file containing the text you wish to style. The text can be styled using the following syntax:

> ```<console[.<styles>]>text</console>```

Each style is separated by a period.

> Eg: ```<console.bold.underline.color-green>text</console>```

The following styles are supported:
- bold
- underline
- reverse-text
- color-\<color\>
- bg-\<color\>

The following colours are supported:
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- grey

RBG colors can be specified in place of the default colors, using the syntax [#hexcode].
> Eg: ```<console.bg-[#ff0000]>text</console>```

Each color has a dark alternative, except black and grey, represented as dark-\<color\>.
> Eg: ```<console.color-dark-red>text</console>```

You may also nest console tags within each other.
> Eg: ```<console.bold>Hello<console.underline>World!</console> How are you?</console>```

**Note:** If you wish to use ```<console``` or ```</console>``` in your text without it being transpiled, you must prefix 'console' with a bang ```!```
> Eg: ```<!console>text</!console>``` will be transpiled to ```<console>text</console>```

One exclaimation mark will be removed from after each ```<```, if present.

## Output File

The output file will be a copy of the input file, with the text styled according to the input file. If no output file is specified, the output file will be `stdout`.

**Note:** If the output file already exists, it will be overwritten.

## Examples

### Input

```test.py```
```
print("<console.color-dark-red.bg-green.bold>Hello <console.underline>World!</console></console>")
print("<console.color-[#B8B8B8]>How are you?</console>!")
print("I <console.color-green>am</console> <console.reverse-text.bold>good</console>")
```

### Output

```
print("\33[0m\33[31m\33[102m\33[1mHello \33[0m\33[31m\33[102m\33[1m\33[4mWorld!\33[0m\33[31m\33[102m\33[1m\33[0m")
print("\33[0m38;2;184;184;184mHow are you?\33[0m!")
print("I \33[0m\33[92mam\33[0m \33[0m\33[7m\33[1mgood\33[0m")
```
