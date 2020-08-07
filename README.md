# UVCare :bug:

Primera versión de la página de UVCare Chile. La finalidad de esta es ser un medio de información y comunicación para clientes, inversionistas, colaboradores, usuarios y público en general.

Puedes encontrar la versión web en: https://uvcarecl.herokuapp.com

## Equipo :robot:

* **Nelson Marabolí:** nimaraboli@uc.cl

* **Karla Ponce:** kaponce@uc.cl

* **Ignacio Serrano:** itserrano@uc.cl

* **Francisco Tobar:** fvtobar@uc.cl

* **Christian Carstens:** ctcarstens@uc.cl 

## For Developers

Si ya tienes incluido el paquete venv en tu versión de python, puedes crear directamente un entorno virtual. 

```
python3 -m venv venv
```

En caso contrario, debes instalar el paquete venv.

```
pip install virtualenv
```

Y luego crear tu entorno virtual. 
```
virtualenv venv
```

Activar el entorno virtual.
```
source venv/bin/activate
```

Para el caso de Windows, el paso anterior se cambia por:
```
venv\Scripts\activate
```

Para instalar dentro del venv todos los paquetes necesarios en el proyecto.
```
pip install -r requirements.txt
```

Finalmente, ya puedes correr localmente la aplicación.
```
python3 uvcare.py
```

E ingresa en tu navegador a: 
```
http://localhost:5000
```

*Para Windows, el comando python3 se reemplaza por python directamente.