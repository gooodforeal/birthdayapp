import re


def date_check(inp_date):
    reg = r"^\d{4}-\d{2}-\d{2}$"
    if re.fullmatch(reg, inp_date):
        return True
    return False