from tkinter import *
vent = Tk()
vent.geometry("995x845")
vent.title(" SLAB DESING ")

# Recuadro 1 Datos iniciales

rec1 = LabelFrame(vent, text = '  Datos iniciales.  ')
rec1.pack()
rec1.place(x=345, y=5, width=320, height=300)

c1tex01 = Label(rec1, text = "fc. Resistencia del concreto _ MPa"); c1tex01.pack()
c1tex01.place(x=10, y=10, width=210, height=20)
c1ent01 = Entry(rec1, justify=CENTER);                              c1ent01.place(x=230, y=10, width=80, height=20)

c1tex02 = Label(rec1, text = "fy. Fluencia del acero _ MPa");       c1tex02.pack()
c1tex02.place(x=10, y=40, width=210, height=20)
c1ent02 = Entry(rec1, justify=CENTER);                              c1ent02.place(x=230, y=40, width=80, height=20)

c1tex03 = Label(rec1, text = "b. Ancho de la sección _ cm");        c1tex03.pack()
c1tex03.place(x=10, y=70, width=210, height=20)
c1ent03 = Entry(rec1, justify=CENTER);                              c1ent03.place(x=230, y=70, width=80, height=20)

c1tex04 = Label(rec1, text = "h. Espesor de la losa _ cm");         c1tex04.pack()
c1tex04.place(x=10, y=100, width=210, height=20)
c1ent04 = Entry(rec1, justify=CENTER);                              c1ent04.place(x=230, y=100, width=80, height=20)

c1tex05 = Label(rec1, text = "pmín. Cuantía mínima.");               c1tex05.pack()
c1tex05.place(x=10, y=130, width=210, height=20)
c1ent05 = Entry(rec1, justify=CENTER);                              c1ent05.place(x=230, y=130, width=80, height=20)

c1tex06 = Label(rec1, text = "øv. Coeficiente de fricción.");        c1tex06.pack()
c1tex06.place(x=10, y=160, width=210, height=20)
c1ent06 = Entry(rec1, justify=CENTER);                              c1ent06.place(x=230, y=160, width=80, height=20)

c1tex07 = Label(rec1, text = "Recubrimiento parrilla sup _ cm");    c1tex07.pack()
c1tex07.place(x=10, y=190, width=210, height=20)
c1ent07 = Entry(rec1, justify=CENTER);                              c1ent07.place(x=230, y=190, width=80, height=20)

c1tex08 = Label(rec1, text = "Recubrimiento parrilla inf_ cm");     c1tex08.pack()
c1tex08.place(x=10, y=220, width=210, height=20)
c1ent08 = Entry(rec1, justify=CENTER);                              c1ent08.place(x=230, y=220, width=80, height=20)

c1tex09 = Label(rec1, text = "Asmin. Acero mínimo _ cm²");          c1tex09.pack()
c1tex09.place(x=10, y=250, width=210, height=20)
c1ent09 = Entry(rec1, justify=CENTER);                              c1ent09.place(x=230, y=250, width=80, height=20); c1ent09.config(bg="#ecf0f1")

# Recuadro 2 Parrilla superior

rec2 = LabelFrame(vent, text = '  Diseño parilla superior.  ')
rec2.pack()
rec2.place(x=5, y=315, width=490, height=370)

c2tex01 = Label(rec2, text = "");                                         c2tex01.pack()
c2tex01.place(x=10, y=10, width=120, height=20)

c2tex02 = Label(rec2, text = "Dir longt _ Mxx", font='Helvetica 7 bold'); c2tex02.pack()
c2tex02.place(x=230, y=10, width=120, height=20)

c2tex03 = Label(rec2, text = "Dir Trans _ Myy", font='Helvetica 7 bold'); c2tex03.pack()
c2tex03.place(x=360, y=10, width=120, height=20)

c2tex04 = Label(rec2, text = "Momento de diseño _ kN.cm");          c2tex01.pack()
c2tex04.place(x=10, y=40, width=210, height=20)
c2ent04 = Entry(rec2, justify=CENTER);                              c2ent04.place(x=230, y=40, width=120, height=20)
c2ent54 = Entry(rec2, justify=CENTER);                              c2ent54.place(x=360, y=40, width=120, height=20)

c2tex05 = Label(rec2, text = "preq. Cuantía requerida.");            c2tex05.pack()
c2tex05.place(x=10, y=70, width=210, height=20)
c2ent05 = Entry(rec2, justify=CENTER);                              c2ent05.place(x=230, y=70, width=120, height=20); c2ent05.config(bg="#ecf0f1")
c2ent55 = Entry(rec2, justify=CENTER);                              c2ent55.place(x=360, y=70, width=120, height=20); c2ent55.config(bg="#ecf0f1")

c2tex06 = Label(rec2, text = "Asreq. Acero requerido _ cm²");       c2tex06.pack()
c2tex06.place(x=10, y=100, width=210, height=20)
c2ent06 = Entry(rec2, justify=CENTER);                              c2ent06.place(x=230, y=100, width=120, height=20); c2ent06.config(bg="#ecf0f1")
c2ent56 = Entry(rec2, justify=CENTER);                              c2ent56.place(x=360, y=100, width=120, height=20); c2ent56.config(bg="#ecf0f1")

c2tex07 = Label(rec2, text = "Ascol. Acero colocado _ cm²");        c2tex07.pack()
c2tex07.place(x=10, y=130, width=210, height=20)
c2ent07 = Entry(rec2, justify=CENTER);                              c2ent07.place(x=230, y=130, width=120, height=20); c2ent07.config(bg="#ecf0f1")
c2ent57 = Entry(rec2, justify=CENTER);                              c2ent57.place(x=360, y=130, width=120, height=20); c2ent57.config(bg="#ecf0f1")

c2tex08 = Label(rec2, text = "N° de barra a usar.");                 c2tex08.pack()
c2tex08.place(x=10, y=160, width=210, height=20)
c2ent08 = Entry(rec2, justify=CENTER);                              c2ent08.place(x=230, y=160, width=120, height=20)
c2ent58 = Entry(rec2, justify=CENTER);                              c2ent58.place(x=360, y=160, width=120, height=20)

c2tex09 = Label(rec2, text = "Distribución del refuerzo.");          c2tex09.pack()
c2tex09.place(x=10, y=190, width=210, height=20)
c2ent09 = Entry(rec2, justify=CENTER);                              c2ent09.place(x=230, y=190, width=120, height=20); c2ent09.config(bg="#ecf0f1")
c2ent59 = Entry(rec2, justify=CENTER);                              c2ent59.place(x=360, y=190, width=120, height=20); c2ent59.config(bg="#ecf0f1")

c2tex10 = Label(rec2, text = "Chequeo momento nominal.");            c2tex10.pack()
c2tex10.place(x=10, y=230, width=210, height=20)

c2tex11 = Label(rec2, text = "Mn _ Dir x", font='Helvetica 7 bold'); c2tex11.pack()
c2tex11.place(x=230, y=230, width=120, height=20)

c2tex12 = Label(rec2, text = "Mn _ Dir y", font='Helvetica 7 bold'); c2tex12.pack()
c2tex12.place(x=360, y=230, width=120, height=20)

c2tex13 = Label(rec2, text = "Ascol. Acero colocado real _ cm²");    c2tex13.pack()
c2tex13.place(x=10, y=260, width=210, height=20)
c2ent13 = Entry(rec2, justify=CENTER);                              c2ent13.place(x=230, y=260, width=120, height=20); c2ent13.config(bg="#ecf0f1")
c2ent63 = Entry(rec2, justify=CENTER);                              c2ent63.place(x=360, y=260, width=120, height=20); c2ent63.config(bg="#ecf0f1")

c2tex14 = Label(rec2, text = "øMn. Momento nominal _ kN.cm");       c2tex14.pack()
c2tex14.place(x=10, y=290, width=210, height=20)
c2ent14 = Entry(rec2, justify=CENTER);                              c2ent14.place(x=230, y=290, width=120, height=20); c2ent14.config(bg="#ecf0f1")
c2ent64 = Entry(rec2, justify=CENTER);                              c2ent64.place(x=360, y=290, width=120, height=20); c2ent64.config(bg="#ecf0f1")

c2tex15 = Label(rec2, text = "Mu. < øMn.");                         c2tex15.pack()
c2tex15.place(x=10, y=320, width=210, height=20)
c2ent15 = Entry(rec2, justify=CENTER);                              c2ent15.place(x=230, y=320, width=120, height=20); c2ent15.config(bg="#ecf0f1")
c2ent65 = Entry(rec2, justify=CENTER);                              c2ent65.place(x=360, y=320, width=120, height=20); c2ent65.config(bg="#ecf0f1")

# Recuadro 3. Parrilla inferior

rec3 = LabelFrame(vent, text = '  Diseño parrilla inferior.  ')
rec3.pack()
rec3.place(x=500, y=315, width=490, height=370)

c3tex01 = Label(rec3, text = "");                                         c3tex01.pack()
c3tex01.place(x=10, y=10, width=120, height=20)

c3tex02 = Label(rec3, text = "Dir longt _ Mxx", font='Helvetica 7 bold'); c3tex02.pack()
c3tex02.place(x=230, y=10, width=120, height=20)

c3tex03 = Label(rec3, text = "Dir Trans _ Myy", font='Helvetica 7 bold'); c3tex03.pack()
c3tex03.place(x=360, y=10, width=120, height=20)

c3tex04 = Label(rec3, text = "Momento de diseño _ kN.cm");          c3tex01.pack()
c3tex04.place(x=10, y=40, width=210, height=20)
c3ent04 = Entry(rec3, justify=CENTER);                              c3ent04.place(x=230, y=40, width=120, height=20)
c3ent54 = Entry(rec3, justify=CENTER);                              c3ent54.place(x=360, y=40, width=120, height=20)

c3tex05 = Label(rec3, text = "preq. Cuantía requerida.");            c3tex05.pack()
c3tex05.place(x=10, y=70, width=210, height=20)
c3ent05 = Entry(rec3, justify=CENTER);                              c3ent05.place(x=230, y=70, width=120, height=20); c3ent05.config(bg="#ecf0f1")
c3ent55 = Entry(rec3, justify=CENTER);                              c3ent55.place(x=360, y=70, width=120, height=20); c3ent55.config(bg="#ecf0f1")

c3tex06 = Label(rec3, text = "Asreq. Acero requerido _ cm²");       c3tex06.pack()
c3tex06.place(x=10, y=100, width=210, height=20)
c3ent06 = Entry(rec3, justify=CENTER);                              c3ent06.place(x=230, y=100, width=120, height=20); c3ent06.config(bg="#ecf0f1")
c3ent56 = Entry(rec3, justify=CENTER);                              c3ent56.place(x=360, y=100, width=120, height=20); c3ent56.config(bg="#ecf0f1")

c3tex07 = Label(rec3, text = "Ascol. Acero colocado _ cm²");        c3tex07.pack()
c3tex07.place(x=10, y=130, width=210, height=20)
c3ent07 = Entry(rec3, justify=CENTER);                              c3ent07.place(x=230, y=130, width=120, height=20); c3ent07.config(bg="#ecf0f1")
c3ent57 = Entry(rec3, justify=CENTER);                              c3ent57.place(x=360, y=130, width=120, height=20); c3ent57.config(bg="#ecf0f1")

c3tex08 = Label(rec3, text = "N° de barra a usar.");                 c3tex08.pack()
c3tex08.place(x=10, y=160, width=210, height=20)
c3ent08 = Entry(rec3, justify=CENTER);                              c3ent08.place(x=230, y=160, width=120, height=20)
c3ent58 = Entry(rec3, justify=CENTER);                              c3ent58.place(x=360, y=160, width=120, height=20)

c3tex09 = Label(rec3, text = "Distribución del refuerzo.");          c3tex09.pack()
c3tex09.place(x=10, y=190, width=210, height=20)
c3ent09 = Entry(rec3, justify=CENTER);                              c3ent09.place(x=230, y=190, width=120, height=20); c3ent09.config(bg="#ecf0f1")
c3ent59 = Entry(rec3, justify=CENTER);                              c3ent59.place(x=360, y=190, width=120, height=20); c3ent59.config(bg="#ecf0f1")

c3tex10 = Label(rec3, text = "Chequeo momento nominal.");            c3tex10.pack()
c3tex10.place(x=10, y=230, width=210, height=20)

c3tex11 = Label(rec3, text = "Mn _ Dir x", font='Helvetica 7 bold'); c3tex11.pack()
c3tex11.place(x=230, y=230, width=120, height=20)

c3tex12 = Label(rec3, text = "Mn _ Dir y", font='Helvetica 7 bold'); c3tex12.pack()
c3tex12.place(x=360, y=230, width=120, height=20)

c3tex13 = Label(rec3, text = "Ascol. Acero colocado real _ cm²");   c3tex13.pack()
c3tex13.place(x=10, y=260, width=210, height=20)
c3ent13 = Entry(rec3, justify=CENTER);                              c3ent13.place(x=230, y=260, width=120, height=20); c3ent13.config(bg="#ecf0f1")
c3ent63 = Entry(rec3, justify=CENTER);                              c3ent63.place(x=360, y=260, width=120, height=20); c3ent63.config(bg="#ecf0f1")

c3tex14 = Label(rec3, text = "øMn. Momento nominal _ kN.cm");       c3tex14.pack()
c3tex14.place(x=10, y=290, width=210, height=20)
c3ent14 = Entry(rec3, justify=CENTER);                              c3ent14.place(x=230, y=290, width=120, height=20); c3ent14.config(bg="#ecf0f1")
c3ent64 = Entry(rec3, justify=CENTER);                              c3ent64.place(x=360, y=290, width=120, height=20); c3ent64.config(bg="#ecf0f1")

c3tex15 = Label(rec3, text = "Mu. < øMn.");                         c3tex15.pack()
c3tex15.place(x=10, y=320, width=210, height=20)
c3ent15 = Entry(rec3, justify=CENTER);                              c3ent15.place(x=230, y=320, width=120, height=20); c3ent15.config(bg="#ecf0f1")
c3ent65 = Entry(rec3, justify=CENTER);                              c3ent65.place(x=360, y=320, width=120, height=20); c3ent65.config(bg="#ecf0f1")

# Recuadro 4 Cortante

rec4 = LabelFrame(vent, text = '  Cortante simple.  ')
rec4.pack()
rec4.place(x=5, y=690, width=490, height=150)

c4tex01 = Label(rec4, text = "Chequeo a cortante simple.");            c4tex01.pack()
c4tex01.place(x=10, y=10, width=210, height=20)

c4tex02 = Label(rec4, text = "Vc _ Dir x", font='Helvetica 7 bold');  c4tex02.pack()
c4tex02.place(x=230, y=10, width=120, height=20)

c4tex03 = Label(rec4, text = "Vc _ Dir Vy", font='Helvetica 7 bold'); c4tex03.pack()
c4tex03.place(x=360, y=10, width=120, height=20)

c4tex04 = Label(rec4, text = "Vu. Cortante de diseño _ kN");          c4tex04.pack()
c4tex04.place(x=10, y=40, width=210, height=20)
c4ent04 = Entry(rec4, justify=CENTER);                              c4ent04.place(x=230, y=40, width=120, height=20)
c4ent54 = Entry(rec4, justify=CENTER);                              c4ent54.place(x=360, y=40, width=120, height=20)

c4tex05 = Label(rec4, text = "øVc. Resitencia del concreto _ kN");  c4tex05.pack()
c4tex05.place(x=10, y=70, width=210, height=20)
c4ent05 = Entry(rec4, justify=CENTER);                              c4ent05.place(x=230, y=70, width=120, height=20); c4ent05.config(bg="#ecf0f1")
c4ent55 = Entry(rec4, justify=CENTER);                              c4ent55.place(x=360, y=70, width=120, height=20); c4ent55.config(bg="#ecf0f1")

c4tex06 = Label(rec4, text = "Vu. < øVc.");                         c4tex06.pack()
c4tex06.place(x=10, y=100, width=210, height=20)
c4ent06 = Entry(rec4, justify=CENTER);                              c4ent06.place(x=230, y=100, width=120, height=20); c4ent06.config(bg="#ecf0f1")
c4ent56 = Entry(rec4, justify=CENTER);                              c4ent56.place(x=360, y=100, width=120, height=20); c4ent56.config(bg="#ecf0f1")

# Recuadro 5 botones

rec5 = LabelFrame(vent, text = '  Opciones.  ')
rec5.pack()
rec5.place(x=500, y=725, width=490, height=60)

bot1 = Button(rec5, text = 'Calcular', font='Helvetica 8 bold'); bot1.pack()
bot1.place(x=10, y=10, width=100, height=20)

bot2 = Button(rec5, text = 'Borrar', font='Helvetica 8 bold'); bot2.pack()
bot2.place(x=124, y=10, width=100, height=20)

bot3 = Button(rec5, text = 'Guardar .xls', font='Helvetica 8 bold'); bot3.pack()
bot3.place(x=236, y=10, width=100, height=20)

bot4 = Button(rec5, text = 'Reporte Detallado .xls', font='Helvetica 8 bold'); bot4.pack()
bot4.place(x=348, y=10, width=130, height=20)

label = Label(vent, text = "IEB - Diseños civiles - Obras Especiales - 2023 w.a.t. ", font='Arial 7'); label.pack()
label.place(x=500, y=795, width=490, height=10)

vent.mainloop()