for j in range(1, 20+1):
    if j%15==0:
        print('fizzbuzz')
    elif j%3==0:
        print('FIZZ')
    elif j%5==0:
        print('BUZZ')
    else:
        print(j)
