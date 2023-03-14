from org.zaproxy.zap import ZAP as zap
from org.zaproxy.zap.eventBus import EventConsumer
import requests

class MyEventConsumer(EventConsumer):

    def eventReceived(self, event):
        if event.getEventType() == "alert.added":
            params = event.getParameters()
            # Extraer información relevante de la alerta
            nombre_alerta = params.get("name", "Desconocido")
            riesgo_alerta = params.get("risk", "Desconocido")
            descripcion_alerta = params.get("description", "No se proporcionó ninguna descripción.")
            # Enviar un ticket de Jira para la alerta
            enviar_ticket_jira(nombre_alerta, riesgo_alerta, descripcion_alerta)

def enviar_ticket_jira(nombre, riesgo, descripcion):
    # Definir la URL de la API de Jira y los encabezados
    url_api_jira = "https://tu-instancia-de-jira.atlassian.net/rest/api/2/issue/"
    encabezados_jira = {
        "Content-Type": "application/json",
        "Authorization": "Basic tu-token-de-API-de-jira"
    }
    # Definir los datos del ticket de Jira
    datos_ticket_jira = {
        "fields": {
            "project": {
                "key": "TU_CLAVE_DE_PROYECTO"
            },
            "summary": nombre,
            "description": descripcion,
            "issuetype": {
                "name": "Bug"
            },
            "customfield_10000": riesgo
        }
    }
    # Enviar el ticket de Jira
    respuesta = requests.post(url_api_jira, headers=encabezados_jira, json=datos_ticket_jira)
    if respuesta.status_code != 201:
        print("Error al crear el ticket de Jira: {}".format(respuesta.text))

def instalar(helper):
    consumidor_eventos = MyEventConsumer()
    if zap.getEventBus().registerConsumer(consumidor_eventos, "org.zaproxy.zap.extension.alert.AlertEventPublisher"):
        print("Se ha llamado a la función Instalar")

def desinstalar(helper):
    consumidor_eventos = MyEventConsumer()
    if zap.getEventBus().unregisterConsumer(MyEventConsumer()):
        print("Se ha llamado a la función Desinstalar")
