import base_elements
from element_schema import Element, CraftElement

# Лекарства от механического урона
bicaridine = Element(
    "Бикаридин",
    [
        CraftElement(base_elements.inaprovaline, 1/2),
        CraftElement(base_elements.carbon, 1/2),
    ],
)
bruisine = Element(
    "Бруизин",
    [
        CraftElement(base_elements.lithium, 0.9/2),
        CraftElement(bicaridine, 1/2),
        CraftElement(base_elements.sugar, 1/2),
    ],
)
puncturase = Element(
    "Пунктураз",
    [
        CraftElement(base_elements.hydroxide, 1/2),
        CraftElement(bicaridine, 1/2),
    ],
)
lacerinole = Element(
    "Лаценирол",
    [
        CraftElement(base_elements.bensole, 1/2),
        CraftElement(bicaridine, 1/2),
    ],
)


# Лекарства от физического урона
dermaline = Element(
    "Дермалин",
    [
        CraftElement(base_elements.celotane, 1/3),
        CraftElement(base_elements.oxygen, 1/3),
        CraftElement(base_elements.phosphorus, 1/3),
    ],
)

element_list = [
    bicaridine,
    bruisine,
    puncturase,
    lacerinole,
    dermaline,
]