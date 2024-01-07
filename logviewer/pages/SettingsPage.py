import flet as ft

class SettingsPage(ft.View):
    def __init__(self, _data):
        data = 'View1 data'
        controls = [
            ft.AppBar(title=ft.Text("View1"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text(f'Top\'s data: {_data}'),
            ft.TextField(value=data, on_change=self.changed),
            ft.ElevatedButton("Go to View2", on_click=self.clicked)
        ]
        super().__init__("/SettingsPage", controls=controls)
        self.data = data
        
    def clicked(self, e):
        pass
    def changed(self, e):
        self.data = e.control.value
        self.update()