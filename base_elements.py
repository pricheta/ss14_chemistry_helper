from element_schema import Element, CraftElement

# Элементы без рецепта
oxygen = Element("Кислород", [])
hydrogen = Element("Водород", [])
carbon = Element("Углерод", [])
sugar = Element("Сахар", [])
lithium = Element("Литий", [])

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
