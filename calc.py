import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Window.size=(400,600)
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text ='0'

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = ""
        if prior == "0":
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        if "." not in prior:
            self.ids.calc_input.text = f'{prior}.'
        else:
            num_list = re.split(r'[+\-*/]', prior)
            last_num = num_list[-1]
            if "." not in last_num:
                self.ids.calc_input.text = f'{prior}.'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        if prior == "":
            self.ids.calc_input.text = "0"
        else:
            self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = round(eval(prior), 10)
        except:
            answer = "Error"
        self.ids.calc_input.text = str(answer)

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()
