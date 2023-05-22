import tkinter.messagebox
from tkinter import *
root = Tk()

accepted_pin = "1234567890" #accepted input of pin

class Graphics(Frame):  
    def __init__(self):
        Frame.__init__(self)    
        root.geometry("380x212")    #set window size
        logo = PhotoImage(file = "logo_icon.png")   #add icon to window
        self.master.iconphoto(False, logo)
        self.master.title("Caesar Cipher")  #window title
        self.pack()

        self.background = PhotoImage(file = "picBG.png")    #set background of window
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")
        canvas.create_text(133, 23, text = "Text Encrypt/Decrypt", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")   #add text
        canvas.create_text(101, 78, text = "Please Choose:", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")         #add text

        encrypt_btn = Button(self, text="Encrypt", font = ("rockwell", 12), command = self.encrypt, fg = "#232323")     #add button for encrypting
        encrypt_btn.place(x = 110, y = 110)

        encrypt_btn = Button(self, text="Decrypt", font = ("rockwell", 12), command = self.decrypt, fg = "#232323")     #add button for decrypting
        encrypt_btn.place(x = 201, y = 110 )

    def encrypt(self): #method for getting text to be encrypted
        Frame.pack_forget(self) #delete previous frame
        
        Frame.__init__(self)
        self.pack()

        self.background = PhotoImage(file = "picBG.png")    #set window background
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")
        canvas.create_text(90, 23, text = "Encrypt Text", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")

        def input():    #for getting and validating input
            try:    #if pin entered is not int, it will display and error message
                user_pin = int(pin.get())   #get pin from user
                user_txt = txt.get("1.0", 'end-1c')
                self.encrypt2(user_pin, user_txt)   #pass the inputs to encrypt2 method where the text will be encrypted
            except:
                tkinter.messagebox.showerror("Invalid Pin", "Enter only numeric pin.")  #error message


        pin = Entry(self, width=40, show="*")   #make the pin entered appear as asterisk
        pin.place(x = 103, y = 67 )
        canvas.create_text(55, 75, text = "Pin (ex. 1234): ", font = ("talios", 10), fill = "#7cc0d8")  #text for description

        txt = Text(self, width=30, height=4 )
        txt.place(x = 103, y = 97 )
        canvas.create_text(64, 105, text = "Enter Text:", font = ("talios", 10), fill = "#7cc0d8")      #text for description

        ok_btn = Button(self, text="Encrypt!", font = ("talios", 10), command=input)    #once user had entered the needed inputs, it will pass it to input method where the inputs are validated
        ok_btn.place(x = 287, y = 174)

    def encrypt2(self, user_pin, user_txt): #method for encrypting text
        text = user_txt #assign value of user_text to text
        pin = user_pin #assign value of user_pin to pin
        pin = pin % ord('z') # modulo the pin entered to the maximum ascii value which is ord('z') or 122
        textEncrypt = "" # stores the converted string

        for index in text: # loop for assigning ascii with shifted value for each character of string  
            asciiVal = ord(index) #assign the ordial value of the character to asciiVal
            asciiVal = asciiVal + pin #assign the value of asciiVal plus the pin
            if asciiVal <= ord('z'): #if the ordinal value of character is less than z, assign the value to asciiVal
                asciiVal = asciiVal
            else: # if the ascii value of a character exceeds ord('z'), it will be modulo-ed, 31 is added to start the shift at the minimum value of ord(' ') or 32
                asciiVal =  (asciiVal % ord('z')) + 31

            #check.append(asciiVal) # write each encrypted ascii value for checking
            textEncrypt += chr(asciiVal)

        Frame.pack_forget(self) #delete the previus frame
        
        Frame.__init__(self) #another frame for encrypting text
        self.pack()

        self.background = PhotoImage(file = "picBG.png")    #set the background of window
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")
        canvas.create_text(90, 23, text = "Encrypted Text", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")
        canvas.create_text(170, 57, text="Warning: Copied text will be gone when you exit the program.", font=("rockwell", 8), fill="#7cc0d8") #a prompt for user
        encrypted_text = Text(self, width = 30, height=4, bd = 0)
        encrypted_text.insert("1.0", textEncrypt)   #insert the encrypted text into the textbox
        encrypted_text.config(state= DISABLED) #make the textbox uneditable for user
        encrypted_text.place(x = 70, y = 70)
        
        menu = Button(self, text = "Menu", font = ("rockwell", 12), command = self.begin, fg = "#232323")   #button for going back to the main frame
        menu.place(x = 110, y = 157)

        menu = Button(self, text = "Exit", font = ("rockwell", 12), command = exit, fg = "#232323") #button for exiting the program
        menu.place(x = 218, y = 157)

    def begin(self): #method for going back to main method
        Frame.pack_forget(self) #delete frame
        main() #go to main method

    def decrypt(self): #method for getting encrypted text
        Frame.pack_forget(self) #delete previous frame
        
        Frame.__init__(self) #create new frame
        self.pack()

        self.background = PhotoImage(file = "picBG.png") #set window background
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")
        canvas.create_text(90, 23, text = "Decrypt Text", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")

        def input(): #for getting and validating input
            try:
                user_pin = int(pin.get()) #if pin entered by user is not int, it will display an error message
                user_txt = txt.get("1.0", 'end-1c')
                self.decrypt2(user_pin, user_txt) #pass the inputs to decrypt2 method
            except:
                tkinter.messagebox.showerror("Invalid Pin", "Enter only numeric pin.") #error message of entered pin is invalid


        pin = Entry(self, width= 30, show="*")  #make the pin entered appear as asterisk
        pin.place(x = 103, y = 67 )
        canvas.create_text(55, 75, text = "Pin (ex. 1234): ", font = ("talios", 10), fill = "#7cc0d8")  #text for description

        txt = Text(self, height = 4, width= 30)
        txt.place(x = 103, y = 97 )
        canvas.create_text(64, 105, text = "Enter Text:", font = ("talios", 10), fill = "#7cc0d8")      #text for description

        ok_btn = Button(self, text="Decrypt!", font = ("talios", 10), command=input)    #button for passing the input to input method
        ok_btn.place(x = 287, y = 174)
    
    def decrypt2(self, user_pin, user_txt): #method for decrypting the text
        text = user_txt
        pin = user_pin

        pin = pin % ord('z') # modulo the pin entered to the maximum ascii value which is ord('z') or 122
        textDecrypt = "" # stores the converted string
        #check = [] # stores ascii values of each character for checking

        for index in text: # loop for decrypting the string using the pin
            asciiVal = ord(index)   #assign the ordial value of the character to asciiVal
            asciiVal = asciiVal - pin #assign the value of asciiVal minus the pin
            if asciiVal >= ord(' '): #if asciiVal if greater than or equal to (space), assign the value to asciival
                asciiVal = asciiVal
            else: # if the ascii value of a character is less than ord(' ') or 32, 31 will be deducted and the ascii value will be modulo-ed to start the shift at ord(' ') or 32
                asciiVal = (asciiVal - 31) % ord('z')

            # check.append(asciiVal) # write each decrypted ascii value for checking
            textDecrypt += chr(asciiVal)

        Frame.pack_forget(self) #delete previous frame
        
        Frame.__init__(self)    #create new frame
        self.pack()
 
        self.background = PhotoImage(file = "picBG.png") #set background of window
        canvas = Canvas(self)
        canvas.pack(fill = "both", expand = FALSE)
        canvas.create_image(0, 0, image = self.background, anchor = "nw")
        canvas.create_text(91, 23, text = "Decrypted Text", font = ("rockwell", 16, "bold"), fill = "#7cc0d8")
        canvas.create_text(170, 57, text="Warning: Copied text will be gone when you exit the program.", font=("rockwell", 8), fill="#7cc0d8")

        encrypted_text = Text(self, width = 30, height=4, bd = 0)
        encrypted_text.insert("1.0", textDecrypt)
        encrypted_text.config(state= DISABLED)
        encrypted_text.place(x = 70, y = 70)
        
        menu = Button(self, text = "Menu", font = ("rockwell", 12), command = self.begin, fg = "#232323")   #button for going back to the main frame
        menu.place(x = 110, y = 157)

        menu = Button(self, text = "Exit", font = ("rockwell", 12), command = exit, fg = "#232323")         #button for exiting program
        menu.place(x = 218, y = 157)

def main():
    Graphics().mainloop()
main() 
