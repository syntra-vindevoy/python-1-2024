from datetime import datetime

from src.ToDOList.domain.statut import Status
from src.ToDOList.domain.todo import Todo
from src.ToDOList.simple.Menu import Menu
from src.ToDOList.simple.TodoManger import ToDoManager


def main():
    manager = ToDoManager.get_instance("ToDo Benoit")

    def exit_menu():
        print("Exiting...")
        exit()

    def show_all_tasks():
        print_list(manager.get_to_do_list())

    def print_list(list_todos):
        for t in list_todos:
            print(f"{t.status} {t.title} {t.description} {t.priority} {t.due_date} {t.status}")

    def show_completed_tasks():
        print_list(manager.get_to_do_list_status(Status=Status.DONE))

    def show_pending_tasks():
        print_list(manager.get_to_do_list_status(Status=Status.IDLE))

    def show_doing():
        print_list(manager.get_to_do_list_status(Status=Status.DOING))

        def show_new():
            print_list(manager.get_to_do_list_status(Status=Status.NEW))

    def delete_task():
        manager.delete_task()

    def delete_all_tasks():
        manager.delete_all_task()

    def add_task():
        print("Add task")
        name = input("Enter task name:")
        description = input("Enter task description:")
        priority = int(input("Enter task priority:"))
        due_date = input("Enter task due date %m-%d-%Y:")

        def __validate() -> Todo | None:
            try:
                dt = datetime.strptime(due_date, '%m-%d-%Y')
            except ValueError:
                print("Incorrect data format, should be MM-DD-YY")
                dt = datetime.now()
            if name == "" or description == "" or priority == 0 or due_date == "" or dt is None:
                return None
            return Todo(title=name, priority=priority, description=description, due_date=dt)

        todo = __validate()
        if todo is not None:
            manager.add_to_do(to_do=todo)

    menu_data: dict[str, list[str]] = {
        "1": ["Add task", add_task],
        "2": ["Show all tasks", show_all_tasks],
        "3": ["Show completed tasks", show_completed_tasks],
        "4": ["Show pending tasks", show_pending_tasks],
        "5": ["Show doing tasks", show_doing],
        "6": ["Delete task", delete_task],
        "7": ["Delete all tasks", delete_all_tasks],
        "8": ["Exit", exit_menu],
    }

    menu = Menu(menu_data)
    menu.start()


if __name__ == '__main__':
    main()
