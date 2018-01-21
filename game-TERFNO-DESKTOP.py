import tkinter
import sys


class Game:
    def __init__(self):
        self.event='title'
        self.opera_x=0
        self.opera_y=0
        self.canvas = tkinter.Canvas(bg="white",width=1080,height=1920)
        self.canvas.place(x=0,y=0)

    def update(self, root):
        print("update")
        if(self.event=="play"):
            self.opera_x+=10
            self.opera_y+=10
    
    def draw(self, root):
        print("draw")
        self.canvas.delete('all')
        if(self.event=='title'):
            print("title")
            #タイトル用のラベル
            label_title=tkinter.Label(root, text="～名前はまだない～",font=('none','45','bold'),bg='white')
            label_title.place(x=10,y=10)
            #謝罪用のラベル
            label_syazai=tkinter.Label(root, text="間に合いませんでした\nごめんなさい", font=('none','25','bold'),bg='white')
            label_syazai.place(x=120,y=80)
            #play画面遷移用のボタン
            button_play=tkinter.Button(text='play')
            button_play.place(x=200,y=300,width=200,height=200)
            #イベント用関数
            def play_click():
                self.event="play"
                label_title.destroy()
            #イベント発火
            button_play["command"]=play_click
        elif(self.event=="play"):
            opera = tkinter.PhotoImage(file="img/s_opera.ppm")
            self.canvas.create_image(self.opera_x,self.opera_y,image=opera,tag="opera")
        root.mainloop()

