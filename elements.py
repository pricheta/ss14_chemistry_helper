from element_schema import Element, CraftElement

# Базовые элементы
oxygen = Element("Кислород", [])
carbon = Element("Углерод", [])
sugar = Element("Сахар", [])

# Промежуточные элементы
inaprovaline = Element(
    "Инапровалин",
    [
        CraftElement(oxygen, 1/3),
        CraftElement(carbon, 1/3),
        CraftElement(sugar, 1/3),
    ]
)
bicaridine = Element(
    "Бикаридин",
    [
        CraftElement(inaprovaline, 1/2),
        CraftElement(carbon, 1/2),
    ],
)
