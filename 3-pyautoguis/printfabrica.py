import pyautogui as pg

pg.press('win')
pg.typewrite('Chrome')
pg.sleep(1)
pg.press('return')
pg.sleep(1)
pg.moveTo(700, 500)
pg.leftClick()
pg.sleep(1)

#pg.hotkey('win', 'up')

pg.typewrite('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval=0.01)
pg.press('return')
pg.sleep(1)

pg.hotkey('win', 'printscreen')
pg.sleep(1)

pg.hotkey('win', 'r')
pg.sleep(1)
pg.typewrite('mspaint')
pg.sleep(1)
pg.press('return')

pg.sleep(1)
pg.hotkey('ctrl', 'v')

for i in range(3):
    pg.hotkey('ctrl', '-')
    pg.sleep(0.5)