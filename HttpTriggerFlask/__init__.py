# import azure.functions as func
# from azure.functions import WsgiMiddleware
# from app import app  # Import the Flask app from app.py

# def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
#     return WsgiMiddleware(app).handle(req, context)

import azure.functions as func
from azure.functions import WsgiMiddleware
from app import app

# Mount Flask app at the correct base path
wsgi_app = WsgiMiddleware(app.wsgi_app)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return wsgi_app.handle(req, context)
