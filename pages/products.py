import flet as ft   
from pages.storage import sm

def product_page(page: ft.Page):
    def see_more(e, product):
        sm.current_product = product
        page.go('/details')

    products = [
            {"name": "Call of Duty: Warzone", "description":"The Season 03 Battle Pass introduces 100+ rewards including new free base weapons plus new Operators and Operator Skins, Weapon Blueprints, Calling Cards, Finishing Moves, and more. Access free rewards including new cosmetic content and base weapons or purchase the premium Battle Pass and earn up to 1,100 COD Points as you progress through the Battle Pass Pages. For the optimal seasonal experience, purchase BlackCell, including exclusive animated Operator Skins, Weapon Blueprints, and other rewards.", "price": 10.99, "image": "https://i.playground.ru/e/BuWudNDwoD9mmqp_2fKQyw.jpeg"},
            {"name": "PUBG", "description":"", "price": 10.99, "image": "https://avatars.mds.yandex.net/i?id=99cfbb7d8677455fe6bca256b2bcc6ae_l-5449748-images-thumbs&n=13"},
            {"name": "Fortnite", "description":"", "price": 10.99, "image": "https://pic.rutubelist.ru/video/2024-09-20/01/76/0176f7eac515637f4f0a5b63ca8056fc.jpg"},
            {"name": "Delta Force", "description":"", "price": 10.99, "image": "https://steamuserimages-a.akamaihd.net/ugc/2492264950613846516/E2F4BC26C7E0B0B8077533DC622CD3128DB64CE6/?imw=512&amp;imh=288&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true"},
            # Добавьте больше товаров, если нужно
        ]
    
    products_cards = []
    for product in products:
        card = ft.Card(
            content=ft.Column(
                [
                    ft.Image(src=product["image"], width=320),
                    ft.Text(product["name"], size=18, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Text(f"{product['price']} $", size=16),
                            ft.ElevatedButton('See more', on_click=lambda e, product=product: see_more(e, product))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            width=320,
            height=250,
        )
        products_cards.append(card)

    return ft.GridView(
        controls=products_cards,
        expand=1,
        runs_count=5,
        max_extent=320,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )