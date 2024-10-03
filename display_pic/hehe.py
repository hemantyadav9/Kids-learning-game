import tkinter as tk
import os
import random
class score:
    name = "vishnu"
    score = "100"
    total = "1"
    highest = "1313123"
    
def home():
    print("vishnu")

    
def hehe():
    hehe = tk.Tk()
    hehe.geometry("+{}+{}".format(280,150))
    frame = tk.Frame(hehe, width = 700, height=500)
    frame.pack()
    canvas = tk.Canvas(frame, width = 800, height = 400, bg="grey")
    canvas.pack()
    path = "/home/vishnubalu/Desktop/hehe"
    arr = os.listdir(path)
    name = random.sample(arr, 1)
    img=tk.PhotoImage(file=path+"/"+name[0])
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.create_text(540, 50, text ="Hello "+ score.name, font = ('Helvetica', 20, 'bold'), fill='blue')
    canvas.create_text(540, 90, text ="Total Score : "+ score.score, font = ('Helvetica', 20, 'bold'), fill='blue')
    canvas.create_text(540, 130, text ="Total Games Played : "+ score.total, font = ('Helvetica', 20, 'bold'), fill='blue')
    canvas.create_text(540, 170, text =" Score Percent : "+ str((int(score.score)/20)/int(score.total)*100/5)+"%", font = ('Helvetica', 20, 'bold'), fill='blue')
    canvas.create_text(540, 210, text ="Highest Scorer : "+ score.name, font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 240, text ="Total Score : "+ score.score, font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 270, text ="Total Games Played : "+ score.total, font = ('Helvetica', 20, 'bold'), fill='black')
    canvas.create_text(540, 300, text =" Score Percent : "+ str((int(score.score)/20)/int(score.total)*100/5)+"%", font = ('Helvetica', 20, 'bold'), fill='black')
    button = tk.Button(canvas, text = "OK", bg = "lightblue", command = home).place(x = 540, y=350) 
    hehe.mainloop()
hehe()
