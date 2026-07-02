from storage.json_storage import JsonStorage


class TaskService:
    def __init__(self):
        self.storage = JsonStorage()
        self.tasks = self.storage.load_tasks()

    # -----------------------
    # Obtener todas las tareas
    # -----------------------
    def get_all_tasks(self):
        return self.tasks

    # -----------------------
    # Crear tarea
    # -----------------------
    def create_task(self, task_data):
        new_id = self._generate_id()

        task = {
            "id": new_id,
            "title": task_data.get("title"),
            "description": task_data.get("description", ""),
            "priority": task_data.get("priority", "media"),
            "status": "pendiente",
            "due_date": task_data.get("due_date"),
            "notes": task_data.get("notes", ""),
            "created_at": task_data.get("created_at")
        }

        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task

    # -----------------------
    # Buscar tarea por ID
    # -----------------------
    def get_task_by_id(self, task_id):
        return next((t for t in self.tasks if t["id"] == task_id), None)

    # -----------------------
    # Editar tarea
    # -----------------------
    def update_task(self, task_id, updates):
        task = self.get_task_by_id(task_id)

        if not task:
            return None

        task.update(updates)
        self.storage.save_tasks(self.tasks)
        return task

    # -----------------------
    # Eliminar tarea
    # -----------------------
    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)

        if not task:
            return False

        self.tasks.remove(task)
        self.storage.save_tasks(self.tasks)
        return True

    # -----------------------
    # Cambiar estado
    # -----------------------
    def change_status(self, task_id, new_status):
        task = self.get_task_by_id(task_id)

        if not task:
            return None

        task["status"] = new_status
        self.storage.save_tasks(self.tasks)
        return task

    # -----------------------
    # Generar ID simple
    # -----------------------
    def _generate_id(self):
        if not self.tasks:
            return 1
        return max(t["id"] for t in self.tasks) + 1