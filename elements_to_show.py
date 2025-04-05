import base_elements
from element_schema import Element, CraftElement


bicaridine = Element(
    "Бикаридин",
    [
        CraftElement(base_elements.inaprovaline, 1/2),
        CraftElement(base_elements.carbon, 1/2),
    ],
)

element_list = [
    bicaridine,
]