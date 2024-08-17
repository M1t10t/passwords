import random

numbers = int(input("Введите количество символов которые должны быть в пароле: "))
simbols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password=""
for i in range(numbers):
    password+=simbols[random.randint(0, len(simbols)-1)]
print(password)
