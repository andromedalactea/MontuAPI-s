from main import app
from serverless_wsgi import handle_request

def google_cloud_handler(request):
    return handle_request(app, request)
