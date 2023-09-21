from tools.constants import txt


def print_terminal_title(show=True):
    if show is True:
        print(get_terminal_title(show))


def get_terminal_title(show=True):
    with open(txt.CRYPTOBOT_BINANCE, "r") as file:
        content = file.read()
    if show is True:
        return content
