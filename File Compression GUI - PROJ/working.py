from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTk
from customtkinter import filedialog as fd
import os
import lzma as xz

#root = Tk()
#frame = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

class Window(CTk):
    def clearFrame(self):
        for widget in customtkinter.CTk.winfo_children(self):
            widget.destroy()

    def openFile(self):
        filename = fd.askopenfilenames(multiple=True)
        return filename
        
    def fileSave(self):
        fileS = fd.asksaveasfilename()
        return fileS

    def __init__(self):
        super().__init__()
        self.geometry("380x212")
        self.title("File Compression")
        logo = Image.open("logo.png")
        photo = ImageTk.PhotoImage(logo)
        self.wm_iconphoto(False, photo)

     #   bgImg = Image.open("_bg.jpg")
     #   self.background = "grey" #ImageTk.PhotoImage(bgImg)    #set background of window
     #   canvas = customtkinter.CTkCanvas(self)
     #   canvas.pack(fill = "both", expand = FALSE)
     #   canvas.create_image(0, 0, image = self.background, anchor = "nw")

        label = customtkinter.CTkLabel(master=self, text="Please Choose: ", font=("rockwell", 25))
        label.place(x = 50, y = 50)
        
        compressBtn = customtkinter.CTkButton(self, text = "Compress", font = ("rockwell", 12), command= self.compress)
        compressBtn.place(relx=0.1, rely = 0.45)

        decompressBtn = customtkinter.CTkButton(self, text = "Decompress", font = ("rockwell", 12), command = self.decompress)
        decompressBtn.place(relx=0.5, rely = 0.45)

        #jpgBtn = customtkinter.CTkButton(self, text = "JPG", font = ("rockwell", 12))
        #jpgBtn.place(relx=0.1, rely = 0.5)

        #pngBtn = customtkinter.CTkButton(self, text = "PNG", font = ("rockwell", 12))
        #pngBtn.place(relx=0.5, rely = 0.5)

        extBtn = customtkinter.CTkButton(self, text ="Exit", font = ("rockwell", 12), fg_color="#CC2936", command = self.destroy)
        extBtn.place(relx = 0.5, rely = 0.7)

    
    def compress(self):
        self.clearFrame()
        
        label = customtkinter.CTkLabel(master=self, text="Choose file: ", font=("rockwell", 25))
        label.place(x = 50, y = 50)

        compressBtn = customtkinter.CTkButton(self, text = "Open", font = ("rockwell", 12), command=self.openfile)
        compressBtn.place(relx=0.3, rely = 0.5)
       

    def openfile(self):
            fpath = self.openFile()
            #spath = self.fileSave()
            
            dir = ""
    
            for fname in fpath:
                #fff = os.path.splitext(fname)[0]
                with open(fname, 'rb') as f, open(fname + ".xz", 'wb') as out:
                    out.write( xz.compress(bytes(f.read())))
                    dir += fname + "\n"


            label = customtkinter.CTkLabel(master=self, text="file/s is saved as "+ dir+"", font=("rockwell", 10), wraplength=400, anchor="e", justify = LEFT)
            label.place(x = 10, y = 150, )
            
    
    def decompress(self):
        self.clearFrame()
        
        label = customtkinter.CTkLabel(master=self, text="Choose file: ", font=("rockwell", 25))
        label.place(x = 50, y = 50)

        compressBtn = customtkinter.CTkButton(self, text = "Open", font = ("rockwell", 12), command=self.openfile2)
        compressBtn.place(relx=0.3, rely = 0.5)
       

    def openfile2(self):
            fpath = self.openFile()
            #spath = self.fileSave()
            dir = ""

            for fname in fpath:
                fff = os.path.splitext(fname)[0]
                with open(fname, 'rb') as f, open(fff , 'wb') as out:
                    out.write( xz.decompress(bytes(f.read())))
                    dir += fname + "\n"
                                
            label = customtkinter.CTkLabel(master=self, text="file/s is saved as "+ dir+"", font=("rockwell", 10), wraplength=400, anchor="e", justify = LEFT)
            label.place(x = 10, y = 150, )
                
    
def main():
    Window().mainloop()
    

main() 