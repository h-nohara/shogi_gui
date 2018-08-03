#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

class Center(BoxLayout):
    
    def __init__(self):
        
        super().__init__()

        self.orientation = "vertical"

        self.HistoryViewer = HistoryViewer()
        self.add_widget(self.HistoryViewer)

    def reflesh_button_clicked(self):
        
        self.clear_widgets()
        self.HistoryViewer = HistoryViewer()
        self.add_widget(self.HistoryViewer)
        


class HistoryViewer(ScrollView):
    
    def __init__(self, *kargs, **kwargs):
    
        super(HistoryViewer, self).__init__(*kargs, **kwargs)

        # シナリオ
        self.ScenarioDict = {"actions" : [], "is_main" : True}
        # シナリオ以外のアクションとidの対応辞書
        self.IdActionDict = {}
        # スクロール表示するボタンのリスト
        self.buttons = []

        self.button_y_ratio = 0.1
        self.default_n_button = 1

        for _ in range(self.default_n_button):
            btn = Label(text="アクション履歴", size_hint_y=self.button_y_ratio)
            self.buttons.append(btn)

        self.scroll = ScrollView()  # ScrollView()
        self.in_scroll = BoxLayout(orientation="vertical")
        self.in_scroll.size_hint_y = 0

        self.scroll.add_widget(self.in_scroll)
        self.add_widget(self.scroll)


        # 現在の状況を表示に反映させる
        self.reflect_action_state()

        # 現在クリックされているアクションボタンのid
        self.now_clicked_action_id = None


        


    def reflect_action_state(self):
        
        '''
        シナリオの履歴から各履歴ボタンウィジェットを作成し、画面に反映させる
        '''

        self.reflect_ScenarioDict_to_buttons()
        self.reflect_buttons_to_view()


    def add_action(self, action):
        
        '''
        action(dict) : {"move":"7776"} or {"message" : {"text":"hoge", "light_up":"55"}}
        '''

        if "move" in action.keys():
            
            id_number = self.get_next_id_number()  # todo
            history_button = ActionHistoryButton(id_number=id_number, text=action["move"], size_hint_y=self.button_y_ratio)
            self.add_history(history_button)  # todo

        self.reflect_buttons_to_view()  # 画面に反映

    # todo
    def get_next_id_number(self):
        return len(self.IdActionDict.keys())

    # todo
    def add_history(self, widget):
        self.IdActionDict[widget.id_number] = widget
        self.buttons.append(widget)
        
        

    def update_ScenarioDict(self):
        
        '''
        アクションのシナリオをアップデートする
        '''
        
        pass

    def reflect_ScenarioDict_to_buttons(self):
        
        '''
        シナリオから各ボタンを生成する
        '''

        pass

    def reflect_buttons_to_view(self):
        
        '''
        現在存在するボタンを表示に反映させる
        '''
        
        for btn in self.buttons:
            if btn not in self.in_scroll.children:
                self.in_scroll.add_widget(btn)
                self.in_scroll.size_hint_y += self.button_y_ratio  # インナーの縦の長さを拡張

        # 縦幅が修正されたインナーをスクロールに登録
        self.scroll.clear_widgets()
        self.scroll.add_widget(self.in_scroll)

        




class ActionHistoryButton(Button):

    def __init__(self, id_number, *kargs, **kwargs):

        super().__init__(*kargs, **kwargs)
        self.id_number = id_number

    
    def on_press(self):
        
        self.parent.now_clicked_action_id = self.id_number