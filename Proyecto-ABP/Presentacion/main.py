import flet as ft
from flet import AppBar,ElevatedButton,View

def main(page: ft.Page):
    
    page.title=("Presentacion")
    page.bgcolor="#338AFF"

    page.window_width = 850
    page.window_height = 1000

    intro=ft.Audio(src="intro.mp3",volume=1,balance=0)
    page.overlay.append(intro)

    instru=ft.Audio(src="instrucciones.mp3",volume=1,balance=0)
    page.overlay.append(instru)

    #audios para la vista de tecnologia

    tec1=ft.Audio(src="Quees-tec.mp3",volume=1,balance=0)
    page.overlay.append(tec1)
    tec2=ft.Audio(src="tecnologia.mp3",volume=1,balance=0)
    page.overlay.append(tec2)
    tec3=ft.Audio(src="tecnologia2.mp3",volume=1,balance=0)
    page.overlay.append(tec3)
    tec4=ft.Audio(src="tecnologia3.mp3",volume=1,balance=0)
    page.overlay.append(tec4)
    tec5=ft.Audio(src="importancia-tec.mp3",volume=1,balance=0)
    page.overlay.append(tec5)
    tec6=ft.Audio(src="tec-benficos-expresarse.mp3",volume=1,balance=0)
    page.overlay.append(tec6)
    tec7=ft.Audio(src="tec-negativos.mp3",volume=1,balance=0)
    page.overlay.append(tec7)
    tec8=ft.Audio(src="tec-peligros.mp3",volume=1,balance=0)
    page.overlay.append(tec8)
    tec9=ft.Audio(src="tec-precauciones.mp3",volume=1,balance=0)
    page.overlay.append(tec9)


    #audios para la vista de stem 

    stem1=ft.Audio(src="quees-stem.mp3",volume=1,balance=0)
    page.overlay.append(stem1)
    stem2=ft.Audio(src="stem.mp3",volume=1,balance=0)
    page.overlay.append(stem2)
    stem3=ft.Audio(src="stem4.mp3",volume=1,balance=0)
    page.overlay.append(stem3)
    stem4=ft.Audio(src="beneficios-stem.mp3",volume=1,balance=0)
    page.overlay.append(stem4)
    stem5=ft.Audio(src="desafios-stem.mp3",volume=1,balance=0)
    page.overlay.append(stem5)
    stem6=ft.Audio(src="stem-soluciones.mp3",volume=1,balance=0)
    page.overlay.append(stem6)
    stem7=ft.Audio(src="stem-ciencia.mp3",volume=1,balance=0)
    page.overlay.append(stem7)
    stem8=ft.Audio(src="stem-tecnologia.mp3",volume=1,balance=0)
    page.overlay.append(stem8)
    stem9=ft.Audio(src="stem-ingenieria.mp3",volume=1,balance=0)
    page.overlay.append(stem9)
    stem10=ft.Audio(src="stem-matematicas.mp3",volume=1,balance=0)
    page.overlay.append(stem10)
    
    #botones y etiquetas para las vista de tecnologia
    
    btna1=ft.ElevatedButton("¿Que es la tecnologia?",on_click=lambda e:play_tec1(e))
    btna3=ft.ElevatedButton("¿Que formas ofrece la tecnologia para expresarnos?",on_click=lambda e:play_tec3(e))
    btna2=ft.ElevatedButton("¿Que beneficios ofrece la tecnologia como medio de expresion?",on_click=lambda e:play_tec2(e))
    btna4=ft.ElevatedButton("¿Como cambio la forma de expresarnos?",on_click=lambda e:play_tec4(e))
    btna5=ft.ElevatedButton("¿Que importancia tiene en la actualidad?",on_click=lambda e:play_tec5(e))
    btna6=ft.ElevatedButton("¿Es importante saber expresarse por medio de la tecnologia?",on_click=lambda e:play_tec6(e))
    btna7=ft.ElevatedButton("¿Que efectos negativos tiene el no saber expresarse por medio de la tecnologia?",on_click=lambda e:play_tec7(e))
    btna8=ft.ElevatedButton("¿A que peligros te enfrentas cuando te expresar por medio de la tecnologia?",on_click=lambda e:play_tec8(e))
    btna9=ft.ElevatedButton("¿Como podemos evitar los peliros que tiene la tecnologia?",on_click=lambda e:play_tec9(e))

    ima1=ft.Image(src="tec1.jpg",width=600,height=400,fit="cover")
    

    #botones y etiquetas para stem
    
    btna_1=ft.ElevatedButton("¿Que es STEM?",on_click=lambda e:play_stem1(e))
    btna_2=ft.ElevatedButton("¿Que importancia tienen las areas STEM en la actualidad?",on_click=lambda e:play_stem2(e))
    btna_3=ft.ElevatedButton("¿Es importante formentar el estudio de areas STEM desde una edad temprana?",on_click=lambda e:play_stem3(e))
    btna_4=ft.ElevatedButton("¿Que beneficios nos ofrecen las areas STEM? ",on_click=lambda e:play_stem4(e))
    btna_5=ft.ElevatedButton("¿Que desafios enfrentan las areas STEM?",on_click=lambda e:play_stem5(e) )
    btna_6=ft.ElevatedButton("¿Como podemos resolver los desafios? ",on_click=lambda e:play_stem6(e))
    btna_7=ft.ElevatedButton("El campo de la ciencia en las areas stem",on_click=lambda e:play_stem7(e))
    btna_8=ft.ElevatedButton("El campo de la tecnologia en las areas stem",on_click=lambda e:play_stem8(e))
    btna_9=ft.ElevatedButton("El campo de la ingenieria en las areas stem",on_click=lambda e:play_stem9(e))
    btna_10=ft.ElevatedButton("El campo de la matematicas  en las areas stem",on_click=lambda e:play_stem10(e))

    img1=ft.Image(src="stem1.jpg",width=680,height=400,fit="cover")


    #funcion para pausar todo 

    def stop_all():
        intro.pause()
        instru.pause()
        tec1.pause()
        tec2.pause()
        tec3.pause()
        tec4.pause()
        tec5.pause()
        tec6.pause()
        tec7.pause()
        tec8.pause()
        tec9.pause()
        stem1.pause()
        stem2.pause()
        stem3.pause()
        stem4.pause()
        stem5.pause()
        stem6.pause()
        stem7.pause()
        stem8.pause()
        stem9.pause()
        stem10.pause()
    def play_intro(e):
        stop_all()
        intro.play()

    def play_instru(e):
        stop_all()
        instru.play()
    
    def play_tec1(e):
        stop_all()
        tec1.play()
        
    def play_tec2(e):
        stop_all()
        tec2.play()

    def play_tec3(e):
        stop_all()
        tec3.play()

    def play_tec4(e):
        stop_all()
        tec4.play()
    
    def play_tec5(e):
        stop_all()
        tec5.play()

    def play_tec6(e):
        stop_all()
        tec6.play()

    def play_tec7(e):
        stop_all()
        tec7.play()

    def play_tec8(e):
        stop_all()
        tec8.play()

    def play_tec9(e):
        stop_all()
        tec9.play()

    def play_stem1(e):
        stop_all()
        stem1.play()

    def play_stem2(e):
        stop_all()
        stem2.play()

    def play_stem3(e):
        stop_all()
        stem3.play()

    def play_stem4(e):
        stop_all()
        stem4.play()    

    def play_stem5(e):
        stop_all()
        stem5 .play()

    def play_stem6(e):
        stop_all()
        stem6.play()

    def play_stem7(e):
        stop_all()
        stem7.play()

    def play_stem8(e):
        stop_all()
        stem8.play()

    def play_stem9(e):
        stop_all()
        stem9.play()

    def play_stem10(e):
        stop_all()
        stem10.play()



    
    #Funciones para comprovar las respuestas 
    def check_answer(e):
        # Aquí defines la respuesta correcta
        correct_answer = "Verdadero"
        if answer_field.value.strip().lower() == correct_answer.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image.visible = True
            btn1.disabled=True
            page.update()
            
            dialog.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            btn2.disabled=True
            dialog.open = False
            page.update()

    def check_answer2(e):
        # Aquí defines la respuesta correcta
        correct_answer2= "Verdadero"
        if answer_field2.value.strip().lower() == correct_answer2.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image2.visible = True
            btn2.disabled=True
            page.update()
            
            dialog2.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog2.open = False
            btn2.disabled=True
            page.update()

    def check_answer3(e):
        # Aquí defines la respuesta correcta
        correct_answer3= "Falso"
        if answer_field3.value.strip().lower() == correct_answer3.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image3.visible = True
            btn3.disabled=True
            page.update()
            dialog3.open = False  # Cierra el cuadro de diálogo
            page.update()
            
            
        else:
            # Mensaje de error si la respuesta es incorrecta
            btn3.disabled=True
            dialog3.open = False
            page.update()

    def check_answer4(e):
        # Aquí defines la respuesta correcta
        correct_answer4= "Verdadero"
        if answer_field4.value.strip().lower() == correct_answer4.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image4.visible = True
            btn4.disabled=True
            page.update()
           
            dialog4.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog4.open = False
            btn4.disabled=True
            page.update()

    def check_answer5(e):
        # Aquí defines la respuesta correcta
        correct_answer5= "Falso"
        if answer_field5.value.strip().lower() == correct_answer5.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image5.visible = True
            page.update()
            btn5.disabled=True
            dialog5.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog5.open = False
            btn5.disabled=True
            page.update()

    def check_answer6(e):
        # Aquí defines la respuesta correcta
        correct_answer6= "Falso"
        if answer_field6.value.strip().lower() == correct_answer6.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image6.visible = True
            btn6.disabled=True
            page.update()
            dialog6.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog6.open = False
            btn6.disabled=True
            page.update()

    def check_answer7(e):
        # Aquí defines la respuesta correcta
        correct_answer7= "Verdadero"
        if answer_field7.value.strip().lower() == correct_answer7.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image7.visible = True
            btn7.disabled=True
            page.update()
            dialog7.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog.open = False
            btn7.disabled=True
            page.update()

    def check_answer8(e):
        # Aquí defines la respuesta correcta
        correct_answer8= "Falso"
        if answer_field8.value.strip().lower() == correct_answer8.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image8.visible = True
            btn8.disabled=True
            page.update()
            dialog8.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog8.open = False
            btn8.disabled=True
            page.update()

    def check_answer9(e):
        # Aquí defines la respuesta correcta
        correct_answer9= "Verdadero"
        if answer_field9.value.strip().lower() == correct_answer9.lower():
            # Si la respuesta es correcta, muestra la imagen
            result_image9.visible = True
            btn9.disabled=True
            page.update()
            dialog9.open = False  # Cierra el cuadro de diálogo
            page.update()
        else:
            # Mensaje de error si la respuesta es incorrecta
            dialog9.open = False
            btn9.disabled=True
            page.update()

    #imagenes del rompecabezas 
    result_image = ft.Image(
        src="p1.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image2 = ft.Image(
        src="p2.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image3 = ft.Image(
        src="p3.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image4 = ft.Image(
        src="p4.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image5 = ft.Image(
        src="p5.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image6 = ft.Image(
        src="p6.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image7 = ft.Image(
        src="p7.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image8 = ft.Image(
        src="p8.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )

    result_image9 = ft.Image(
        src="p9.jpg",  # URL o ruta de la imagen
        visible=False,  # La imagen está oculta inicialmente
        width=170,
        height=170,
    )
    #Cuadros de dialogo para todas las preguntas
    dialog = ft.AlertDialog(
        title=ft.Text("Pregunta_1"),
        content=ft.Column([
            ft.Text("Las areas STEM cuantan con 4 campos de estudio"),
            (answer_field := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer(e)),
            ],
            actions_alignment="end",
            )

    dialog2 = ft.AlertDialog(
        title=ft.Text("Pregunta_2"),
        content=ft.Column([
            ft.Text("la tecnologia es un conjunto de conocimiento,habilidades y procesos "),
            (answer_field2 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer2(e)),
            ],
            actions_alignment="end",
            )

    dialog3 = ft.AlertDialog(
        title=ft.Text("Pregunta_3"),
        content=ft.Column([
            ft.Text("El arte es un campo de estudio de las area STEM"),
            (answer_field3 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer3(e)),
            ],
            actions_alignment="end",
            )

    dialog4 = ft.AlertDialog(
        title=ft.Text("Pregunta_4"),
        content=ft.Column([
            ft.Text('''configurar tus perfiles para que sean privados es una 
                    manera de prevenir los peligros de la tecnologia'''),
            (answer_field4 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer4(e)),
            ],
            actions_alignment="end",
            )

    dialog5 = ft.AlertDialog(
        title=ft.Text("Pregunta_5"),
        content=ft.Column([
            ft.Text("AL expresarte por internet no hay ningun peligro por que todo es 100% protejido"),
            (answer_field5 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer5(e)),
            ],
            actions_alignment="end",
            )

    dialog6 = ft.AlertDialog(
        title=ft.Text("Pregunta_6"),
        content=ft.Column([
            ft.Text("El estudio de las areas STEM desde una edad temprana es malo"),
            (answer_field6 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer6(e)),
            ],
            actions_alignment="end",
            )

    dialog7 = ft.AlertDialog(
        title=ft.Text("Pregunta_7"),
        content=ft.Column([
            ft.Text("Las areas STEM te ofrecen muchos befencios como preparacion para el futuro laboral "),
            (answer_field7 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer7(e)),
            ],
            actions_alignment="end",
            )

    dialog8 = ft.AlertDialog(
        title=ft.Text("Pregunta_8"),
        content=ft.Column([
            ft.Text("No saber expresarse atravez de la tecnologia no trae ninguna consecuencia "),
            (answer_field8 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer8(e)),
            ],
            actions_alignment="end",
            )

    dialog9 = ft.AlertDialog(
        title=ft.Text("Pregunta_9"),
        content=ft.Column([
            ft.Text("La ciencia es parte de las areas STEM"),
            (answer_field9 := ft.TextField(hint_text="Escribe tu respuesta aquí")),
            ]),
            actions=[
                ft.TextButton("Responder", on_click=lambda e:check_answer9(e)),
            ],
            actions_alignment="end",
            )

    #botones para le quizziz

    btn1=ft.ElevatedButton("Responder Pregunta", on_click=lambda e:open_dialog(e))
    btn2=ft.ElevatedButton("Responder Pregunta_2", on_click=lambda e:open_dialog2(e))
    btn3=ft.ElevatedButton("Responder Pregunta_3", on_click=lambda e:open_dialog3(e))
    btn4=ft.ElevatedButton("Responder Pregunta_4", on_click=lambda e:open_dialog4(e))
    btn5=ft.ElevatedButton("Responder Pregunta_5", on_click=lambda e:open_dialog5(e))
    btn6=ft.ElevatedButton("Responder Pregunta_6", on_click=lambda e:open_dialog6(e))
    btn7=ft.ElevatedButton("Responder Pregunta_7", on_click=lambda e:open_dialog7(e))
    btn8=ft.ElevatedButton("Responder Pregunta_8", on_click=lambda e:open_dialog8(e))
    btn9=ft.ElevatedButton("Responder Pregunta_9", on_click=lambda e:open_dialog9(e))

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

    def open_dialog7(e):
        page.dialog = dialog7
        dialog7.open = True
        page.update()

    def open_dialog8(e):
        page.dialog = dialog8
        dialog8.open = True
        page.update()

    def open_dialog9(e):
        page.dialog = dialog9
        dialog9.open = True
        page.update()  

    # funcion para reiniciar el juego y volver a habilitar los botones 
    
    def intento(e):
        result_image.visible=False
        result_image2.visible=False
        result_image3.visible=False
        result_image4.visible=False
        result_image5.visible=False
        result_image6.visible=False
        result_image7.visible=False
        result_image8.visible=False
        result_image9.visible=False
        btn1.disabled=False
        answer_field.value=""
        btn2.disabled=False
        answer_field2.value=""
        btn3.disabled=False
        answer_field3.value=""
        btn4.disabled=False
        answer_field4.value=""
        btn5.disabled=False
        answer_field5.value=""
        btn6.disabled=False
        answer_field6.value=""
        btn7.disabled=False
        answer_field7.value=""
        btn8.disabled=False
        answer_field8.value=""
        btn9.disabled=False
        answer_field9.value=""
        page.update()

        
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
                                        on_click=lambda _:[stop_all(),page.go('/Tec')]
                                    ),
                                    ft.Image(
                                        src='Portada.jpg',
                                        width=1250,
                                        height=500,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Introduccion",
                                        on_click=lambda e:play_intro(e)),
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
                                    ft.Column(
                                        alignment="CENTER",
                                        controls=[
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna1,btna2,btna3,]
                                            ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna4,btna5,btna6,]
                                                ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna7,btna8,]
                                                ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna9]
                                                ),
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[
                                                    ima1,]),]),
                                    ft.Row(
                                        alignment="CENTER",
                                        controls=[
                                            ElevatedButton("<",
                                                            on_click=lambda _:[stop_all(),page.go('/')]),
                                            ElevatedButton(">",
                                                            on_click=lambda _:[ stop_all(),page.go('/STEM')])
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
                                    ft.Column(
                                        alignment="CENTER",
                                        controls=[
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna_1,btna_2,btna_3,]
                                            ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna_4,btna_5,btna_6,]
                                                ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna_7,btna_8,btna_9]
                                                ),
                                            
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[btna_10]
                                                ),
                                            ft.Row(
                                                alignment="CENTER",
                                                controls=[img1]
                                            ),
                                            
                                            
                                            ]
                                        ),
                                    
                                    ft.Row(
                                        alignment="CENTER",
                                        controls=[
                                            ElevatedButton("<",
                                                            on_click=lambda _:[stop_all(),page.go('/Tec')]),
                                            ElevatedButton("Home",
                                                            on_click=lambda _:[stop_all(),page.go('/')]),
                                            ElevatedButton(">",
                                                            on_click=lambda _:[stop_all(),page.go('/question')])
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
                            AppBar(title=ft.Text("MINIJUEGO"),
                                bgcolor="black"
                                ),
                            
                            ft.Container(
                                
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment='STAR',
                                            controls=[
                                                ElevatedButton("<",
                                                                on_click=lambda _:[stop_all(),page.go('/STEM')]),
                                                ElevatedButton("Home",
                                                                on_click=lambda _:[stop_all,page.go('/')]),
                                                ElevatedButton("Volver intentar",
                                                                on_click=lambda e:intento(e)),
                                                ElevatedButton("instrucciones",
                                                                on_click=lambda e:play_instru(e)),
                                                ]
                                            ),
                                        ft.Row(
                                            controls=[
                                                btn1,btn2,btn3,btn4,btn5,btn6]

                                            ),
                                        ft.Row(
                                            alignment="CENTER",
                                            controls=[
                                                btn7,btn8,btn9]),
                                        ft.Row(
                                            alignment='CENTER',
                                            controls=[
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image,result_image4,result_image7
                                                        ]
                                                    ),
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image2,result_image5,result_image8
                                                        ]
                                                    ),
                                                ft.Column(
                                                    alignment='CENTER',
                                                    controls=[
                                                        result_image3,result_image6,result_image9])]),
                                        
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
