import flet as ft
import sys
import Functions_bd
import pyperclip
import time
import os

def main(page: ft.Page):

    # inicializa o page maximizado

    page.window_maximized = True
    principal_row = ft.Text("inicio")
    page.add(principal_row)
    
    global dlg_loading; dlg_loading = ft.AlertDialog(
        title=ft.Text("CARREGANDO...",weight="BOLD",color="#444444",text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.BLUE_100,
        content=ft.Row(controls=[ft.ProgressRing(color="#444444")], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        title_padding=ft.padding.all(25),
    )
    
    page.open(dlg_loading)



if __name__ == '__main__':
    try:
        ft.app(target=main, assets_dir="assets")

    except Exception as ex:
        print(ex, flush=True)
