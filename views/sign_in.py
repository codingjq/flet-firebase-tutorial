
import flet as ft


def SignInView(page, ft=ft, Pyre=None):
    page.title = "Flet + Pyrebase"

    myFirebase = Pyre(page)


    def handle_sign_in(e):
        myFirebase.sign_in(email.value, password.value)
        if myFirebase.check_token() == True:
            page.route = "/dashboard"
        page.update()
        

    email = ft.TextField(label="Email", width=250)
    password = ft.TextField(label="Password", width=250)

    sign_in_button = ft.TextButton("Sign In", on_click=handle_sign_in)
    
    
    myPage = ft.Column(
        [
            ft.Row([email]),
            ft.Row([password]),
            ft.Row([sign_in_button])
        ],
            )
    
    return myPage