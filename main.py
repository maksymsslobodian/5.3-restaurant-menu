# Початкове меню
dishes = [
    {"name": "Борщ", "price": 100},
    {"name": "Вареники", "price": 80},
    {"name": "Узвар", "price": 30}
]

# 1. Функція показу меню (Твоя частина - красивий вивід)
def show_menu():
    print("\n" + "="*30)
    print("      МЕНЮ РЕСТОРАНУ")
    print("="*30)
    for index, dish in enumerate(dishes, 1):
        print(f"{index}. {dish['name']:<15} | {dish['price']:>5} грн")
    print("="*30)

# 2. Функція додавання (Твоя частина)
def add_dish():
    print("\n--- Додавання нової страви ---")
    name = input("Введіть назву: ")
    try:
        price = int(input("Введіть ціну: "))
        dishes.append({"name": name, "price": price})
        print(f"✅ Страву '{name}' додано успішно!")
    except ValueError:
        print("❌ Помилка! Ціна має бути числом.")

# 3. Функція редагування (Твоя частина)
def edit_dish():
    show_menu()
    try:
        index = int(input("\nВведіть номер страви для редагування: ")) - 1
        if 0 <= index < len(dishes):
            new_name = input("Введіть нову назву: ")
            new_price = int(input("Введіть нову ціну: "))
            dishes[index] = {"name": new_name, "price": new_price}
            print("✅ Дані оновлено!")
        else:
            print("❌ Такої страви немає.")
    except ValueError:
        print("❌ Помилка введення. Ціна має бути числом.")

# 4. Функція підрахунку суми (Твоя частина)
def calculate_total():
    total = sum(dish['price'] for dish in dishes)
    print(f"\n💰 Загальна вартість усіх страв: {total} грн")

# Основний цикл програми
if __name__ == "__main__":
    while True:
        show_menu()
        print("1. Додати страву")
        print("2. Порахувати загальну суму")
        print("3. Редагувати страву")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        if choice == "1":
            add_dish()
        elif choice == "2":
            calculate_total()
        elif choice == "3":
            edit_dish()
        elif choice == "0":
            print("Дякуємо, що завітали!")
            break
        else:
            print("❌ Невірний вибір, спробуйте ще раз.")
