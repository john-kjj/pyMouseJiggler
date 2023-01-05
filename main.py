import pyautogui
import time
import sys

pyautogui.FAILSAFE = True


class MouseJiggler:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update_coor(self) -> None:
        self.x, self.y = pyautogui.position()

    def detect_user(self) -> bool:
        temp_x, temp_y = pyautogui.position()
        if temp_x != self.x and temp_y != self.y:
            return True
        else:
            return False

    def jiggle_mouse(self) -> None:
        try:
            while True:
                self.update_coor()
                pyautogui.moveRel(10, 0)
                time.sleep(1)
                if self.detect_user():
                    time.sleep(30)
                pyautogui.moveRel(-10, 0)
                time.sleep(1)
                if self.detect_user():
                    time.sleep(30)
                sys.stdout.flush()
        except KeyboardInterrupt:
            print("\n")


if __name__ == "__main__":
    mj = MouseJiggler()
    mj.jiggle_mouse()
