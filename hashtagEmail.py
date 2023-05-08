from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
load_dotenv()
import os

url = os.environ.get('URL')

browser = webdriver.Firefox()
browser.get(url)

emailLogin = os.environ.get('CADASTRO_EMAIL')
nomeCadastro = os.environ.get('CADASTRO_NOME')

def locationClick(cssSeleionado):
    browser.find_element(By.CLASS_NAME, cssSeleionado).click()

def locationSendKeys(key, id):
    browser.find_element(By.ID, id).send_keys(key)

locationSendKeys(nomeCadastro, 'firstname')
locationSendKeys(emailLogin, 'email')

locationClick('botao-formulario-newsletter')