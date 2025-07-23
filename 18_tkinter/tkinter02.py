import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

#place: 절대 위치
#grid: 빈 공간을 비우지 않음

label1 = tk.Label(root, text="텍스트1", bg = "blue")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="텍스트2" , bg = "yellow")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="텍스트3", bg = "pink")
label3.grid(row=2, column=0, rowspan=2)

label4 = tk.Label(root, text="텍스트4", bg = "red")
label4.grid(row=4, column=0)

label5 = tk.Label(root, text="텍스트5", bg = "brown")
label5.grid(row=0, column=1)

label6 = tk.Label(root, text="텍스트6", bg = "black")
label6.grid(row=0, column=2)

label7 = tk.Label(root, text="텍스트7", bg = "orange")
label7.grid(row=2, column=1, rowspan=2)

label8 = tk.Label(root, text="텍스트8", bg = "gray")
label8.grid(row=3, column=3)

root.mainloop()