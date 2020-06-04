# import time
import random

aaa={'A.q':1,'B.qq':2,'C,qqq':3,'D.qqqq':4}
bbb={'A.w':1,'B.ww':2,'C,www':3,'D.wwww':4}
ccc={'A.e':1,'B.ee':2,'C,eee':3,'D.eeee':4}
ddd={'A.r':1,'B.rr':2,'C,rrr':3,'D.rrrr':4}
qiz ={
    '1':aaa,
    '2':bbb,
    '3':ccc,
    '4':ddd
}
qizkey = ['1', '2', '3', '4']  # qizkey = list(qiz.keys())
random.shuffle(qizkey)

newqiz=[]
count = 3   # 控制出几道题
while count:
    a = str(random.randint(1,4))
    b = qiz[a]
    if a in newqiz:
        continue
    else:
        print("This is question ?")  #这里可以考虑具体的问题，否则每次都是一样的问题
        print(b)   
        newqiz.append(a)   #这里可以插入用户输入的选项，计算分数
        count -= 1
