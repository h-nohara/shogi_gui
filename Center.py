#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

class Center(BoxLayout):
    
    def __init__(self):
        
        super().__init__()

        self.orientation = "vertical"

        self.HistoryViewer = HistoryViewer()
        self.add_widget(self.HistoryViewer)
        


class HistoryViewer(ScrollView):
    
    def __init__(self, *kargs, **kwargs):
    
        super(HistoryViewer, self).__init__(*kargs, **kwargs)

        # self.orientation = "vertical"
        self.in_scroll = BoxLayout(orientation="vertical")
        for i in range(10):
            btn = Button(text=str(i))
            self.in_scroll.add_widget(btn)
        
        self.add_widget(self.in_scroll)