print("==========문제 1==========")
input_ = input("정수를 입력하세요: ")
number = 0
try:
    number = int(input_)
except ValueError:
    print("That's not a valid integer!")
if number % 2:
    print(f"{number} 홀수입니다!")
else:
    print(f"{number} 짝수입니다!")
print("==========문제 2==========")
input_ = input("정수를 입력하세요: ")
number = 0
try:
    number = int(input_)
except ValueError:
    print("That's not a valid integer!")
if number < 0:
    print(f"{number} 음의 정수입니다!")
elif number > 0:
    print(f"{number} 양의 정수입니다!")
else:
    print(f"{number} 입니다!")
print("==========문제 3==========")
arr = {1: input("당신은 성인인가요(예:1, 아니오: 0): "), 2: input("당신은 기혼자이신가요(예:1, 아니오: 0): ")}
res = ["결혼한", "결혼하지 않은", "성인", "미성년자"]
number_arr = {0, 0}
for i in range(1, 3):
    try:
        arr[i] = int(arr[i])
    except ValueError:
        print("That's not a valid integer!")
print(f"당신은 " + arr[2] * res[0] + (not arr[2]) * res[1] + " " + arr[1] * res[2] + (not arr[1]) * res[3] + "입니다")
print("==========문제 4==========")
input_ = input("년도를 입력하세요: ")
input_ = int(input_)
print(input_ + "는 " + (not (input_ % 4)) * (0 != (input_ % 100)) * "윤년" + (0 == (input_ % 100)) * "평년")
