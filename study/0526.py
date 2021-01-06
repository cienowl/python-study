a='"Hello, World!!!!!!!!"'  #""랑 ''은 구분없음
b="\tI \nsaid \"hello\""
print(a)
print(b)

c="hello,"
d="\tworld"
print(c+d)

e="^"+"_"*40+"^"
print(e)

#주석달기
# space한것은 index X
f="Life is too short, You need Python"

#Slicing
print("12: ",f[2])    #s
print("-1: ", f[-1])  #n (-는 거꾸로)
print("-2: ", f[-2])
print("0:3 ->",f[0:4])   #0번째부터 4번쨰까지 출력(차이만큼=>0부터 4개)-> Life
print("5:11 ->",f[5:11])
print("5:10 ->",f[-5:-3])   #-도 됨
print(":6 ->", f[:6])   #안적으면 처음부터
print(":6 ->",f[6:])    #6번째부터 끝까지
print("0:12:2 ->",f[0:12:2])    #건너 뛰어서 출력

#String formatting
name="김나예"
num=12
str_template1="%s, 안녕! %d"  #%s는 String
# %s(string) %d(digit숫자)

print(str_template1 % (name, num))   #!!순서!!랑 타입을 잘 맞춰야함

str_template2="{}, 안녕! {}"
print(str_template2.format(name,num))   #타입을 걱정안해도 알아서 순서대로 들어감

print(f"{name}, 안녕! {num}")        #f를 쓰면 직관적으로 쓸수있다(최신)

a2="hobby"
print(a2.count("b"))    #count는 ()안의 문자 갯수 셈
print(a2.find("y"))     #find는 index가 나옴(못찾으면 -1출력), 여러개인경우 첫번쨰출력
print(','.join(a2))     #문자열 a2 사이사이에 ,를 써줌

text_lines=["라인1", "라인2", "라인3"]
print('\n'.join(text_lines))
print(a2.upper())   #다 대문자
print(a2.lower())   #다 소문자
print(a2.replace('b','a'))  #문자 b를 모두 a로 바꿔줌
print(a2.replace('a','b'))
print(a2.replace('bb','a'))

#list
first_list = []
first_list.append(1)    #값을 넣어줌
print(first_list[0])
first_list.append(2)
print(first_list)
print(first_list.pop())     #마지막값을 뺴줌?
print(first_list)

print()
second_list = [[0,1,2],'abc',True,4, 3.01]  #값은  모든형식이 다들어갈수있다
print(second_list)
print(second_list[0])
print(second_list[0][1])    #2차원 배열
print(second_list[1])
# list도 slicing이 전부 된다
print()
print(second_list[-1])
print(second_list[1])
print(second_list[1:4])
print(second_list[2::2])    #index=2부터 2칸씩 띄어서
second_list[0:2] = []   #지우는 방법1: 0부터 2까지 지움
print(second_list)
del second_list[0]      #지우는 방법2: 0번째 지움
print(second_list)
print()
third_list=[3,1,2.84,8,7.33,10]
third_list.sort()   #정렬
print(third_list)
third_list.reverse()    #역순으로 정렬
print(third_list)
print()

#********hash_map(많이사용)
first_dict={'a':1, 'second':2,'hohe':3}   #hash_map을 dictionary라고 한다
#index 를 :숫자로 해줌
print(first_dict)
print("a: ",first_dict['a'])
print("hohe: ",first_dict['hohe'])
print()
#print("1: ",first_dict[1])  #???????????????출력안됨


# 조건문과 반복문

#sequence타입
for i in range(10):     #i가 0부터 <10까지 (10번)반복
    print('hi')
print()
# for var in [0,1,2,3,4,5,6,7,8,9]: 와 같음
for var in range(10):   #0부터 9까지 출력
    print(var)
print()
for var in range(0,10,2):
    print(var)          #0부터 9까지 2칸씩 띄어서 출력
                        #여러줄이어도 안묶어도됨(공백으로 알아서 구분/ 공백을 틀리면안됨)
print()
test=[0,1,2,3,4,5,6]
for var in test[1::3]:
    print(var,end="\n")
    print("var + 1 =", var+1)
print()

i=0
while True:
    print(test[i])
    i += 1
    if i == len(test):   #i가 test의 길이와 같아지면 멈춤
        break
#    elif 조건2:
#       statement
#    else:
#       statement
print()
# == 같다 / <= 작거나 같다 / >= 크거나 같다 / != 같지않다
# and / or

name="gg"
age=11

if name!='김나예' and age!= 23:
    pass    #그냥 무시하고 지나감
print()
if 17 <= age < 30:   #java에선 X
    pass
print()

l = ['Life','is','too','short']
print(' '.join(l))