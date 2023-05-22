import customtkinter
from tkinter.filedialog import *
from customtkinter import filedialog as fd
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
import os
import lzma as xz

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def clearFrame(self):
        for widget in customtkinter.CTk.winfo_children(self):
            widget.destroy()
        
    def fileSave(self):
        fileS = fd.asksaveasfilename()
        return fileS

    def openFile(self):
        filename = fd.askopenfilenames(multiple=True)
        return filename
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("File Compression and Decompression")
        self.geometry(f"{703}x{480}")
        logo = Image.open("logo.png")
        photo = ImageTk.PhotoImage(logo)
        self.wm_iconphoto(False, photo)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Please Choose: ", font=("Arial",23))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress", command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)

        self.extBtn = customtkinter.CTkButton(self.sidebar_frame, text ="Exit", command=self.destroy)
        self.extBtn.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create frame
        self.intro_frame = customtkinter.CTkFrame(self)
        self.intro_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.intro_group = customtkinter.CTkLabel(master=self.intro_frame, text="\nWelcome to File Compression and Decompression!", )
        self.intro_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

        
    def compress(self):
        fpath = self.openFile()
            
        dir = ""
    
        for fname in fpath:
            with open(fname, 'rb') as f, open(fname + ".xz", 'wb') as out:
                out.write( xz.compress(bytes(f.read())))
                dir += fname + ".xz\n"
            self.path(dir)
    
    def pdf(self):
        fpath = self.openFile()
        dir = ""

        for fname in fpath:
            fff = os.path.splitext(fname)[0]
            with open(fname, 'rb') as f, open(fff, 'wb') as out:
                out.write( xz.decompress(bytes(f.read())))
                dir += fff + "\n"                     
        self.path(dir)

    def deCompAsFile(self):
        self.filesave = ""
        self.fileType_frame = customtkinter.CTkFrame(self)
        self.fileType_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.fileType_group = customtkinter.CTkLabel(master=self.fileType_frame, text="Choose a file:")
        self.fileType_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        
        self.openbutton= customtkinter.CTkButton(self.fileType_frame, text="PDF", command=self.decompress, width=420)
        self.openbutton.grid(row=1, column=2, pady=10, padx=20, sticky="n")


    def path(self, dir):
        self.fileType_frame = customtkinter.CTkFrame(self)
        self.fileType_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.fileType_group = customtkinter.CTkLabel(master=self.fileType_frame, text="File saved as:")
        self.fileType_group.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="")

        self.label = customtkinter.CTkLabel(master=self.fileType_frame, text=dir+"", wraplength=400, anchor="e", justify = LEFT)
        self.label.grid(row=2, column=1, pady=10, padx=30, sticky="n")    

    def compressFileType(self):
        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", fg_color="green", command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress", command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)


        self.fileType_frame = customtkinter.CTkFrame(self)
        self.fileType_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.fileType_group = customtkinter.CTkLabel(master=self.fileType_frame, text="Choose a file:")
        self.fileType_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        
        self.openbutton= customtkinter.CTkButton(self.fileType_frame, text="Open", command=self.compress, width=420)
        self.openbutton.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        
    def decompressFileType(self):
        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress", fg_color="green",command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)

        self.fileType_frame = customtkinter.CTkFrame(self)
        self.fileType_frame.grid(row=1, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.fileType_group = customtkinter.CTkLabel(master=self.fileType_frame, text="Choose a file:")
        self.fileType_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        
        self.openbutton= customtkinter.CTkButton(self.fileType_frame, text="Open", command=self.pdf, width=420)
        self.openbutton.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()