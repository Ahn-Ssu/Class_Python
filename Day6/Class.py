# 자바의 클래스 -> 객체(인스턴스) 개념과 동일함 
# 인스턴스는 관계 위주로 설명할 때 사용하는 편 
class Cookie :
    # 클래스변수 (static 성격)
    flour = "곰표"

    
    # self -> 호출을 실행한 객체를 의미함 
    # cookieA가 호출한 경우 self는 cookie A로 해석하면 된다
    # self.first == cookieA.first
    def __init__(self, first, second):
        # 객체변수
        self.first = first
        self.second = second 
    # 메소드 마다 self로 전달하는 이유는 어떤 객체의 필드 값 혹은 변수값을 조정해야 하는지 알려주기 위함 
    def framing(self,tool):
        pass
    def bake(self):
        pass

cookieA = Cookie()
cookieB = Cookie()


# 상속
# class 클래스 이름(상속할 클래스 이름)
# 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에 사용 
class ChocoCookie(Cookie) :

    # 메소드 오버라이딩
    # @ 등의 인디케이터 없이 그냥~ 바로 메소드 덮어 쓰면 끝
    def bake(self):
        print("초코초코초코쿠키초코")
    pass