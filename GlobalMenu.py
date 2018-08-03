#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *


class GlobalMenu(BoxLayout):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.SaveButton = SaveButton()
        self.add_widget(self.SaveButton)

        self.ExitButton = ExitButton()
        self.add_widget(self.ExitButton)




class SaveButton(Button):

    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)
        self.text = "保存する"

    def on_press(self):
        pass



class ExitButton(Button):
    
    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)
        self.text = "終了"

    def on_press(self):
        pass



