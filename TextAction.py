#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *


class TextAction(BoxLayout):
    
    def __init__(self):
        
        super().__init__()

        self.orientation = "vertical"

        # ヘッダー
        self.TextHeader = TextHeader()
        self.add_widget(self.TextHeader)

        # テキスト入力
        self.TextInput = TextInput(text='Hello world', multiline=True)
        self.add_widget(self.TextInput)


class TextHeader(BoxLayout):

    def __init__(self):
        
        super().__init__()

        self.orientation = "horizontal"

        self.label = Label(text="text")
        self.label.size_hint_x = 0.8
        self.add_widget(self.label)

        self.TextDelButton = TextDelButton(text="del")
        self.TextDelButton.size_hint_x = 0.2
        self.add_widget(self.TextDelButton)


class TextDelButton(Button):
    
    def __init__(self, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)

        # self.background_color = RGBA_to_kivy_format([0, 0, 255, 1])

    def on_press(self):

        pass