year = int(input('1~3000 사이의 숫자를 입력: '))
def is_leap(year):
    leap = False
    if(year%4==0 and year%100 != 0) or (year%400==0):
        print(year, '년은 윤년입니다')
    else:
        print(year, '년은 윤년이 아닙니다')
print(is_leap(year))
