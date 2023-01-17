import flet as ft

class Note(ft.UserControl):
    def __init__(self, page, message="Loading...", uuid="None", myPyrebase="None", width=250, height=50, dialog_text=None):
        super().__init__()
        self.page = page
        self.message = ft.TextButton(message)
        self.uuid = uuid
        self.myPyrebase = myPyrebase
        self.width = width
        self.height = height
        self.dialog_text = ft.TextField(value=self.message.text)
        self.dialog = self.dialog_modal()

    def build(self):
        self.message.width = self.width
        self.message.height = self.height
        self.message.on_click = self.handle_press
        return ft.Card(
            content=ft.Container(
                self.message
                    ))

    def handle_press(self, e):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()


    def cancel_dialog(self, e):
        self.page.dialog.open = False
        self.page.update()

    def delete_dialog(self, e):
        self.myPyrebase.delete_note(self.uuid)
        self.visible = False
        self.dialog.open = False
        self.page.update()

    def accept_dialog(self, e):
        try:
            self.myPyrebase.edit_note(self.uuid, {"note": self.dialog_text.value})
            self.message.text = self.dialog_text.value
            self.page.dialog.open = False
            self.message.update()
            self.page.update()
        except:
            print("something went wronng")

    def handle_copy(self, e):
        self.page.set_clipboard(self.dialog_text.value)
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("Note Copied", color=ft.colors.WHITE),
            bgcolor=ft.colors.GREEN
        )
        self.page.snack_bar.open = True
        self.page.update()
        

    def dialog_modal(self):
        return ft.AlertDialog(
            modal=True,
            title=ft.Row([
                ft.Text("Edit Note"), 
                ft.IconButton(icon=ft.icons.COPY, on_click=self.handle_copy)
                ]),
            content=self.dialog_text,
            actions=[
                ft.IconButton(on_click=self.delete_dialog, icon=ft.icons.DELETE, icon_color=ft.colors.RED),
                ft.IconButton(on_click=self.cancel_dialog, icon=ft.icons.UNDO, icon_color=ft.colors.AMBER),
                ft.IconButton(on_click=self.accept_dialog, icon=ft.icons.SAVE_ALT, icon_color=ft.colors.GREEN),
            ], 
            actions_alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )

if __name__ == "__main__":
    def main(page: ft.Page):

        note = Note(page)
        page.add(
            note
        )

    ft.app(target=main)