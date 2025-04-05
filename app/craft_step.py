import math

from elements import Element


class CraftStep:
    def __init__(
        self,
        crafted_element: Element,
        amount_to_craft: int,
        step_number: list[int],
    ) -> None:
        self.crafted_element = crafted_element
        self.amount_to_craft = amount_to_craft
        self.step_number = step_number

    def __str__(self):
        if self.step_number:
            step_number = [str(number) for number in self.step_number]
            version = '.'.join(step_number)
            version += '. '
        else:
            version = ''

        if not self.crafted_element.recipe:
            return f'{version}Добавляем {self.amount_to_craft} ед. элемента \"{self.crafted_element}\"'

        temperature_str = (
            f", при температуре {self.crafted_element.temperature}"
            if self.crafted_element.temperature
            else ""
        )

        if self.crafted_element.catalyst:
            catalyst_element = self.crafted_element.catalyst[0]
            catalyst_amount = self.crafted_element.catalyst[1]
            catalyst_str = f", катализатор реакции - {catalyst_amount} ед. элемента \"{catalyst_element}\""
        else:
            catalyst_str = ""

        return f"{version}Получаем {self.amount_to_craft} ед. элемента \"{self.crafted_element}\"{temperature_str}{catalyst_str}"



def get_element_recipe(
    crafted_element: Element,
    amount_to_craft: int,
    step_number: list[int],
) -> list[CraftStep]:

    recipe: list[CraftStep] = [
        CraftStep(
            crafted_element,
            amount_to_craft,
            step_number,
        )
    ]

    step = 0
    if crafted_element.recipe:
        for element, amount in crafted_element.recipe:
            step += 1
            ingredient_amount = amount * amount_to_craft
            ingredient_amount = math.ceil(ingredient_amount)
            recipe += get_element_recipe(element, ingredient_amount, step_number + [step])

    return recipe
