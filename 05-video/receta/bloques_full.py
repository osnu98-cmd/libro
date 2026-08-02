import json
SEG=json.load(open("segmentos_full.json"))
def g(i,j): return [tuple(SEG[k]) for k in range(i,j+1)]
BLOQUES=[
 (g(0,4),   "Hola, mi nombre es Oscar Núñez y soy el presidente de la Fundación Soy del Campo. "
            "Este lunes 3, por tercera o cuarta vez ya, se va a volver a votar un proyecto que busca "
            "prohibir las carreras de galgos, junto con él un proyecto que busca su regulación. "
            "Si eres un diputado nuevo o tienes alguna duda de cómo votar este proyecto,"),
 (g(5,12),  "escucha lo que te voy a decir. En primer lugar, los autores de este proyecto: "
            "Félix González, Melo, Sagardía, Camila Musante, Yovana Ahumada, están todos fuera del Congreso. "
            "Una de las diputadas que sobrevivió fue ayudada con un tremendo espaldarazo"),
 (g(13,15), "por un conocido canal que puso su mejor rostro en una investigación sobre las carreras de galgos, "
            "que por supuesto, una vez más, no concluyó nada, pero le sirvió para salir reelecta. "
            "Pon atención y ojo a este video,"),
 (g(16,19), "porque si tú no tienes un canal de televisión que te respalde días antes de la elección, "
            "entonces tienes que escuchar esto. Con gran elocuencia y teatralidad te van a contar cómo"),
 (g(20,29), "cada vez que se corre una carrera de perros, el perro que pierde o lo matan, o le quiebran "
            "las patas en represalia; que cuando llegan a cierta edad son abandonados en las calles, "
            "o que los inyectan en las pistas delante de los niños con todo tipo de sustancias ilícitas "
            "y prohibidas. Sin embargo, en varios años de tramitación, innumerable cantidad de informes "
            "de las policías, de tribunales"),
 (g(30,39), "y de los organismos competentes han demostrado que todo esto es falso, pero igualmente se "
            "sigue transmitiendo como si fuese un mantra religioso por todo tipo de actores, actrices, "
            "influencers y políticos firmemente comprometidos con la causa."),
 (g(40,47), "Aquí es donde cabe entonces usar un poco la lógica. Si correr es tan malo para los perros, "
            "¿por qué nadie dice nada de las carreras de caballos? Si las supuestas apuestas contra las "
            "que van a hablar también mañana son tan malas, ¿por qué no dice nadie nada respecto al fútbol? "
            "La respuesta es muy sencilla. Los caballos y el fútbol representan gente de poder."),
 (g(48,56), "Los perros, en cambio, pertenecen al pueblo. Y esta razón queda más que clara con el argumento "
            "que ahora van a dar para prohibir la regulación: es que si se regula, entonces el Estado va a "
            "tener que poner fondos para esta actividad."),
 (g(57,62), "Qué terrible, ¿no? Ahora queremos cuidarle los fondos al Estado. O sea, está muy bien que los "
            "ricos y poderosos se lleven los fondos del Estado, pero que el pueblo se pueda llevar estos "
            "fondos, eso les parece bastante malo. La lógica es evidente. Por eso te invito a que tomes "
            "lección de lo que pasó con los diputados fanáticos."),
 (g(63,71), "Bueno, salvo que tengas un canal de televisión que te respalde, por supuesto. Escucha el sentir "
            "de tu gente. La gente vota con el corazón, pero también con el sentido común. Y aquí vienen "
            "dos proyectos. Uno que busca prohibir, dejando en desamparo muchos perros, y hay otro que "
            "busca regular, que efectivamente va a cuidar a los animales."),
 (g(72,76), "La decisión es tuya, pero la razón indica que la protección es el mejor camino."),
]
CLAVES=["prohibir","regulación","escucha","fuera","Congreso","sobrevivió","canal","nada",
        "reelecta","falso","mantra","caballos","fútbol","pueblo","fanáticos","desamparo","protección"]
NOMBRES=["González","Melo","Sagardía","Musante","Ahumada"]
