#Цикл for. Элементы списка. Полезные функции в цикле.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True    #flag
k = 0
k_not = 0

for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    for j in range (len(numbers)):
        if numbers[j] == 1:
            continue
        elif numbers[i] == numbers[j]:
            break
        elif numbers[i] % numbers[j] == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
        k = k + 1
    else:
        not_primes.append(numbers[i])
        k_not = k_not + 1
    is_prime = True

print(primes)
print(not_primes)