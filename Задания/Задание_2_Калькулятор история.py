def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

def log(result):
    with open("calculations.txt", "a") as file:
        file.write(result + "\n")  # добавлен перевод строки для читаемости

def show_history():
    """Читает и выводит историю всех выполненных вычислений."""
    try:
        with open("calculations.txt", "r") as file:
            history = file.readlines()
        
        if not history:
            print("\nИстория вычислений пуста.")
            return
        
        print("\n--- История вычислений ---")
        for i, line in enumerate(history, start=1):
            print(f"{i}. {line.strip()}")
        print("--------------------------")
    except FileNotFoundError:
        print("\nФайл истории ещё не создан. Выполните хотя бы одно вычисление.")

def main():
    while True:
        print("\nВыберите операцию: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Просмотр истории вычислений")
        print("0. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/0): ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '5':
            show_history()
            continue
        elif choice not in ('1', '2', '3', '4'):
            print("Неверный ввод")
            continue

        try:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: необходимо ввести целое число.")
            continue

        if choice == '1':
            r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
        elif choice == '2':
            r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
        elif choice == '3':
            r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
        elif choice == '4':
            r = f"Результат: {num1} / {num2} = {divide(num1, num2)}"

        print(r)
        log(r)

if __name__ == "__main__":
    main()