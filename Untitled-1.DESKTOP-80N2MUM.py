import tkinter
import sys

#初期化
root = tkinter.Tk()
root.title=('2017弥生祭展示作品')
root.minsize(1000,1500)
event='title'
canvas = tkinter.Canvas(bg='white',width=8000,height=10000)
canvas.place(x=0,y=0)

#title用
def title_drow():
    label_title = tkinter.Label(root, text='～名前はまだ無い～',font=('none','45','bold'),bg='white')
    label_title.place(x=10,y=10)
    label_syazai = tkinter.Label(root, text='ごめんなさい 間に合いませんでした',font=('none','20','bold'),bg)
title_drow()
























#しっぽ
root.mainloop()