# <tuple>
#list : 정렬 O, 부분변형 O
#tuple : 정렬 X("튜플은 순서가 중요"), 부분변형 X

mylist = [0,1,2,3,4]    #list(대괄호)
mytup = (0,1,2,3,4)     #tuple(괄호)

print(mytup[1]) #1
print(mytup[1:3])   #1,2
print(mytup[:3:2])  #0부터 2(3개)까지 2씩 건너뛰어서 -> 0,2
print(mytup[0:3:2])
print('-'*30)
mylist[0]=5     #mylist는 값을 바꿀수있다 -> tuple은 type 에러가남
                #tuple은 부분적으로 바꿀 수 없다.(전체 다 다시줘야함)
print(mylist)
mytup=(5,4,3,2,1,0)     #도표, 표같은걸 만들때 사용하기 위해 tuple을 사용(순서대로 값을 넣을수있다)
print(mytup)
print('-'*30)
#(a,b)=(1,2) 괄호 생략가능
a,b =1,2    #-> a에 1, b에 2가 들어감
print("a : ",a, ", b : ",b)
print('-'*30)
a, b = b, a      #a와b를 이렇게 바꿀수있다(java에서는 temp이용해서 바꿈)
print(a,",",b)

# <pip> (Package Iinstaller for Python)

import flask
import sqlalchemy

# flask
# sqlalchemy

# Web Framework
# Java -> flask
# Ruby -> Ruby on rails
# Python -> Django
# flask?? -> (web) micro framework :