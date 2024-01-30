#desc : 구구단 프로그램 
#spec : for 문 잘 써야함 . 2중 for 문의 이해 

# 2 x 1 = 2 , 2 x 2 = 4 , 2 x 3 = 6 , 2 x 4 = 8 ... 2 x 9 = 18


print('구구단 시작 !')
x = 2 
for x in range(2, 10):
    print(f'{x} 단 ---- > ')
    for y in range(1 , 9):
        print(f'{x}x{y} = {x*y:2d}' , end= ' ')
    print() 

