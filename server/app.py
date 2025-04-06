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
async def root(request: Request, element_id: int = 0, element_amount: int = 0):
    element = ELEMENT_DICT.get(element_id)

    available_elements_str = "Список доступных элементов\n"
    for number, element in ELEMENT_DICT.items():
        available_elements_str += f"\n{number}. {element}"

    jinja_dict = {
        "request": request,
        "available_elements_str": available_elements_str,
    }

    print(element, element_amount, element and element_amount)
    if element and element_amount:
        recipe = get_element_recipe(element, element_amount, [])
        jinja_dict |= {
            "recipe": recipe,
        }

    print(jinja_dict)

    return templates.TemplateResponse(
        "content.html",
        jinja_dict,
    )