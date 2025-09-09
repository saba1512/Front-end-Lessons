# 4. დაწერე ფუნქცია მიანიჭე a, b და c არგუმენტი - def entered_num(a, b, c):
# მომხმარებელს შეაყვანინი a, b და c და ფუნქციით გამოთვალე შემდეგი a-ს დაუმატე b და ამათგან მიღებული ჯამი გაამრავლე c-ზე,


a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

def entered_num(a, b, c):
    summer = a + b
    mult = summer * c

    return mult, summer

print(entered_num(a,b,c))