# Дополнительное практическое задание по модулю: "Слишком древний шифр".

def initial():  # определение корректности числа
    is_our = False
    while is_our == False:
        x = int(input('Введите число из первой вставки: '))
        if 3 <= x <= 20:
            return x


def password(x):  # подбор пароля
    our_password = ''
    y = int(x / 2) + 1
    for i in range(1, y):
        for j in range(2, x):
            if i == j:
                continue
            if x % (i + j) == 0:
                our_password += str(i)
                our_password += str(j)
    return our_password


n = initial()
result = password(n)
print('Пароль для данного числа:', int(result))
