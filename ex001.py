import pyautogui
import pandas
from time import sleep
import pyperclip
import datetime


pyautogui.PAUSE = 1

pyautogui.press('Win')
pyautogui.write('Edge')
pyautogui.press('Enter')

pyautogui.write('https://www.catho.com.br/')
pyautogui.press('Enter')
sleep(3)
pyautogui.click(1450, 172)
sleep(3)
pyautogui.click(992, 415)

pyautogui.write('email@email.com')
sleep(3)
pyautogui.press('Tab')
pyautogui.press('Tab')
pyautogui.write('minha_senha')
pyautogui.press('Enter')
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://drive.google.com/file/d/1Oef0ZRtfitBPZNdU7WSwTWTt2a9sLCsf/view')
pyautogui.press('Enter')
sleep(5)

pyautogui.click(1678, 176)
pyautogui.hotkey('ctrl', 't')

sleep(4)
tabela = pandas.read_csv(r'C:\Users\ezioa\Downloads\Compras.csv', sep = ';')
print(tabela)
total_gasto = tabela['ValorFinal'].sum()
quantidade = tabela['Quantidade'].sum()
preco_medio = total_gasto / quantidade

pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('Enter')
sleep(2)

pyautogui.click(113, 263)
sleep(2)

pyautogui.write('email@email.com')
sleep(2)
pyautogui.press('tab')

pyautogui.press('tab')
pyperclip.copy('Automação Python')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

ontem = f'{(datetime.date.today().day)-1}/{datetime.date.today().month}'
corpo = f'''Prezados,

Segue a relação de compras de ontem({ontem}):

Total gasto: R$ {total_gasto:.2f}
Quantidade: {quantidade}
Preço médio: R$ {preco_medio:.2f}

Qualquer dúvida estou à disposição!

Att. Gabriel Rodrigues'''

pyperclip.copy(corpo)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
