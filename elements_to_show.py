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
leporasine = Element(
    "Лепоразин",
    [
        CraftElement(base_elements.iron_silicide, 1/2),
        CraftElement(base_elements.copper, 1/2),
        CraftElement(base_elements.plasma, 0.0000000000000000000000001),
    ],
)
pirasine = Element(
    "Пиразин",
    [
        CraftElement(leporasine, 1/3),
        CraftElement(dermaline, 1/3),
        CraftElement(base_elements.carbon, 1/3),
    ],
)
insusine = Element(
    "Инсузин",
    [
        CraftElement(leporasine, 1/3),
        CraftElement(base_elements.silicon, 1/3),
        CraftElement(base_elements.celotane, 1/3),
    ],
)
siginate = Element(
    "Сигинат",
    [
        CraftElement(base_elements.water, 1/4),
        CraftElement(base_elements.sugar, 1/4),
        CraftElement(base_elements.sodium_carbonate, 1/4),
        CraftElement(base_elements.celotane, 1/4),
        CraftElement(base_elements.sodium_hydroxide, 1/4),
    ],
)


# Лекарства от токсинов
diloven = Element(
    "Диловен",
    [
        CraftElement(base_elements.potassium, 1/3),
        CraftElement(base_elements.silicon, 1/3),
        CraftElement(base_elements.nitrogen, 1/3),
    ],
)



element_list = [
    bicaridine,
    bruisine,
    puncturase,
    lacerinole,

    dermaline,
    leporasine,
    pirasine,
    insusine,
    siginate,

    diloven,
]