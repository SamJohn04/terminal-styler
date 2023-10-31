# Terminal Styler

CLI tool for adding foreground and background colours, as well as styles such as bold, underline, and more to your terminal output.

## Prerequisites

- Python
- Support for ANSI codes in your terminal

## Installation

To install the program, you may use pip or any package manager of your choice as the program is available on PyPI. To install using pip, execute the following command:

> ```pip install terminal-styler```

## Execution

To run the program, execute the following command from the root directory of the project:

> ```stylet <input-file> [<output-file>]```

If no output file is specified, the output file will be 

> ```styled-<input-file>```.

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

The output file will be a copy of the input file, with the text styled according to the input file. If no output file is specified, the output file will be named styled-*input-file*.

The output file will be of the same type as the input file.

**Note:** If the output file already exists, it will be overwritten.

**Note:** The application will not check if the input file is a valid file, or if the output file is a valid file name.

## Examples

### Input

```test.py```
```
print("<console.color-dark-red.bg-green.bold>Hello <console.underline>World!</console></console>")
print("<console.color-[#B8B8B8]>How are you?</console>!")
print("I <console.color-green>am</console> <console.reverse-text.bold>good</console>")
```

### Output

```styled-test.py```
```
print("[0m[31m[102m[1mHello [0m[31m[102m[1m[4mWorld![0m[31m[102m[1m[0m")
print("[0m[38;2;184;184;184mHow are you?[0m!")
print("I [0m[92mam[0m [0m[7m[1mgood[0m")
```

### Input

```Test.java```
```
package test;

public class Test {
    public static void main(String[] args) {
        System.out.println("Hello <console.bold>World!</console>");
    }
}
```

### Output

```Test.java```
```
package test;

public class Test {
    public static void main(String[] args) {
        System.out.println("Hello [0m[1mWorld![0m");
    }
}
```
