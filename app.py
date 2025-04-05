import elements
from clear_screen import clear_screen
from element_schema import Element


def get_user_answer(element_dict: dict[int, Element]) -> int:
    print("Представленные элементы")
    for number, element in element_dict.items():
        print(f"{number}. {element}")
    print(f"0. Выход")
    return int(input("Введите номер элемента: "))


if __name__ == "__main__":
    element_list: list[Element] = []
    for variable_name, variable_value in elements.__dict__.items():
        if (
            not variable_name.startswith('__') and
            not "Element" in variable_name and
            variable_value.recipe
        ):
            element_list.append(variable_value)

    clear_screen()
    element_dict: dict[int, Element] = {number + 1: element for number, element in enumerate(element_list)}
    user_answer = get_user_answer(element_dict=element_dict)

    while user_answer:
        element = element_dict[user_answer]
        recipe = element.get_full_recipe(90)

        print(f"\nПоследовательность для варки 90 унций {element}а:")
        for recipe_step in recipe:
            element = recipe_step[0]
            amount = recipe_step[1]
            print(f"{element}: {amount}")
        input("\nНажмите Enter для продолжения")
        clear_screen()

        user_answer = get_user_answer(element_dict=element_dict)
