import tkinter as k
t=k.Tk()
t.title('Quiz portal')
t.geometry('1200x720')
t.config(bg="#2A3335")

def login():
    print("login button clicked")
    
def sign_up():
    print("Sign up button clicked")
    
def forgot_password():
    print("Forgot password clicked")
    
main_frame = k.Frame(t,bg="#3D365C")
main_frame.pack(fill="both", expand=True , padx=20, pady=20)

left_frame = k.Frame(main_frame,bg="#3a7ebf")
left_frame.pack(side="left",fill="both",expand=True,padx=(0,10))

right_frame = k.Frame(main_frame,bg="#222222")
right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

t.mainloop()