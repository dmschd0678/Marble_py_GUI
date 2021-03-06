from tkinter import *
import tkinter.font as tkfont

bg_color = "#B85D5D"

is_use = 0

def yesButton(window):
    global is_use
    is_use = 1

    window.destroy()

def noButton(window):
    global is_use
    is_use = 0

    window.destroy()

# 돈 출력 형식
def moneyStr(money):
    str = ""
    if money // 100000000 > 1:
        str += f"{money // 100000000}" + "억"
        money %= 100000000
    elif money // 10000 > 1:
        str += f"{money // 10000}" + "만"
        money %= 10000
    elif money % 10000 != 0:
        str += money % 10000
    else:
        str += "0"
    str += "원"
    return str

def useKey(name, args):

    global is_use
    w = 400
    h = 600

    x = (1920 - w) // 2
    y = (1080 - h) // 2

    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))

    font = tkfont.Font(size=20, family="malgun gothic")

    boarder = Frame(root, padx=10, pady=10, bg="#FFD15A")
    boarder.pack(fill="both", expand=True)

    frame = Frame(boarder, bg=bg_color, pady=10)
    frame.pack(fill="both", expand=True)

    font = tkfont.Font(size=20, family="malgun gothic")

    KeyName = Label(frame, text="    " + name + "    ", bg="#FFD15A", fg="white", font=font)
    KeyName.pack(side="top")

    image = PhotoImage(file="key_func/{}.png".format(name), master=root)
    KeyImage = Label(frame, bg=bg_color)
    KeyImage.configure(image=image, borderwidth=0)
    KeyImage.image = image
    KeyImage.pack(side="top", pady=10)

    func = Label(frame, bg="#616161", font = font, fg = "white")
    func.pack(side = "top",pady = 10)

    word = Label(frame, bg = bg_color, font = font, fg = "white")
    word.pack(side = "top", pady = 10)

    if name == "우대권":
        func.configure(text = "통행료 : {} -> 무료".format(moneyStr(args)))
        word.configure(text = "우대권을 사용하시겠습니까?")
    else:
        func.configure(text = "무인도에서 즉시 탈출")
        word.configure(text="무인도 탈출권을\n사용하시겠습니까?")

    image = PhotoImage(file = "key_func/cancel.png", master=root)
    noBtn = Button(frame, image = image, bg = bg_color, borderwidth=0, activebackground= bg_color, command = lambda : noButton(root))
    noBtn.image = image
    noBtn.pack(side = "left", padx = 34)

    image = PhotoImage(file = "key_func/use.png", master= root)
    yesBtn = Button(frame, image = image, bg = bg_color, borderwidth=0, activebackground= bg_color, command = lambda : yesButton(root))
    yesBtn.image = image
    yesBtn.pack(side = "right", padx = 34)

    root.mainloop()

    return is_use

if __name__ == "__main__":
    useKey("우대권",1000011200230)