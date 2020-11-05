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
        # self.win = "0"
        self.state = "GameMenu"

    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key == arcade.key.X:
                self.human = 1
                self.bot = 2
                self.state = "GameOn"
            elif key == arcade.key.O:
                self.human = 2
                self.bot = 1
                self.state = "GameOn"
    def on_show(self):
        arcade.set_background_color(arcade.color.PERSIAN_INDIGO)

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Snail Game", 300, 300,
                             arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text("Press O for Snail 1 & X for snail 2..",
                             300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

        elif self.state == "GameOn":
            self.shape_list = arcade.ShapeElementList()
            # drawing lines
            for i in range(60, 600, 60):
                arcade.draw_line(0, i, 600, i, arcade.color.WHITE, 2)

            for i in range(60, 600, 60):
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
#on mouse press function
    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            if self.human == 1:
                for i in range(9,-1,-1):
                    for j in range(10):
                         if self.board[i][j] == 20:
                            self.board[i][j] = 2 
                try:
                    x1=0
                    x2=60
                    y1=0
                    y2=60
                    for i in range(9,-1,-1):
                        for j in range(10):
                            if x1 <= x <= x2 and y1 <= y <= y2:
                                if self.board[i][j] == 0:
                                    self.board[i][j] = 20 
                            x1=x2
                            x2=x2+60
                        y1=y2
                        y2=y2+60
                        x1=0
                        x2=60
                except Exception:
                    pass
            if self.human == 2:
                for i in range(9,-1,-1):
                    for j in range(10):
                        if self.board[i][j] == 10:
                           self.board[i][j] = 1
                try:
                    x1=540
                    x2=600
                    y1=540
                    y2=600
                    for i in range(10):
                        for j in range(9,-1,-1):
                            if x1 <= x <= x2 and y1 <= y <= y2:
                                if self.board[i][j] == 0:
                                    self.board[i][j] = 10
                            x2=x1
                            x1=x1-60
                        y2=y1
                        y1=y1-60
                        x1=540
                        x2=600
                except Exception:
                    pass  
if __name__ == "__main__":
    window = arcade.Window(600, 600, "Tic Tac Toe")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()