
# https://www.youtube.com/watch?v=4haMUvUxUJI&list=PLlWXhlUMyooab9Tji3bNX8iyVDkllA3mP&index=2

# https://www.youtube.com/watch?v=4haMUvUxUJI&list=PLlWXhlUMyooab9Tji3bNX8iyVDkllA3mP&index=2

import socket
# import struct


def start_socket():
    # создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # от зависания открытых сокетов вторичное использование
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # связывания сокета
    server_socket.bind(('localhost', 5000))
    # прослушивание ходящих соединений
    server_socket.listen()
    return server_socket


def run():

    server_socket = start_socket()
    while True:
        # установка соединения сокета при входящем подключении
        client_socket, address = server_socket.accept()
        # приём данных от сокета
        request = client_socket.recv(1024)

        print(request)  # вывод полученных данных bytes
        print('-'*40)
        print(request.decode('utf-8'))  # вывод полученных данных соеинения декодирования
        print()  # пустая строка
        print(address)  # вывод адресс соеденения

        # отправка данных
        client_socket.sendall('HTTP/1.1 200 OK\n\n<!DOCTYPE html><html><head><title>esp8266</title><meta charset="utf-8"></head><body><h2>hello world</h2></body></html>'.encode('utf-8'))
        # закрытие сркета
        client_socket.close()


html = '<!DOCTYPE html><html><head><title>esp8266</title><meta charset="utf-8"></head><body><h2>{}</h2></body></html>'

html_index = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>esp8266</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h2>Index page</h2>
    </body>
    </html>"""

html_blog = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>esp8266</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h2>Blog page</h2>
    </body>
    </html>"""


def index():
    return html_index


def blog():
    return html_blog


def run_2():
    server_socket = start_socket()
    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)
        # ответ
        if len(request) > 3:
            response = generate_response(request.decode('utf-8'))
            client_socket.sendall(response)
        # закрытие сркета
        client_socket.close()


# формируем ответ
def generate_response(request):
    method, url = parse_request(request)
    headers, code_response = generate_headers(method, url)
    # заголовок + тело
    body = generate_content(code_response, url)  # html.format('hello')
    return (headers + body).encode('utf-8')


def generate_content(code_response, url):
    if code_response == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code_response == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()


# парсим запрос
def parse_request(request):
    print('parse_request _____ len:', len(request), request)
    parsed = request.split(' ')
    print('parsed', parsed)
    method = parsed[0]
    url = parsed[1]
    print('parse_request:', method, url)
    return method, url


def generate_headers(method, url):
    headers, code_response = '', 200
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if url not in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    headers = 'HTTP/1.1 200 OK\n\n'
    code_response = 200

    return (headers, code_response)


URLS = {
    '/': index,
    '/blog': blog
}

# Tabbed Postman - REST Client  - расширение для хрома

if __name__ == '__main__':
    # run()
    run_2()


