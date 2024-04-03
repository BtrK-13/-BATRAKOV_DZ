print("Результат вызова функции test_head_pain c произвольным числом и типом параметров:")
def test_head_pain(*args):
    print(args)
test_head_pain('Паника!',666, True)

print()
print("Результат выполнения рекурсивной функции считающей факториал числа 13:")
def factorial(n):
    if n==1:
        return 1
    factorial_n_minus_1 = factorial(n=n-1)
    return n*factorial_n_minus_1
print(factorial(13))
