import tkinter as tk

root = tk.Tk()
root.title("SUPPPPPPPPPPPPAAAAAAAAAAAANIGGGGGGGGGGGAAAAAAAAAAAA")
root.geometry("400x300")
root.configure(bg="CYAN")

label = tk.Label(root, text="This is Label")
label.grid(row=2, column=3)#, padx=10, pady=10)

anime_character = tk.Label(root, text="Saitama")
anime_character.grid(row=0, column=0)
'''
frame = tk.Frame(root)
frame.pack(pady=20)
'''

'''
label = tk.Label(frame, text="This is Label")
label.grid(row=0, column=0, padx=10, pady=10)

anime_character = tk.Label(root, text="Saitama")
anime_character.grid(row=0, column=0)
'''
root.mainloop()