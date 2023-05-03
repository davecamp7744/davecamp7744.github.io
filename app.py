from flask import Flask, request, Markup, render_template

app = Flask(__name__)
global usuario
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    usuario = user_text
    return "Hola: " + user_text + " un gusto ahora puedes comenzar"


@app.route('/') 
def index():
    return render_template('index.html')
buttons = [
        Markup('<button onclick="send_message(\'Algoritmos\')" class="custom-btn btn-16">Algoritmos</button>'),
        Markup('<button onclick="send_message(\'EstructurasControl\')" class="custom-btn btn-16">Estructuras de Control de algoritmos</button>'),
        Markup('<button onclick="send_message(\'Metodologia\')" class="custom-btn btn-16">Metodología del desarrollo de programas</button>'),
        Markup('<button onclick="send_message(\'Codificacion\')" class="custom-btn btn-16">Codificacion</button>'),
        Markup('<button onclick="send_message(\'salir\')" class="custom-btn btn-16">Salir</button>')
    ]
butop1 = '<button onclick="send_message(\'op1\')" class="custom-btn btn-16">op1</button>'
butop2 = '<button onclick="send_message(\'op2\')" class="custom-btn btn-16">op2</button>'
butop3 = '<button onclick="send_message(\'op3\')" class="custom-btn btn-16">op3</button>'
butop4 = '<button onclick="send_message(\'op4\')" class="custom-btn btn-16">op4</button>'
regresar = '<button onclick="send_message(\'regresar\')" class="custom-btn btn-16">regresar</button>'

algoritmos = [
        Markup('<button onclick="send_message(\'significado\')" class="custom-btn btn-16">¿Que es?</button>'),
        Markup('<button onclick="send_message(\'funcion\')" class="custom-btn btn-16">¿Como funciona un algoritmo?</button>'),
        Markup('<button onclick="send_message(\'uso\')" class="custom-btn btn-16">¿Para que sirve un algoritmo?</button>'),
        Markup('<button onclick="send_message(\'fundamentos\')" class="custom-btn btn-16">Fundamentos de algoritmos</button>')
    ]
EstructurasControl = [
        Markup('<button onclick="send_message(\'usocontrol\')" class="custom-btn btn-16">¿Para qué sirven las estructuras de control?</button>'),
        Markup('<button onclick="send_message(\'tiposcontrol\')" class="custom-btn btn-16">¿Cuáles son los tipos de estructuras de control?</button>'),
        Markup('<button onclick="send_message(\'subalgoritmos\')" class="custom-btn btn-16">Subalgoritmos</button>'),
    ]
Metodologia = [
        Markup('<button onclick="send_message(\'significadometo\')" class="custom-btn btn-16">¿Para qué sirven las estructuras de control?</button>'),
        Markup('<button onclick="send_message(\'tiposmeto\')" class="custom-btn btn-16">¿Cuáles son los tipos de estructuras de control?</button>')
    ]
Codificacion = [
        Markup('<button onclick="send_message(\'significadocodi\')" class="custom-btn btn-16">Significado de codificacion</button>'),
        Markup('<button onclick="send_message(\'etapas\')" class="custom-btn btn-16">Etapas</button>')
    ]


@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    if message == 'Comenzar':
        return buttons

    elif message == 'Concepto':
        texto = "texto de concepto"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , butop1, butop2, butop3, butop4, regresar]
        return info 
    #===============================================================================================================================
    elif message == 'EstructurasControl':
        texto = "Tema de Estructura de control"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , EstructurasControl, regresar]
        return info 
    elif message == 'subalgoritmos':
        texto = "Uno de los métodos fundamentales para resolver un problema es dividirlo en problemas más pequeños, llamados subproblemas. Estos problemas pueden a su vez dividirse repetidamente en problemas más pequeños hasta que los problemas sean de fácil solución."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , EstructurasControl, regresar]
        return info
    elif message == 'usocontrol':
        texto = "Las estructuras de control nos dan el poder de alterar, controlar o modificar el orden o el flujo en el que se ejecutan las instrucciones de un software a voluntad."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , EstructurasControl, regresar]
        return info
    elif message == 'tiposcontrol':
        texto1 = "<li>Secuenciales o de secuencia: Esta es la estructura básica, ya que nos permite asegurar que una instrucción se ejecuta después de la otra siguiendo el orden en que fueron escritas</li>"
        texto2 = "<li>Selectivas, de selección o condicionales: Este tipo de estructuras de control nos sirven cuando necesitamos que se evalúe el valor de alguna variable o de alguna condición para decidir qué instrucciones ejecutar a continuación.</li>"
        texto3 = "<li>Iterativas, de iteración, de repetición o repetitivas: Este tipo de estructuras de control nos sirven cuando necesitamos que se ejecute un conjunto específico de instrucciones en diversas ocasiones.</li>"
        info = [f"<ul class='comentario burbuja'>{texto1}{texto2}{texto3}</ul>" , EstructurasControl, regresar]
        return info 
    
    #===============================================================================================================================
    elif message == 'Metodologia':
        texto = "Tema de Metodologia"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , Metodologia, regresar]
        return info 
    elif message == 'significadometo':
        texto = "Diagramas de flujo.- permiten crear algoritmos mediante símbolos gráficos que representan operaciones específicas y que indican la secuencia de las operaciones mediante flechas. Están regidos por normas ISO."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , Metodologia, regresar]
        return info 
    elif message == 'tiposmeto':
        texto1 = "<p>Los algoritmos se pueden clasificar de una manera general en dos tipos básicos:</p>"
        texto2 = "<li>Cuantitativos: Son los algoritmos en los que se utilizan ya cálculos cálculos numéricos durante la definición del propio algoritmo</li>"
        texto3 = "<li>Cualitativos: Son los algoritmos que describen los pasos utilizando palabras.</li>"
        info = [f"<ul class='comentario burbuja'>{texto1}{texto2}{texto3}</ul>" , Metodologia, regresar]
        return info 
    #===============================================================================================================================
    elif message == 'Codificacion':
        texto = "Tema de Codificacion"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , Codificacion, regresar]
        return info 
    elif message == 'significadocodi':
        texto = "Una vez que los algoritmos de una aplicación han sido diseñados, ya se puede iniciar la fase de codificación. En esta etapa se tienen que traducir dichos algoritmos a un lenguaje de programación específico; es decir, las acciones definidas en los algoritmos hay que convertirlas a instrucciones."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , Codificacion, regresar]
        return info 
    elif message == 'etapas':
        texto1 = "<p>Prueba y depuración</p>"
        texto2 = "<li>Los errores humanos dentro de la programación de computadoras son muchos y aumentan considerablemente con la complejidad del problema. El proceso de identificar y eliminar errores, para dar paso a una solución sin errores se le llama Depuración.</li>"
        texto3 = "<li>La Depuración o prueba resulta una tarea tan creativa como el mismo desarrollo de la solución, por ello se debe considerar con el mismo interés y entusiasmo.</li>"
        texto4 = "<p>Codificación</p>"
        texto5 = "<li>La codificación es la operación de escribir la solución del problema (de acuerdo a la lógica del diagrama de flujo o pseudocódigo), en una serie de instrucciones detalladas en un código reconocible por la computadora, la serie de instrucciones detalladas se le conoce como programa fuente, el cual se escribe en un lenguaje de programación o lenguaje alto nivel.</li>"
        texto6 = "<p>Documentación</p>"
        texto7 = "<li>Es la guía o comunicación escrita en sus variadas formas, ya sean en enunciados, procedimientos, dibujos o diagramas. A menudo un programa escrito por una persona, es usado por muchas otras. Por ello la documentación sirve para ayudar a comprender o usar un programa o para facilitar futuras modificaciones (mantenimiento).</li>"
        info = [f"<ul class='comentario burbuja'>{texto1}{texto2}{texto3}{texto4}{texto5}{texto6}{texto7}</ul>" , Codificacion, regresar]
        return info  
    #===============================================================================================================================
    elif message == 'Algoritmos':
        texto = "Tema de algoritmos"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , algoritmos, regresar]
        return info
    elif message == 'significado':
        texto = "Se puede entender un algoritmo como una secuencia de pasos finitos bien definidos que resuelven un problema."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , algoritmos, regresar]
        return info
    elif message == 'funcion':
        texto = "El proceso de funcionamiento de un algoritmo informático es similar a un diagrama de flujo y, en términos generales, consta de tres etapas:"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , algoritmos, regresar]
        return info
    elif message == 'uso':
        texto = "Su idea básica era simple: un algoritmo establece una serie de pasos (una fórmula) para realizar un resultado particular. Es esencialmente una receta que define una secuencia de acciones cuidadosamente descritas."
        info = [f"<p class='comentario burbuja'>{texto}</p>" , algoritmos, regresar]
        return info
    elif message == 'fundamentos':
        youtube_id = '<iframe width="560" height="315" src="https://www.youtube.com/embed/MNVpJpX8OiE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
        info = [youtube_id, '<br>' ,algoritmos, regresar]
        return info
    #===============================================================================================================================
        # return 'Hasta luego!'
    elif message == 'salir':
        texto = "Hasta luego"
        info = [f"<p class='comentario burbuja'>{texto}</p>"]
        return info 
    elif message == 'Tipos':
        texto = "texto de tipos"
        info = [f"<p class='comentario burbuja'>{texto}</p>" , butop1, butop2, butop3, butop4, regresar]
        return info 
    elif message == 'regresar':
        return buttons
    elif message == 'video':
        info = '<iframe width="560" height="315" src="https://www.youtube.com/embed/p1L6GEdBSrw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
        return info
    else:
        return 'Lo siento, no entendí tu mensaje.'
   

if __name__ == '__main__':
    app.run()
