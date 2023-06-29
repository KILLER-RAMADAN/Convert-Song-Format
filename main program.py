import tkinter as tk
from tkinter import messagebox,filedialog,ttk
import pydub
import os
import webbrowser

class change_sound_format(tk.Tk):
    
    
    
    
    
    def browse(self):
      self.entry_song.delete(0,1000)
      self.raed_file=filedialog.askopenfilename(title="Image Reader Browser",filetypes=[("Mp3 Song", "*.mp3"),("Wav Song", "*.wav")],)
      self.entry_song.insert(0,self.raed_file)
      
    def change_format(self):
      try:
        if self.entry_song.get()=="":
            messagebox.showerror("Error","Enter Sound Location.")
        elif self.entry_name.get()=="":
            messagebox.showerror("Error","Rename Sound To Convert.")
        else:
         if self.combo_box.get()=="mp3 to wav":
            mp3_song=pydub.AudioSegment.from_mp3(self.raed_file)
            mp3_song.export(f"{self.home_directory}//Desktop//{self.entry_name.get()}.wav",format="wav")
            messagebox.showinfo("Convert File Successful","Check Your Desktop....")
         elif self.combo_box.get()=="wav to mp3":
            wav_song=pydub.AudioSegment.from_wav(self.raed_file)
            wav_song.export(f"{self.home_directory}//Desktop//{self.entry_name.get()}.mp3",format="mp3")
            messagebox.showinfo("Convert File Successful","Check Your Desktop....")
         else:
             messagebox.showerror("Error","Select Correct Format...")
             
      except:
          messagebox.showerror("Error","1)Enter real File Location...\n2)Rename File To Save It..")
    def about_me(self):
        messagebox.showinfo("Hello Im Ahmed Ramadan","Aouther;Ahmed Ramadan Abd Elnaser\nVersion;1.0\nDeveloped By Me Dont Worry.")
        
    def git_hub(self):
        webbrowser.open("https://github.com/KILLER-RAMADAN")  
        
        
    def white_theme(self):
        
        self.configure(bg="white")
        
        self.name_label.configure(bg="white",fg="black")
        
        self.browse_button.configure(bg="white",fg="black")
        
        self.convert_button.configure(bg="white",fg="black")
        
        self.song_label.configure(bg="white",fg="black")
        
        self.entry_song.configure(bg="white",fg="black")
        
        self.entry_name.configure(bg="white")
        
        self.combo_label.configure(bg="white",fg="black")
        
        self.combo_box.configure(bg="white",fg="black")
        
    def dark_theme(self):
        
        self.configure(bg="#2d2d2d")
        
        self.name_label.configure(bg="#2d2d2d",fg="white")
        
        self.browse_button.configure(bg="white",fg="black")
        
        self.song_label.configure(bg="#2d2d2d",fg="white")
        
        self.entry_song.configure(bg="white")
        
        self.entry_name.configure(bg="white")
        
        self.combo_label.configure(bg="#2d2d2d",fg="white")
        
        self.combo_box.configure(bg="#2d2d2d")
        
        self.convert_button.configure(bg="white",fg="white")
    
   
    
    def __init__(self):
        
        super().__init__()
            
        
            
        self.title("Change Sound Format")
         
        self.geometry("400x300+550+150")
        
        self.resizable(0,0)
        
        self.attributes("-topmost",True)
        
        
        self.iconbitmap("images//format.ico")
        
        self.home_directory = os.path.expanduser( '~' )

        self.img1=tk.PhotoImage(file="images//search1.png")
        self.img2=tk.PhotoImage(file="images//convert.png")
        self.img3=tk.PhotoImage(file="images//about.png")
        self.img4=tk.PhotoImage(file="images//git.png")
        
        self.img5=tk.PhotoImage(file="images//theme.png")
        
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        
        m1 = tk.Menu(self.menu,background="white",activebackground="black")
        self.menu.add_cascade(label="Help",menu=m1)
        m1.add_command(label="developed by",command=self.about_me,image=self.img3,compound="left")
        m1.add_command(label="My GitHub",command=self.git_hub,image=self.img4,compound="left")
        m2 = tk.Menu(self.menu,background="white",tearoff=True,bd=0,activebackground="black")
        self.menu.add_cascade(label="Theme",menu=m2)
        m2.add_command(label="Light",command=self.white_theme,image=self.img5,compound="left")
        m2.add_command(label="Dark",command=self.dark_theme,image=self.img5,compound="left")
        self.menu.add_cascade(label="Exit",command=self.destroy)
        
        
        
        self.song_label=tk.Label(text="Select Song:",font=("Arial,10,bold"))
        
        self.song_label.place(x=3,y=10)
        
        
        self.entry_song=tk.Entry(width=18,relief="solid",font=(("Arial",20,"bold")))
        self.entry_song.place(x=5,y=50)
        
        
        self.browse_button=tk.Button(text="  Search",image=self.img1,compound="left",command=self.browse,relief="groove",font=("Arial",14,"bold"))
        self.browse_button.place(x=283,y=50)
        
        
        self.name_label=tk.Label(text="Enter Song Name:",font=("Arial,10,bold"))
        
        self.name_label.place(x=3,y=100)
        
        
        self.entry_name=tk.Entry(width=18,relief="solid",font=(("Arial",20,"bold")))
        self.entry_name.place(x=5,y=140)
        
        self.convert_button=tk.Button(text="Convert",image=self.img2,compound="left",command=self.change_format,relief="groove",font=("Arial",14,"bold"))
        self.convert_button.place(x=283,y=140)
        
        
        self.combo_label=tk.Label(text="Select Format:",font=("Arial,10,bold"))
        
        self.combo_label.place(x=3,y=190)
        
        
        
        self.combo_box=ttk.Combobox(width=10,values=["mp3 to wav","wav to mp3"],font=("arial",15,"bold"))
        self.combo_box.place(x=5,y=230)
        
        self.combo_box.set("mp3 to wav")
        
        
        
        
        





app=change_sound_format()
app.mainloop()    
            
            