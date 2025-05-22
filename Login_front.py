import flet as ft
import sys
import Functions_bd
import pyperclip
import time
import os

print('Bibliotecas importadas com sucesso!')
print(f'Executando python da pasta: {sys.executable}')


'''VARIAVEIS GLOBAIS''' 
caminho_do_script = os.path.abspath(__file__)
pasta_do_script = os.path.dirname(caminho_do_script)
cor_fonte_escura = "#444444"
cor_fonte_clara = "#ebebeb"
nome_usuario = "Desconhecido"

def registrar(page):
    def dlg_clicou(e = None):
        if not dlg_usuarios.value or not dlg_email.value or not dlg_senha.value : dlg_mensagem.value = "Preencha corretamente\ntodos os campos" ; page.update()
        
        cadastrado = Functions_bd.cadastrar_usuario(dlg_usuarios.value, dlg_email.value, dlg_senha.value)
        if cadastrado:
            global nome_usuario
            nome_usuario = dlg_usuarios.value
            home_front(page)
            
        else:
            dlg_mensagem.value = "Tente novamente..."
            page.update()
    
    dlg_mensagem = ft.Text("",color=cor_fonte_escura,size=20,weight="BOLD")
    dlg_usuarios = ft.TextField(label="Usuário", on_submit=dlg_clicou, bgcolor="#eff7ff", border_color=cor_fonte_escura, color=cor_fonte_escura, password=False)
    dlg_email = ft.TextField(label="Email", on_submit=dlg_clicou, bgcolor="#eff7ff", border_color=cor_fonte_escura, color=cor_fonte_escura, password=False)
    dlg_senha = ft.TextField(label="Senha", on_submit=dlg_clicou, bgcolor="#eff7ff", border_color=cor_fonte_escura, color=cor_fonte_escura, password=True)
    btn_cadastrar = ft.ElevatedButton("CRIAR CADASTRO",style=ft.ButtonStyle(color=cor_fonte_clara),on_click=dlg_clicou)
    
    container_main = ft.Container(
        bgcolor="#ddeeff",
        padding=20,
        height=450,
        width=500,
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            width=400,
            height=400,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ 
                ft.Image(src=os.path.join(pasta_do_script,"assets","LogoBaseClaro.png")),
                ft.Container(padding=15, 
                    content=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name=ft.icons.KEY, color=ft.colors.BLUE),
                        ]
                    )
                ),
                dlg_usuarios,
                dlg_email,
                dlg_senha,
                dlg_mensagem,
                ft.Row(
                    controls=[
                        btn_cadastrar,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=50
        ),
    )
    
    principal_row = ft.Row(
        controls=[
            ft.Column(
                controls=[container_main],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    page.controls.clear()
    page.add(principal_row)

def login_front(page):
    
    def dlg_clicou(e):
        if not dlg_usuarios.value or not dlg_senha.value: dlg_mensagem.value = "Usuário não identificado..."; page.update()

        dict_acess = Functions_bd.usuario_logado(dlg_usuarios.value,dlg_senha.value)
        #email nao existe
        if not dict_acess["email_existente"]:
            dlg_mensagem.value = "Usuário não cadastrado. Realize o cadastro"
            page.update()
            
        #senha errada
        elif not dict_acess["senha_correta"]:
            dlg_mensagem.value = "Senha incorreta"
            page.update()
        #senha correta e email existente
        else:
            global nome_usuario
            nome_usuario = dict_acess['nome']
            home_front(page)
            
    
    dlg_mensagem = ft.Text("",color=cor_fonte_escura,size=20,weight="BOLD")
    dlg_usuarios = ft.TextField(label="Email", on_submit=dlg_clicou, bgcolor="#eff7ff",text_style=ft.TextStyle(color=cor_fonte_escura), password=False)
    dlg_senha = ft.TextField(label="Senha", on_submit=dlg_clicou, bgcolor="#eff7ff", text_style=ft.TextStyle(color=cor_fonte_escura), password=True)
    btn_acessar = ft.ElevatedButton("ACESSAR",style=ft.ButtonStyle(text_style=ft.TextStyle(color=cor_fonte_clara)),on_click=dlg_clicou)
    btn_registrar = ft.ElevatedButton("REGISTRAR",style=ft.ButtonStyle(text_style=ft.TextStyle(color=cor_fonte_clara)),on_click=lambda _, page_ft = page: registrar(page_ft))
    
    container_main = ft.Container(
        bgcolor="#ddeeff",
        padding=20,
        height=450,
        width=500,
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            width=400,
            height=400,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[ 
                ft.Image(src=os.path.join(pasta_do_script,"assets","LogoBaseClaro.png")),
                ft.Container(padding=15, 
                    content=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name=ft.icons.KEY, color=ft.colors.BLUE),
                        ]
                    )
                ),
                dlg_usuarios,
                dlg_senha,
                dlg_mensagem,
                ft.Row(
                    controls=[
                        btn_acessar,
                        btn_registrar,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=50
        ),
    )
    
    principal_row = ft.Row(
        controls=[
            ft.Column(
                controls=[container_main],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    page.controls.clear()
    page.add(principal_row)

def diagnostic_front(page):
    pass

def home_front(page):
    nome_usuario_campo = ft.Text(nome_usuario, color="#4dd0d5", weight="BOLD", size=14)
    btn_start_diag = ft.ElevatedButton("NOVO DIAGNÓSTICO", icon="ADD_SHARP", bgcolor="#4dd0d5", color=cor_fonte_clara, on_click=lambda _, page_ft = page: diagnostic_front(page_ft))
    area_ult_diag = ft.ElevatedButton("Ultimo diagnóstico...", bgcolor="#4dd0d5", color=cor_fonte_clara, on_click=lambda _: pyperclip.copy(_.control.text))
    num_emerg = ft.ElevatedButton("EM CASO DE EMERGÊNCIA\n LIGAR 192",icon="LOCAL_HOSPITAL_OUTLINED", bgcolor="#e74848", color=cor_fonte_clara, on_click=lambda _, page_ft = page: login_front(page_ft))
    btn_logout = ft.ElevatedButton("SAIR",icon="EXIT_TO_APP", bgcolor="#e74848", color=cor_fonte_clara, on_click=lambda _, page_ft = page: login_front(page_ft))
    
    container_main = ft.Container(
        bgcolor="#ddeeff",
        padding=20,
        height=450,
        width=500,
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            width=400,
            height=400,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon("PERSON", color="#4dd0d5"),
                        nome_usuario_campo
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                ),
                btn_start_diag,
                area_ult_diag,
                num_emerg,
                btn_logout,
            ],
            spacing=50
        ),
    )
    
    principal_row = ft.Row(
        controls=[
            ft.Column(
                controls=[container_main],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    page.controls.clear()
    page.add(principal_row)

def main(page: ft.Page):
    
    #inicializa o page maximizado
    page.window_maximized = True
    principal_row = ft.Text("inicio")
    page.add(principal_row)
    
    login_front(page)
    
        


if __name__ == '__main__':
    try:
        ft.app(target=main, assets_dir="assets")
        
    except Exception as ex:
        print(ex,flush=True)