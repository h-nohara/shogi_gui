#!/user/bin/env python 
# -*- coding: utf-8 -*-

import os, sys, glob2
import numpy as np

# 日本語入力
from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc")

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView

from kivy.app import App

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.window import Window

from kivy.properties import BooleanProperty
from kivy.properties import StringProperty, ListProperty
from kivy.utils import get_color_from_hex
from kivy.resources import resource_add_path
from kivy.graphics import Color

from kivy.factory import Factory

from util import RGBA_to_kivy_format


