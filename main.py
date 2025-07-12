from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.result = TextInput(font_size=32,size_hint_y=0.15, readonly=True, halign='center', multiline=False,background_color='white', foreground_color=(1, 1, 1, 1))
        self.add_widget(self.result)
        buttons=[['C', '+/-', '%', '/'],
                ['7', '8', '9', '*'],
                ['4', '5', '6', '-',],
                ['1', '2', '3', '+',],
                ['0', '00', '.', '=',]]
        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for item in row:
                button = Button(text=item, font_size=24,background_color=self.button_color(item))
                button.bind(on_press=self.button_click)
                grid.add_widget(button)
        self.add_widget(grid)
    def button_color(self, label):
        if label in {'C', '+/-', '%'}:
            return [0.9, 0.9, 0.9, 1]
        elif label in {'/', '*', '-', '+','='}:
            return [1, 0.65, 0, 1]
        return [0.3, 0.3, 0.3, 2]
    def button_click(self, instance):   
        text=instance.text
        if text == 'C':
            self.result.text = ''
        elif text == '+/-':
            if self.result.text.startswith('-'):
                self.result.text = self.result.text[1:]
            else:
                self.result.text = '-' + self.result.text
        elif text == '%':
            self.convert_percent()
        elif text == '=':
            try:
                self.result.text = str(eval(self.result.text))
            except Exception as e:
                self.result.text = 'Error'
        else:
            self.result.text += text

    def convert_percent(self):
        try:
            self.result.text = str(float(self.result.text) / 100)
        except ValueError:
            self.result.text = 'Error'
class CalculatorApp(App):
    def build(self):
        Window.size = (300, 500)
        return Calculator()
if __name__ == '__main__':
    CalculatorApp().run()
