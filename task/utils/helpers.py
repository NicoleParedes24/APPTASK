from datetime import datetime


# -----------------------
# FORMATEAR UNA TAREA
# -----------------------
def format_task(task):
    return f"""
--------------------------------
ID: {task.get('id')}
Título: {task.get('title')}
Descripción: {task.get('description', '')}
Prioridad: {task.get('priority')}
Estado: {task.get('status')}
Fecha límite: {task.get('due_date', 'N/A')}
Creada: {task.get('created_at', 'N/A')}
--------------------------------
"""


# -----------------------
# HEADER BONITO
# -----------------------
def print_header(title):
    print("\n" + "=" * 40)
    print(title.upper())
    print("=" * 40)


# -----------------------
# MENSAJE VACÍO
# -----------------------
def print_empty(message="No hay tareas registradas"):
    print(f"\n⚠️ {message}")


# -----------------------
# VALIDAR FECHA SIMPLE
# -----------------------
def is_valid_date(date_str):
    if not date_str:
        return True

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# -----------------------
# LIMPIAR INPUT
# -----------------------
def clean_input(text):
    return text.strip() if text else ""