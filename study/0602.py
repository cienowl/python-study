#dictionary for문

person={
    "last_name":"김",  #key값 : value값
    "first_name":"나예",
    "birthday":"1996/5/3"
}

for key in person:
    print(person[key])

print('-'*30)

for a,b in person.items():
    print(a)

print('-'*30)

#*****지능형 리스트(List comprehension)*****

nums = [n for n in range(1,6)]
print(nums) #[1,2,3,4,5]    #for문

squares = [n*n for n in nums]
print(squares) #제곱근이 들어감 [1,4,9,16,25]

odd_nums =[n for n in nums if n%2==1]   #for문, if문
print(odd_nums) #2로 나눠서 나머지가 1인것들만 출력(홀수만 출력) [1,3,5]

new_nums=[n+1 for n in nums]
print(new_nums)

print('-'*30)

#2중 for문
people = [{     #dictionary가 두개인것
    "last_name":"김",
    "first_name":"나예",
    "birthday":"1996/5/3"      #하나하나가 밑에서 person
},{
    "last_name":"홍",
    "first_name":"준선",
    "birthday":"1996/11/15"
}]
birthdays=[
    person[term]
    for person in people
    for term in person      #이중for문
    if term=="birthday"
]
print(birthdays)
print('-'*30)
#exam(평균구하기)
result=0
nums=[2,3,7,1,9,10]

for num in nums:
    result=result+num
print(result/6)

#answer
result=0
nums=[2,3,7,1,9,10]

for i in nums:
    result += i
result /= len(nums) #len는 길이구하는 함수
print(result)
print('-'*30)

nums=[2,3,7,1,9,10]
print(sum(nums)/len(nums))     #내장함수
print(sum(n for n in nums if n%2==1)/len([n for n in nums if n%2==1]))    #홀수값만 평균
print('-'*30)
#내장함수 <최솟값 최댓값 dir>
print(min(nums))
print(max(nums))

print(dir(nums))    #dir이 할수있는 모든것(기능)들이 나옴
print('-'*30)

#함수
def add1(a,b):  #def : 함수선언 / add1 : 함수이름
    return a+b      #return은 해도 되고 안해도됨
print(add1(1,2))    #타입이 동적(타입이 안맞게 입력하면 오류가남 (string+int))
print(add1('abc','def'))    #string은 이어서 나옴
print(add1([1,2,3],[4,5,6]))    #리스트도 더할수있음(합쳐짐)
print('-'*30)
def returning_nothing(n):
    print('아무것도 리턴하지 않아!')
    if n==1:
        return n    #n의 값이 1일때만 리턴값이 나옴
returning_nothing(1) #리턴값이 없어도 위에 프린트문장이 출력됨
print('-'*30)
def add2(a,b=1):    #b는 기본값이 1
    return a+b

print(add2(1))
print(add2(1,2))    #하나나 두개만 받을수 있음 (a=1, b=2)

def multiple_args_func(*args):  #이름앞에 *을 쓰면 여러개를 받을 수 있음
    print(args)
multiple_args_func(1,2,3,4,5)
print()
multiple_args_func(*[1,2,3,4])
print()
multiple_args_func('가',1,3.45)

def key_args_func(**kwargs):
    print(kwargs)

print()
key_args_func(name='나예', age=25, say='Hi')
person={
    'name':'나예',
    'age':25,
    'say':'Hi'
}
key_args_func(**person) #*을 붙이면 펼쳐서 보여줌
print('-'*30) #지금 아무 것도 수행하지 않을때 pass를 써줌 (항상 pass나 return을 써줘야함)

#연습문제 : 여러 인자를 받아 그 중 최솟값을 구하는 함수(multi args), built-in function 사용해보기
def min_from(*args):
    return min(args)
print(min_from(1,2,3,4,5,6,7,8,9,10,11))
print('-'*30)

# 지역변수 local variable, 전역변수 global variable
# 범위 scope

def a1(arg1, arg2):     #arg1, arg2 는 함수밖으로 나가지못함(지역변수)
    print(arg1)         #앞에 블럭이 많아질수록 지역이 좁아지는것

a1(1,2)
print('-'*30)

#재귀 함수
#팩토리얼은 n>=0 , !0=1
def factorial(n):
    if n==0 or n==1:    #break
        return 1
    return factorial(n-1)*n
print(factorial(5))

#재귀로 1부터 n까지의 합을 구하는 함수 구현해보기
def factorialsum(n):
    if n==1:
        return 1
    elif n==0:
        return 0       #n이 0일때 안해주면 무한루프
    return factorialsum(n-1)+n

print(factorialsum(10)) #55
print(factorialsum(30))