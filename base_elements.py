from element_schema import Element, CraftElement

# Элементы без рецепта
oxygen = Element("Кислород", [])
hydrogen = Element("Водород", [])
carbon = Element("Углерод", [])
sugar = Element("Сахар", [])
lithium = Element("Литий", [])
silicon = Element("Кремний", [])
phosphorus = Element("Фосфор", [])
iron = Element("Железо", [])
copper = Element("Медь", [])
plasma = Element("Плазма", [])
water = Element("Вода", [])
sodium = Element("Натрий", [])
chlorine = Element("Хлор", [])
ammonia = Element("Аммиак", [])
potassium = Element("Калий", [])
nitrogen = Element("Азот", [])
radium = Element("Радий", [])


# Промежуточные элементы
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
dexolyne =Element(
    "Дексалин",
    [
        CraftElement(oxygen, 2/3),
        CraftElement(plasma, 0.0000000000000000000000001),
    ],
)
