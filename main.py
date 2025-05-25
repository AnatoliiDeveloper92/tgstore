import flet as ft
from pages.products import product_page
from pages.details import details_page
from pages.cart import cart_page
from pages.storage import sm

def main(page:ft.Page):
    page.title = 'Store'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.window.width = 320
    # page.window.min_width = 320
    # # page.window.height = 700

    def set_page(e):
        ind = e.control.selected_index
        if ind == 0:
            page.go("/products")
        elif ind == 1:
            page.go("/cart")
        elif ind == 2:
            page.go("/products")

    menu = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART_OUTLINED, label="Cart"),
            ft.NavigationBarDestination(icon=ft.Icons.LOGOUT, label="Logout"),
        ],
        on_change=lambda e: set_page(e)
    )

    def route_change(route):
        page.views.clear()

        if page.route == '/products':
            page.views.append(
                ft.View(
                    '/products',
                    [product_page(page), menu],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        elif page.route == '/details':
            page.views.append(
                ft.View(
                    '/details',
                    [details_page(page, sm.current_product), menu],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        elif page.route == '/cart':
            page.views.append(
                ft.View(
                    '/cart',
                    [cart_page(page, sm.cart), menu],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go('/products')

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)