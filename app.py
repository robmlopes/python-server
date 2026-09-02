import http.server
import socketserver

# DEFINA AQUI A SUA NOVA PORTA
PORTA = 7900

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Servidor Python</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Servidor Python Ativo!</h1>
    <p>Esta pagina esta rodando no arquivo app.py.</p>
</body>
</html>
"""

class MeuHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))

with socketserver.TCPServer(("", PORTA), MeuHandler) as httpd:
    print(f"Servidor rodando em: http://192.168.68.244:{PORTA}")
    print("Para desligar, pressione Ctrl+C")
    httpd.serve_forever()
