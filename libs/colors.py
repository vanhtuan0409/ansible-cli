class Color(object):
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def red(text):
        return Color.RED + text + Color.ENDC

    @staticmethod
    def yellow(text):
        return Color.YELLOW + text + Color.ENDC

    @staticmethod
    def blue(text):
        return Color.BLUE + text + Color.ENDC

    @staticmethod
    def green(text):
        return Color.GREEN + text + Color.ENDC
