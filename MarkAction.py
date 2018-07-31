#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

class MarkAction(BoxLayout):
    
    def __init__(self):
        
        super().__init__()

        self.orientation = "vertical"

        # ヘッダー
        self.MarkHeader = MarkHeader()
        self.add_widget(self.MarkHeader)

        # リスト
        self.MarkList = MarkList()
        self.add_widget(self.MarkList)


class MarkHeader(BoxLayout):

    def __init__(self):
        
        super().__init__()

        self.orientation = "horizontal"

        # 文字ラベル
        self.label = Label(text="mark locs")
        self.label.size_hint_x = 0.8
        self.add_widget(self.label)

        # 追加ボタン
        self.AddButton = AddButton(text="add")
        self.AddButton.size_hint_x = 0.2
        self.add_widget(self.AddButton)


class AddButton(Button):

    def on_press(self):

        pass


class MarkList(BoxLayout):

    def __init__(self):
        
        super().__init__()

        self.orientation = "horizontal"