from random import choice
from captcha.image import ImageCaptcha
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

image = ImageCaptcha(width=250,height=90)

text = str('')
for x in range(8):text = text + choice(list("qwetyuiopasdfghjkklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"))

image.write(text, "captch1.png")

img = Image.open("captch1.png")
captch_answer = text
def captch_func():
    global _captca
    if _captca.get() == captch_answer:
        if messagebox.showinfo("captchaGAME","you win"):exit()
    elif _captca.get() == "show_answer": print(captch_answer)
    else:messagebox.showinfo("captchaGAME","captcha incorect")
root = Tk()
root.title("captchaGAME")
root["bg"] = "white"

_captca = StringVar()

text = Label(text="♠captcaGAME♠").pack()
captca_input = Entry(textvariable=_captca)
image = ImageTk.PhotoImage(img)
captca_image = Label(image=image).pack()
captca_input.pack()

enter_btn = Button(text="I'm not robot",command=captch_func)
enter_btn.pack()

root.mainloop()