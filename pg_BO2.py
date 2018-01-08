import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('netflix.com\n',0.5)
time.sleep(2)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('enter')
