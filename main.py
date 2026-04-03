# Початкове меню (просто дані)
dishes = [
    {"name": "Борщ", "price": 100, "description": "Суп", "category": "Супи"},
    {"name": "Вареники", "price": 80, "description": "З картоплею", "category": "Основні"},
    {"name": "Узвар", "price": 30, "description": "Напій", "category": "Напої"}
]

def show_menu():
    print("\n--- Меню ресторану ---")
    cats = []
    for dish in dishes:
        if dish["category"] not in cats:
            cats.append(dish["category"])
    for c in cats:
        print("\n" + c)
        for dish in dishes:
            if dish["category"] == c:
                print(f"{dish['name']} - {dish['price']} грн | {dish['description']}")

# функція редагування
def edit_dish():
    name = input("Введіть назву страви для редагування: ")
    found = False
    for dish in dishes:
        if dish["name"] == name:
            found = True
            print("Що редагувати?")
            print("1. Ціна")
            print("2. Опис")
            print("3. Категорія")
            choice = input("Ваш вибір: ")
            if choice == "1":
                new_price = input("Нова ціна: ")
                if new_price.isdigit():
                    dish["price"] = int(new_price)
                    print("Ціну оновлено")
                else:
                    print("Невірна ціна")
            elif choice == "2":
                dish["description"] = input("Новий опис: ")
                print("Опис оновлено")
            elif choice == "3":
                dish["category"] = input("Нова категорія: ")
                print("Категорію оновлено")
            else:
                print("Невірний вибір")
    if not found:
        print("Такої страви не існує!")
if __name__ == "__main__":
    while True:
        show_menu()
        print("1. Додати страву")
        print("2. Редагувати ціну/опис/категорію")
        print("3. Видалити страву")
        print("4. Порахувати загальну суму")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        # Тут поки нічого не працює - це просто текст для вибору
        if choice == "1":
            print("Функція додавання буде реалізована в окремій гілці.")
        elif choice == "2":
            edit_dish()
        elif choice == "3":
            print("Функція видалення буде реалізована в окремій гілці.")
        elif choice == "4":
            print("Функція підрахунку буде реалізована в окремій гілці.")
        elif choice == "0":
            break
        else:
            print("Невірний вибір.")
