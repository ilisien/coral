import flet as ft

class Status:
    ACTIVE = "active"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Task:
    def __init__(self,id,label,description=None,status=None,children=None):
        self.id = id
        self.label = label
        self.description = description

        if status is None:
            self.status = Status.ACTIVE
        else:
            self.status = status

        if children is None:
            self.children = []

class TaskListItem(ft.UserControl):
    def __init__(self,task_instance,task_status_changed,navigate_forward):
        super().__init__()
        self.task_instance = task_instance
        self.navigate_forward = navigate_forward
        self.task_status_changed = task_status_changed


    def build(self):
        self.checkbox = ft.Checkbox(value=False,on_change=self.checkboxed)
        self.label = ft.Markdown(value=self.task_instance.label)
        description_text = f"{self.task_instance.description[10:]}..."
        self.description = ft.Markdown(value=description_text)
        self.edit_button = ft.IconButton(
            icon=ft.icons.CREATE_OUTLINED,
            tooltip="edit",
            on_click=self.edit_clicked,
        )
        self.archive_button = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED,
            tooltip="archive",
            on_click=self.archive_clicked,
        )
        self.navigate_forward_button = ft.IconButton(
            icon=ft.icons.DOUBLE_ARROW,
            icon_color=ft.colors.BLUE,
            tooltip="navigate forward",
            on_click=self.navigate_forward_clicked,
        )

        self.edit_label = ft.TextField(expand=1)
        self.save_button = ft.IconButton(
            icon=ft.icons.DONE,
            icon_color=ft.colors.GREEN,
            tooltip="save",
            on_click=self.save_clicked,
        )

        self.task_list_item = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(spacing=5,controls=[self.checkbox,self.label,self.description]),
                ft.Row(spacing=0,controls=[self.edit_button,self.archive_button,self.navigate_forward_button]),
            ],
        )

        self.edit_task_label = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[self.edit_label,self.save_button],
        )

        return ft.Column(controls=[self.task_list_item,self.edit_task_label])
    
    def edit_clicked(self,e):
        self.edit_label.value = self.task_instance.label
        self.task_list_item.visible = False
        self.edit_task_label.visible = True
        self.update()

    def archive_clicked(self,e):
        self.task_instance.status = Status.ARCHIVED
        self.task_status_changed(self)
    
    def navigate_forward_clicked(self,e):
        self.navigate_forward(self)

    def save_clicked(self,e):
        self.task_instance.label = self.edit_label.value
        self.label.value = self.task_instance.label
        self.task_list_item.visible = True
        self.edit_task_label.visible = False
        self.update()
    
    def checkboxed(self, e):
        if self.checkbox.value:
            self.task_instance.status = Status.COMPLETED
        else:
            self.task_instance.status = Status.COMPLETED
        
        self.task_status_changed(self)

class TaskList(ft.UserControl):
    def __init__(self,task_instance):
        self.task_instance = task_instance
        self.children = self.task_instance.children
    
    def build(self):
        pass #wip

