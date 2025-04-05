import math


class Element:
    instances: list["Element"] = []

    def __init__(
        self,
        name: str,
        recipe: list["CraftElement"] | None = None,
        show_user: bool = False,
    ) -> None:
        self.name = name
        self.recipe = recipe
        self.show_user = show_user
        if show_user:
            Element.instances.append(self)

    def __str__(self) -> str:
        return self.name

    def get_full_recipe(self, amount: float) -> list[tuple["Element", float]]:
        full_recipe: list[tuple["Element", float]] = []
        if not self.recipe:
            full_recipe = [(self, math.ceil(amount))]
        else:
            for craft_element in self.recipe:
                full_recipe += craft_element.element.get_full_recipe(amount * craft_element.amount)
        return full_recipe


class CraftElement:
    def __init__(
        self,
        element: Element,
        amount: float,
    ) -> None:
        self.element = element
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.element}: {self.amount}"


oxygen = Element("Кислород")
hydrogen = Element("Водород")
carbon = Element("Углерод")
sugar = Element("Сахар")
lithium = Element("Литий")
silicon = Element("Кремний")
phosphorus = Element("Фосфор")
iron = Element("Железо")
copper = Element("Медь")
plasma = Element("Плазма")
water = Element("Вода")
sodium = Element("Натрий")
chlorine = Element("Хлор")
ammonia = Element("Аммиак")
potassium = Element("Калий")
nitrogen = Element("Азот")
radium = Element("Радий")
ethanol = Element("Этанол")


inaprovaline = Element(
    "Инапровалин",
    [
        CraftElement(oxygen, 1/3),
        CraftElement(carbon, 1/3),
        CraftElement(sugar, 1/3),
    ],
)
hydroxide = Element(
    "Гидроксид",
    [
        CraftElement(oxygen, 1/2),
        CraftElement(hydrogen, 1/2),
    ],
)
bensole = Element(
    "Бензол",
    [
        CraftElement(carbon, 1),
        CraftElement(hydrogen, 1),
    ],
)
celotane = Element(
    "Келотан",
    [
        CraftElement(silicon, 1/2),
        CraftElement(carbon, 1/2),
    ],
)
iron_silicide = Element(
    "Силицид железа",
    [
        CraftElement(silicon, 1/2),
        CraftElement(iron, 1/2),
    ],
)
salt = Element(
    "Столовая соль",
    [
        CraftElement(sodium, 1/2),
        CraftElement(chlorine, 1/2),
    ],
)
sodium_carbonate = Element(
    "Карбонат натрия",
    [
        CraftElement(oxygen, 1/4),
        CraftElement(ammonia, 1/4),
        CraftElement(carbon, 1/4),
        CraftElement(salt, 1/4),
    ],
)
sodium_hydroxide = Element(
    "Гидроксид натрия",
    [
        CraftElement(sodium, 1/2),
        CraftElement(hydroxide, 1/2),
    ],
)
dexolyne = Element(
    "Дексалин",
    [
        CraftElement(oxygen, 2/3),
        CraftElement(plasma, 0.0000000000000000000000001),
    ],
)
unstable_mutagen = Element(
    "Нестабильный мутаген",
    [
        CraftElement(chlorine, 1/3),
        CraftElement(phosphorus, 1/3),
        CraftElement(radium, 1/3),
    ],
)
bicaridine = Element(
    "Бикаридин",
    [
        CraftElement(inaprovaline, 1/2),
        CraftElement(carbon, 1/2),
    ],
    True,
)
bruisine = Element(
    "Бруизин",
    [
        CraftElement(lithium, 0.9/2),
        CraftElement(bicaridine, 1/2),
        CraftElement(sugar, 1/2),
    ],
    True,
)
puncturase = Element(
    "Пунктураз",
    [
        CraftElement(hydroxide, 1/2),
        CraftElement(bicaridine, 1/2),
    ],
    True,
)
lacerinole = Element(
    "Лаценирол",
    [
        CraftElement(bensole, 1/2),
        CraftElement(bicaridine, 1/2),
    ],
    True,
)
dermaline = Element(
    "Дермалин",
    [
        CraftElement(celotane, 1/3),
        CraftElement(oxygen, 1/3),
        CraftElement(phosphorus, 1/3),
    ],
    True,
)
leporasine = Element(
    "Лепоразин",
    [
        CraftElement(iron_silicide, 1/2),
        CraftElement(copper, 1/2),
        CraftElement(plasma, 0.0000000000000000000000001),
    ],
    True,
)
pirasine = Element(
    "Пиразин",
    [
        CraftElement(leporasine, 1/3),
        CraftElement(dermaline, 1/3),
        CraftElement(carbon, 1/3),
    ],
    True,
)
insusine = Element(
    "Инсузин",
    [
        CraftElement(leporasine, 1/3),
        CraftElement(silicon, 1/3),
        CraftElement(celotane, 1/3),
    ],
    True,
)
siginate = Element(
    "Сигинат",
    [
        CraftElement(water, 1/4),
        CraftElement(sugar, 1/4),
        CraftElement(sodium_carbonate, 1/4),
        CraftElement(celotane, 1/4),
        CraftElement(sodium_hydroxide, 1/4),
    ],
    True,
)
diloven = Element(
    "Диловен",
    [
        CraftElement(potassium, 1/3),
        CraftElement(silicon, 1/3),
        CraftElement(nitrogen, 1/3),
    ],
    True,
)
hyronalyne = Element(
    "Хироналин",
    [
        CraftElement(diloven, 1/2),
        CraftElement(radium, 1/2),
    ],
)
aritrazine = Element(
    "Аритразин",
    [
        CraftElement(hyronalyne, 1/2),
        CraftElement(hydrogen, 1/2),
    ],
    True,
)
dexolyne_plus = Element(
    "Дексалин Плюс",
    [
        CraftElement(dexolyne, 1/3),
        CraftElement(carbon, 1/3),
        CraftElement(iron, 1/3),
    ],
    True,
)
saline_solution = Element(
    "Физраствор",
    [
        CraftElement(water, 4/5),
        CraftElement(salt, 1/5),
    ],
    True,
)
falangimin = Element(
    "Фалангимин",
    [
        CraftElement(unstable_mutagen, 1/3),
        CraftElement(hyronalyne, 1/3),
        CraftElement(ethanol, 1/3),
    ],
    True,
)

