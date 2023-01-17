import flet as ft


from user_controls.note import Note
from collections import OrderedDict

def DashboardView(page, ft, myPyrebase):
    title = "My Dashboard"

    username = ft.Text("Welcome", size=16)

    def handle_stream(message):
        try:
            build_notes()
            page.update()
        except:
            pass

    def on_page_load():
        clean_notes()
        username.value = "Welcome"
        if myPyrebase.check_token() == "Success":
            myPyrebase.stream_data(handle_stream)
            handle = myPyrebase.get_username()
            if handle:
                username.value = "Welcome, " + "@" + handle
            page.update()
     

    def handle_add(e):
        myPyrebase.add_note({"note": note_field.value})
        note_field.value = ""
        page.update()
        
    def handle_logout(*e):
        clean_notes()
        username.value = ""
        myPyrebase.kill_all_streams()
        myPyrebase.sign_out()
        page.go("/")

    
    note_field = ft.TextField(label="Enter note here", width=250)
    all_notes = []

    def build_notes():
        all_notes.clear()
        data = myPyrebase.get_notes()
        keys = data['notes'].keys()
        for key in keys:
            note_text = data['notes'][key]['note']
            note = Note(page, note_text, key, myPyrebase)
            all_notes.append(note)

    def clean_notes():
        all_notes.clear()
        all_notes.append(ft.Text(" "))
        page.update()


    add_note_button = ft.TextButton("Add Note", on_click=handle_add)
    logout_button = ft.TextButton("Logout", on_click=handle_logout, style=ft.ButtonStyle(ft.colors.RED))


    myPage = ft.Column([
            ft.Row([ft.Text("Dashboard", size=20)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([username], alignment=ft.MainAxisAlignment.CENTER),
            ft.Column(all_notes, alignment="center"),
            ft.Row([note_field], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([add_note_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([logout_button], alignment=ft.MainAxisAlignment.CENTER)
            ])
            
    return {
        "view":myPage,
        "title": title,
        "load": on_page_load
        }