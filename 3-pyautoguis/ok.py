import pyautogui as pg

pg.hotkey('win', 'r')
pg.typewrite('calc')
pg.press('return')

pg.sleep(2)

pg.press('8')
pg.press('+')
pg.press('2')
pg.press('return')

pg.alert("ok 👍", title="ok 👍")
