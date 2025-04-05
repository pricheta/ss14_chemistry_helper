class CraftElement:
    element: "Element"
    amount: int


class Element:
    def __init__(
        self,
        name: str,
        base: bool,
        recipe: list[CraftElement] | None = None,
    ) -> None:
        self.name = name
        self.base = base
        self.recipe = recipe if base else None


    def __str__(self):
        return self.name


    def get_full_recipe(self, amount: int):
        if not self.base:
            ...
        return {self: amount}
