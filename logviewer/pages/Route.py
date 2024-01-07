import flet as ft
from pages.HomePage import HomePage
from pages.SettingsPage import SettingsPage

def Route(page : ft.Page):
    page.title = "test app"

    pop_flag = False

    def route_change(e):
        nonlocal pop_flag

        if pop_flag:
            pop_flag = False
        else:
            if page.route == "/":
                page.views.clear()
                page.views.append(
                    HomePage(page)
                )
            elif page.route == "/SettingsPage":
                page.views.append(
                    SettingsPage(page.views[-1].data)
                )
        
    def view_pop(e):
        nonlocal pop_flag
        pop_flag = True
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.views.clear()
    page.go("/")