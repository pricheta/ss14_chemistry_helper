from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.craft_step import get_element_recipe
from app.elements import Element


app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "frontend")


ELEMENT_DICT: dict[int, Element] = {
    number + 1: element for number, element in enumerate(Element.instances)
    if element.show_user
}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, element_id: int | None = None, element_amount: int = 180):
    element = ELEMENT_DICT.get(element_id)

    if element and element_amount:
        raw_recipe = get_element_recipe(element, element_amount, [])
        recipe = []
        for step in raw_recipe:
            spaces = " " * 4 * len(step.step_number)
            recipe.append(f"{spaces}{step}")
    else:
        recipe = None

    available_elements = []
    for number, element in ELEMENT_DICT.items():
        available_elements.append(f"{number}. {element}")

    return templates.TemplateResponse(
        "content.html",
        {
            "request": request,
            "available_elements": available_elements,
            "recipe": recipe,
            "element_id": element_id,
            "element_amount": element_amount,
        },
    )
