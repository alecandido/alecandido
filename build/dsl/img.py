import inspect
import re
from typing import Optional

pattern = re.compile(r"!img\[(.*?)\](\(.*?\))?(\{.*?\})?")


def replace(src: str, url: Optional[str] = None, props: Optional[str] = None) -> str:
    """Define custom syntax for image tag.

    Parameters
    ----------
    src: str
    url: str or None
    props: str or None

    Returns
    -------
    str
        the HTML result

    """
    propstr = ""
    if props is not None:
        items = [[el.strip() for el in prop.split(":")] for prop in props.split(",")]
        propstr = " ".join(f'{key}="{value}"' for key, value in items)

    if not src.startswith("https://"):
        src = f"https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/{src}"

    img = f'<img src="{src}" {propstr} />'

    # encapsulate in anchor (if specified)
    if url is not None:
        img = inspect.cleandoc(
            f"""
            <a href="{url}">
                {img}
            </a>
            """
        )

    return img


def apply(text: str):
    result = text

    while True:
        matched = re.search(pattern, result)
        if matched is not None:
            url = matched[2][1:-1] if matched[2] is not None else None
            props = matched[3][1:-1] if matched[3] is not None else None
            expanded = replace(src=matched[1], url=url, props=props)

            result = result[: matched.start()] + expanded + result[matched.end() :]
        else:
            break

    return result
