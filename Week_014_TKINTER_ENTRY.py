import tkinter as tk

anime_title = "One Piece"
root = tk.Tk()
root.title("OOP")
root.geometry("400x300")
root.configure(bg="CYAN")

pangalan = tk.Entry(root)
pangalan.grid(row=0, column=0, padx=20)
counter = 0 
'''
def iprint():
    global counter
    print(f"My favorite anime is {anime_title}")
    counter += 1
'''
def iprint():
    print(pangalan.get())

button_print = tk.Button(root, text="Print", command=iprint)
button_print.grid(row=0, column=1, padx=20, pady=20)
    
root.mainloop()