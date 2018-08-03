#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

from ShogiBoard import ShogiBoard
from GlobalMenu import GlobalMenu



class Left(BoxLayout):
    
    def __init__(self, *kargs, **kwargs):
    
        super().__init__(*kargs, **kwargs)

        self.orientation = "vertical"

        # グローバルメニュー
        self.global_menu = GlobalMenu()
        self.global_menu.size_hint_y = 0.15
        self.add_widget(self.global_menu)

        # リフレッシュボタン
        self.LeftSecondRow = LeftSecondRow()
        self.LeftSecondRow.size_hint_y = 0.15
        self.add_widget(self.LeftSecondRow)

        # 将棋盤
        self.ShogiBoard = ShogiBoard()
        self.ShogiBoard.size_hint_y = 0.7
        self.add_widget(self.ShogiBoard)


    def reflesh_button_clicked(self):
        
        # 盤面と表示をリセット
        self.ShogiBoard.reset()
        # アクション履歴をリセット
        self.parent.my_parent.Center.reflesh_button_clicked()


# ヘルパーウィジェットたち

class LeftSecondRow(BoxLayout):
    
    def __init__(self, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.orientation = "horizontal"

        # リフレッシュボタン
        self.RefleshButton = RefleshButton()
        self.RefleshButton.size_hint_x = 0.5
        self.add_widget(self.RefleshButton)

        # メッセージアクション追加ボタン
        self.AddMessageActionButton = AddMessageActionButton()
        self.AddMessageActionButton.size_hint_x = 0.5
        self.add_widget(self.AddMessageActionButton)



class RefleshButton(Button):
    
    def __init__(self, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.text = "reflesh!"

    def on_press(self):
        
        self.parent.parent.reflesh_button_clicked()


class AddMessageActionButton(Button):
    
    def __init__(self, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.text = "メッセージアクションを追加"


