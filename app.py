from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    datos = {
        "Nombre": ["Ana", "Juan", "Maria"],
        "Edad": [20, 22, 21],
        "Ciudad": ["CDMX", "GDL", "MTY"]
    }

    df = pd.DataFrame(datos)

    tabla = df.to_html(classes='table table-dark')

    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>

        <title>OpenRefine Inteligente</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

        <style>

            body {{
                background: linear-gradient(135deg,#0f172a,#1e293b);
                color: white;
                padding: 40px;
                font-family: Arial;
            }}

            h1 {{
                text-align:center;
                margin-bottom:30px;
            }}

            .card {{
                padding:30px;
                border-radius:20px;
                background:#111827;
                box-shadow:0px 0px 25px cyan;
            }}

        </style>

    </head>

    <body>

        <div class="container">

            <div class="card">

                <h1>🚀 Sistema Inteligente de Limpieza de Datos</h1>

                <p>
                Plataforma inspirada en OpenRefine para limpieza,
                validación y auditoría de datasets empresariales.
                </p>

                {tabla}

            </div>

        </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)