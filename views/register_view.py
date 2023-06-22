import flet as ft

def RegisterView(page, myPyrebase):
    title = "Register to Flet + Pyrebase"

    def handle_sign_up(e):
        try:
            myPyrebase.register_user(name.value, username.value, email.value, password.value)
            name.value, username.value, email.value, password.value = '', '', '', ''
            page.go('/')
        except:
            handle_sign_in_error()

    def handle_sign_in_error():
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Something's wrong. Please Try Again.", color=ft.colors.WHITE),
            bgcolor=ft.colors.RED
        )
        page.snack_bar.open = True
        page.update()

    banner = ft.Image(src='banner.png', width=250, border_radius=5, fit=ft.ImageFit.COVER)
    welcome_text = ft.Text("User Registration", size=26, bottom=10, right=10, color=ft.colors.WHITE70)
    name = ft.TextField(label="Name", width=250)
    username = ft.TextField(label="Username", width=250)
    email = ft.TextField(label="Email", width=250)
    confirm_email = ft.TextField(label="Confirm Email", width=250)
    password = ft.TextField(label="Password", width=250, password=True, can_reveal_password=True)
    confirm_password = ft.TextField(label="Confirm Password", width=250)

    back_button = ft.TextButton("Go Back", icon=ft.icons.UNDO, icon_color=ft.colors.RED, on_click=lambda _:page.go('/'))
    register_button = ft.TextButton("Sign Up", on_click=handle_sign_up)
    
    myPage = ft.Column(
        [
            ft.Stack(
                [
                    banner,
                    welcome_text
                    ]
            ),
            ft.Row(
                [name]
            ),
            ft.Row(
                [username]
            ),
            ft.Row(
                [email]
                ),
       #     ft.Row(
       #         [confirm_email]
       #         ),
            ft.Row(
                [password]
                ),
        #    ft.Row(
         #       [confirm_password]
         #       ),
            ft.Row(
                [back_button, register_button],
            alignment=ft.MainAxisAlignment.CENTER),

        ]
            )
    
    return {
        "view":myPage,
        "title": title
        }
