# suscripcion-al-sistema-de-alertas-de-ZAP
suscripción al sistema de alertas de ZAP

## tener en cuenta:
En este ejemplo, la clase MyEventConsumer se utiliza para escuchar eventos de alerta agregados en ZAP. Cuando se detecta una alerta nueva, se extrae información relevante de la alerta, como su nombre, riesgo y descripción. Luego, se utiliza la API de Jira para crear un ticket en el proyecto especificado en la variable TU_CLAVE_DE_PROYECTO. El nombre de la alerta se utiliza como el resumen del ticket, la descripción de la alerta se utiliza como la descripción del ticket, y el nivel de riesgo de la alerta se utiliza como un campo personalizado en el ticket.

Es importante configurar las variables tu-instancia-de-jira, tu-token-de-API-de-jira y TU_CLAVE_DE_PROYECTO con los valores correctos antes de ejecutar el script. Además, se requeriría tener los permisos necesarios en Jira para crear y actualizar tickets en el proyecto especificado.

Este es solo un ejemplo de cómo se podría integrar ZAP con Jira para enviar alertas de seguridad. La implementación exacta dependería de los requisitos específicos del
