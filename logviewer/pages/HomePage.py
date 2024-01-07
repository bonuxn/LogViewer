"""Class representing a person"""

from cgi import print_form
from typing import Dict
import flet as ft

class HomePage(ft.View):
    """ view class of HomePage """
    file_picker = None
    fileNameText = ft.TextField(label="please select file.....")
    page = None # ページ再描画を使用するため、pageのオブジェクトが必要となる

    def __init__(self,page) :
        data = "Top data"
        self.page = page
        self.file_picker = ft.FilePicker(on_result=self.file_picker_result, on_upload=self.on_upload_progress)
        self.page.overlay.append(self.file_picker)
        controls = [
            ft.AppBar(title=ft.Text("Log Viewer"), bgcolor=ft.colors.SURFACE_VARIANT),
            self.fileNameText,
            ft.ElevatedButton(
                "Select files...",
                icon=ft.icons.FOLDER_OPEN,
                on_click=lambda _: self.file_picker.pick_files(allow_multiple=True),
            ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("DateTime")),
                    ft.DataColumn(ft.Text("Log1")),
                    ft.DataColumn(ft.Text("Log2")),
                ],
            )
        ]
        super().__init__("/", controls=controls)
        self.data = data

    def onClickFileUpload(self):
        if self.file_picker is None:
            return None
        else :
            return self.file_picker.pick_files(allow_multiple=True)
    
    def file_picker_result(self,e: ft.FilePickerResultEvent):
        
        if e.files is not None:
            for f in e.files:
                self.fileNameText.label = f.path + "\\" + f.name
                self.page.update()

    def on_upload_progress(self,e: ft.FilePickerUploadEvent):
        pass

    def clicked(self, e):
        e.page.go("/SettingsPage")
    
    def changed(self, e):
        self.data = e.control.value
        self.update()