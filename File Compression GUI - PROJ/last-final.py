from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTk
from customtkinter import filedialog as fd
import os
import shutil
import tarfile
import lzma as xz

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

class Window(CTk):
    def clearFrame(self):
        for widget in customtkinter.CTk.winfo_children(self):
            widget.destroy()

    def openFile(self):
        filename = fd.askopenfiles(multiple=True)
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

        label = customtkinter.CTkLabel(master=self, text="Please Choose: ", font=("rockwell", 25))
        label.place(x = 50, y = 50)
        
        compressBtn = customtkinter.CTkButton(self, text = "Compress", font = ("rockwell", 12), command= self.compress)
        compressBtn.place(relx=0.1, rely = 0.45)

        decompressBtn = customtkinter.CTkButton(self, text = "Decompress", font = ("rockwell", 12), command = self.decompress)
        decompressBtn.place(relx=0.5, rely = 0.45)

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
            
            dir = ""
           
            for fname in fpath:
                print(fname)
                    #ldir = os.mkdir(fname)
                    #ldir = os.path.dirname(fname)
                #shutil.copyfile(fname, ldir)
            #shutil.make_archive(base_name=fname, format="xztar", root_dir= ldir)


           

            if len(fpath) == 1:
                spath = self.fileSave()
                print(spath)
                #os.makedirs(spath)
                #fff = os.path.splitext(fname)[0]
                for fname in fpath:
                    shutil.copy(fname, spath)
                    #for fname in fpath:

                shutil.make_archive(base_name=spath, format="xztar", root_dir= spath)
                #with open(spath, 'wb') as f, open(spath + ".xz", 'wb') as out:
                    #out.write( xz.compress(bytes(f.read())))
                dir += spath + ".tar.xz\n"


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
            
            dir = ""

            if len(fpath) == 1:
                for fname in fpath:
                    spath = self.fileSave()
                    tar = tarfile.open(fname)
                    tar.extractall(path = spath)
                    tar.close()

            else:
                spath = self.fileSave()
                #os.makedirs(spath)
                #fff = os.path.splitext(fname)[0]
                for fname in fpath:
                    shutil.copy(fname, spath)
                    #for fname in fpath:

                shutil.make_archive(spath, "xztar")
                #with open(spath, 'wb') as f, open(spath + ".xz", 'wb') as out:
                    #out.write( xz.compress(bytes(f.read())))
                dir += spath + ".tar.xz\n"

            label = customtkinter.CTkLabel(master=self, text="file/s is saved as "+ dir+"", font=("rockwell", 10), wraplength=400, anchor="e", justify = LEFT)
            label.place(x = 10, y = 150, )
                
    
def main():
    Window().mainloop()
    

main() 