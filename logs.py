def print_line():
    print('<----------------------------------------------------->')

def colored_output(color, message):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'black': '\033[90m',
        'bright_red': '\033[91;1m',
        'bright_green': '\033[92;1m',
        'bright_yellow': '\033[93;1m',
        'bright_blue': '\033[94;1m',
        'bright_magenta': '\033[95;1m',
        'bright_cyan': '\033[96;1m',
        'bright_white': '\033[97;1m',
        'reset': '\033[0m'  
    }
    
    if color in colors:
        print(colors[color] + message + colors['reset'])
    else:
        print("Invalid color specified.")