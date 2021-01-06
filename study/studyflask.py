# a = "Hello, World!"
# b = 'Hello, World! I said "Hi"\nThis is a new line'
# c = "\tHi\t"
# print(a)
# print(b)
#
# c="hello,"
# d="\tworld"
# print(c+d)
#
# e = "^"+"_"*40+"^"
# print(e)
#
# #주석달기
# f="List is too short, You need Python"
# print(f[12]) #s
#
# print("-1:", a[-1]) #n
# print("12: ", a[12])
# print("-1: ", a[-1])
#
# print("0:4 -> ", a[0:4])
# print("0:3 -> ", a[0:3])
#
# #String formatting
#
# name = "송정우"
# num =12
# str_template = "%s, 안녕! %d"
# #%ㄴ, %d(igit)
# print(str_template % (name, num))
#
# str_template2 = "{}, 안녕! {}"
# print(str_template2.format(name, num))
#
#
# print(f"{name}, 안녕! {num}")
#
# a = "hobby"
# print(a.count("b"))
# print(a.find("y"))
# print(','.join(a))
#
# text_lines = ["라인1", "라인2", "라인3"]
# print('\n'.join(text_lines))
# print(a.upper())
# print(a.lower())
# print(a.replace('b', 'a'))
# print(a.replace('bb', 'a'))
#
# first_list = []
# first_list.append(1)    #[1]
# print(first_list[0])
# first_list.append(2)    #[1,2]
# print(first_list)
# print(first_list.pop())

# second_list = [[0,1,2], 2,3,4]
# print(second_list)
#
# print(second_list[-1])
# print(second_list[1:3])
#
#
# third_list = [3, 1, 2.84, 8, 7.33, 10]
# third_list.sort()
# print(third_list)
# third_list.reverse()
# print(third_list)

# hash_map
# first_dict = {'a':1, 'second':2, 'hohe':3}
# print(first_dict)
# print("a: ", first_dict['a'])
# print("hohe: ", first_dict['hohe'])
#

# for i in range(10):
#     print('hi')
#
# a = ['Life', 'is', 'too', 'short']
# print(" ".join(a))





#2020/06/02
#
# person = {
#     "last_name": "이",
#     "first_name": "호준",
#     "birthday": "1948/2/21"
# }
#
# for key in person:
#     print(key, person[key]) #키와 밸류값 출력
#
# print('-' * 10)
# for a, b in person.items():
#     print(a, b) #위 포문과 같은 내용
#
# print('-' * 10)
#
# #지능형 리스트 (list comprehension)
# nums = [n for n in range(1,6)]
#
# empty_list = []
# for n in range(1,6):
#     empty_list.append(n)
#
# print(nums) #[1,2,3,4,5]
#
# print('-' * 10)
#
# #제곱근을 구하는 지능형 리스트
# nums = [1,2,3,4,5]
# squares = [n*n for n in nums]
# print(squares)  #[1,4,9,16,25]
#
# #아래는 위 구문과 같은 내용
# nums = []
# for n in nums:
#     nums.append(n*n)
#
# print('-' * 10)
#
# #홀수를 구하는 지능형 리스트
# odd_nums = [n for n in nums if n % 2 == 1]
# print(odd_nums)
#
# nums = [1,2,3,4,5]
# new_nums = [n+1 for n in nums]   #지능형
# print(new_nums) #[2,3,4,5,6]
#
#
# people = [{
#     "last_name": "이",
#     "first_name": "호준",
#     "birthday": "1948/2/21"
# },{
#     "last_name": "박",
#     "first_name": "호순",
#     "birthday": "1942/3/23"
# }]
#
# #이 방법도 되지만 가독성이 매우 떨어지므로 추천하지 않음
# birthdays = [
#     person[term]
#     for person in people
#     for term in person
#     if term == "birthday"
# ]
#
# #따라서 2중 for문은 아래와 같이 쓰는 것이 나음
# birthdays = []
# for person in people:
#     for term in person:
#         if term == "birthday":
#             birthdays.append(person[term])
#
# print(birthdays)
#
# #연습문제 평균 구하기 (for, list comprehension)
# #tuple
# result = 0
# nums = [2,3,7,1,9,10]
#
# for n in nums:
#     result += n     #총합 구함
# result /= len(nums) #result = result / leng(nums), leng()은 길이 구하는 내장함수
# print(result)
#
# #sum()함수를 사용해서 평균 구하기
# result = sum(nums)/len(nums)
# print(result)
#
# #홀수 값만 평균
# print(sum(n for n in nums if n% 2 == 1) / len([n for n in nums if n %2 ==1]))
#
# print(min(nums))
# print(max(nums))
#
#

#def는 함수 선언부
def add1(a,b):
    return a + b

print(add1(1,2))
print(add1('abc', 'def'))
print(add1([1,2,3], [4,5,6]))

def returning_nothing(n):
    print('아무것도 리턴하지 않아!')
    if n == 1:
        return n

returning_nothing([1,2])
print('-' *10)


def add2(a, b=1):
    return a+b

print(add2(1))
print(add2(1,2))

#
def multiple_args_func(*args):
    print(args)

multiple_args_func(1,2,3,4,5)
print()
multiple_args_func([1,2,3,4])
print()
multiple_args_func('가', 1,3.45)


#**의 경우 키값과 밸류값을 알아서 매칭해서 넣어줌
def key_args_func(**kwargs):
    print(kwargs)

#def 선언후 아래 줄에는 무조건 실행문이 있어야 함. 구현할 것이 없다면 pass로 선언

print()
key_args_func(name='호준', age=40, say='hi')
person = {
    'name': '호준',
    'age': 40,
    'say': 'hi'
}
print('-'*20)
##연습문제) 여러 인자를 받아 그 중 최소값을 구하는 함수 (multi args), built-in function 사용해보기
def min_from(*args):
    return min(args)

def min_from2(*args):
    min_num = args[0]
    for num in args[1:]:
        if min_num > num:
            min_num = num
    return min_num

assert min_from(1,2,3,4,5,6,7,8,10,11,12) == 1  #assert는 조건이 맞는 경우 참 거짓 판단
assert min_from2(1,2,3,4,5,6,7,8,10,11,12) == 1
print(min_from(1,2,3,4,5,6,7,8,10,11,12))
print(min_from2(1,2,3,4,5,6,7,8,10,11,12))

print(min(1,2,3,4,5,6,7,8,10,11,12))

#재귀 함수
# !0 = 1
# !1 = 1
# !2 = 1*2
# !3 = 1*2*3
# !4 = 1*2*3*4
#...

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1)*n

print(factorial(5))


#재귀로 1부터 n까지의 합을 구하는 함수 구현해보기

# def sum_to(n):
#     if n == len(n)
#     pass sum_to(n)
#
# print(sum_to(7))



