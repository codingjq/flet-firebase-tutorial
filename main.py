
import flet as ft
from views.FletRouter import Router
from db.flet_pyrebase import PyrebaseWrapper

def main(page: ft.Page):

    page.window_height = 500
    page.window_width = 300


    page.theme_mode = "dark"

    myPyrebase = PyrebaseWrapper(page)

    myRouter = Router(page, ft, myPyrebase)

    page.on_route_change = myRouter.route_change


    page.scroll = "auto"

    page.add(
        myRouter.body
    )

    if myPyrebase.check_token() == "Success":
        page.go('/dashboard')
    else:
        page.go('/')
    


if __name__ == "__main__":
    import os
    ft.app(target=main, assets_dir="./assets", port=int(os.getenv("FLET_PORT", 8502)), name=os.getenv("FLET_PATH", ''), view=ft.FLET_APP_HIDDEN)

    