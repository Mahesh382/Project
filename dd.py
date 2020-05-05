from tkinter import *
from PIL import ImageTk,Image
import random
import time


root = Tk()
root.title("Graphics Project")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=500, height=400, bd=0,highlightthickness=0)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Mahesh Mahato\\Desktop\\e.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

root.update()

count = 0
lost = False

class Ball:

    def __init__(self,canvas,paddle,block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,
                 color):
        self.canvas = canvas
        self.paddle = paddle
        self.block1 = block1
        self.block2 = block2
        self.block3 = block3
        self.block4 = block4
        self.block5 = block5
        self.block6 = block6
        self.block7 = block7
        self.block8 = block8
        self.block9 = block9
        self.block10 = block10
        self.block11 = block11
        self.block12 = block12
        self.block13 = block13
        self.block14 = block14

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


        self.paddle_pos = self.canvas.coords(self.paddle.id)


        if pos[2] >= self.paddle_pos[0] and pos[0] <= self.paddle_pos[2]:
            if pos[3] >= self.paddle_pos[1] and pos[3] <= self.paddle_pos[3]:
                self.y = -3


        block1_pos = self.canvas.coords(self.block1.id)
        if block1_pos and (pos[2] >= block1_pos[0] and pos[0] <= block1_pos[2]):
            if block1_pos and (pos[3] >= block1_pos[1] and pos[3] <= block1_pos[3]):
                global count
                self.y=3
                count += 1
                score()
                self.canvas.delete(self.block1.id)




        block2_pos = self.canvas.coords(self.block2.id)
        if block2_pos and (pos[2] >= block2_pos[0] and pos[0] <= block2_pos[2]):
            if block2_pos and (pos[3] >= block2_pos[1] and pos[3] <= block2_pos[3]):
                count += 1
                score()
                self.canvas.delete(self.block2.id)
                self.y = 3



        block3_pos = self.canvas.coords(self.block3.id)
        if block3_pos and (pos[2] >= block3_pos[0] and pos[0] <= block3_pos[2]):
            if block3_pos and (pos[3] >= block3_pos[1] and pos[3] <= block3_pos[3]):
                self.canvas.delete(self.block3.id)
                self.y = 3

                count += 1
                score()

        block4_pos = self.canvas.coords(self.block4.id)
        if block4_pos and (pos[2] >= block4_pos[0] and pos[0] <= block4_pos[2]):
            if block4_pos and (pos[3] >= block4_pos[1] and pos[3] <= block4_pos[3]):
                self.canvas.delete(self.block4.id)
                self.y = 3

                count += 1
                score()


        block5_pos = self.canvas.coords(self.block5.id)
        if block5_pos and (pos[2] >= block5_pos[0] and pos[0] <= block5_pos[2]):
            if block5_pos and (pos[3] >= block5_pos[1] and pos[3] <= block5_pos[3]):
                self.canvas.delete(self.block5.id)
                self.y = 3

                count += 1
                score()


        block6_pos = self.canvas.coords(self.block6.id)
        if block6_pos and (pos[2] >= block6_pos[0] and pos[0] <= block6_pos[2]):
            if block6_pos and (pos[3] >= block6_pos[1] and pos[3] <= block6_pos[3]):
                self.canvas.delete(self.block6.id)
                self.y = 3

                count += 1
                score()


        block7_pos = self.canvas.coords(self.block7.id)
        if block7_pos and (pos[2] >= block7_pos[0] and pos[0] <= block7_pos[2]):
            if block7_pos and (pos[3] >= block7_pos[1] and pos[3] <= block7_pos[3]):
                self.canvas.delete(self.block7.id)
                self.y = 3

                count += 1
                score()


        block8_pos = self.canvas.coords(self.block8.id)
        if block8_pos and (pos[2] >= block8_pos[0] and pos[0] <= block8_pos[2]):
            if block8_pos and (pos[3] >= block8_pos[1] and pos[3] <= block8_pos[3]):
                self.canvas.delete(self.block8.id)
                self.y = 3

                count += 1
                score()


        block9_pos = self.canvas.coords(self.block9.id)
        if block9_pos and (pos[2] >= block9_pos[0] and pos[0] <= block9_pos[2]):
            if block9_pos and (pos[3] >= block9_pos[1] and pos[3] <= block9_pos[3]):
                self.canvas.delete(self.block9.id)
                self.y = 3
                count += 1
                score()


        block10_pos = self.canvas.coords(self.block10.id)
        if block10_pos and (pos[2] >= block10_pos[0] and pos[0] <= block10_pos[2]):
            if block10_pos and (pos[3] >= block10_pos[1] and pos[3] <= block10_pos[3]):
                self.canvas.delete(self.block10.id)
                self.y = 3

                count += 1
                score()


        block10_pos = self.canvas.coords(self.block10.id)
        if block10_pos and (pos[2] >= block10_pos[0] and pos[0] <= block10_pos[2]):
            if block10_pos and (pos[3] >= block10_pos[1] and pos[3] <= block10_pos[3]):
                self.canvas.delete(self.block10.id)
                self.y = 3

                count += 1
                score()


        block11_pos = self.canvas.coords(self.block11.id)
        if block11_pos and (pos[2] >= block11_pos[0] and pos[0] <= block11_pos[2]):
            if block11_pos and (pos[3] >= block11_pos[1] and pos[3] <= block11_pos[3]):
                self.canvas.delete(self.block11.id)
                self.y = 3

                count += 1
                score()


        block12_pos = self.canvas.coords(self.block12.id)
        if block12_pos and (pos[2] >= block12_pos[0] and pos[0] <= block12_pos[2]):
            if block12_pos and (pos[3] >= block12_pos[1] and pos[3] <= block12_pos[3]):
                self.canvas.delete(self.block12.id)
                self.y = 3

                count += 1
                score()


        block13_pos = self.canvas.coords(self.block13.id)
        if block13_pos and (pos[2] >= block13_pos[0] and pos[0] <= block13_pos[2]):
            if block13_pos and (pos[3] >= block13_pos[1] and pos[3] <= block13_pos[3]):
                self.canvas.delete(self.block13.id)
                self.y = 3

                count += 1
                score()


        block14_pos = self.canvas.coords(self.block14.id)
        if block14_pos and (pos[2] >= block14_pos[0] and pos[0] <= block14_pos[2]):
            if block14_pos and (pos[3] >= block14_pos[1] and pos[3] <= block14_pos[3]):
                self.canvas.delete(self.block14.id)
                self.y = 3

                count += 1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)   #ball speed
        else:

            game_over()
            global lost
            lost = True


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)


    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x =3
        if self.pos[2] >= self.canvas_width:
            self.x = -3

        global lost
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -2

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 2
class Block:

    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = int(x)
        self.y = int(y)
        self.id = canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 20, fill=color)
        self.canvas.move(self.id, self.x, self.y)


block1 = Block(canvas, 125, 20, 'green')
block2 = Block(canvas, 150, 20, 'green')
block3 = Block(canvas, 175, 20, 'green')
block4 = Block(canvas, 200, 20, 'green')
block5 = Block(canvas, 75, 20, 'green')
block6 = Block(canvas, 50, 20, 'green')
block7 = Block(canvas, 25, 20, 'green')
block8 = Block(canvas, 125, 30, 'yellow')
block9 = Block(canvas, 100, 30, 'yellow')
block10 = Block(canvas, 175, 30, 'yellow')
block11 = Block(canvas, 150, 30, 'yellow')
block12 = Block(canvas, 75, 30, 'yellow')
block13= Block(canvas, 50, 30, 'yellow')
block14= Block(canvas, 100, 20, 'green')


def start_game(event):
    label1.configure(text="")

    global lost,count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    #time.sleep(0000000000000.1)
    paddle.draw()
    ball.draw()


def score():
    canvas.itemconfig(score_now, text="Score: " + str(count))
    if count == 14:
        canvas.create_text(245, 100, text="You Win", font=('Arial', 30,  'italic'))
        self.count(1)


def game_over():
    canvas.itemconfig(game, text="You Lose !")


paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle,block1,block2, block3, block4, block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,"red")

score_now = canvas.create_text(250, 10, text=" ", fill = "red", font=("Times 20 italic"))
game = canvas.create_text(250, 150, text=" ", fill="black", font=("Arial", 20))

label1=Label(root,text='Press Space Button Start',font=("Times 20 italic"))
label1.pack()
canvas.bind_all("<space>", start_game)
quit_qame = Button(root, text='Quit', bg='Black', fg='White', command=quit)
quit_qame.pack(side='right')
root.mainloop()