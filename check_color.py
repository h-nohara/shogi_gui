#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *


class MyApp(App):
    
    '''
    全体のUI
    '''
    
    def __init__(self):
        
        # super(ShogiApp, self).__init__()
        super().__init__()

        self.layout = ScrollView(size_hint=(1, 1), do_scroll_x=False, scroll_type=["content", "bars"])

        num = 10
        each_y = int(255/num)

        self.inner_layout = GridLayout(size_hint=(1, 0.1*num**3))
        self.inner_layout.cols = 1

        for i in range(num):
            for j in range(num):
                for k in range(num):
                    rgba = [i*each_y, j*each_y, k*each_y, 100]
                    btn = Button(text=str(rgba[:-1]))
                    btn.background_color = RGBA_to_kivy_format(rgba)
                    self.inner_layout.add_widget(btn)

        self.layout.add_widget(self.inner_layout)



    def build(self):
        
        return self.layout

if __name__ == "__main__":
    
    MyApp().run()


