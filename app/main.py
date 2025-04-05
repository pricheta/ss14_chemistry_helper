# pylint: disable=redefined-outer-name, import-error, missing-function-docstring, missing-module-docstring
from clear_screen import clear_screen
from elements import Element
from craft_step import get_element_recipe

def get_user_answer(element_dict: dict[int, Element]) -> int:
    print("Представленные элементы")
    for number, element in element_dict.items():
        print(f"{number}. {element}")
    print("0. Выход")
    return int(input("Введите номер элемента: "))


if __name__ == "__main__":
    clear_screen()
    element_dict: dict[int, Element] = {
        number + 1: element
        for number, element in enumerate(Element.instances)
        if element.show_user
    }
    user_answer = get_user_answer(element_dict=element_dict)
    clear_screen()

    while user_answer:
        element = element_dict[user_answer]
        recipe = get_element_recipe(element, 90, [])

        for step in recipe:
            spaces = " " * len(step.step_number) * 4
            print(f'{spaces}{step}')

        input("\nНажмите Enter, чтобы продолжить")
        clear_screen()

        user_answer = get_user_answer(element_dict=element_dict)
        clear_screen()
