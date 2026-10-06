import  math
def calculate_triangle(a_str: str, b_str: str, c_str: str):
    try:
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)
    except ValueError:
        return "", [(-2, -2), (-2, -2), (-2, -2)]

    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if a == b == c:
        t_type = "равносторонний"
    elif a == b or b == c or a == c:
        t_type = "равнобедренный"
    else:
        t_type = "разносторонний"

    cos_alpha = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    alpha = math.acos(cos_alpha)

    x3_raw = b * math.cos(alpha)
    y3_raw = b * math.sin(alpha)

    scale = 80 / max(a, b, c)

    x1, y1 = 10, 10
    x2, y2 = int(10 + c * scale), 10
    x3 = int(10 + x3_raw * scale)
    y3 = int(10 + y3_raw * scale)

    coords = [(x1, y1), (x2, y2), (x3, y3)]

    return t_type, coords