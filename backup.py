import arcade
import random
cross = arcade.load_texture("11-removebg-preview.png")
circle = arcade.load_texture("12-removebg-preview.png")
splash1= arcade.load_texture("sp1.png")
splash2 = arcade.load_texture("download.png")
class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 20], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.human = 1
        self.bot = 2
        self.win = "0"
        self.state = "GameMenu"
        self.turn="Human"

    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key == arcade.key.X:
                self.human = 1
                self.bot = 2
                self.state = "GameOn"
               # self.turn="Human"
            elif key == arcade.key.O:
                self.human = 2
                self.bot = 1
                self.state = "GameOn"
              #  self.turn="bot"
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Snail Game", 400, 300,
                             arcade.color.WHITE, font_size=60, anchor_x="center" )
            arcade.draw_text("Press 'O' for Snail 1 and 'X' for snail 2..",
                             400, 250, arcade.color.WHITE, font_size=30, anchor_x="center")

        elif self.state == "GameOn":
            self.shape_list = arcade.ShapeElementList()
            # drawing lines
            arcade.draw_text("Player 1 Scores",
                             620, 500, arcade.color.WHITE, font_size=20)
            arcade.draw_text("Player 2 Scores",
                             620, 300, arcade.color.WHITE, font_size=20)
            arcade.draw_text("Player '1' TURN",
                             620, 150, arcade.color.WHITE, font_size=20)              
            # arcade.draw_text("Player '2' TURN",
            #                  620, 150, arcade.color.WHITE, font_size=20)          
            for i in range(0, 600, 60):
                arcade.draw_line(0, i, 600, i, arcade.color.WHITE, 2)

            for i in range(0, 660, 60):
                arcade.draw_line(i, 0, i, 600, arcade.color.WHITE, 2)

            x = 0
            y = 540
            for i in range(10):
                for j in range(10):
                    if self.board[i][j] == 1:
                        arcade.draw_lrwh_rectangle_textured(
                            x, y, 60, 60, splash1)
                    elif self.board[i][j] == 2:
                        arcade.draw_lrwh_rectangle_textured(
                            x, y, 60, 60, splash2)
                    elif self.board[i][j] == 10:
                        arcade.draw_lrwh_rectangle_textured(
                            x, y, 60, 60, cross)
                    elif self.board[i][j] == 20:
                        arcade.draw_lrwh_rectangle_textured(
                            x, y, 60, 60, circle)                
                    x = x+60
                x = 0
                y = y-60    
    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            if self.turn=="Human":
                if self.human == 1:
                    Sum=0
                    Row_num=0
                    col_num=0
                    check_variable=0
                    try:#restricting user to not click on already clicked block
                        x1=0
                        x2=60
                        y1=0
                        y2=60
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] ==20:
                                        check_variable+=1
                                    elif self.board[i][j] != 0:
                                        check_variable+=1
                                    elif self.board[i][j] == 0:
                                        check_r=j
                                        check_c=i
                                        check_sum=i+j
                                x1=x2
                                x2=x2+60
                            y1=y2
                            y2=y2+60
                            x1=0
                            x2=60
                    except Exception:
                        pass
                    if check_variable==0:#if he clicks on empty block update frontend and board
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if self.board[i][j] == 20:
                                    Sum=i+j
                                    Row_num=j
                                    col_num=i
                                    if j-check_r==1 or j-check_r==-1 :  
                                        if i-check_c==0 :
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 2 
                                    elif i-check_c==-1 or i-check_c==1  :  
                                        if j-check_r==0:
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 2               
                    else:
                        pass   
                    try:
                        x1=0
                        x2=60
                        y1=0
                        y2=60
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum==(i+j)+1 or Sum==(i+j)-1:
                                            if Row_num+1==j  or Row_num-1==j :
                                                if col_num==i:
                                                    self.board[i][j] = 20
                                            elif col_num-1==i or col_num+1==i:
                                                if Row_num==j:
                                                    self.board[i][j] = 20
                                            else:
                                                raise Exception        
                                        else:
                                            raise Exception    
                                    else:
                                        raise Exception 
                                x1=x2
                                x2=x2+60
                            y1=y2
                            y2=y2+60
                            x1=0
                            x2=60
                        self.turn="bot"    
                    except Exception:
                        pass
                if self.human == 2:
                    Row_num=0
                    col_num=0
                    Sum=0
                    check_variable=0
                    try:#restricting user to not click on already clicked block
                        x1=540
                        x2=600
                        y1=540
                        y2=600
                        for i in range(10):
                            for j in range(9,-1,-1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] ==10:
                                        check_variable+=1
                                    elif self.board[i][j]!=0:
                                        check_variable+=1 
                                    elif self.board[i][j]==0:
                                        check_r=j
                                        check_c=i
                                        check_sum=i+j
                                x2=x1
                                x1=x1-60
                            y2=y1
                            y1=y1-60
                            x1=540
                            x2=600
                    except Exception:
                        pass  

                    if check_variable==0:#if he clicks on empty block update frontend and board
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if self.board[i][j] == 10:
                                    Sum=i+j
                                    Row_num=j
                                    col_num=i
                                    #if human take illegal move then not update board for splashes
                                    if j-check_r==1 or j-check_r==-1 :  
                                        if i-check_c==0 :
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 1
                                    elif i-check_c==-1  or  i-check_c==1  :  
                                        if j-check_r==0:
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 1
                    else:
                        pass
                    try:
                        x1=540
                        x2=600
                        y1=540
                        y2=600
                        for i in range(10):
                            for j in range(9,-1,-1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum==(i+j)+1 or Sum==(i+j)-1:
                                            if Row_num+1==j  or Row_num-1==j :
                                                if col_num==i:
                                                    self.board[i][j] = 10
                                            elif col_num-1==i or col_num+1==i:
                                                if Row_num==j:
                                                    self.board[i][j] = 10
                                            else:
                                                raise Exception    
                                        else:
                                            raise Exception
                                x2=x1
                                x1=x1-60
                            y2=y1
                            y1=y1-60
                            x1=540
                            x2=600
                        self.turn="bot"    
                    except Exception:
                        pass 
                
            #bot Turn Here              
            if self.turn=="bot":
                if self.bot == 1:
                    Sum=0
                    Row_num=0
                    col_num=0
                    check_variable=0
                    try:#restricting user to not click on already clicked block
                        x1=0
                        x2=60
                        y1=0
                        y2=60
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] ==20:
                                        check_variable+=1
                                    elif self.board[i][j] != 0:
                                        check_variable+=1
                                    elif self.board[i][j] == 0:
                                        check_r=j
                                        check_c=i
                                        check_sum=i+j
                                x1=x2
                                x2=x2+60
                            y1=y2
                            y2=y2+60
                            x1=0
                            x2=60
                    except Exception:
                        pass
                    if check_variable==0:#if he clicks on empty block update frontend and board
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if self.board[i][j] == 20:
                                    Sum=i+j
                                    Row_num=j
                                    col_num=i
                                    if j-check_r==1 or j-check_r==-1 :  
                                        if i-check_c==0 :
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 2 
                                    elif i-check_c==-1 or i-check_c==1  :  
                                        if j-check_r==0:
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 2               
                    else:
                        pass   
                    try:
                        x1=0
                        x2=60
                        y1=0
                        y2=60
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum==(i+j)+1 or Sum==(i+j)-1:
                                            if Row_num+1==j  or Row_num-1==j :
                                                if col_num==i:
                                                    self.board[i][j] = 20
                                            elif col_num-1==i or col_num+1==i:
                                                if Row_num==j:
                                                    self.board[i][j] = 20
                                            else:
                                                raise Exception        
                                        else:
                                            raise Exception    
                                    else:
                                        raise Exception 
                                x1=x2
                                x2=x2+60
                            y1=y2
                            y2=y2+60
                            x1=0
                            x2=60
                        self.turn="Human"    
                    except Exception:
                        pass
                if self.bot== 2:
                    Row_num=0
                    col_num=0
                    Sum=0
                    check_variable=0
                    try:#restricting user to not click on already clicked block
                        x1=540
                        x2=600
                        y1=540
                        y2=600
                        for i in range(10):
                            for j in range(9,-1,-1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] ==10:
                                        check_variable+=1
                                    elif self.board[i][j]!=0:
                                        check_variable+=1 
                                    elif self.board[i][j]==0:
                                        check_r=j
                                        check_c=i
                                        check_sum=i+j
                                x2=x1
                                x1=x1-60
                            y2=y1
                            y1=y1-60
                            x1=540
                            x2=600
                    except Exception:
                        pass  

                    if check_variable==0:#if he clicks on empty block update frontend and board
                        for i in range(9,-1,-1):
                            for j in range(10):
                                if self.board[i][j] == 10:
                                    Sum=i+j
                                    Row_num=j
                                    col_num=i
                                    #if human take illegal move then not update board for splashes
                                    if j-check_r==1 or j-check_r==-1 :  
                                        if i-check_c==0 :
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 1
                                    elif i-check_c==-1  or  i-check_c==1  :  
                                        if j-check_r==0:
                                            if Sum-check_sum==1 or Sum-check_sum==-1:
                                                self.board[i][j] = 1
                    else:
                        pass
                    try:
                        x1=540
                        x2=600
                        y1=540
                        y2=600
                        for i in range(10):
                            for j in range(9,-1,-1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum==(i+j)+1 or Sum==(i+j)-1:
                                            if Row_num+1==j  or Row_num-1==j :
                                                if col_num==i:
                                                    self.board[i][j] = 10
                                            elif col_num-1==i or col_num+1==i:
                                                if Row_num==j:
                                                    self.board[i][j] = 10
                                            else:
                                                raise Exception    
                                        else:
                                            raise Exception
                                x2=x1
                                x1=x1-60
                            y2=y1
                            y1=y1-60
                            x1=540
                            x2=600
                        self.turn="Human"    
                    except Exception:
                        pass
                    
                 
if __name__ == "__main__":
    window = arcade.Window(800, 600, "Tic Tac Toe")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()