import pyautogui as pg

ipsum = open("text.txt", "r")
leia = ipsum.read()

pg.press('win')

pg.typewrite('chrome')
pg.press('enter')

pg.sleep(1)
pg.moveTo(1000, 500)
pg.leftClick()
pg.typewrite('https://docs.google.com')
pg.press('enter')
pg.sleep(4)
pg.moveTo(435,374)
pg.leftClick()
pg.sleep(8)
pg.typewrite(leia, interval=0.01)