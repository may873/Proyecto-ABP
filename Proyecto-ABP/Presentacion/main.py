import flet as ft


def main(page: ft.Page):
    page.title=("Presentacion")
    page.bgcolor="black"

    lbl1=ft.Text("¿Que es la tecnologia ?")
    btna1=ft.ElevatedButton("Respuesta Audio")
    btnt1=ft.ElevatedButton("Respuesta Texto ")

    page.add(
        ft.Column(
            controls=[
            ft.Row(controls=[lbl1],alignment="CENTER"),
            ft.Row(controls=[btna1,btnt1],alignment="CENTER"),
            ],alignment="CENTER"))
ft.app(main)
