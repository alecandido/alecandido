import copy
import re

pattern = re.compile(r"!img\[(.*)\]\{(.*)\}")


def apply(text: str):
    result = copy.copy(text)

    for tag in re.finditer(pattern, result):
        __import__("pdb").set_trace()

    return result
