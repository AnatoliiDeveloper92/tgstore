import flet as ft
from pages.storage import sm
import requests

def cart_page(page: ft.Page, product):
    login_field = ft.TextField(label="Login in game or game id", width=300)
    phone_field = ft.TextField(label="Phone number +79998887766", width=300)
    comment_field = ft.TextField(label="Comments", width=300, height=300)

    def send_order(order):
        TOKEN = '8074565110:AAHfY_8dWI2ZB7aBGYYXOEuZ7ZGiWk4FGHQ'
        chat_id = "929204762"
        message = f"""
        Новый заказ!\n
        Наименование товара: {order['product']}\n
        Данные игрового аккаунта: {order['login']}\n
        Номер для связи: {order['phone_number']}\n
        Комментарий к заказу: {order['comment']}"""
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

    def get_values(e):
        o = {
                'product': sm.cart['name'],
                'login': login_field.value,
                'phone_number': phone_field.value,
                'comment': comment_field.value
            }
        send_order(o)


    if product:
        good = ft.Row(
                [
                    ft.Image(product['image'], width=70, height=70),
                    ft.Text(product['name'], size=24),
                    ft.Text(f'{product["price"]} $', size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
    else:
        good = ft.Text('No products', size=32)


    return ft.ListView(
        [
            ft.Column(
                    [
                        good,
                        ft.Divider(),
                        login_field,
                        phone_field,
                        comment_field,
                        ft.ElevatedButton('Confirm', width=300, on_click=get_values)
                    ],
                    # alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    scroll=ft.ScrollMode.ALWAYS
                    )
        ],
        expand=True  # Растягивается на всю доступную высоту
    )
