import customtkinter
from tkinter.filedialog import *
from customtkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import lzma as xz

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def clearFrame(self):
        for widget in customtkinter.CTk.winfo_children(self):
            widget.destroy()
        
    def fileSave(self):
        fileS = fd.askdirectory(title = "Save Location")
        return fileS

    def openFile(self):
        filename = fd.askopenfilenames(multiple=True)
        return filename
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("File Compression and Decompression")
        self.geometry(f"{400}x{480}")
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

        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", hover_color="green",command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress",hover_color="green",command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)

        self.extBtn = customtkinter.CTkButton(self.sidebar_frame, text ="Exit",hover_color="red", command=self.destroy)
        self.extBtn.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

        
    def compress(self):
        dir = ""
        fpath = self.openFile()
        
    
        for fname in fpath:
            with open(fname, 'rb') as f, open(fname + ".xz", 'wb') as out:
                out.write( xz.compress(bytes(f.read())))
                dir += fname + ".xz\n"
            self.path(dir)
    
    def decfile(self):
        fpath = self.openFile()
        dir = ""
        for fname in fpath:
            fileNoExtension = os.path.splitext(fname)[0]    # remove extention of filename
            fileNoDirectory = os.path.basename(fileNoExtension) #remove path of file and retains filename
            getSaveLoc = self.fileSave()    #ask for savelocation
            finalFile = getSaveLoc+"/"+fileNoDirectory # concat the filename and savelocation
            with open(fname, 'rb') as f, open(finalFile, 'wb') as out:
                try:
                    out.write( xz.decompress(bytes(f.read())))
                    dir += finalFile + "\n"   
                except:
                    out.close()
                    messagebox.showerror("Invalid File", "Please choose an XZ compressed file")      
                    os.remove(finalFile)
            if dir == "":
                break
            else:
                self.path(dir)

    def path(self, dir):
        self.fileType_frame = customtkinter.CTkFrame(self)
        self.fileType_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.fileType_group = customtkinter.CTkLabel(master=self.fileType_frame, text="File saved as:", font=("arial", 20))
        self.fileType_group.grid(row=0, column=0, padx=20, pady=30, sticky="nw")

        self.labelFrame = customtkinter.CTkFrame(master=self.fileType_frame)
        self.labelFrame.grid(row=1, column=0, padx=20, ipadx=30, sticky="ew")

        self.label = customtkinter.CTkLabel(master=self.labelFrame, text=dir+"", wraplength=400, anchor="e", pady=20, padx=0)
        self.label.grid(row=1, column=2, padx=(20, 0))    

    def compressFileType(self):
        self.geometry(f"{703}x{480}")

        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", hover_color="green",fg_color="green", command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress", hover_color="green", command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)


        self.intro_frame = customtkinter.CTkFrame(self)
        self.intro_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.fileType_group = customtkinter.CTkLabel(master=self.intro_frame, text="Choose a file:", font=("arial", 20), anchor=W)
        self.fileType_group.grid(row=0, column=2, columnspan=1, padx=10, pady=(50, 30))
        
        self.openbutton= customtkinter.CTkButton(self.intro_frame, text="OPEN", command=self.compress, width=420, height=60, font=("arial", 20))
        self.openbutton.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        
    def decompressFileType(self):
        self.geometry(f"{703}x{480}")

        self.compressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Compress", hover_color="green", command=self.compressFileType)
        self.compressBtn.grid(row=1, column=0, padx=20, pady=10)

        self.decompressBtn = customtkinter.CTkButton(self.sidebar_frame, text = "Decompress", hover_color="green",fg_color="green",command=self.decompressFileType)
        self.decompressBtn.grid(row=2, column=0, padx=20, pady=10)

        self.intro_frame = customtkinter.CTkFrame(self)
        self.intro_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.fileType_group = customtkinter.CTkLabel(master=self.intro_frame, text="Choose a file:", font=("arial", 20), anchor=W)
        self.fileType_group.grid(row=0, column=2, columnspan=1, padx=10, pady=(50, 30))
        
        self.openbutton= customtkinter.CTkButton(self.intro_frame, text="OPEN", command=self.decfile, width=420, height=60, font=("arial", 20))
        self.openbutton.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()