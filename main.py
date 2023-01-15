
import flet as ft
from views.sign_in import SignInView
from views.dashboard import DashboardView
from db.flet_pyrebase import PyrebaseWrapper

def main(page: ft.Page):

    page.window_height = 500
    page.window_width = 300

    def route_change(e):
        page.views.clear()
        if page.route == "/": 
            page.views.append(
                ft.View(
                    "/",
                    [
                        SignInView(page,ft,PyrebaseWrapper)
                        ]
                    )
            )
        if page.route == "/dashboard":
            page.views.append(
                ft.View(
                    "/dashboard",
                    [
                        DashboardView(page,ft,PyrebaseWrapper)
                    ]
                )
            )
        page.update()



    page.on_route_change = route_change

    page.go(page.route)


if __name__ == "__main__":
    import os
    ft.app(target=main, assets_dir="./assets", port=int(os.getenv("FLET_PORT", 8502)), name=os.getenv("FLET_PATH", ''))

