# pylint: disable=too-few-public-methods, too-many-positional-arguments, too-many-arguments,
# pylint: disable=missing-module-docstring, missing-class-docstring
class Element:
    instances: list["Element"] = []

    def __init__(
        self,
        name: str,
        recipe: list[tuple["Element", float]] | None = None,
        show_user: bool = False,
        temperature: str = "",
        catalyst: tuple["Element", int] | tuple = (),
    ) -> None:
        self.name = name
        self.recipe = recipe
        self.show_user = show_user
        self.temperature = temperature
        self.catalyst = catalyst
        if show_user:
            Element.instances.append(self)

    def __str__(self) -> str:
        return self.name


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
        (sugar, 1 / 3),
        (carbon, 1 / 3),
    ],
)
hydroxide = Element(
    "Гидроксид",
    [
        (oxygen, 1 / 2),
        (hydrogen, 1 / 2),
    ],
    temperature="выше 310К",
)
bensole = Element(
    "Бензол",
    [
        (hydrogen, 1),
        (carbon, 1),
    ],
    temperature="выше 310К",
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
    temperature="выше 310К",
)
salt = Element(
    "Столовая соль",
    [
        (sodium, 1 / 2),
        (chlorine, 1 / 2),
    ],
    temperature="выше 370К",
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
    ],
    catalyst=(plasma, 1),
)
unstable_mutagen = Element(
    "Нестабильный мутаген",
    [
        (chlorine, 1 / 3),
        (phosphorus, 1 / 3),
        (radium, 1 / 3),
    ],
    show_user=True,
)
bicaridine = Element(
    "Бикаридин",
    [
        (carbon, 1 / 2),
        (inaprovaline, 1 / 2),
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
    temperature="выше 325К",
)
lacerinole = Element(
    "Лацеринол",
    [
        (bensole, 1 / 2),
        (bicaridine, 1 / 2),
    ],
    True,
    temperature="выше 335К",
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
    ],
    True,
    catalyst=(plasma, 1),
)
pirasine = Element(
    "Пиразин",
    [
        (leporasine, 1 / 3),
        (dermaline, 1 / 3),
        (carbon, 1 / 3),
    ],
    True,
    temperature="выше 540К",
)
insusine = Element(
    "Инсузин",
    [
        (leporasine, 1 / 3),
        (silicon, 1 / 3),
        (celotane, 1 / 3),
    ],
    True,
    "выше 433К",
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
    "выше 370К",
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
        (iron, 1 / 3),
        (dexolyne, 1 / 3),
        (carbon, 1 / 3),
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
falanhymyne = Element(
    "Фалангимин",
    [
        (unstable_mutagen, 1 / 3),
        (hyronalyne, 1 / 3),
        (ethanol, 1 / 3),
    ],
    True,
)
