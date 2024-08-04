# Usa una imagen base de Python
FROM python:3.9-slim

# Permitir que los mensajes y declaraciones de log aparezcan inmediatamente en los logs de Knative
ENV PYTHONUNBUFFERED True

# Copiar el código local al contenedor
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Instalar las dependencias de producción
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8080
EXPOSE 8080
EXPOSE 9100
# Ejecutar el servicio web al iniciar el contenedor
CMD ["python", "app.py"]
