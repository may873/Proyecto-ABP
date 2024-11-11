import flet as ft
from flet import AppBar,ElevatedButton,View

def main(page: ft.Page):
    
    page.title=("Presentacion")
    page.bgcolor="#26B69D"

    #Funciones para comprovar las respuestas 
    def check_answer(e):
        # Aquí defines la respuesta correcta
        correct_answer = "V"
        if answer_field.value.strip().lower() == correct_answer.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image.visible = True
            page.update()
            dialog.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    def check_answer2(e):
        # Aquí defines la respuesta correcta
        correct_answer2= "F"
        if answer_field2.value.strip().lower() == correct_answer2.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image2.visible = True
            page.update()
            dialog2.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    def check_answer3(e):
        # Aquí defines la respuesta correcta
        correct_answer3= "V"
        if answer_field3.value.strip().lower() == correct_answer3.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image3.visible = True
            page.update()
            dialog3.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    def check_answer4(e):
        # Aquí defines la respuesta correcta
        correct_answer4= "F"
        if answer_field4.value.strip().lower() == correct_answer4.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image4.visible = True
            page.update()
            dialog4.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    def check_answer5(e):
        # Aquí defines la respuesta correcta
        correct_answer5= "V"
        if answer_field5.value.strip().lower() == correct_answer5.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image5.visible = True
            page.update()
            dialog5.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    def check_answer6(e):
        # Aquí defines la respuesta correcta
        correct_answer6= "V"
        if answer_field6.value.strip().lower() == correct_answer6.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image6.visible = True
            page.update()
            dialog6.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            error_label.value = "Respuesta incorrecta. Intenta de nuevo."
            page.update()

    result_image = ft.Image(
        src="p1.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    result_image2 = ft.Image(
        src="p2.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    result_image3 = ft.Image(
        src="p3.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    result_image4 = ft.Image(
        src="p4.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    result_image5 = ft.Image(
        src="p5.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )

    result_image6 = ft.Image(
        src="p6.png",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=200,
        height=200,
    )
    #Cuadros de dialogo para todas las preguntas
    dialog = ft.AlertDialog(
        title=ft.Text("Pregunta"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer(e)),
            ],
            actions_alignment="end",
            )

    dialog2 = ft.AlertDialog(
        title=ft.Text("Pregunta2"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field2 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer2(e)),
            ],
            actions_alignment="end",
            )

    dialog3 = ft.AlertDialog(
        title=ft.Text("Pregunta3"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field3 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer3(e)),
            ],
            actions_alignment="end",
            )

    dialog4 = ft.AlertDialog(
        title=ft.Text("Pregunta4"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field4 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer4(e)),
            ],
            actions_alignment="end",
            )

    dialog5 = ft.AlertDialog(
        title=ft.Text("Pregunta5"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field5 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer5(e)),
            ],
            actions_alignment="end",
            )

    dialog6 = ft.AlertDialog(
        title=ft.Text("Pregunta6"),
        content=ft.Column([
            ft.Text("¿El Lenguaje de programacion Python es el mas usado en la actualidad?"),
            (answer_field6 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            (error_label := ft.Text("", color="red"))  # Para mostrar un mensaje de error
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer6(e)),
            ],
            actions_alignment="end",
            )

    #Funcion para abrir todos los dialogos
    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    def open_dialog2(e):
        page.dialog = dialog2
        dialog2.open = True
        page.update()

    def open_dialog3(e):
        page.dialog = dialog3
        dialog3.open = True
        page.update()

    def open_dialog4(e):
        page.dialog = dialog4
        dialog4.open = True
        page.update()

    def open_dialog5(e):
        page.dialog = dialog5
        dialog5.open = True
        page.update()

    def open_dialog6(e):
        page.dialog = dialog6
        dialog6.open = True
        page.update()        

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

    txtR1=ft.TextField(label="ingresa el indice de tu respuesta")
    lblP1=ft.Text("¿Que es la tecnologia?",color="white")
    lblia=ft.Text("a)",color="white")
    lblib=ft.Text("b)",color="white")
    lblic=ft.Text("c)",color="white")

    

    
    


    
    #vistas del proyecto
    def route_change(route):
        page.views.clear()
        

        #Vista de portada 
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("¿La tecnologia como medio de exprecion?"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'La Tecnologia',
                                        on_click=lambda _:page.go('/Tec')
                                    ),
                                    ft.Image(
                                        src='Portada.jpg',
                                        width=1250,
                                        height=500,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Introduccion",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment
                                ),
                                bgcolor=page.bgcolor,
                                expand=True
                            )
                        ],
                        bgcolor=page.bgcolor
                    )
                )
            
        elif page.route == '/Tec':
            page.views.append(
                View(
                    "/Tec",
                    controls=[
                        AppBar(
                            title=ft.Text("¿Sabes usar la tecnoligia para expresarte?"),
                            bgcolor="black",
                            ),
                        ft.Container(
                            ft.Column(
                                
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
                                    
                                    ft.Row(
                                        alignment="CENTER",
                                        controls=[
                                            ElevatedButton("<",
                                                            on_click=lambda _:page.go('/')),
                                            ElevatedButton("Home",
                                                    on_click=lambda _:page.go('/')),
                                            ElevatedButton(">",
                                                            on_click=lambda _:[ page.go('/STEM')])
                                                            ]
                                                        ),
                                        ],
                                        alignment=ft.MainAxisAlignment

                                    ),
                                bgcolor=page.bgcolor,
                                expand=True
                            )
                        ],
                        bgcolor=page.bgcolor
                    )
                )
        elif page.route == '/STEM':
            page.views.append(
                View(
                    "/STEM",
                    controls=[
                        AppBar(
                            title=ft.Text("¿Sabes que son las areas STEM?"),
                            bgcolor="black",
                            ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment="CENTER",
                                        controls=[
                                            ElevatedButton("<",
                                                            on_click=lambda _:page.go('/Tec')),
                                            ElevatedButton("Home",
                                                            on_click=lambda _:page.go('/')),
                                            ElevatedButton(">",
                                                            on_click=lambda _:[page.go('/video')])
                                                ]
                                            )
                                    ],
                                    alignment=ft.MainAxisAlignment
                                ),
                                bgcolor=page.bgcolor,
                                expand=True
                            )
                        ],
                        bgcolor=page.bgcolor
                    )
                )
        elif page.route == '/video':
            page.views.append(
                View(
                    '/video',
                    controls=[
                        AppBar(
                            title=ft.Text("VIDEOS DE RETROALIMENTACION"),
                            bgcolor="black",
                            ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    
                                    ft.Row(
                                        alignment='CENTER',
                                        controls=[
                                            ElevatedButton("<",
                                                            on_click=lambda _:page.go('/STEM')),
                                            ElevatedButton("Home",
                                                            on_click=lambda _:page.go('/')),
                                            ElevatedButton(">",
                                                            on_click=lambda _:[page.go('/question')]
                                                            )
                                            ]
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment
                                ),
                                bgcolor=page.bgcolor,
                                expand=True
                            )
                        ],
                        bgcolor=page.bgcolor
                    )
                )
        elif page.route == '/question':
            
            page.views.append(
                    View(
                        '/question',
                        controls=[
                            AppBar(title=ft.Text("QUIZZIZ"),
                                bgcolor="black"
                                ),
                            
                            ft.Container(
                                
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.ElevatedButton("Responder Pregunta", on_click=lambda e:open_dialog(e)),
                                                ft.ElevatedButton("Responder Pregunta_2", on_click=lambda e:open_dialog2(e)),
                                                ft.ElevatedButton("Responder Pregunta_3", on_click=lambda e:open_dialog3(e)),
                                                ft.ElevatedButton("Responder Pregunta_4", on_click=lambda e:open_dialog4(e)),
                                                ft.ElevatedButton("Responder Pregunta_5", on_click=lambda e:open_dialog5(e)),
                                                ft.ElevatedButton("Responder Pregunta_6", on_click=lambda e:open_dialog6(e)),
                                                ]
                                            ),
                                        ft.Row(
                                            alignment='CENTER',
                                            controls=[
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image,result_image4
                                                        ]
                                                    ),
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image2,result_image5
                                                        ]
                                                    ),
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image3,result_image6])]),
                                        ft.Row(
                                            alignment='CENTER',
                                            controls=[
                                                ElevatedButton("<",
                                                                on_click=lambda _:page.go('/STEM')),
                                                ElevatedButton("Home",
                                                                on_click=lambda _:page.go('/')),
                                                ]
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment
                                    ),
                                    bgcolor=page.bgcolor,
                                    expand=True
                                ),
                                
                            ],
                            bgcolor=page.bgcolor,
                            
                        ),
                    ),
               
        
        page.update()
        
    page.on_route_change = route_change
    page.go(page.route)
    

ft.app(target=main, assets_dir="assets")
