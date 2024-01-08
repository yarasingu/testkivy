from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

# set the app size
Window.size = (500, 700)

calc = """
<MyLayout>

    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            font_size: 65
            size_hint: (1, .15)


        GridLayout:
            cols: 4
            rows: 5

            #Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "%"
                on_press:root.math_sign("%")
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "C"
                on_press: root.clear()

            Button:
                id: clear
                size_hint: (.2, .2)
                font_size: 32
                text: u"\u00AB"
                on_press:root.remove()


            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "/"
                on_press:root.math_sign("/")
             #Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "7"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(7)
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "8"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(8)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "9"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(9)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "X"
                on_press:root.math_sign("*")
             #Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "4"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(4)
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "5"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(5)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "6"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(6)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "-"
                on_press:root.math_sign("-")

             #Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "1"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(1)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "2"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(2)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "3"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(3)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+"
                on_press:root.math_sign("+")

             #Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+/-"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.pos_neg()
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "0"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(0)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "."
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.dot()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "="
                on_press: root.equals()



"""
Builder.load_string(calc)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        #
        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = ''
        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'

        else:
            self.ids.calc_input.text = f'{prior}{button}'
        # create a addition function

    def math_sign(self, sign):
        prior = self.ids.calc_input.text

        # add  a plus sign to txt box
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)

        except:
            self.ids.calc_input.text = "Error"

        
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    def remove(self):
        prior = self.ids.calc_input.text
        # removing last digit
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
