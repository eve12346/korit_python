#Book 클래스
#제목과 저자 => title, author
#display_info => "제목: [제목], 저자:[저자]"
#Book 클래스의 객체 두개 이상 만들어보고 display_info호출
#소멸자 => 소멸 시 "[제목]의 객체가 소멸 되었습니다."출력

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"제목:[{self.title}], 저자:[{self.author}]")

    def __del__(self):
        print(f"{self.title}의 객체가 소멸 되었습니다.")

book1 = Book("홍길동", "옛날사람")
book2 = Book("견우와직녀", "옛날사람")

book1.display_info()
book2.display_info()