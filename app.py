
#Passo a Passo

import pyautogui
from time import sleep

#1 - abrir a ferramenta ou programa
pyautogui.press('win')
sleep(2)
pyautogui.write('sistema.xlsx')
sleep(2)
pyautogui.press('enter')
sleep(2)


"""
Os sleeps foram usados aqui dar tempo de colocar o mouse em cima da posição do campo a ser preenchido e pegar a sua localização, em campos de user e passowrd

sleep(3)
positionUser = pyautogui.position(x=358, y=282)

sleep(3)
positionPassword = pyautogui.position(x=372, y=339)

sleep(3)
positionLogin = pyautogui.position(x=359, y=436)

Lembrando que essas posições podem variar de acordo com o seu computador, por isso é importante que use o pyautogui.position() e colocar o mouse sobre o campo que queira ser selecionado 
ao dar um print em positionLogin, teremos no terminal os valores das coordenadas de x e y

"""

#2 - preencher o login
sleep(2)
pyautogui.click(x=358, y=282)
sleep(1)
pyautogui.write('Teste')
sleep(2)

#3 - preencher a senha
pyautogui.click(x=372, y=339)
sleep(1)
pyautogui.write('teste1')
sleep(2)

#4 - clicar em fazer loguin
pyautogui.click(x=359, y=436)





