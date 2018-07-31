#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

from TextAction import TextAction
from MarkAction import MarkAction
from LightUpAction import LightUpAction


class Right(BoxLayout):
    
    def __init__(self):
        
        super().__init__()

        self.orientation = "vertical"

        self.add_widget(TextAction())
        self.add_widget(MarkAction())
        self.add_widget(LightUpAction())


