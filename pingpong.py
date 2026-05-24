import tkinter

#open window
window = tkinter.Tk()
window.title("PingPong")
window.resizable(False, False)
window.geometry("800x500")
window.configure(bg="grey")

#center window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#labeling
frame = tkinter.Frame(window, background="grey")
frame.place(relwidth=1, relheight=1)
label = tkinter.Label(frame, text="Ping Pong", font="Georgia, 50", background=window["bg"], foreground="black", anchor="center")
label.place(relx=0.5, rely=0.3, anchor="center")

#button function
def strt():
    window.destroy()
    game = tkinter.Tk()
    game.title("Ping Pong")
    game.attributes("-fullscreen", True)
    game.configure(bg="black")
    #game
    C = tkinter.Canvas(game, bg="black")
    line = C.create_rectangle(0, 1040, 2000, 1100, fill="red")
    C.pack(fill=tkinter.BOTH, expand=True)
    paddle = C.create_rectangle(800, 975, 1100, 1000, fill="white")
    C.pack(fill=tkinter.BOTH, expand=True)
    def go_right(event):
        posP = C.coords(paddle)
        if posP[2] >= screen_width:
           C.move(paddle, 0, 0)
        else:
           C.move(paddle, +20, 0)
    def go_left(event):
        posP = C.coords(paddle)
        if posP[0] <= 0:
           C.move(paddle, 0, 0)
        else:
         C.move(paddle, -20, 0)
    game.update()
    C.focus_set()
    C.bind("<Right>", go_right)
    C.bind("<Left>", go_left)
    ball = C.create_oval(500, 500, 600, 600, fill="blue")
    C.pack(fill=tkinter.BOTH, expand=True)
    timer = None
    deathscreen = None
    xspeed = 10
    yspeed = -15
    score = 0
    highscore = 0
    score_text = C.create_text(100, 50, text="Score: 0", fill="white", font=("Comic Sans MS", 18))
    highscore_text = C.create_text(110, 75, text="Highscore: 0", fill="yellow", font=("Comic Sans MS", 18))
    def move_ball(event=None):
        nonlocal xspeed, yspeed, deathscreen, score, highscore
        C.move(ball, xspeed, yspeed)
        nonlocal timer 
        timer = game.after(16, move_ball)
        pos = C.coords(ball) 
        if pos[0] < 0:
         xspeed = xspeed * -1
        if pos[1] < 0:
         yspeed = yspeed * -1
        if pos[2] > screen_width:
         xspeed = xspeed * -1
        if pos[3] > screen_height:
         yspeed = yspeed * -1 
        posP = C.coords(paddle)
        if pos[3] >= posP[1] and pos[0] <= posP[2] and pos[2] >= posP[0]:
           yspeed = yspeed * -1
           if deathscreen is None:
             score += 5
             C.itemconfig(score_text, text="Score: " + str(score))
        if pos[3] >= 1040 and deathscreen is None:
           yspeed = 0
           xspeed = 0
           deathscreen = C.create_text(500, 500, text="Press SPACE To Restart", fill="red", font=("Comic Sans MS", 50))
           C.bind("<space>", lambda e: reset_ball())
    def reset_ball():
             nonlocal xspeed, yspeed, timer, deathscreen, score, highscore
             if timer:
                game.after_cancel(timer)
             C.coords(ball, 500, 500, 600, 600)
             xspeed = 10
             yspeed = -15
             if score > highscore:
                highscore = score
                C.itemconfig(highscore_text, text= "Highscore: " + str(highscore))
             score = 0
             C.itemconfig(score_text, text="Score: 0")
             C.delete(deathscreen)
             deathscreen = None
             move_ball()
                 
    game.after(2000, move_ball)
    
    
   



#button
start = tkinter.Button(window, background="green", text="START", font=("Futura, 45"), command=strt)
start.place(relx=0.5, rely=0.6, anchor="center")




window.mainloop() 