import os
from app import create_app

# Obtiene el entorno, por defecto 'production'
env = os.getenv('FLASK_ENV', 'production')

print(f"Ejecutando en entorno: {env}")
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("SECRET_KEY definida:", os.getenv("SECRET_KEY") is not None)

app = create_app(env)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
