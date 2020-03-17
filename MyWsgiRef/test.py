from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(environ['PATH_INFO'].encode('iso-8859-1').decode('utf8'))
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'].encode('iso-8859-1').decode('utf8')[1:] or 'web')
    return [body.encode('utf-8')]


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    httpd = make_server(host, port, application)
    print('Serving HTTP on port {port}...'.format(port=port))
    httpd.serve_forever()
