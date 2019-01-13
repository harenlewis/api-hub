GET = 100
POST = 200
PUT = 300
DELETE = 400

METHOD_TYPES = (
    (GET, 'GET'),
    (POST, 'POST'),
    (PUT, 'PUT'),
    (DELETE, 'DELETE'),
)

METHOD_TYPES_DICT = {
    'GET': GET,
    'POST': POST,
    'PUT': PUT,
    'DELETE': DELETE,
}

JSON = 500
HTML = 600
TEXT = 700

RESP_TYPES = (
    (JSON, 'JSON'),
    (HTML, 'HTML'),
    (TEXT, 'TEXT'),
)

RESP_TYPES_DICT = {
    'JSON': 'application/json; charset=utf-8',
    'HTML': 'text/html; charset=utf-8',
    'TEXT': 'text/plain; charset=utf-8',
}