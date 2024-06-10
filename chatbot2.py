from flask import Flask, request

import nltk
from nltk.chat.util import Chat, reflections

# Descarga los recursos necesarios de NLTK (solo la primera vez)
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("nps_chat")

# Define los tipos de investigación y sus enfoques metodológicos
tipos_investigacion = {
    "Descriptiva": "Se enfoca en describir características o fenómenos, sin manipular variables.",
    "Exploratoria": "Se utiliza para investigar un tema poco conocido, para generar hipótesis o ideas.",
    "Explicativa": "Busca determinar relaciones causales entre variables, mediante experimentos o análisis estadístico.",
    "Correlacional": "Analiza la relación entre dos o más variables sin establecer una relación de causalidad.",
    "Experimental": "Se manipulan una o más variables independientes para observar su efecto en una variable dependiente.",
    "Cuantitativa": "Recoge datos numéricos para análisis estadístico.",
    "Cualitativa": "Se enfoca en comprender fenómenos sociales o humanos desde una perspectiva más subjetiva.",
    "Mixta": "Combina elementos de investigación cuantitativa y cualitativa.",
    "Documental": "Se basa en el análisis de documentos, como libros, artículos, registros, etc.",
    "Bibliográfica": "Realiza un estudio exhaustivo de la literatura existente sobre un tema específico.",
    "Experimental": "Se realizan experimentos controlados para probar hipótesis.",
    "Observacional": "Se observan y registran fenómenos naturales sin intervenir en ellos.",
    "Participativa": "Los participantes son parte activa en la investigación, colaborando en la toma de decisiones y análisis."
}

# Define pares de patrones y respuestas para el chatbot
pairs = [
    [
        r"tipos de investigacion",
        [f"{tipo}: {descripcion}" for tipo, descripcion in tipos_investigacion.items()]
    ],
    [
        r"enfoques metodologicos",
        ["Los enfoques metodológicos comunes incluyen: cuantitativo, cualitativo y mixto."]
    ],
    [
        r"(.*?) tu nombre?",
        ["Mi nombre es ChatBot. ¿Cómo puedo ayudarte?",]
    ],
    [
        r"adiós",
        ["Adiós, ¡que tengas un buen día!",]
    ],
    [
        r"(.*?)",
        ["Lo siento, no te entiendo bien. ¿Podrías reformular tu pregunta?",]
    ]
]

# Crea un ChatBot utilizando los pares de patrones y respuestas
chatbot = Chat(pairs, reflections)

# Crea una aplicación Flask
app = Flask(__name__)

# Define la ruta para manejar las solicitudes de chat
@app.route("/chat", methods=["POST"])
def chat():
    # Obtén el mensaje del usuario desde la solicitud
    user_message = request.form["message"]
    # Genera la respuesta del chatbot utilizando el mensaje del usuario
    bot_response = chatbot.respond(user_message)
    # Devuelve la respuesta del chatbot como una respuesta HTTP
    return "\n".join(bot_response)

# Ejecuta la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
