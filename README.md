# Todolisto Django

## Funcionalidades

- Distinción por usuario administrador o usuario regular (debe asignarse mediante dashboard administrativo de Django)

  - El tipo Tarea cuenta con:

    - Titulo
  
    - Descripción
  
    - Fecha de inicio
  
    - Fecha de término
  
    - Tipo
  
    - Estado

- Usuario regular

  - CRUD Tarea

  - Visualizar calendario con Tareas activas.

  - La pantalla principal muestra las Tareas activas a menos que presione (al final de la lista) el enlace para mostrar todas.

- Usuario Administrador

  - La pantalla principal muestra las Tareas activas (de todos los usuarios) a menos que presione (al final de la lista) el enlace para mostrar todas.

  - No puede ver ni modificar Tareas de usuarios, pero si eliminarlas desde la lista anterior.

  - No puede crear Tareas propias.

  - Puede visualizar calendario con Tareas activas de todos los usuarios.

- Dashboard administrativo del sistema

  - CRUD para tipos de tareas.

  - CRUD para estados de tareas.

  - CRUD para usuarios.

### Cristian Duartes Lizama