def s(q):
    onetwofreefour =q//1000
    print (onetwofreefour)
    twofreefourone =(q%1000) //100
    print(twofreefourone)
    freefouronetwo =(q%100) //10
    print(freefouronetwo)
    fouronetwotree =(q%10) //1
    print(fouronetwotree)

q =int(input('введіть 4-х значне'))
s(q)