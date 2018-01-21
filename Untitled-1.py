import tkinter
import sys
import random

#tkinter用の準備
root = tkinter.Tk()
root.title=('2017弥生祭展示作品')
root.minsize(500,500)
canvas = tkinter.Canvas(bg='white',width=8000,height=10000)
canvas.place(x=0,y=0)
class HOGE:
    def __init__(self):
        print('__init__')
        #変数宣言
        self.event='title'#イベント変数
        #タイトル画面用宣言
        self.label_title = tkinter.Label(root, text='～名前はまだ無い～',font=('none','30','bold'),bg='white')#タイトル用ラベル用意
        self.label_syazai = tkinter.Label(root, text='ごめんなさい 間に合いませんでした',font=('none','20','bold'),bg='white')#謝罪文用ラベル用意
        self.button_play = tkinter.Button(text='PLAY',font=('none','50','bold'))#play画面遷移用ボタン用意
        #play画面用宣言
        self.stage = tkinter.Frame(root,width=500,height=500)
        #自機用
        self.label_player=tkinter.Label(root,text='P',font=('none','20','bold'),bg='red')
        self.px=250
        self.py=250
        #弾用
        self.label_bullet=tkinter.Label(root,text='|',font=('noen','20','bold'))
        self.bx=0
        self.by=0
        self.bullet=0
        #rnemy用
        self.label_enemy=tkinter.Label(root,text='●',font=('noen','30','bold'))
        self.ex=random.randint(5,496)
        self.ey=random.randint(5,495)
    def draw(self):
        # print('draw')
        #描画
        if(self.event=='title'):
            #タイトル用のラベル配置
            self.label_title.place(x=10,y=10)
            #謝罪文用のラベル配置
            self.label_syazai.place(x=10,y=80)
            #play画面遷移用のボタン配置
            self.button_play.place(x=150,y=150,width=200,height=200)
        elif(self.event=='play'):
            #test
            pass
    def update(self):
        # print('update')
        #更新(イベントドリブン)
        if(self.event=='title'):
            def title_event_play():
                self.event='play'
                self.label_title.destroy()
                self.label_syazai.destroy()
                self.button_play.destroy()
                gameloop()
            self.button_play['command']=title_event_play
        elif(self.event=='play'):
            def bullet():
                sys.setrecursionlimit(114514)
                self.label_bullet.destroy()
                if(self.bullet==0):
                    self.bullet+=1
                    self.bx=self.px
                    self.by=self.py
                elif(self.bullet<70):
                    self.by-=5
                    self.bullet+=1
                else:
                    self.bullet=0
                self.label_bullet=tkinter.Label(root,text='|',font=('noen','20','bold'))
                self.label_bullet.place(x=self.bx,y=self.by)
                self.label_bullet.lower(self.label_player)
                gameloop()
            def get_motion(event):
                self.label_player.destroy()
                self.px=event.x
                self.py=event.y
                self.label_player=tkinter.Label(root,text='P',font=('none','20','bold'),bg='red')
                self.label_player.place(x=self.px,y=self.py)
            def enemy():
                self.label_enemy.place(x=self.ex,y=self.ey)
                if(self.ex==self.bx and self.ey==self.by):
                    print('die')
                    self.label_enemy.destroy()
                self.ex=random.randint(5,496)
                self.ey=random.randint(5,496)
            # root.bind('<KeyPress>',bullet)
            self.stage.bind('<Motion>',get_motion)
            self.stage.pack()
            enemy()
            root.after(5,bullet)

hoge=HOGE()
def gameloop():
    hoge.draw()
    hoge.update()

gameloop()

#しっぽ
root.mainloop()