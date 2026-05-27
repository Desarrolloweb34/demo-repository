from flask import Flask

app = Flask(__name__)

@app.route('/')
def mapa_mental():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mapa Mental - Vroom</title>

        <style>

            body{
                margin:0;
                padding:0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#0f172a,#1e293b);
                overflow:hidden;
                color:white;
            }

            .mapa{
                position:relative;
                width:100vw;
                height:100vh;
            }

            /* CENTRO */
            .centro{
                position:absolute;
                top:50%;
                left:50%;
                transform:translate(-50%, -50%);
                background:#f59e0b;
                color:black;
                padding:25px;
                border-radius:50%;
                width:220px;
                height:220px;
                display:flex;
                align-items:center;
                justify-content:center;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                box-shadow:0px 0px 25px rgba(255,255,255,0.5);
            }

            /* CAJAS */
            .rama{
                position:absolute;
                width:260px;
                padding:20px;
                border-radius:20px;
                background:white;
                color:black;
                box-shadow:0px 5px 20px rgba(0,0,0,0.5);
                transition:0.3s;
            }

            .rama:hover{
                transform:scale(1.05);
            }

            /* POSICIONES */
            .expectativa{
                top:8%;
                left:10%;
                border-left:12px solid #3b82f6;
            }

            .instrumentalidad{
                top:8%;
                right:10%;
                border-left:12px solid #22c55e;
            }

            .valencia{
                bottom:10%;
                left:50%;
                transform:translateX(-50%);
                border-left:12px solid #eab308;
            }

            h2{
                margin-top:0;
            }

            img{
                width:100%;
                border-radius:10px;
            }

            button{
                margin-top:10px;
                padding:10px;
                border:none;
                border-radius:10px;
                background:#0f172a;
                color:white;
                cursor:pointer;
            }

            button:hover{
                background:#1e40af;
            }

            .nota{
                display:none;
                margin-top:10px;
                background:#e2e8f0;
                padding:10px;
                border-radius:10px;
            }

            iframe{
                width:100%;
                height:180px;
                margin-top:10px;
                border-radius:10px;
            }

            a{
                color:#2563eb;
                font-weight:bold;
            }

            /* LINEAS */
            .linea1, .linea2, .linea3{
                position:absolute;
                background:white;
                height:4px;
                transform-origin:left;
            }

            .linea1{
                width:280px;
                top:34%;
                left:28%;
                transform:rotate(20deg);
            }

            .linea2{
                width:280px;
                top:34%;
                right:28%;
                transform:rotate(-20deg);
            }

            .linea3{
                width:250px;
                bottom:32%;
                left:45%;
                transform:rotate(90deg);
            }

        </style>

        <script>
            function mostrarNota(id){
                let nota = document.getElementById(id);

                if(nota.style.display === "block"){
                    nota.style.display = "none";
                }else{
                    nota.style.display = "block";
                }
            }
        </script>

    </head>

    <body>

        <div class="mapa">

            <!-- LINEAS -->
            <div class="linea1"></div>
            <div class="linea2"></div>
            <div class="linea3"></div>

            <!-- CENTRO -->
            <div class="centro">
                🧠<br>
                Teoría de<br>
                Expectativas<br>
                de Vroom
            </div>

            <!-- EXPECTATIVA -->
            <div class="rama expectativa">

                <h2>🎯 Expectativa</h2>

                <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?q=80&w=1000">

                <p>
                    El esfuerzo produce un buen desempeño.
                </p>

                <ul>
                    <li>Capacitación</li>
                    <li>Confianza</li>
                    <li>Habilidades</li>
                </ul>

                <button onclick="mostrarNota('nota1')">
                    Ver Nota
                </button>

                <div class="nota" id="nota1">
                    El trabajador cree que puede lograr la meta.
                </div>

                <br><br>

                <a href="https://es.wikipedia.org/wiki/Teor%C3%ADa_de_la_expectativa" target="_blank">
                    Más información
                </a>

            </div>

            <!-- INSTRUMENTALIDAD -->
            <div class="rama instrumentalidad">

                <h2>💼 Instrumentalidad</h2>

                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=1000">

                <p>
                    El desempeño genera recompensas.
                </p>

                <ul>
                    <li>Bonos</li>
                    <li>Ascensos</li>
                    <li>Reconocimiento</li>
                </ul>

                <button onclick="mostrarNota('nota2')">
                    Ver Nota
                </button>

                <div class="nota" id="nota2">
                    Si trabaja bien, recibirá una recompensa.
                </div>

                <iframe
                    src="https://www.youtube.com/embed/WC5fL6s3J5E"
                    allowfullscreen>
                </iframe>

            </div>

            <!-- VALENCIA -->
            <div class="rama valencia">

                <h2>⭐ Valencia</h2>

                <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=1000">

                <p>
                    Valor que tiene la recompensa.
                </p>

                <ul>
                    <li>Dinero</li>
                    <li>Vacaciones</li>
                    <li>Tiempo libre</li>
                </ul>

                <button onclick="mostrarNota('nota3')">
                    Ver Nota
                </button>

                <div class="nota" id="nota3">
                    Cada persona valora recompensas diferentes.
                </div>

                <br>

                <a href="https://www.canva.com/es_mx/mapas-mentales/" target="_blank">
                    Crear más mapas mentales
                </a>

            </div>

        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)