[README.md](https://github.com/user-attachments/files/29614840/README.md)
# 🗂️ Task Manager CLI (Python)

Un gestor de tareas desarrollado en Python utilizando únicamente la línea de comandos.  
Permite a los usuarios crear, organizar, editar y eliminar tareas de forma sencilla, almacenando toda la información en un archivo JSON local.

---

## 🚀 Características

- Crear tareas con título, descripción, prioridad y fecha límite
- Listar todas las tareas registradas
- Editar tareas existentes
- Eliminar tareas con confirmación
- Persistencia de datos usando JSON (sin base de datos)
- Interfaz de consola simple y amigable
- Validaciones básicas y manejo de errores

---

## 🧱 Estructura del proyecto

```
task_manager/
│
├── main.py
├── cli/
│   └── menu.py
├── core/
│   ├── task_service.py
│   └── task_manager.py
├── models/
│   └── task.py
├── storage/
│   └── json_storage.py
├── utils/
│   └── helpers.py
└── data/
    └── tasks.json
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- No requiere librerías externas

---

## ▶️ Cómo ejecutar el proyecto

Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/task-manager-cli.git
cd task-manager-cli
```

Ejecuta la aplicación:

```bash
python3 main.py
```

---

## 📌 Uso del sistema

Al iniciar el programa verás el menú principal:

```
===== TASK MANAGER =====
1. Crear tarea
2. Ver tareas
3. Editar tarea
4. Eliminar tarea
5. Salir
```

---

## 🧠 Estructura de una tarea

```json
{
  "id": 1,
  "title": "Estudiar Python",
  "description": "Repasar conceptos básicos",
  "priority": "alta",
  "status": "pendiente",
  "due_date": "2026-07-10",
  "created_at": "2026-07-02T10:00:00"
}
```

---

## 💾 Persistencia

Las tareas se almacenan en:

```
data/tasks.json
```

No se utiliza base de datos, todo se guarda localmente en formato JSON.

---

## 🛠️ Futuras mejoras

- Filtros por estado y prioridad
- Búsqueda de tareas
- Ordenamiento automático
- Mejora de UI en consola
- Migración a base de datos
- Interfaz gráfica (GUI)

---

## 👨‍💻 Autor

Proyecto desarrollado en Python para práctica de:
- Arquitectura de software
- CLI applications
- Manejo de archivos JSON
- Separación de capas

---

## 📄 Licencia

Uso libre para fines educativos.
