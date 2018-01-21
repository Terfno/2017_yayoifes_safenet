#このファイルは共有テスト用のファイルです
#共有を確認したらvscodeかお好きなコンパイラとか使って動かして見てください

#クラスに関するサンプルコード
#このコードをvisual studio codeかなにかに貼り付けて
# そのファイルを皆さんの作業フォルダ内に入れ
# 「Ctrlキー+@キー」で簡易ターミナルを開き「python ファイル名.py」 で実行してみてください
#これでpythonのクラスとオブジェクト指向が学習できるはずです

#クラス定義
#testというクラスを定義
class test:
    #testというクラスの中にhogeというモジュールを定義
    #（）内には引数が入る
    #もし引数が必要ない場合にはselfという引数を入れなければエラ－が出る
    def hoge(self):
        #hogeというモジュールの動きを記述
        print("test")

#クラスの使用
#hugaという変数にtestというクラスを代入
#(基本的にはクラス名とクラスを代入する変数の名前は同一にする)
#別ファイルの場合は オブジェクト変数＝ファイル名.クラス名() で呼び出せる それ以降は同様
huga = test()
#先程のhugaという変数内にあるtestというクラスにあるhogeというモジュールを使用（）内には引数を入れれる
#なのでtestというクラス内のhogeという関数が呼び出さされ，その中の処理が実行されるので先程記述したprint("test")が実行される
#オブジェクト変数.関数名
huga.hoge()

# 変数の用意
image_x = 0
image_y = 0
# インポート
import tkinter #tkinterをインポート
# ウィンドウ作成
root = tkinter.Tk() #ウィンドウ作成
root.title("practice") #ウィンドウのタイトルの作成
root.minsize(600,600) #ウィンドウのサイズの指定
root.option_add("*font", ["MS Pゴシック", 22]) #ウィンドウ内のフォントを指定i
# 画像表示
canvas = tkinter.Canvas(bg="white",width=1920,height=1080)#背景色用の画像を生成
canvas.place(x=0,y=0)#背景用画像の場所指定
img = tkinter.PhotoImage(file="img/joujaku.PNG")
image_x=300
image_y=300
canvas.create_image(image_x,image_y,image=img,tag="j")
# ボタンの表示
button_ue = tkinter.Button(text="↑")
button_ue.place(x=300,y=500)
button_sita = tkinter.Button(text="↓")
button_sita.place(x=300,y=550)
button_migi = tkinter.Button(text="→")
button_migi.place(x=350,y=550)
button_hidari = tkinter.Button(text="←")
button_hidari.place(x=250,y=550)
button_jibaku = tkinter.Button(text="自爆")
button_jibaku.place(x=20,y=20)
button_hukkatu = tkinter.Button(text="復活")
button_hukkatu.place(x=20,y=80)
# イベント設定
## イベント用関数
def ue_click():
    canvas.delete("j")
    global image_y
    image_y = image_y - 5
    canvas.create_image(image_x,image_y,image=img,tag="j")
def sita_click():
    canvas.delete("j")
    global image_y
    image_y = image_y + 5
    canvas.create_image(image_x,image_y,image=img,tag="j")
def migi_click():
    canvas.delete("j")
    global image_x
    image_x = image_x + 5
    canvas.create_image(image_x,image_y,image=img,tag="j")
def hidari_click():
    canvas.delete("j")
    global image_x
    image_x = image_x - 5
    canvas.create_image(image_x,image_y,image=img,tag="j")
def jibaku_click():
    canvas.delete("j")
def hukkatu_click():
    global image_x
    global image_y
    canvas.create_image(image_x,image_y,image=img,tag="j")
## イベント発火
button_ue["command"] = ue_click
button_sita["command"] = sita_click
button_migi["command"] = migi_click
button_hidari["command"] = hidari_click
button_jibaku["command"] = jibaku_click
button_hukkatu["command"] = hukkatu_click
#メインループ
root.mainloop()
