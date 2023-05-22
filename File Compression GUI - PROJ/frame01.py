import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
root = Tk()


class Window(Frame):
    def __init__(self):
        Frame.__init__(self)
        root.geometry("380x212")
        img = Image.open("C:\Coding\Python Coding\File Compression GUI - PROJ\logo.jpg")
        photo = ImageTk.PhotoImage(img)
        root.iconphoto(False, photo)
        self.master.title("File Compression")
        self.pack()

        bg = Image.open("C:\Coding\Python Coding\File Compression GUI - PROJ\_bg.jpg")
        self.background = ImageTk.PhotoImage(bg)
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")

        canvas.create_text(133, 23, text = "Choose file to compress", font = ("rockwell", 16, "bold"), fill = "white")   #add text
        canvas.create_line(10,45,370,45, fill = "white")
        canvas.create_text(101, 78, text = "Please Choose:", font = ("rockwell", 16, "bold"), fill = "#7cc0e9")         #add text

        

def main():
    Window().mainloop()

main() 
