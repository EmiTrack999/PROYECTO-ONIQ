from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Añadir el directorio python_backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python_backend'))

# Importar la aplicación
from python_backend.app import app

# Configurar CORS para Vercel
CORS(app, resources={r"/*": {"origins": "*"}})

# Esta es la función handler que Vercel ejecutará
def handler(event, context):
    return app(event, context)
