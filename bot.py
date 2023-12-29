import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

global driver



def responderComentarios(comentario,mensagem,inscrito):
    try:
        comentario.find_element(By.ID,'reply-button').click()
        cx_text = driver.find_element(By.TAG_NAME,'textarea')
        driver.execute_script("arguments[0].click();", cx_text)
        driver.find_element(By.TAG_NAME,'textarea').send_keys(f'{inscrito}\n{mensagem}')
        responder = driver.find_element(By.ID,'submit-button')
        driver.execute_script("arguments[0].click();", responder)
        sleep(5)
        driver.execute_script("arguments[0].scrollIntoView(true);",comentario)
        sleep(2)
    except:
        pass


def main():
    respondidos = []
    while True:
        try:
            comentarios = driver.find_elements(By.ID,'content')
            for comentario in comentarios:
                inscrito = comentario.text.split('\n')[0]
                if inscrito not in respondidos:
                    responderComentarios(comentario,mensagem,inscrito)
                    respondidos.append(inscrito)
                    print(inscrito)
            nao_respondidos = 0
            comentarios_verificar = driver.find_elements(By.ID,'content')
            for comentario_v in comentarios_verificar:
                if comentario_v.text.split('\n')[0] not in respondidos:
                    nao_respondidos += 1
            if nao_respondidos == 0:
                break
        except:
            pass



mensagem = '''
Peço desculpas pela minha ausência recente no canal.
Problemas pessoais surgiram, mas estou de volta e mais comprometido do que nunca.
Aguardem por muito conteúdo interessante em breve. Obrigado pela compreensão!

'''


driver = uc.Chrome()
driver.get('https://www.youtube.com/')
print('Conectado')





