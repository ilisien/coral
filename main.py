import flet as ft
from task_list import Task,TaskListItem

def task_status_changed(task):
    print(f"task status changed on task:{task.task_instance.label}")

def navigate_forward(task):
    print(f"navigate forward on task:{task.task_instance.label}")

class CoralApp(ft.UserControl):
    def build(self):
        task = Task("_hello!_","this is a description!!!!!")
        task_item = TaskListItem(task,task_status_changed,navigate_forward)

        return task_item

def main(page: ft.Page):
    page.title = "coral app"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    app = CoralApp()

    page.add(app)

ft.app(target=main)