import flet as ft
import math

def main(page: ft.Page):
    page.title = "Average Calculator"

    num1 = ft.TextField(label="num1")
    num2 = ft.TextField(label="num2")
    num3 = ft.TextField(label="num3")
    result_text = ft.Text()

    def calculate(e):
        try:
            n1 = int(num1.value)
            n2 = int(num2.value)
            n3 = int(num3.value)

            avg = (n1 + n2 + n3) / 3
            result = math.floor(avg + 0.5)

            result_text.value = f"Result: {result}"
        except:
            result_text.value = "Invalid input"

        page.update()

    page.add(
        num1,
        num2,
        num3,
        ft.ElevatedButton("Calculate", on_click=calculate),
        result_text
    )

ft.app(target=main)
