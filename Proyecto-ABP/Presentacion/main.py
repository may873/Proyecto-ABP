import flet as ft


def main(page: ft.Page):
    page.title=("Presentacion")
    page.bgcolor="black"

    btnIntro=ft.FilledButton("que es la tecnoligia")

    lbl1=ft.Text("¿Que es la tecnologia ?")
    btna1=ft.ElevatedButton("Respuesta Audio")
    btnt1=ft.ElevatedButton("Respuesta Texto ")

    lbl2=ft.Text("¿Que es la tecnologia ?")
    btna2=ft.ElevatedButton("Respuesta Audio")
    btnt2=ft.ElevatedButton("Respuesta Texto ")

    lbl3=ft.Text("¿Que es la tecnologia ?")
    btna3=ft.ElevatedButton("Respuesta Audio")
    btnt3=ft.ElevatedButton("Respuesta Texto ")

    lbl4=ft.Text("¿Que es la tecnologia ?")
    btna4=ft.ElevatedButton("Respuesta Audio")
    btnt4=ft.ElevatedButton("Respuesta Texto ")

    lbl5=ft.Text("¿Que es la tecnologia ?")
    btna5=ft.ElevatedButton("Respuesta Audio")
    btnt5=ft.ElevatedButton("Respuesta Texto ")

    lbl6=ft.Text("¿Que es la tecnologia ?")
    btna6=ft.ElevatedButton("Respuesta Audio")
    btnt6=ft.ElevatedButton("Respuesta Texto")

    page.add(
        ft.Row(
            alignment="STAR",
            controls=[btnIntro]
            ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl1,btna1,btnt1]
                            ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl2,btna2,btnt2]
                            ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl3,btna3,btnt3]
                            ),
                        ]
                    ),
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl4,btna4,btnt4]
                            ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl5,btna5,btnt5]
                            ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[lbl6,btna6,btnt6]
                            ),
                        ]
                    ),
                ]
            )
        
        )
ft.app(main)
