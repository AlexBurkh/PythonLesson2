# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def count_sum(user_input):
    sum = 0
    alphas = []
    if ',' in user_input:
        alphas = user_input.split(',')
    elif '.' in user_input:
        alphas = user_input.split('.')

    for group in alphas:
        for num in group:
            sum += int(num)

    return sum


user_input = input("Введите вещественное число: ")
print(count_sum(user_input))


