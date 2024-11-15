import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("400x300")
root.configure(bg="white")

counter = 0 
def iprint():
    global counter
    print(f"{counter} OOP")
    counter += 1
    
button_print = tk.Button(root, text="Print", command=iprint)
button_print.grid(row=0, column=0, padx=20, pady=20)
    
root.mainloop()