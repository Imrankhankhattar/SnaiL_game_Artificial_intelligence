import arcade
import random
cross = arcade.load_texture("11-removebg-preview.png")
circle = arcade.load_texture("12-removebg-preview.png")
splash1 = arcade.load_texture("sp1.png")
splash2 = arcade.load_texture("download.png")
display = arcade.load_texture("12.png")


class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = [[0 for i in range(10)] for j in range(10)]
        self.board[0][9]=20
        self.board[9][0]=10
        self.win = "0"
        self.state = "GameMenu"
        self.turn = "Human"
        self.score_1 = 0
        self.score_2 = 0

    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key == arcade.key.ENTER:
                self.state = "GameOn"
                self.turn="bot"
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Snail Game", 400, 300,
                             arcade.color.WHITE, font_size=60, anchor_x="center")
            arcade.draw_text("Press  'ENTER' To Start Game",
                             400, 250, arcade.color.WHITE, font_size=30, anchor_x="center")
        elif self.state == "GameOn":
            self.shape_list = arcade.ShapeElementList()
            # updating scores
            ouput1 = f"Score: {self.score_1}"
            ouput2 = f"Score: {self.score_2}"
            # ouput2=self.score_2
            arcade.draw_text(ouput1,
                             630, 160, arcade.color.WHITE, font_size=26)
            arcade.draw_text(ouput2,
                             630, 390, arcade.color.WHITE, font_size=26)

            # drawing for Player 1
            arcade.draw_text("Player 1 ",
                             640, 540, arcade.color.WHITE, font_size=30)
            arcade.draw_lrwh_rectangle_textured(640, 440, 100, 80, display)
            arcade.draw_rectangle_outline(700, 490, 178, 200,
                                          arcade.color.GREEN, 4)
            # drawing for Player 2
            arcade.draw_rectangle_outline(700, 260, 178, 210,
                                          arcade.color.GREEN, 4)
            arcade.draw_text("Player 2",
                             640, 310, arcade.color.WHITE, font_size=30)
            arcade.draw_lrwh_rectangle_textured(640, 200, 100, 100, circle)
            # drawing for turn
            arcade.draw_rectangle_outline(700, 70, 178, 115,
                                          arcade.color.GREEN, 4)

            arcade.draw_text("TURN",
                             655, 90, arcade.color.BABY_BLUE, font_size=25)
            if self.turn == "Human":
                arcade.draw_text("Player '2'",
                                 645, 40, arcade.color.RASPBERRY, font_size=24)
            elif self.turn == "bot":
                arcade.draw_text("Player '1'",
                                 645, 40, arcade.color.RAJAH, font_size=24)
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
           
            if self.score_1 > 50 or self.score_2>50:
                self.state="win"

        elif self.state == "win":
            if self.score_1 > self.score_2 :
                arcade.draw_text("Player '2' WON",
                                 400, 300, arcade.color.RAJAH, font_size=40, anchor_x="center")
            elif self.score_1 < self.score_2 :
                arcade.draw_text("Player '1' WON",
                                 400, 300, arcade.color.RAJAH, font_size=40, anchor_x="center")
            else:
                arcade.draw_text("DRAW",
                                 400, 300, arcade.color.RAJAH, font_size=40, anchor_x="center")

    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            if self.turn == "Human":
                for i in range(9, -1, -1):#loop for finding snail position
                    for j in range(10):
                        if self.board[i][j] == 20:
                            slip_x_old=i
                            slip_y_old=j
                            break
                    Sum = 0
                    Row_num = 0
                    col_num = 0
                    check_variable = 0
                    try:  # restricting user to not click on already clicked block
                        x1 = 0
                        x2 = 60
                        y1 = 0
                        y2 = 60
                        for i in range(9, -1, -1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 20:
                                        check_variable += 1
                                    elif self.board[i][j] == 2:#checking if user clicks on his own track.....
                                        check_variable = 11    
                                        slip_x_new=i
                                        slip_y_new=j
                                    elif self.board[i][j] != 0:
                                        check_variable += 1
                                    elif self.board[i][j] == 0:
                                        check_r = j
                                        check_c = i
                                        check_sum = i+j
                                x1 = x2
                                x2 = x2+60
                            y1 = y2
                            y2 = y2+60
                            x1 = 0
                            x2 = 60
                    except Exception:
                        pass
                    if check_variable == 0:  # if he clicks on empty block update frontend and board
                        for i in range(9, -1, -1):
                            for j in range(10):
                                if self.board[i][j] == 20:
                                    Sum = i+j
                                    Row_num = j
                                    col_num = i
                                    if j-check_r > 1 or j-check_r < -1:
                                        self.turn = "bot"
                                        print("step1")
                                        return
                                    elif i-check_c < -1 or i-check_c > 1:
                                        self.turn = "bot" 
                                        print("step1")  
                                        return
                                    elif j-check_r == 1 or j-check_r == -1:
                                        if i-check_c == 0:
                                            if Sum-check_sum == 1 or Sum-check_sum == -1:
                                                self.board[i][j] = 2
                                    elif i-check_c == -1 or i-check_c == 1:
                                        if j-check_r == 0:
                                            if Sum-check_sum == 1 or Sum-check_sum == -1:
                                                self.board[i][j] = 2
                    elif check_variable==11:
                        if slip_x_old==slip_x_new and slip_y_new==slip_y_old+1:
                            print("forward")
                            for i in range(9-slip_y_old):
                                if self.board[slip_x_old][slip_y_new]==2:
                                    pass
                                else:
                                    break
                                slip_y_new=slip_y_new+1   
                            self.board[slip_x_old][slip_y_new-1]=20
                            self.board[slip_x_old][slip_y_old]=2
                            self.turn = "bot"
                            return
                        elif slip_x_old==slip_x_new and slip_y_new==slip_y_old-1:
                            print("back")
                            for i in range(slip_y_old+1):
                                if self.board[slip_x_old][slip_y_new]==2:
                                    pass
                                else:
                                    break
                                slip_y_new=slip_y_new-1   
                            self.board[slip_x_old][slip_y_new+1]=20
                            self.board[slip_x_old][slip_y_old]=2
                            self.turn = "bot"
                            return
                            
                        elif slip_y_old==slip_y_new and slip_x_new==slip_x_old+1:
                            print("down")
                            for i in range(9-slip_x_old):
                                if self.board[slip_x_new][slip_y_old]==2:
                                    pass
                                else:
                                    break
                                slip_x_new=slip_x_new+1   
                            self.board[slip_x_new-1][slip_y_old]=20
                            self.board[slip_x_old][slip_y_old]=2
                            self.turn = "bot"
                            return
                            
                        elif slip_y_old==slip_y_new and slip_x_new==slip_x_old-1:
                            print("up")
                            for i in range(slip_x_old+1):
                                if self.board[slip_x_new][slip_y_old]==2:
                                    pass
                                else:
                                    break
                                slip_x_new=slip_x_new-1   
                            self.board[slip_x_new+1][slip_y_old]=20
                            self.board[slip_x_old][slip_y_old]=2
                            self.turn = "bot"
                            return
                        else:
                            self.turn = "bot"
                            return
                    try:
                        x1 = 0
                        x2 = 60
                        y1 = 0
                        y2 = 60
                        for i in range(9, -1, -1):
                            for j in range(10):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum == (i+j)+1 or Sum == (i+j)-1:
                                            if Row_num+1 == j or Row_num-1 == j:
                                                if col_num == i:
                                                    self.board[i][j] = 20
                                                    self.score_1 = self.score_1+1
                                            elif col_num-1 == i or col_num+1 == i:
                                                if Row_num == j:
                                                    self.board[i][j] = 20
                                                    self.score_1 = self.score_1+1

                                            else:
                                                raise Exception
                                        else:
                                            raise Exception
                                    else:
                                        raise Exception
                                x1 = x2
                                x2 = x2+60
                            y1 = y2
                            y2 = y2+60
                            x1 = 0
                            x2 = 60
                        # print("turning to bot:Human1")
                        self.turn = "bot"
                    except Exception:
                        pass
            if self.turn == "bot":
                    Row_num = 0
                    col_num = 0
                    Sum = 0
                    check_variable = 0
                    for i in range(9, -1, -1):#loop for finding snail position
                        for j in range(10):
                            if self.board[i][j] == 10:
                                slip_x_old=i
                                slip_y_old=j
                                break
                    try:  # restricting user to not click on already clicked block
                        x1 = 540
                        x2 = 600
                        y1 = 540
                        y2 = 600
                        for i in range(10):
                            for j in range(9, -1, -1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 1:
                                        check_variable = 11    
                                        slip_x_new=i
                                        slip_y_new=j    
                                    elif self.board[i][j] == 10:
                                        check_variable += 1  
                                    elif self.board[i][j] != 0:
                                        check_variable += 1
                                    elif self.board[i][j] == 0:
                                        check_r = j
                                        check_c = i
                                        check_sum = i+j
                                x2 = x1
                                x1 = x1-60
                            y2 = y1
                            y1 = y1-60
                            x1 = 540
                            x2 = 600
                    except Exception:
                        pass

                    if check_variable == 0:  # if he clicks on empty block update frontend and board
                        for i in range(9, -1, -1):
                            for j in range(10):
                                if self.board[i][j] == 10:
                                    Sum = i+j
                                    Row_num = j
                                    col_num = i
                                    # if human take illegal move then not update board for splashes
                                    if j-check_r > 1 or j-check_r < -1:
                                        self.turn = "Human"
                                        print("step3")
                                        return
                                    elif i-check_c < -1 or i-check_c > 1:
                                        self.turn = "Human"
                                        print("step3")
                                        return
                                    elif j-check_r == 1 or j-check_r == -1:
                                        if i-check_c == 0:
                                            if Sum-check_sum == 1 or Sum-check_sum == -1:
                                                self.board[i][j] = 1
                                    elif i-check_c == -1 or i-check_c == 1:
                                        if j-check_r == 0:
                                            if Sum-check_sum == 1 or Sum-check_sum == -1:
                                                self.board[i][j] = 1
                    elif check_variable==11:
                        if slip_x_old==slip_x_new and slip_y_new==slip_y_old+1:
                            print("forward")
                            for i in range(9-slip_y_old):
                                if self.board[slip_x_old][slip_y_new]==1:
                                    pass
                                else:
                                    break
                                slip_y_new=slip_y_new+1   
                            self.board[slip_x_old][slip_y_new-1]=10
                            self.board[slip_x_old][slip_y_old]=1
                            self.turn = "Human"
                            return
                        elif slip_x_old==slip_x_new and slip_y_new==slip_y_old-1:
                            print("back")
                            for i in range(slip_y_old+1):
                                if self.board[slip_x_old][slip_y_new]==1:
                                    pass
                                else:
                                    break
                                slip_y_new=slip_y_new-1   
                            self.board[slip_x_old][slip_y_new+1]=10
                            self.board[slip_x_old][slip_y_old]=1
                            self.turn = "Human"
                            return
                            
                        elif slip_y_old==slip_y_new and slip_x_new==slip_x_old+1:
                            print("down")
                            for i in range(9-slip_x_old):
                                if self.board[slip_x_new][slip_y_old]==1:
                                    pass
                                else:
                                    break
                                slip_x_new=slip_x_new+1   
                            self.board[slip_x_new-1][slip_y_old]=10
                            self.board[slip_x_old][slip_y_old]=1
                            self.turn = "Human"
                            return
                            
                        elif slip_y_old==slip_y_new and slip_x_new==slip_x_old-1:
                            print("up")
                            for i in range(slip_x_old+1):
                                if self.board[slip_x_new][slip_y_old]==1:
                                    pass
                                else:
                                    break
                                slip_x_new=slip_x_new-1   
                            self.board[slip_x_new+1][slip_y_old]=10
                            self.board[slip_x_old][slip_y_old]=1
                            self.turn = "Human"
                            return
                        else:
                            self.turn = "Human"
                            return                            
                    try:
                        x1 = 540
                        x2 = 600
                        y1 = 540
                        y2 = 600
                        for i in range(10):
                            for j in range(9, -1, -1):
                                if x1 <= x <= x2 and y1 <= y <= y2:
                                    if self.board[i][j] == 0:
                                        if Sum == (i+j)+1 or Sum == (i+j)-1:
                                            if Row_num+1 == j or Row_num-1 == j:
                                                if col_num == i:
                                                    self.board[i][j] = 10
                                                    self.score_2 = self.score_2+1

                                            elif col_num-1 == i or col_num+1 == i:
                                                if Row_num == j:
                                                    self.board[i][j] = 10
                                                    self.score_2 = self.score_2+1

                                            else:
                                                raise Exception
                                        else:
                                            raise Exception
                                    else:
                                        raise Exception
                                x2 = x1
                                x1 = x1-60
                            y2 = y1
                            y1 = y1-60
                            x1 = 540
                            x2 = 600
                        self.turn = "Human"
                    except Exception:
                        pass              
            try:
                win = 0
                for i in range(10):
                    for j in range(10):
                        if self.board[i][j] == 0:
                            win = 1
                if win == 0:
                    self.state = "win"
            except Exception:
                pass
if __name__ == "__main__":
    window = arcade.Window(800, 600, "Tic Tac Toe")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()
