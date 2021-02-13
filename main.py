#calculadora
from kivy.app import App
from kivy.lang import  Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


Window.size=(300,500)

class calcApp(App):
    title = 'Calculadora'
    def build(self):
        self.icon='icon.jpg'
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.pantalla= TextInput(
            multiline= False,halign="right", font_size=30,
            background_color=(3/255,249/255,67/255), readonly=True,
            border=(1,0,0,1)
        )
        main_layout.add_widget(self.pantalla)

        botones=[
            ['7','8','9','*'],
            ['4','5','6','+'],
            ['1', '2', '3', '-'],
            ['.', '0', 'c', '/']
        ]
        for linea in botones:
            teclado=BoxLayout()
            for i in linea:
                boton=Button(
                    text=i,pos_hint={"center_x": 0.5, "center_y": 0.5})
                boton.bind(on_press=self.on_button_press)
                teclado.add_widget(boton)
            main_layout.add_widget(teclado)

        ultimaBox=BoxLayout()
        delete = Button(text='del', pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint_x=.25)
        delete.bind(on_press=self.del_press)
        ultimaBox.add_widget(delete)
        igual=Button(text='=',pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint_x=.75)
        igual.bind(on_press=self.igual_press)
        ultimaBox.add_widget(igual)
        main_layout.add_widget(ultimaBox)
        return main_layout

    def on_button_press(self, instance): #self.last_was_operator, self.last_button
        pantallaActual=self.pantalla.text
        texto_boton=instance.text
        if texto_boton=='c' or pantallaActual == 'ERROR':
            self.pantalla.text=''
        else:
            if pantallaActual and (
                    self.last_was_operator and texto_boton in self.operators):
                return
            elif pantallaActual=='' and texto_boton in self.operators:
                return
            else:
                texto_nuevo = pantallaActual + texto_boton
                self.pantalla.text = texto_nuevo
        self.last_button = texto_boton
        self.last_was_operator = self.last_button in self.operators

    def igual_press(self,*args):
        texto = self.pantalla.text
        try:
            if texto:
                solucion=str(eval(self.pantalla.text))
                self.pantalla.text=solucion
        except:
            self.pantalla.text = 'ERROR'

    def del_press(self,*args):
        texto = self.pantalla.text
        if texto == 'ERROR' or texto == '': pass
        else:
            self.pantalla.text= str(texto[:-1])

if __name__ == '__main__':
    calcApp().run()