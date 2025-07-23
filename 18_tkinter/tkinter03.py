import tkinter as tk
from faulthandler import is_enabled

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0,column=0,pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

#entry옆에 버튼 하나 만들고 해당 버튼 클릭ㄷ시 아이디 출력
#아이디 밑에 비밀번호도 똑같이 만드세요
def id_button_click():
    print(id_entry.get())

id_button = tk.Button(root, text="중복확인",command=id_button_click)
id_button.grid(row=0, column=2)

pwd_label = tk.Label(root, text="비밀번호:")
pwd_label.grid(row=1, column=0, pady=10)

pwd_entry = tk.Entry(root)
pwd_entry.grid(row=1, column=1, padx=5)
def pwd_button_click():
    print(pwd_entry.get())

pwd_button = tk.Button(root, text="사용가능확인", command=pwd_button_click)
pwd_button.grid(row=1, column=2)

root.mainloop()