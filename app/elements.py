import math


class Element:
    instances: list["Element"] = []

    def __init__(
        self,
        name: str,
        recipe: list[tuple["Element", float]] | None = None,
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
        ...


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
        (oxygen, 1 / 3),
        (carbon, 1 / 3),
        (sugar, 1 / 3),
    ],
)
hydroxide = Element(
    "Гидроксид",
    [
        (oxygen, 1 / 2),
        (hydrogen, 1 / 2),
    ],
)
bensole = Element(
    "Бензол",
    [
        (carbon, 1),
        (hydrogen, 1),
    ],
)
celotane = Element(
    "Келотан",
    [
        (silicon, 1 / 2),
        (carbon, 1 / 2),
    ],
)
iron_silicide = Element(
    "Силицид железа",
    [
        (silicon, 1 / 2),
        (iron, 1 / 2),
    ],
)
salt = Element(
    "Столовая соль",
    [
        (sodium, 1 / 2),
        (chlorine, 1 / 2),
    ],
)
sodium_carbonate = Element(
    "Карбонат натрия",
    [
        (oxygen, 1 / 4),
        (ammonia, 1 / 4),
        (carbon, 1 / 4),
        (salt, 1 / 4),
    ],
)
sodium_hydroxide = Element(
    "Гидроксид натрия",
    [
        (sodium, 1 / 2),
        (hydroxide, 1 / 2),
    ],
)
dexolyne = Element(
    "Дексалин",
    [
        (oxygen, 2 / 3),
        (plasma, 0.0000000000000000000000001),
    ],
)
unstable_mutagen = Element(
    "Нестабильный мутаген",
    [
        (chlorine, 1 / 3),
        (phosphorus, 1 / 3),
        (radium, 1 / 3),
    ],
)
bicaridine = Element(
    "Бикаридин",
    [
        (inaprovaline, 1 / 2),
        (carbon, 1 / 2),
    ],
    True,
)
bruisine = Element(
    "Бруизин",
    [
        (lithium, 0.9 / 2),
        (bicaridine, 1 / 2),
        (sugar, 1 / 2),
    ],
    True,
)
puncturase = Element(
    "Пунктураз",
    [
        (hydroxide, 1 / 2),
        (bicaridine, 1 / 2),
    ],
    True,
)
lacerinole = Element(
    "Лаценирол",
    [
        (bensole, 1 / 2),
        (bicaridine, 1 / 2),
    ],
    True,
)
dermaline = Element(
    "Дермалин",
    [
        (celotane, 1 / 3),
        (oxygen, 1 / 3),
        (phosphorus, 1 / 3),
    ],
    True,
)
leporasine = Element(
    "Лепоразин",
    [
        (iron_silicide, 1 / 2),
        (copper, 1 / 2),
        (plasma, 0.0000000000000000000000001),
    ],
    True,
)
pirasine = Element(
    "Пиразин",
    [
        (leporasine, 1 / 3),
        (dermaline, 1 / 3),
        (carbon, 1 / 3),
    ],
    True,
)
insusine = Element(
    "Инсузин",
    [
        (leporasine, 1 / 3),
        (silicon, 1 / 3),
        (celotane, 1 / 3),
    ],
    True,
)
siginate = Element(
    "Сигинат",
    [
        (water, 1 / 4),
        (sugar, 1 / 4),
        (sodium_carbonate, 1 / 4),
        (celotane, 1 / 4),
        (sodium_hydroxide, 1 / 4),
    ],
    True,
)
diloven = Element(
    "Диловен",
    [
        (potassium, 1 / 3),
        (silicon, 1 / 3),
        (nitrogen, 1 / 3),
    ],
    True,
)
hyronalyne = Element(
    "Хироналин",
    [
        (diloven, 1 / 2),
        (radium, 1 / 2),
    ],
)
aritrazine = Element(
    "Аритразин",
    [
        (hyronalyne, 1 / 2),
        (hydrogen, 1 / 2),
    ],
    True,
)
dexolyne_plus = Element(
    "Дексалин Плюс",
    [
        (dexolyne, 1 / 3),
        (carbon, 1 / 3),
        (iron, 1 / 3),
    ],
    True,
)
saline_solution = Element(
    "Физраствор",
    [
        (water, 4 / 5),
        (salt, 1 / 5),
    ],
    True,
)
falangimin = Element(
    "Фалангимин",
    [
        (unstable_mutagen, 1 / 3),
        (hyronalyne, 1 / 3),
        (ethanol, 1 / 3),
    ],
    True,
)

