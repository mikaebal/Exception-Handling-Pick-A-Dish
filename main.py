def select_dish(foods, selected_food):
    print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    try:
        index = 1
        for dish in foods:
            print(f"{index}. {dish}")
            index += 1

        selected_choice = int(input("Your order number? "))
        select_dish(foods, selected_choice - 1)
    except IndexError as error:
        print(f"{error} was entered.")
        print("Next time try entering something on the menu!")
    except (SyntaxError, ValueError) as error:
        print(f"{error} was entered.")
        print(f"Next time enter dish number!")


menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")