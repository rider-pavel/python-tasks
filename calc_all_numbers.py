n = h = int(input())
total, count = (0,0)
product = 1

while h != 0:
    total += h % 10
    product *= h % 10
    count += 1
    h //= 10

print("Сумма цифр равна:", total)
print("Количество цифр равно:", count)
print("Произведение цифр равно:", product)
print("Среднее арифметическое цифр равно:", total / count)
print("Первая цифра равна:", n // 10 ** (count-1))
print("Сумма первой и последней цифры", n // 10 ** (count-1) + n % 10)



































