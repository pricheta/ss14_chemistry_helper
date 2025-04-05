class CraftElement:
    def __init__(
        self,
        element: "Element",
        amount: float,
    ) -> None:
        self.element = element
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.element}: {self.amount}"


class Element:
    def __init__(
        self,
        name: str,
        recipe: list[CraftElement],
    ) -> None:
        self.name = name
        self.recipe = recipe

    def __str__(self) -> str:
        return self.name

    def get_full_recipe(self, amount: float) -> list[tuple["Element", float]]:
        full_recipe: list[tuple["Element", float]] = []

        if not self.recipe:
            full_recipe = [(self, amount)]
        else:
            for craft_element in self.recipe:
                full_recipe += craft_element.element.get_full_recipe(amount * craft_element.amount)

        return full_recipe
