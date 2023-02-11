def calculate_percent(to_calculate: int, percent: int, tax: int) -> int | float:
    discount = to_calculate - (to_calculate / 100 * percent)
    return discount - (to_calculate / 100 * tax)
