import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class Colored:
    def __init__(self, text: str):
        """Creates a Colored object.

        Args:
            text (str): The text to be colored.
        """
        self.text = text
        self.color = Fore.RESET
        self.bg_color = Back.RESET
        self.style = Style.RESET_ALL

    def __str__(self):
        """Returns the colored text.

        Returns:
            str: The colored text.
        """
        return f"{self.style}{self.color}{self.bg_color}{self.text}{Style.RESET_ALL}"

    def set_color(self, color):
        """Set foreground color of text.

        Args:
            color (str): Color to change to.
        """
        self.color = color

    def set_bg_color(self, bg_color):
        """Set background color of text.

        Args:
            bg_color (str): Color to change to.
        """
        self.bg_color = bg_color

    def set_style(self, style):
        self.style = style

    # Foreground Colors
    def color_black(self):
        self.set_color(Fore.BLACK)

    def color_red(self):
        self.set_color(Fore.RED)

    def color_green(self):
        self.set_color(Fore.GREEN)

    def color_yellow(self):
        self.set_color(Fore.YELLOW)

    def color_blue(self):
        self.set_color(Fore.BLUE)

    def color_magenta(self):
        self.set_color(Fore.MAGENTA)

    def color_cyan(self):
        self.set_color(Fore.CYAN)

    def color_white(self):
        self.set_color(Fore.WHITE)

    # Background Colors
    def bg_color_black(self):
        self.set_bg_color(Back.BLACK)

    def bg_color_red(self):
        self.set_bg_color(Back.RED)

    def bg_color_green(self):
        self.set_bg_color(Back.GREEN)

    def bg_color_yellow(self):
        self.set_bg_color(Back.YELLOW)

    def bg_color_blue(self):
        self.set_bg_color(Back.BLUE)

    def bg_color_magenta(self):
        self.set_bg_color(Back.MAGENTA)

    def bg_color_cyan(self):
        self.set_bg_color(Back.CYAN)

    def bg_color_white(self):
        self.set_bg_color(Back.WHITE)

    # Text Styles

    def style_bold(self):
        self.set_style(Style.BRIGHT)

    def style_dim(self):
        self.set_style(Style.DIM)

    def style_reverse(self):
        self.set_style(Style.REVERSE)

    def style_hidden(self):
        self.set_style(Style.HIDDEN)
