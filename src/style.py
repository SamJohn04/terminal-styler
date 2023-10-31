class Style:
    def __init__(self, string, styles, style_codes):
        self.string = string
        self.styles = []
        i = 0
        while i < len(styles):
            for style in styles[i]:
                self.styles.append(style)
            i += 1
        self.style_codes = style_codes

    def __str__(self):
        style_code = ''
        for style in self.styles:
            style_code += '\u001b[' + self.get_style_code(style)
        default_style_code = '\u001b[' + self.style_codes.get('DEFAULT', '0m')
        return f'{style_code}{self.string}{default_style_code}'
    
    def hex_to_rgb(self, hex):
        hex = hex.lstrip('#')
        hlen = len(hex)
        return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))
    
    def get_style_code(self, style):
        if not '[' in style:
            return self.style_codes.get(style, '0m')
        else:
            style_code = ''
            style_code += ('38' if style[:style.index('-')] == 'COLOR' else '48') + ';2;'
            style = style[style.index('[') + 1:style.index(']')]
            rgb = self.hex_to_rgb(style)
            style_code += str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + 'm'
            return style_code