#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

import shogi
from util import get_piece_from_board, locs_normal, loc_usi2normal, loc_normal2usi

from Left import Left
from Center import Center
from Right import Right




class AllHandler:

    def __init__(self):
        
        self.ShogiApp = ShogiApp
        

    def run_app(self):
        
        self.ShogiApp().run()



class ShogiApp(App):
    
    '''
    全体のUI
    '''
    
    def __init__(self):
        
        # super(ShogiApp, self).__init__()
        super().__init__()

        self.title = "make_movie"
        self.myname = "ShogiApp"
        self.layout = BoxWithMyParent(my_parent=self, orientation='horizontal')

        # 左（将棋盤等）
        self.Left = Left()
        self.Left.size_hint_x = 0.6
        self.layout.add_widget(self.Left)


        # 棋譜履歴
        self.Center = Center()
        self.Center.size_hint_x = 0.15
        self.layout.add_widget(self.Center)


        # 右側
        self.Right = Right()
        self.Right.size_hint_x = 0.25
        self.layout.add_widget(self.Right)



    def build(self):
        
        return self.layout



class BoxWithMyParent(BoxLayout):
    
    def __init__(self, my_parent, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.my_parent = my_parent


        




# if __name__ == "__main__":
    
    # # for c in ShogiBoard().children:
    # #     print(c)

    # # for m in dir(GridLayout()))
        
    # ShogiApp().run()

    # # collide_widget
    # # get_parent_window
    # # parent


if __name__ == "__main__":
    
    handler = AllHandler()
    handler.run_app()


