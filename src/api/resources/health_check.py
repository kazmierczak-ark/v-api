from flask import Response


def register(app):
    app.add_url_rule('/health', 'health_check', health_check)


def health_check():
    return Response('', status=200, mimetype='application/json')
