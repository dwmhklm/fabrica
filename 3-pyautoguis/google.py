import pyautogui as pg

pg.press('win')
pg.typewrite('Chrome')
pg.sleep(1)
pg.press('return')

def gogle(wait):

    for i in range(2):
        pg.sleep(wait)
        pg.moveTo(700, 500)
        pg.sleep(wait)
        pg.leftClick()
        pg.sleep(wait)
        pg.typewrite('google')
        pg.sleep(wait)
        pg.press('return')
        pg.sleep(wait)
        pg.moveTo(250, 300)
        pg.sleep(wait)
        pg.leftClick()
        pg.sleep(wait)

    pg.moveTo(220,64)
    pg.leftClick()
    pg.typewrite('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval=0.01)
    pg.press('return')

gogle(0.2)