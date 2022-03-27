from . import img


def main(content: str) -> str:
    result = img.apply(content)

    return result
