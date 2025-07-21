# 루브릭) #1. 프로젝트 1번에서 평행사변형, 사다리꼴 넓이를 구하는 메서드를 직접 작성할 수 있다.
# 루브릭) #2.프로젝트 2번에서 Kiosk 클래스를 생성하고, 주문, 추가 주문 메서드를 적절하게 구현할 수 있다.	
         #3. 프로젝트 2번의 지불, 주문표 작성 메서드를 적절하게 구현할 수 있다. 

class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1. 평행사변형 2. 사다리꼴))
        if self.square == 1:
            print('평행사변형 함수는 par()입니다.')
        elif self.square == 2:
            print('사다리꼴 함수는 trape()입니다.')
        else:
            print('1, 2 중에서 다시 입력해주세요.')
    def par(self):
        width, height = map(int,input('가로, 높이를 입력하세요. 예시: 가로, 높이\n >>>').split(','))
        area = width * height
        result = '평행사변형의 넓이는 :' + str(area)
        return result

    def trape(self):
        top, bottom, height = map(int,input('윗변, 아랫변, 높이를 입력하세요. 예시: 윗변, 아랫변, 높이/n >>>').split(','))
        area= (top+bottom)*height/2.
        result = '사다리꼴의 넓이는 :' + str(area)
        return result
a=Suqare()
print(a.par())
print(a.trape())
    


class Kiosk:
    def __init__(self):
        self.menu=[['americano':2000],['latte',3000],['mocha',3000],['yuza_tea',2500],['green_tea',2500],['choco_latte',3000]]
        self.temp=""
        self.order_menu=[]
        self.order_price=[]
        self.price_sum=0
        
    def menu_print(self):
        print("ㅡㅡㅡ메뉴판ㅡㅡㅡ")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item[0]}: {itemi1]}원")

    def menu_select(self):
        print()
        n = 0
        While n < 1 or n > len(self.menu):
            n = int(input("음료 번호를 입력하세요 : "))

            if 1 <= n <= len(self.menu):
                name, price = self.menu[n-1]
                self.order_price.append(price)
                self.price_sum += price
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.")

            t = 0
            while t not in [1,2]:
                t= int(input("HOT 음료는 1 을, ICE 음료는 2 를 입력하세요.:")
                if t == 1:
                    self.temp = "HOT"
                elif t == 2:
                    self.temp = "ICE"
                else:
                    print( "1 과 2 중 하나를 입력하세요.\n")
            full_name = f"{self.temp} {self.menu[n-1][0]}"
            self.order_menu.append(full_name)            
        while n ! = 0 :
            print()
            n= int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요:"))
            if n>0 and n<len(self.menu)+1:
                print('추가 주문 음료', self.temp, self.menu[n-1], ":" self.price[n-1], '원\n', '합계:', self.price_sum, '원')
            else:
                if n == 0 :
                    print("주문이 완료되었습니다.")
                    print(self.order_menu, self.order_price)
        else:
            print('없는 메뉴입니다. 다시 주문해 주세요.")

K.Kiosk()
def pay(self):
    method = input("결제 수단을 입력하세요. (cash or card, or 1/2 :")
    if method == cash or method == 1: 
        print('직원을 호출 하겠습니다.')
    elif method == card or method == 2:
        print('IC칩 방향에 맞게 카드를 꽂아주세요.')
    else:
        print('다시 결제를 시도해 주세요.')
a=Kiosk
a.pay
 
 주세요.')

from datetime import datetime
    def show_datetime(self):
        now = datetime.now()
        print("주문시각:", nowstrftime("%y - %m - %d %H : %M : %S")

    def frame_decorator(func):
        def wrapper(self):
            print("ㅡ" + "-"*30 + "ㅡ")
            func(self)
            print("ㅡ" + "-"*30 + "ㅡ")
        return @frame_decorator
def table(self):
    print("ㅡ 주문표 ㅡ")
    for i in range(len(self.order_menu):
        print(f"{self.order_menu[i]:<20} :{self.order_price[i]}원")
    print("-"*30)
    print(f"{'총합계':<20 : {self.price_sum}원")
    self.show_datetime()
    
k=Kiosk()
k.menu_select()
k.table()

         
                    
                
             

    
  
            
    
        
        
            

    