import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0,column=0)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

#entry옆에 버튼 하나 만들고 해당 버튼 클릭ㄷ시 아이디 출력
#아이디 밑에 비밀번호도 똑같이 만드세요
def id_button_click():
    #실제 서버와 데이터베이스에 정보를 요청해서
    #비교후에 중복확인 절차
    if id_entry.get() == "":
        messagebox.showerror("경고","아이디를 입력해 주세요.")
    else:
        messagebox.showinfo("중복확인", id_entry.get())

id_button = tk.Button(root, text="중복확인",command=id_button_click)
id_button.grid(row=0, column=2)

pwd_label = tk.Label(root, text="비밀번호:")
pwd_label.grid(row=1, column=0)

pwd_entry = tk.Entry(root, show="*")
pwd_entry.grid(row=1, column=1)

pwd_check_label = tk.Label(root, text="비밀번호 확인:")
pwd_check_label.grid(row=2, column=0)

pwd_check_entry = tk.Entry(root, show="*")
pwd_check_entry.grid(row=2, column=1)

chk_var = tk.IntVar()
chk_box = tk.Checkbutton(root, text="위 약관 내용에 동의합니다.", variable=chk_var)
chk_box.grid(row=3, column=1)

def signup_click():
    if pwd_entry.get() != pwd_check_entry.get():
        messagebox.showerror("에러","비밀번호가 틀림니다.")
    elif chk_var.get() != 1:
        messagebox.showerror("에러","약관을 동의해 주세요.")
    else:
        messagebox.showinfo("회원가입","회원가입이 정상적으로 되었습니다.")

signup_button = tk.Button(root,text="회원가입", command=signup_click)
signup_button.grid(row=4, column=1)

root.mainloop()