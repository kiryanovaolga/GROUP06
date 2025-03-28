"""
1. manuální testování
- alfa - v rámci týmu
- beta - mimo vývojový tým

2. polo-automatické testování

3. automatické testování
- velká zodpovědnost
- DDT
"""


def get_triangle_perimeter(a, b, c):
    result = a + b + c
    return result


print(get_triangle_perimeter(10, 10, 10) == 30)
print(get_triangle_perimeter(10, 20, 15) == 45)

def test_get_triangle_perimeter():
    assert get_triangle_perimeter(10, 10, 10) == 30
    assert get_triangle_perimeter(10, 20, 15) == 45

test_get_triangle_perimeter()
