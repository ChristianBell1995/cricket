from pycricbuzz import Cricbuzz

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import json
import time

class CricketService:
    def __init__(self, **args):
        self.cricbuzz = Cricbuzz()

    def current_matches(self):
        return self.cricbuzz.matches()

class DotMatrixService:
    def __init__(self, **args):
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=4, block_orientation=-90,
                     rotate=0, blocks_arranged_in_reverse_order=0)

    def show_teams(self, team1, team2):
        msg = f'{team1} vs {team2}'
        print(msg)
        show_message(self.device, msg, fill="white", font=proportional(CP437_FONT))


if __name__ == "__main__":
    c = CricketService()
    d = DotMatrixService()
    matches = c.current_matches()  # for pretty prinitng
    for match in matches:
        d.show_teams(match['team1']['name'], match['team2']['name'])
        time.sleep(1)




