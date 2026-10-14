"""
pytermkit - A lightweight terminal toolkit for Python.

Provide terminal color, font styling, cursor control
and utility functions using ANSI escape codes.
No dependencies required except standard library.

Classes:
    Colors: ANSI color codes for foreground and background.
    Fonts: ANSI font style codes with activate/deactivate support.
    Term: Terminal utilities (clear, typewriter, color/font management).
    Cursor: Cursor movement and visibility control.

Example:
    from pytermkit import Term, Colors, Cursor

    Term.set_color("red", "blue")
    Term.set_font(("bold", True))
    Term.typewriter("Hello World!")
    Term.clear()
"""

#!######## TODO LIST #########
# TODO: Complete the main function.


from time import sleep

class Colors:
    """ANSI color codes for terminal output.

    Example:
        Colors.fg["red"]
        Colors.bg["blue"]
        print(Colors.get_color_rgb((255, 255, 255), (10, 10, 10)))
    """
    fg = {
        "reset": "\x1b[39m",
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "purple": "\x1b[35m",
        "cyan": "\x1b[36m",
        "gray": "\x1b[90m",
        "light_red": "\x1b[91m",
        "light_green": "\x1b[92m",
        "light_yellow": "\x1b[93m",
        "light_blue": "\x1b[94m",
        "light_purple": "\x1b[95m",
        "light_cyan": "\x1b[96m",
        "light_gray": "\x1b[37m"
        }
    bg = {
        "reset": "\x1b[49m",
        "red": "\x1b[41m",
        "green": "\x1b[42m",
        "yellow": "\x1b[43m",
        "blue": "\x1b[44m",
        "purple": "\x1b[45m",
        "cyan": "\x1b[46m",
        "gray": "\x1b[47m"
        }
    
    @staticmethod
    def get_color_rgb(fg: tuple=(255, 255, 255), bg: tuple=(0, 0, 0)) -> dict:
        """Return ANSI color code from rgb codes.
        
        Args:
            fg: Foreground color rgb code, gets a tuple. (Default: (255, 255, 255))
            bg: Background color rgb code, gets a tuple. (Default: (0, 0, 0))
        
        Example:
            Colors.get_color_rgb((255, 20, 20), (20, 0, 255)) (Returns color ANSI code, print to use.)
            Colors.get_color_rgb(fg=(100, 150, 70), bg=(10, 100, 110)) (Returns color ANSI code, print to use.)
        """
        if len(fg)!=3 or len(bg)!=3:
            raise ValueError("RGB colors must contain exactly 3 values.")

        for value in fg + bg:            
            if not isinstance(value, int):
                raise TypeError("RGB values must be integers.")
            elif not 0 <= value <= 255:
                raise ValueError(f"RGB must be 0-255, got {value}")

        rgb = {}
        rgb["fg"] = f"\x1b[38;2;{fg[0]};{fg[1]};{fg[2]}m"
        rgb["bg"] = f"\x1b[48;2;{bg[0]};{bg[1]};{bg[2]}m"
        return rgb


class Fonts:
    """ANSI font codes for terminal output.
    
    Example:
        Fonts.font["bold"][True] # activate bold
        Fonts.font["bold"][False] # deactivate bold
    """
    font = {
        "reset": {True:"\x1b[0m",
                  False: "\x1b[0m"},
        
        "bold": {True: "\x1b[1m",
                 False: "\x1b[22m"},

        "italic": {True: "\x1b[3m",
                   False: "\x1b[23m"},

        "underline": {True: "\x1b[4m",
                      False: "\x1b[24m"},
        "double_underline": {
            True: "\x1b[21m",
            False: "\x1b[24m"},

        "blink": {True: "\x1b[5m",
                  False: "\x1b[25m"},

        "reverse": {True: "\x1b[7m",
                    False: "\x1b[27m"},

        "hidden": {True: "\x1b[8m",
                   False: "\x1b[28m"},

        "strike": {True: "\x1b[9m",
                   False: "\x1b[29m"}
    }


class Term:
    """Useful methods for the terminal.
    
    Methods:
        clear
        clear_line
        typewriter
        add_lines
        set_fg_color
        set_bg_color
        set_font
        set_color
        set_color_rgb
    """
    @staticmethod
    def set_color(fg: str="reset", bg: str="reset") -> None:
        """Set the terminal color.
        
        Args:
            fg: Foreground color, gets a string. (Default: "reset")
            bg: Background color, gets a string. (Default: "reset")
        
        Example:
            term.set_color("red", "blue")
        """
        if fg.lower() not in Colors.fg.keys() or bg.lower() not in Colors.bg.keys():
            raise ValueError(f"Unknown color:{fg} or {bg}")
        fg = Colors.fg[fg.lower()]
        bg = Colors.bg[bg.lower()]
        print(fg + bg, end="")

    @staticmethod
    def set_fg_color(color: str) -> None:
        """
        Set terminal foreground color.
        
        Args:
            color: New color of the terminal, gets a string.
        
        Example:
            Term.set_fg_color("green")
        """
        if color.lower() not in Colors.fg:
            raise ValueError(f"Unknown foreground color: {color}")
        
        print(Colors.fg[color.lower()], end="")

    @staticmethod
    def set_bg_color(color: str) -> None:
        """
        Set terminal background color.
        
        Args:
            color: New color of the terminal, gets a string.
        
        Example:
            Term.set_bg_color("green")
        """
        if color.lower() not in Colors.bg:
            raise ValueError(f"Unknown background color: {color}")
                
        print(Colors.bg[color.lower()], end="")        

    @staticmethod
    def set_color_rgb(fg: tuple=(255, 255, 255), bg: tuple=(0, 0, 0)) -> None:
        """Set terminal color with rgb.
        
        Args:
            fg: Foreground color rgb codes, gets a tuple. (Default: (255, 255, 255))
            bg: Background color rgb codes, gets a tuple. (Default: (0, 0, 0))
        
        Example:
            term.set_color_rgb((255, 20, 20), (20, 0, 255))
            term.set_color_rgb(fg=(100, 150, 70), bg=(10, 100, 110))
        """
        if not (len(fg)==3 and len(bg)==3):
            raise ValueError(f"RGB must contain exactly 3 values, got ({len(fg)}, {len(bg)}).")

        for value in fg + bg: 
            if not isinstance(value, int):
                raise TypeError(f"RGB values must be integers.")

            elif not 0 <= value <= 255:
                raise ValueError(f"RGB must be 0-255, got {value}")
        

        fg = f"\x1b[38;2;{fg[0]};{fg[1]};{fg[2]}m"
        bg = f"\x1b[48;2;{bg[0]};{bg[1]};{bg[2]}m"
        print(fg+bg, end="")

    @staticmethod
    def set_font(fnt: tuple) -> None:
        """Set terminal font style.
        
        Args:
            fnt: tuple of (font_name, bool)
        
        Example:
            Term.set_font(("bold", True))
            Term.set_font(("italic", False))
        """
        if len(fnt) != 2:
            raise IndexError("Font setter requires a tuple of (font_name, bool).")
        
        elif not isinstance(fnt[0], str):
            raise TypeError(f"Font name must be string, got {type(fnt[0])}")
        
        elif fnt[0].lower() not in Fonts.font.keys():
            raise ValueError(f"Unknown font name: {fnt[0]}")
        
        elif not isinstance(fnt[1], bool):
            raise TypeError(f"Font status must be bool. Got: {fnt[1]}")

        print(Fonts.font[fnt[0].lower()][fnt[1]], end="")

    @staticmethod
    def clear() -> None:
        """Clear the terminal screen."""
        print("\x1b[2J\x1b[H\x1b[3J", end="")
    
    @staticmethod
    def clear_line() -> None:
        """Clear the entire line."""
        print("\x1b[2K", end="")

    @staticmethod
    def typewriter(*args, delay: float=0.05, sep=" ", end="\n") -> None:
        """
        Print text with a typewriter effect.
        
        Args:
            args: The text to print.
            delay: Seconds between each characters, gets a float. (Default: 0.05)
            sep: Separator between arguments, gets any type. (Default: " ")
            end: End character after all text, gets any type. (Default: "\n")
        
        Example:
            Term.typewriter("Hello", "World", delay=0.3, sep="-", end="")
        """
        if delay < 0:
            raise ValueError(f"Delay value cannot be less than 0, got {delay}.")
        
        text = [] # Contain the args items.
        for arg in args:
            arg = str(arg)
            text.append(arg)

        for i, txt in enumerate(text): # Iterate over the words in the list: text.
            for letter in txt: # Iterate over the letters in the word: txt.
                print(letter, end="", flush=True)
                sleep(delay) # Typerwriter effect.

            if i < len(text) - 1: # If the loop is not on the last word.
                print(sep, end="", flush=True)

        print(end=end, flush=True)


    @staticmethod
    def add_lines(n: int=1) -> None:
        """Add new void line.
        
        Args:
            n: Number of lines, gets int. (Default: 1)
        
        Example:
            Term.add_lines(10)
        """
        if n < 0:
            raise ValueError(f"Number of lines cannot be less than 0, got {n}.")
        print(n * "\n", end="")
    

class Cursor:
    """Useful methods for the cursor.
    
    Methods:
        up
        down
        right
        left
        to_column
        save
        restore
        hide
        show
    """
    @staticmethod
    def up(n: int = 1) -> None:
        """ Print ANSI code to move the cursor up.
        Args:
            n: Number of lines to move. (Default: 1)
        
        Example:
            Cursor.up(3)
        """
        if n < 0:
            raise ValueError(f"Number of lines cannot be less than 0, got {n}.")
        print(f"\x1b[{n}A", end="")
    
    @staticmethod
    def down(n: int = 1) -> None:
        """Print ANSI code to move the cursor down.
        
        Args:
            n: Number of lines to move.
        
        Example:
            Cursor.down(1)
        """
        if n < 0:
            raise ValueError(f"Number of lines cannot be less than 0, got {n}.")
        print(f"\x1b[{n}B", end="")
    
    @staticmethod
    def right(n: int = 1) -> None:
        """Print ANSI code to move the cursor right.
        
        Args:
            n: Number of columns to move.
        
        Example:
            Cursor.right(5)
        """ 
        if n < 0:
            raise ValueError(f"Number of column cannot be less than 0, got {n}.")
        print(f"\x1b[{n}C", end="")
    
    @staticmethod
    def left(n: int = 1) -> None:
        """Print ANSI code to move the cursor left.
        
        Args:
            n: Number of columns to move.
        
        Example:
            Cursor.left(3)
        """
        if n < 0:
            raise ValueError(f"Number of column cannot be less than 0, got {n}.")
        print(f"\x1b[{n}D", end="")
    
    @staticmethod
    def to_column(n: int) -> None:
        """Print ANSI code to move the cursor to column number.
        
        Args:
            n: Column number.
        
        Example:
            Cursor.to_column(10)
        """
        if n < 1:
            raise ValueError(f"Number of column cannot be less than 1, got {n}.")
        print(f"\x1b[{n}G", end="")
    
    @staticmethod
    def save() -> None:
        """Save the current cursor position."""
        print("\x1b[s", end="")
    
    @staticmethod
    def restore() -> None:
        """Move the cursor to last saved position."""
        print("\x1b[u", end="")
    
    @staticmethod
    def hide() -> None:
        """Hide the cursor."""
        print("\x1b[?25l", end="")


    @staticmethod
    def show() -> None:
        """Show the cursor."""
        print("\x1b[?25h", end="")


class Test:
    """Interactive test interface for pytermkit.

    Provides menus to test colors, font styles, terminal utilities,
    cursor controls, and class/method information.

    Used to demonstrate and verify the functionality of pytermkit.
    """

    banner = f"""
    {Colors.fg["red"]}______  __      __    ______________ ________ ______                        __  ____________
    |#####\\ \\#\\    /#/    |############| |#######||#####\\  |\\        /||#|  /#/|##||############|
    {Colors.fg["yellow"]}|##  ##\\ \\#\\  /#/     |----|  |----| |##|-----|##  ##\\ |#\\      /#||#| /#/ |##||----|  |----|
    |##  ##/  \\#\\/#/           |##|      |##|____ |##  ##/ |##\\    /##||#|/#/  |##|     |##|
    {Colors.fg["green"]}|##__#/    |##|            |##|      |#######||##__#/  |###\\  /###||###|   |##|     |##|
    |##|       |##|            |##|      |##|-----|##|\\#\\  |#|\\#\\/#/|#||#|\\#\\  |##|     |##|
    {Colors.fg["blue"]}|##|       |##|            |##|      |##|____ |##| \\#\\ |#|      |#||#| \\#\\ |##|     |##|
    |##|       |##|            |##|      |#######||##|  \\#\\|#|      |#||#|  \\#\\|##|     |##|{Colors.fg["reset"]}
          """

    main_menu = """
    1) Test Colors 
    2) Test Fonts
    2) Class / Method Informations
    3) Test Terminal Methods
    4) Test Cursor Methods

    0) Exit
    """
    
    colors_menu = """
    1) Foreground Colors
    2) Background Colors
    """
    
    fg_colors_menu = """
    1) reset
    2) red
    3) green
    4) yellow
    5) blue
    6) purple
    7) cyan
    8) gray
    9) light_red
    10) light_green
    11) light_yellow
    12) light_blue
    13) light_purple
    14) light_cyan
    15) light_gray

    0) Back
    """

    bg_colors_menu = """
    #list like fg_colors_menu but for background colors
    1) reset
    2) red
    3) green
    4) yellow
    5) blue
    6) purple
    7) cyan
    8) gray

    0) Back
    """

    class_methods_menu = """
    1) Colors
    2) Fonts
    3) Term:
        Methods:
        3.1) set_color
        3.2) set_fg_color
        3.3) set_bg_color
        3.4) set_color_rgb
        3.5) set_font
        3.6) clear
        3.7) clear_line
        3.8) clear
        3.9) typewriter
        3.10) add_lines

    0) Back

    4) Cursor:
        Methods:
        4.1) up
        4.2) down
        4.3) right
        4.4) left
        4.5) to_column
        4.6) save
        4.7) restore
        4.8) hide
        4.10) show

    0) Back
    """
    
    test_term_methods_menu = """
    1) set_color
    2) set_fg_color
    3) set_bg_color
    4) set_color_rgb
    5) set_font
    6) clear
    7) clear_line
    8) clear
    9) typewriter
    10) add_lines

    0) Back
    """
    
    test_cursor_methods_menu = """
    1) up
    2) down
    3) right
    4) left
    5) to_column
    6) save
    7) restore
    8) hide
    10) show

    0) Back
    """

    @staticmethod
    def print_banner():
        """Print the banner for the test interface."""
        Term.typewriter(Test.banner, delay=0.001, end="\n\n")

def main():
    """Main function to run the interactive test interface."""
    Term.clear()
    while True:
        Test.print_banner()
        sleep(0.7)
        print(Test.main_menu)
        choice = input("Select an option: ")
        break
    
    
    Term.set_color("reset")

if __name__ == "__main__":
    main()