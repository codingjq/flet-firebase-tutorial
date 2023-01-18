
import flet as ft
from views.FletRouter import Router
from db.flet_pyrebase import PyrebaseWrapper

def main(page: ft.Page):

    page.window_height = 500
    page.window_width = 300
    page.scroll = "auto"
    page.theme_mode = "dark"

    myPyrebase = PyrebaseWrapper(page)
    myRouter = Router(page, ft, myPyrebase)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

    page.go('/')
    
if __name__ == "__main__":
    ft.app(target=main)

    