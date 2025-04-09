from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from recipe_maker.craft_step import get_element_recipe
from recipe_maker.elements import Element, ElementGroup


AVAILABLE_ELEMENT_GROUPS = [
    ElementGroup.MECHANIC,
    ElementGroup.PHYSIC,
    ElementGroup.TOXIN,
    ElementGroup.GASP,
    ElementGroup.CELLULAR,
    ElementGroup.BOTANIC,
]



app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "frontend")


AVAILABLE_ELEMENTS_DICT: dict[str, Element] = {
    element.name: element for element in Element.available_elements
}


GROUPED_ELEMENTS: dict[ElementGroup, list[Element]] = {group: [] for group in ElementGroup if group in AVAILABLE_ELEMENT_GROUPS}
for element in  Element.available_elements:
    if element.group not in AVAILABLE_ELEMENT_GROUPS:
        continue
    if element.group not in GROUPED_ELEMENTS:
        GROUPED_ELEMENTS[element.group] = []
    GROUPED_ELEMENTS[element.group].append(element)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, element_name: str = "", element_amount: int = 180):
    element = AVAILABLE_ELEMENTS_DICT.get(element_name)

    if element and element_amount:
        raw_recipe = get_element_recipe(element, element_amount, [])
        recipe = []
        for step in raw_recipe:
            spaces = " " * 4 * len(step.step_extended_number)
            recipe.append(f"{spaces}{step}")
    else:
        recipe = None


    return templates.TemplateResponse(
        "content.html",
        {
            "request": request,
            "grouped_elements": GROUPED_ELEMENTS,
            "recipe": recipe,
            "element_name": element_name,
            "element_amount": element_amount,
        },
    )
