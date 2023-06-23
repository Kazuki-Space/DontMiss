import random
import flet as ft

def main(page: ft.Page):
    page.title = "2AM"
    page.bgcolor = ft.colors.BLACK
    page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, scale=2)

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def change_text(e):
        e.control.left = random.randint(100, 200)
        e.control.top = random.randint(10, 200)
        txt_number.value = str(int(txt_number.value) + 1)
        e.control.update()
        page.update()

    def minus_value(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    page.add(
      txt_number,
      ft.Container(
          ft.Stack(
              [
                  ft.Container(
                      ft.Text("Click", text_align=ft.TextAlign.CENTER),
                      bgcolor=ft.colors.PURPLE,
                      left=0,
                      top=0,
                      width=50,
                      height=30,
                      border_radius=20,
                      on_click=change_text,
                  )
              ]
          ),
          border_radius=8,
          padding=5,
          width=300,
          height=300,
          bgcolor=ft.colors.WHITE,
          on_click=minus_value
      )
    )

ft.app(target=main)