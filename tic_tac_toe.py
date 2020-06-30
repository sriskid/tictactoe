import arcade

# Creating the window
screen_width = 600
screen_height = 650
game_title = "Tic Tac Toe"



class MyGame(arcade.Window):
    """CREATING THE GAME"""
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.turn_counter = 0
        arcade.set_background_color(arcade.color.BLACK)
        self.shape_list = None

    def on_draw(self):
        """CREATING THE GRID LAYOUT"""
        arcade.start_render()
        horizontal_point_list = [
            [100,125], [500,125],
            [100,275], [500,275],
            [100,425], [500,425],
            [100,575], [500,575]
        ]

        vertical_point_list = [
            [100,125], [100,575],
            [233,125], [233,575],
            [366,125], [366,575],
            [500,125], [500,575]
        ]

        arcade.create_lines(horizontal_point_list, arcade.color.GREEN).draw()
        arcade.create_lines(vertical_point_list, arcade.color.GREEN).draw()
        for shape in self.shape_list:
            shape.draw()
        # arcade.finish_render()  

    def set_up(self):
        """CREATE LIST SHAPE"""
        self.shape_list = []

    def mouse_snap(self, x, y):
        """MOUSE SNAPPING"""
        if 100 < x < 233 and 125 < y < 275:
            return 166, 200
        if 233 < x < 366 and 125 < y < 275:
            return 299, 200
        if 366 < x < 500 and 125 < y < 275:
            return 433, 200
        if 100 < x < 233 and 275 < y < 425:
            return 166, 350
        if 233 < x < 366 and 275 < y < 425:
            return 299, 350
        if 366 < x < 500 and 275 < y < 425:
            return 433, 350
        if 100 < x < 233 and 425 < y < 575:
            return 166, 500
        if 233 < x < 366 and 425 < y < 575:
            return 299, 500
        if 366 < x < 500 and 425 < y < 575:
            return 433, 500

    def on_mouse_press(self, x, y, button, modifiers):
        """CREATING THE SHAPES"""
        x,y = self.mouse_snap(x,y)
        center_x = x
        center_y = y
        triangle_x1 = x - 50
        triangle_y1 = y - 50
        triangle_x2 = x + 50
        triangle_y2 = y - 50
        triangle_x3 = x
        triangle_y3 = y + 50
            
        if button == arcade.MOUSE_BUTTON_LEFT and self.turn_counter % 2 == 0:
            self.shape_list.append(arcade.create_ellipse(center_x,center_y,50,50,arcade.color.RED))
            self.turn_counter = self.turn_counter + 1
        elif button == arcade.MOUSE_BUTTON_LEFT and self.turn_counter % 2 != 0:
            self.shape_list.append(arcade.create_polygon([[triangle_x1,triangle_y1],[triangle_x2,triangle_y2],[triangle_x3,triangle_y3]],
            arcade.color.BLUE))
            self.turn_counter = self.turn_counter + 1
            
                 


def main():
    """RUNNING THE GAME"""
    m = MyGame(screen_width,screen_height, game_title)
    m.set_up()
    arcade.run()
        
    

if __name__ == "__main__":
    main()


