#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

from ShogiBoard import ShogiBoard



class Left(BoxLayout):
    
    def __init__(self):
    
        super().__init__()

        self.orientation = "vertical"

        # リフレッシュボタン
        self.reflesh_button = RefleshButton(my_parent=self, text='reflesh!')
        self.reflesh_button.size_hint_y = 0.3
        self.add_widget(self.reflesh_button)

        # 将棋盤
        self.ShogiBoard = ShogiBoard()
        self.ShogiBoard.size_hint_y = 0.7
        self.add_widget(self.ShogiBoard)


    def reflesh_button_touched(self):
        
        self.ShogiBoard.reflesh()


# ヘルパーウィジェットたち

class RefleshButton(Button):
    
    def __init__(self, my_parent, *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)
        self.my_parent = my_parent

    def on_press(self):
        
        self.my_parent.reflesh_button_touched()

