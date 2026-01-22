# Zona-Fit-Python-MySQL

# Zona Fit - Sistema de Gestión de Gimnasio

Aplicación de consola para la gestión de clientes de un gimnasio, desarrollada en **Python** con persistencia en **MySQL**.

## 🏗️ Arquitectura del Proyecto
Este proyecto implementa el patrón de diseño **DAO (Data Access Object)** para separar la lógica de negocio del acceso a datos, garantizando un código limpio y escalable.

### Características Técnicas:
* **Pool de Conexiones:** Uso de `mysql.connector.pooling` para optimizar el manejo de conexiones a la base de datos.
* **Operaciones CRUD:** Implementación completa de Crear, Leer, Actualizar y Eliminar registros.
* **Manejo de Excepciones:** Control de errores robusto durante la interacción con la DB.
* **Modularización:** División clara entre el modelo (`Cliente`), el acceso a datos (`ClienteDAO`) y la interfaz de usuario.

## 🛠️ Requisitos
* Python 3.x
* MySQL Server
* Librería `mysql-connector-python`
