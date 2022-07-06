#from PySimpleGUI import PySimpleGUI as sg
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import Account

nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
nav.get("https://www.linkedin.com/")
nav.find_element(By.ID, 'session_key').send_keys(Account.linkedIn()[0])
nav.find_element(By.ID, 'session_password').send_keys(Account.linkedIn()[1])
sleep(5)
nav.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button').click()
sleep(5)
nav.find_element(By.CLASS_NAME, 'share-box-feed-entry__trigger').click()
sleep(5)

'''
#Design do monitor
sg.theme('Reddit')

#Iniciando construção do monitor
menu = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar Login')],
    [sg.Button('Entrar')]
]

monitor = [
    [sg.Text('Parabéns, você acessou a primeira tela disponível.')],
    [sg.Button('Sair')]
]
 
#Tela inicial após o código executar
janela = sg.Window('PAINEL - CAOATEC', menu)

#janela_1

#Sistema de funcionamento
while True:
    ev, valores = janela.read()
    if ev == sg.WINDOW_CLOSED:
        monitor = sg.Window('PAINEL - CAOATEC', monitor)
        monitor.read()
        break
    if ev == 'Entrar':
        if valores['usuario'] == 'pedro' and valores['senha'] == '12345':
            print('acess')

'''