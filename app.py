# pip install pyautogui pillow mouseinfo
import pyautogui # automatiza o movimento do mouse, teclado e digitação
from time import sleep # para pausar o programa por alguns segundos

# se não tiver usuário cadastrado > criar novo usuário
# pyautogui.click(958,590, duration=0.5)

# 1. clicar no campo e digitar meu usuário
pyautogui.click(960,541, duration=0.5)
pyautogui.write('marcela')
# 2. clicar no campo e digitar minha senha
pyautogui.click(958,567, duration=0.5)
pyautogui.write('654321')
# 4. se o usuário estiver cadastrado > clicar em "entrar"
pyautogui.click(868,596, duration=0.5)



with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0] # toda vez que encontrar uma virgula no produtos.txt, vai identificar como um campo diferente p ser cadastrado
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #   1 - clicar e digitar produto
        pyautogui.click(679,528, duration=0.5)
        pyautogui.write(produto)
        #   2 - clicar e digitar quantidade
        pyautogui.click(683,553, duration=0.5)
        pyautogui.write(quantidade)
        #   3 - clicar e digitar o preço
        pyautogui.click(683,580, duration=0.5)
        pyautogui.write(preco)
        #   4 - clicar em registrar
        pyautogui.click(585,733, duration=0.5)
        sleep(1) # pausar por 1sec após registrar um novo


