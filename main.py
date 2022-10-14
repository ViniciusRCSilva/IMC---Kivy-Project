from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
# Cria duas telas.
# Por favor preste atenção que  root.manager.current: é como você pode
# controlar the ScreenManager from kv ativando a tela atual.
# Cada screen tem por padrão a propriedade manager
# Que permite que você ative a tela pelo ScreenManager.
Builder.load_file("main.kv")

# Declaração das Telas
class UserInfo(Screen):
    pass

class ImcCalc(Screen):
    pass

class MedicOrientation(Screen):
    pass

class IMC(App):
    def build(self):
        # Cria o Gerenciador de Telas
        sm = ScreenManager()
        sm.add_widget(UserInfo(name='userinfo'))
        sm.add_widget(ImcCalc(name='imccalc'))
        sm.add_widget(MedicOrientation(name='medicorientation'))
        # Retorna o Gerenciador de Telas
        return sm

if __name__ == '__main__':
    # Inicia a Classe
    IMC().run()