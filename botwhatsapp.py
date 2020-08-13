from selenium import webdriver
import time

class Whatsappbot(object):
    def __init__(self):
        self.mensagens = "Bom dia pessoal, tudo bem??"
        self.grupos = ["Grupo Família", "Grupo amigos"]
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10) # time.spleep() é usado para não sobregarregar a pagina por fazer varias ações muito rapdio
        for grupo in self.grupos:
            # Vai procurar o elemento dentro da pagina, aqui procurei pela tag <span> passando o title do elemento
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            #Vai procurar pela classa fornesida nesse caso é class do TextBox da whatsappweb
            text_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)

            text_box.click()
            text_box.send_keys(self.mensagens)
            # Aqui ele procura o elemoto do mesma forma do primeiro passo a tag HTML <span> e passo a forma pra ele encontra o elemento exato q preciso
            botão_enviar=self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botão_enviar.click()
            time.sleep(5)

bot = Whatsappbot()
bot.EnviarMensagens()
