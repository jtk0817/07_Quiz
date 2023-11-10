import random

def 로또번호생성():
    result = []

    for l in range(6):
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)

    result.sort()
    return result

result = 로또번호생성()
print(f"생성된 로또 번호는 {result} 입니다.")

