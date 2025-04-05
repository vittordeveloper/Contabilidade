from openpyxl import load_workbook
import pyautogui

# Definindo variaveis para poder acessar a planilha;
vendas_de_lanches = load_workbook('cadastro.xlsx')
pagina1 = vendas_de_lanches['Cadastro']

for linha in pagina1.iter_rows(min_row=2, values_only=True):
    # Nome
    pyautogui.click(266,171, duration=1.5)
    pyautogui.write(linha[0])
    # Produto
    pyautogui.click(266,195, duration=1.5)
    pyautogui.write(linha[1])
    # Quantidadeedro Santos
    pyautogui.click(266,217, duration=1.5)
    pyautogui.write(str(linha[2]))
    # Data
    pyautogui.click(266, 234,duration=1.5)
    pyautogui.write(linha[3])

    # Salvar
    pyautogui.click(301, 259, duration=1.5)
    pyautogui.click(285, 305, duration=1.5)
