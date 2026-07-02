from core.task_service import TaskService
from utils.helpers import format_task, print_header, print_empty


class Menu:
    def __init__(self):
        self.service = TaskService()

    # -----------------------
    # MENÚ PRINCIPAL
    # -----------------------
    def show_menu(self):
        print("\n===== TASK MANAGER =====")
        print("1. Crear tarea")
        print("2. Ver tareas")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

    def run(self):
        while True:
            self.show_menu()
            option = input("\nSelecciona una opción: ").strip()

            if option == "1":
                self.create_task()

            elif option == "2":
                self.list_tasks()

            elif option == "3":
                self.edit_task()

            elif option == "4":
                self.delete_task()

            elif option == "5":
                print("Saliendo...")
                break

            else:
                print("❌ Opción inválida")

    # -----------------------
    # CREAR TAREA
    # -----------------------
    def create_task(self):
        print_header("Crear tarea")

        title = input("Título: ").strip()
        description = input("Descripción: ").strip()
        priority = input("Prioridad (baja/media/alta): ").strip()
        due_date = input("Fecha límite (YYYY-MM-DD): ").strip()

        task = self.service.create_task({
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date
        })

        print("\n✔ Tarea creada correctamente:")
        print(format_task(task))

    # -----------------------
    # LISTAR TAREAS
    # -----------------------
    def list_tasks(self):
        tasks = self.service.get_all_tasks()

        print_header("Lista de tareas")

        if not tasks:
            print_empty()
            return

        for task in tasks:
            print(format_task(task))

    # -----------------------
    # EDITAR TAREA
    # -----------------------
    def edit_task(self):
        print_header("Editar tarea")

        try:
            task_id = int(input("ID de la tarea: "))

            new_title = input("Nuevo título (ENTER para omitir): ").strip()
            new_status = input("Nuevo estado (pendiente/en progreso/completada): ").strip()

            updates = {}

            if new_title:
                updates["title"] = new_title

            if new_status:
                updates["status"] = new_status

            if not updates:
                print("⚠️ No se realizaron cambios")
                return

            updated = self.service.update_task(task_id, updates)

            if updated:
                print("\n✔ Tarea actualizada:")
                print(format_task(updated))
            else:
                print("❌ Tarea no encontrada")

        except ValueError:
            print("❌ ID inválido")

    # -----------------------
    # ELIMINAR TAREA
    # -----------------------
    def delete_task(self):
        print_header("Eliminar tarea")

        try:
            task_id = int(input("ID de la tarea: "))

            confirm = input("¿Seguro? (s/n): ").lower()

            if confirm != "s":
                print("Cancelado")
                return

            result = self.service.delete_task(task_id)

            if result:
                print("✔ Tarea eliminada")
            else:
                print("❌ Tarea no encontrada")

        except ValueError:
            print("❌ ID inválido")