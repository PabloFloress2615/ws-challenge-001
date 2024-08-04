from bottle import Bottle, response
from prometheus_client import start_http_server, Counter

app = Bottle()

# Crear el contador para las requests a /heavywork
REQUEST_COUNT = Counter('heavywork_requests_total', 'Total number of requests to heavywork')

@app.post('/heavywork')
def heavywork():
    REQUEST_COUNT.inc()  # Incrementar el contador en cada request
    response.status = 202
    return {"message": "Heavy work started"}

@app.post('/lightwork')
def lightwork():
    return {"message": "Light work done"}

@app.get('/metrics')
def metrics():
    from prometheus_client import generate_latest
    response.content_type = 'text/plain; version=0.0.4; charset=utf-8'
    return generate_latest()

if __name__ == "__main__":
    start_http_server(9100)  # Iniciar servidor para métricas de Prometheus en el puerto 9100
    app.run(host="0.0.0.0", port=8080)
