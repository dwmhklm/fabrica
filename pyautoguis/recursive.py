import pyautogui as pg


for i in range(3):
    pg.sleep(1)
    pg.hotkey('ctrl', 'alt', 'win', 'n')
    pg.typewrite(f'codigo{i}.py')
    pg.press('return')
    pg.sleep(1)
    pg.press('return')

    code = open('code.txt', 'r')
    leia = code.read()

    pg.sleep(1)

    pg.typewrite(leia, interval=0.01)
    pg.sleep(1)
    code.close()
    pg.sleep(1)