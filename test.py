from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "El uso excesivo de dispositivos electrónicos puede llevar a la dependencia y afectar la calidad del sueño",
    "El uso constante de redes sociales puede generar ansiedad y afectar la autoestima",
    "El uso excesivo de videojuegos puede afectar el rendimiento académico y social de los jóvenes",
    "El uso excesivo de dispositivos electrónicos puede afectar la capacidad de concentración y memoria",
    "El uso excesivo de dispositivos electrónicos puede afectar la salud física, como problemas de visión y dolor de cuello y espalda",
]

@app.route('/')
def index():
    return f"""
        <h1>Hechos sobre la adicción tecnológica</h1> 
        <br><a href='/facts'>Ver datos curiosos</a>
        <br><a href='/random_fact'>Ver un facto aleatorio ✨</a>
        <br><a href='/consejos'>Ver consejos útiles</a>
        <br><a href='/cara-o-cruz'>Jugar al Cara o Cruz 🪙</a>
    """

@app.route('/facts')
def facts():
    return f"<p>{random.choice(facts_list)}</p> <br><a href='/'>Volver al inicio</a>"

@app.route('/consejos')
def consejos():
    return f"<h1>Consejos para desconectar</h1><p>Intenta hacer actividades al aire libre o leer un libro físico antes de dormir.</p> <br><a href='/'>Volver al inicio</a>"

# --- NUEVA RUTA DE CARA O CRUZ ---
@app.route('/cara-o-cruz')
def cara_o_cruz():
    resultado = random.choice(["¡Cara! 🪙", "¡Cruz! 🪙"])
    return f"""
        <h1>Lanzamiento de moneda</h1>
        <h2>{resultado}</h2>
        <br><a href='/cara-o-cruz'>¡Lanzar otra vez!</a>
        <br><a href='/'>Volver al inicio</a>
    """

# --- RUTA DE FACTO ALEATORIO ---
@app.route("/random_fact")
def random_fact():
    facto = random.choice(facts_list)
    return f"""
        <h1>Facto aleatorio</h1>
        <p>{facto}</p>
        <br><a href='/random_fact'>Otro facto aleatorio 🔄</a>
        <br><a href='/'>Volver al inicio</a>
    """

app.run(debug=True)
