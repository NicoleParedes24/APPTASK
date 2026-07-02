import json
import os


class JsonStorage:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path

        # Asegurar que el archivo exista
        if not os.path.exists(self.file_path):
            self._write_file([])

    # ---------------------------
    # Leer datos
    # ---------------------------
    def load_tasks(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Si el JSON está corrupto
            return []
        except FileNotFoundError:
            return []

    # ---------------------------
    # Guardar datos
    # ---------------------------
    def save_tasks(self, tasks):
        try:
            self._write_file(tasks)
        except Exception as e:
            raise Exception(f"Error guardando tareas: {str(e)}")

    # ---------------------------
    # Escritura interna
    # ---------------------------
    def _write_file(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)