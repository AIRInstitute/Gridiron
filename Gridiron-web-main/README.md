# Despliegue de la página

instalar todo con npm install 

Dentro de vue-template-main, ejecutar con npm run serve

Ejecutar flask_app.py para manda órdenes a la pipeta. Dependencias en requirements.txt. IMPORTANTE la versión de paramiko.


## Funcionamiento de la pagina

El login no está hecho, así que darle a Sign in, y luego al boton sign in

En el dashboard principal, muestra las opciones de la página. Data visualization no es nada.

En la parte del liquid handler, se selecciona cada protocolo. Está puesto para ejecutar los protocolos en el robot, por lo que no pulsar el boton de START PROTOCOL sin supervisión.

En la colección de postman adjunta, se pueden probar los endpoints de test, suscripciones, entidades, etc


## Protocolos y pipeta

Para simular un protocolo:

instalar la biblioteca de opentrons con pip install opentrons

- Ejecutar "opentrons_simulate protocol_1" para ejecutar la simulacion del protocolo puesto. En windows es "opentrons_simulate.exe protocol_1"
- Ejecutar "opentrons_execute protocol_1" para ejecutar el protocolo. Esto se debe hacer en la terminal del robot.

Para conectarse al robot:

"ssh -i  ot2_ssh_key root@192.168.2.110"

ot2_ssh_key está en la carpeta de flask_app/keys/


El robot deberá tener copiados los protocolos en /data 

Tras ejecutar un protocolo, cargar el archivo con los resultados como json_data.json y se leen y envían a orion
