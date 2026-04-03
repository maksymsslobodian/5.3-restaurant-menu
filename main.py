# Початкове меню (просто дані)
dishes = [
    {"name": "Борщ", "price": 100},
    {"name": "Вареники", "price": 80},
    {"name": "Узвар", "price": 30}
]

def show_menu():
    print("\n--- Меню ресторану ---")
    for index, dish in enumerate(dishes, 1):
        print(f"{index}. {dish['name']} - {dish['price']} грн")

if __name__ == "__main__":
    while True:
        show_menu()
        print("1. Додати страву")
        print("2. Редагувати ціну")
        print("3. Видалити страву")
        print("4. Порахувати загальну суму")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        # Тут поки нічого не працює - це просто текст для вибору
        if choice == "1":
            print("Функція додавання буде реалізована в окремій гілці.")
        elif choice == "2":
            print("Функція редагування буде реалізована в окремій гілці.")
        elif choice == "3":
            print("Функція видалення буде реалізована в окремій гілці.")
        elif choice == "4":
            print("Функція підрахунку буде реалізована в окремій гілці.")
        elif choice == "0":
            break
        else:
            print("Невірний вибір.")
