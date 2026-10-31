while True:
    password = input("Введите пароль:")
    if len(password) >= 8:
        print("Пароль принят!")
        break
    else:
        print('Пароль должен содержать 8 символов. Попробуйте еще раз.')
