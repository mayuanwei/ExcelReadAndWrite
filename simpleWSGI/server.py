from simpleWSGI.hello import application
from wsgiref.simple_server import make_server

http = make_server('127.0.0.1',8001 ,application)
print('Serving HTTP on port 8000...')
http.serve_forever()