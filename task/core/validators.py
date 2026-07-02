from datetime import datetime


class TaskValidator:

    VALID_PRIORITIES = ["baja", "media", "alta"]
    VALID_STATUS = ["pendiente", "en progreso", "completada"]

    # -----------------------
    # Validar tarea completa
    # -----------------------
    def validate_task(self, task_data):
        self.validate_title(task_data.get("title"))
        self.validate_priority(task_data.get("priority"))
        self.validate_date(task_data.get("due_date"))

    # -----------------------
    # Título obligatorio
    # -----------------------
    def validate_title(self, title):
        if not title or title.strip() == "":
            raise ValueError("El título es obligatorio")

    # -----------------------
    # Prioridad válida
    # -----------------------
    def validate_priority(self, priority):
        if priority and priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Prioridad inválida: {priority}")

    # -----------------------
    # Estado válido
    # -----------------------
    def validate_status(self, status):
        if status and status not in self.VALID_STATUS:
            raise ValueError(f"Estado inválido: {status}")

    # -----------------------
    # Validar fecha
    # -----------------------
    def validate_date(self, date_str):
        if date_str is None or date_str == "":
            return

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido (YYYY-MM-DD)")