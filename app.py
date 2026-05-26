from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Proyecto Web Integral</h1>
    <h2>Login funcionando correctamente</h2>
    <a href='/login'>Ir al Login</a>
    """

@app.route('/login')
def login():
    return """
    <h1>Pantalla Login</h1>

    <form>
        <input type='text' placeholder='Usuario'><br><br>
        <input type='password' placeholder='Contraseña'><br><br>
        <button>Ingresar</button>
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)