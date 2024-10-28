import time
import pyautogui as py
import pandas as pd

py.PAUSE = 0.3

#entrar no navegador
py.press('win')     
py.write('opera')
py.press('enter')

#acessar o site
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')
time.sleep(3)

#validar email e senha
py.click(x=755, y=354)
py.write('testeautomacao@gmail.com')
py.press('tab')
py.write('senha')
py.press('tab')
py.press('enter')
time.sleep(3)

#cadastrar produtos
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    py.click(x=742, y=243)

    py.write(str(tabela.loc[linha, 'codigo']))
    py.press('tab')

    py.write(str(tabela.loc[linha, 'marca']))
    py.press('tab')

    py.write(str(tabela.loc[linha, 'tipo']))
    py.press('tab')

    py.write(str(tabela.loc[linha, 'categoria']))
    py.press('tab')

    py.write(str(tabela.loc[linha, 'preco_unitario']))
    py.press('tab')

    py.write(str(tabela.loc[linha, 'custo']))
    py.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        py.write(str(obs))
    py.press('tab')

    py.press('enter')