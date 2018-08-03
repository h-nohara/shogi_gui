#!/user/bin/env python 
# -*- coding: utf-8 -*-

from __init__ import *

import shogi
from util import get_piece_from_board, get_pieces_in_hand, locs_normal, loc_usi2normal, loc_normal2usi, PieceNames_normal_NotNari, PieceName_normal2kanji

class ShogiBoard(BoxLayout):
    
    def __init__(self):
        
        super().__init__()
        self.myname = "ShogiBoard"
        self.orientation = "vertical"

        # boardオブジェクト
        self.board = shogi.Board()

        # 将棋盤
        self.MainBoard = MainBoard(parent_layout=self)
        self.MainBoard.size_hint_y = 0.8

        # 持ち駒
        self.SubBoard_sente = SubBoard(parent_layout=self, is_sente=True)
        self.SubBoard_sente.size_hint_y = 0.1
        self.SubBoard_gote = SubBoard(parent_layout=self, is_sente=False)
        self.SubBoard_gote.size_hint_y = 0.1


        self.add_widget(self.SubBoard_gote)
        self.add_widget(self.MainBoard)
        self.add_widget(self.SubBoard_sente)

        # 成るかどうかのチェック
        self.NariCheckWindow = NariCheckWindow(my_parent=self)


        # ユーザの操作の現在
        self.now_is_touched = False
        self.now_touched_loc = None
        self.now_legal_moves = []


        self.main_sub_boards = [self.MainBoard, self.SubBoard_sente, self.SubBoard_gote]

        # 現在の状況を反映
        for b in self.main_sub_boards:
            b.reflect_board_state()

    
    def reset(self):
        
        '''局面をリセット＋表示をリセット＋ユーザ操作の現在をリセット
        '''
        
        # 局面を初期状態に
        self.board.reset()

        # 表示に反映
        for b in self.main_sub_boards:
            b.reflect_board_state()

        self.init_state_now()


    def init_state_now(self):
        
        '''ユーザの操作の現在をリセット
        '''
        
        self.now_is_touched = False
        self.now_touched_loc = None
        self.now_legal_moves = []


    # todo : 持ち駒も含める
    def get_legal_moves(self, loc):
        
        '''
        locの位置の駒が動ける範囲を表示する

        loc(str) : 動かす駒の元の場所 "55"
        
        return(str) : "56", "77+"
        '''
        
        all_legal_moves = list(self.board.generate_legal_moves())
        all_legal_moves_usi = [move.usi() for move in all_legal_moves]  # usi形式の文字列で取得
        all_legal_moves_normal = [loc_usi2normal(move) for move in all_legal_moves_usi]  # 標準形式の文字列に

        print(all_legal_moves_normal)

        legal_moves_the_piece_destination = []
        for move in all_legal_moves_normal:
            if move[:2] == loc:
                legal_moves_the_piece_destination.append(move[2:])

        print(legal_moves_the_piece_destination)

        return legal_moves_the_piece_destination


    def show_legal_moves(self, loc):
        
        '''
        動ける範囲を保存し、その背景色を変化させる
        '''
        
        # 移動可能なマス目を取得
        self.now_legal_moves = self.get_legal_moves(loc)

        # 移動可能なマス目の背景色を変化
        for loc in self.now_legal_moves:
            self.MainBoard.loc_piece_dict[loc[:2]].background_color = RGBA_to_kivy_format([0, 0, 255, 0.5])


    def push_and_reflect_and_init_user_state(self, start_loc, destination_loc):
        
        '''
        >>> push_and_reflect_and_init_user_state("77", "22+")  # 22成り
        '''
        
        # Boardエンジンに反映させる
        self.board.push_usi(loc_normal2usi(start_loc) + loc_normal2usi(destination_loc))

        # 盤面を表示に反映
        for b in self.main_sub_boards:
            b.reflect_board_state()

        # ユーザの操作状況をリセット
        self.init_state_now()

        # アクション履歴を更新
        action = {"move" : start_loc + destination_loc}
        self.parent.parent.my_parent.Center.HistoryViewer.add_action(action)


    def piece_touched(self, loc):
        
        '''
        loc(str) : "77" or "HI"
        '''
        
        if self.now_is_touched:
            
            # 移動可能な場所を押された時
            if (loc in self.now_legal_moves) or (loc+"+" in self.now_legal_moves):
                

                # 成るか成らないか選べる時は選択ウィンドウを出し、その後の処理はウィンドウウィジェット側で行う
                if (loc in self.now_legal_moves) and (loc+"+" in self.now_legal_moves):
                    self.NariCheckWindow.start_loc = self.now_touched_loc
                    self.NariCheckWindow.destination_loc = loc
                    self.NariCheckWindow.open()

                    
                # 選べない時
                else:
                    
                    # 成れない時は自動でそのまま

                    # 必ず成らなければいけない時
                    if (loc not in self.now_legal_moves) and (loc+"+" in self.now_legal_moves):
                        loc = loc + "+"

                    self.push_and_reflect_and_init_user_state(start_loc=self.now_touched_loc, destination_loc=loc)
                

            else:
                
                # 盤面を表示に反映
                for b in self.main_sub_boards:
                    b.reflect_board_state()  # 盤面を反映させた表示に

                # ユーザの操作状況を反映
                self.now_touched_loc = loc
                self.show_legal_moves(loc)
            

        else:
            
            # ユーザの操作状況を反映
            self.now_is_touched = True
            self.now_touched_loc = loc
            self.show_legal_moves(loc)




class MainBoard(GridLayout):
    
    '''
    将棋盤の部分だけ
    '''
    
    def __init__(self, parent_layout, *kargs, **kwargs):

        super(MainBoard, self).__init__(*kargs, **kwargs)

        self.cols = 9
        self.parent_layout = parent_layout

        # 色
        self.default_color = get_color_from_hex("#ffdddd")

        # 各マス目

        self.loc_piece_dict = {}  # キーがloc_normal,値がsquareオブジェクト
        for y in range(1, 10):
            for x in range(1, 10)[::-1]:
                
                loc = "{}{}".format(x,y)
                square_obj = OneSquare(loc=loc, text="", size=(100, 100), background_color=self.default_color)

                self.loc_piece_dict[loc] = square_obj
                self.add_widget(square_obj)



    def reflect_board_state(self):
        
        '''
        現在の局面（boardインスタンス）の駒位置を画面に反映させる
        '''
                
        for loc in locs_normal:
            is_sente, piece_name = get_piece_from_board(self.parent_layout.board, loc)

            if piece_name is not None:
                piece_name = PieceName_normal2kanji[piece_name]  # 漢字表記に
                if not is_sente:
                    piece_name = "v" + piece_name
                self.loc_piece_dict[loc].text = piece_name

            else:
                
                self.loc_piece_dict[loc].text = ""

            self.loc_piece_dict[loc].background_color = self.default_color  # 背景色をデフォルトに

        


    def child_touched(self, loc):
        
        '''
        locの位置のsquareがクリックされた時
        '''

        self.parent_layout.piece_touched(loc)


        


class SubBoard(BoxLayout):
    
    def __init__(self, parent_layout, is_sente):
        
        super().__init__()

        self.orientation = "horizontal"
        self.parent_layout = parent_layout
        self.is_sente = is_sente

        # 持ち駒の数
        self.piece_n_dict = {}
        for piece in PieceNames_normal_NotNari:
            self.piece_n_dict[piece] = 0

        # 持ち駒とオブジェクト
        self.piece_button_dict = {}

        for piece in PieceNames_normal_NotNari:
            btn = PieceInHand(loc=piece, text="{}:{}".format(piece, self.piece_n_dict[piece]))
            self.piece_button_dict[piece] = btn
            self.add_widget(btn)



    def reflect_board_state(self):
        
        '''
        現在の局面（boardインスタンス）の駒位置を画面に反映させる
        '''
        
        
        pieces_in_hand = get_pieces_in_hand(self.parent_layout.board)

        if self.is_sente:
            pieces_in_hand = pieces_in_hand[0]
        else:
            pieces_in_hand = pieces_in_hand[1]

        for piece in PieceNames_normal_NotNari:
            self.piece_n_dict[piece] = pieces_in_hand[piece]
            self.piece_button_dict[piece].text = "{}:{}".format(PieceName_normal2kanji[piece], self.piece_n_dict[piece])

    
    def child_touched(self, loc):
        
        '''
        locの位置のsquareがクリックされた時
        '''

        self.parent_layout.piece_touched(loc)




class OneSquare(Button):
    
    def __init__(self, loc, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.loc = loc

    
    def on_press(self):
        
        self.parent.child_touched(self.loc)



class PieceInHand(Button):
    
    def __init__(self, loc, *kargs, **kwargs):
        
        super().__init__(*kargs, **kwargs)
        self.loc = loc

    
    def on_press(self):
        
        if (self.parent.is_sente and self.parent.parent_layout.board.turn == 0) or (not self.parent.is_sente and self.parent.parent_layout.board.turn == 1):
        
            self.parent.child_touched(self.loc)



class NariCheckWindow(ModalView):
    
    def __init__(self, my_parent):
        
        '''
        NariCheckWindow - main_view - NariCheckButton * 2
        my_parentはShogiBoardビューを想定
        '''
        
        super().__init__()

        self.my_parent = my_parent
        self.start_loc = None
        self.destination_loc = None

        self.size_hint = (0.3, 0.3)

        class NariCheckButton(Button):
            
            def __init__(self, naru, *kargs, **kwargs):
                
                super().__init__(*kargs, **kwargs)
                self.naru = naru

            def on_press(self):
                
                self.parent.parent.click(self.naru)


        self.now_nari = None


        # 全体
        self.main_view = BoxLayout()
        self.main_view.orientation = "horizontal"

        # yes, noボタン
        self.yes_button = NariCheckButton(naru=True, text="naru")
        self.no_button = NariCheckButton(naru=False, text="naranai")
        self.yes_button.size_hint = (0.2, 0.2)
        self.no_button.size_hint = (0.2, 0.2)

        self.main_view.add_widget(self.yes_button)
        self.main_view.add_widget(self.no_button)

        self.add_widget(self.main_view)

    
    def click(self, naru):
                
        self.handle_board(naru)  # boardオブジェクト、表示等に反映させる
        self.dismiss()  # ウィンドウを閉じる

    def handle_board(self, naru):
        
        if naru:
            self.destination_loc = self.destination_loc + "+"

        self.my_parent.push_and_reflect_and_init_user_state(start_loc=self.start_loc, destination_loc=self.destination_loc)

        self.start_loc = None
        self.destination_loc = None

    




# class ShogiBoard(GridLayout):
    
#     '''
#     将棋盤の部分だけ
#     '''
    
#     def __init__(self, *kargs, **kwargs):

#         super(ShogiBoard, self).__init__(*kargs, **kwargs)

#         self.cols = 9

#         # 色
#         self.default_color = get_color_from_hex("#ffdddd")

#         # 各マス目

#         self.loc_piece_dict = {}  # キーがloc_normal,値がsquareオブジェクト
#         for y in range(1, 10):
#             for x in range(1, 10)[::-1]:
                
#                 loc = "{}{}".format(x,y)
#                 square_obj = OneSquare(loc=loc, text="", size=(100, 100), background_color=self.default_color)

#                 self.loc_piece_dict[loc] = square_obj
#                 self.add_widget(square_obj)

#         self.board = shogi.Board()  # boardオブジェクト

#         # boardオブジェクトを反映
#         self.reflect_board_state()


#         # ユーザの操作の現在
#         self.now_is_touched = False
#         self.now_touched_loc = None
#         self.now_legal_moves = []



#     def reflesh(self):
        
#         self.board.reset()

#         self.reset_text_on_board()
#         self.reflect_board_state()
#         self.init_state_now()


#     # 盤上の全ての文字を""にする
#     def reset_text_on_board(self):
#         for square_obj in self.loc_piece_dict.values():
#             square_obj.text = ""
#             square_obj.background_color = self.default_color

#     # 現在の局面（boardインスタンス）の駒位置を画面に反映させる
#     def reflect_board_state(self):
        
#         for loc in locs_normal:
#             is_sente, piece_name = get_piece_from_board(self.board, loc)
#             if piece_name is not None:
#                 if not is_sente:
#                     piece_name = "v" + piece_name
#                 self.loc_piece_dict[loc].text = piece_name


#     def init_state_now(self):
        
#         self.now_is_touched = False
#         self.now_touched_loc = None
#         self.now_legal_moves = []


#     def get_legal_moves(self, loc):
        
#         '''
#         locの位置の駒が動ける範囲を表示する
#         '''
        
#         all_legal_moves = list(self.board.generate_legal_moves())
#         all_legal_moves_usi = [move.usi() for move in all_legal_moves]
#         all_legal_moves_normal = [loc_usi2normal(move) for move in all_legal_moves_usi]
#         legal_moves_the_piece_destination = []
#         for move in all_legal_moves_normal:
#             if move[:2] == loc:
#                 legal_moves_the_piece_destination.append(move[2:])

#         return legal_moves_the_piece_destination

    
#     def show_legal_moves(self, loc):
        
#         '''
#         動ける範囲の背景色を変化させる
#         '''
        
#         self.now_legal_moves = self.get_legal_moves(loc)

#         for loc in self.now_legal_moves:
#             self.loc_piece_dict[loc[:2]].background_color = get_color_from_hex("#FFCC66")
        


#     def child_touched(self, loc):
        
#         '''
#         locの位置のsquareがクリックされた時
#         '''

#         if self.now_is_touched:
            
#             if (loc in self.now_legal_moves) or (loc+"+" in self.now_legal_moves):
                
#                 self.board.push_usi(loc_normal2usi(self.now_touched_loc) + loc_normal2usi(loc))

#                 self.reset_text_on_board()
#                 self.reflect_board_state()
#                 self.init_state_now()

#             else:
#                 self.reset_text_on_board()
#                 self.reflect_board_state()
#                 self.now_touched_loc = loc
#                 self.show_legal_moves(loc)
            

#         else:
            
#             self.now_is_touched = True
#             self.now_touched_loc = loc
#             self.show_legal_moves(loc)




# ヘルパーウィジェットたち


# class OnePiecesInHand(Button):
    
#     def __init__(self):
        
#         super().__init__()

#         self.orientation = "horizontal"

#         for i in range(7):
#             btn = Button(text="hand_"+str(i))
#             self.add_widget(btn)
