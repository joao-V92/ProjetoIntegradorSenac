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
    def dlg_clicou(e=None):
        if not dlg_usuarios.value or not dlg_email.value or not dlg_senha.value:
            dlg_mensagem.value = "Preencha corretamente todos os campos"
            dlg_mensagem.color = ft.Colors.RED_400
            page.update()
            return

        cadastrado = Functions_bd.cadastrar_usuario(
            dlg_usuarios.value, dlg_email.value, dlg_senha.value)
        if cadastrado:
            global nome_usuario
            nome_usuario = dlg_usuarios.value
            home_front(page)
        else:
            dlg_mensagem.value = "Tente novamente..."
            dlg_mensagem.color = ft.Colors.RED_400
            page.update()

    def on_hover_cadastrar(e):
        btn_cadastrar.bgcolor = ft.Colors.BLUE_700 if e.data == "true" else ft.Colors.BLUE_600
        page.update()

    def on_hover_voltar(e):
        btn_voltar.bgcolor = ft.Colors.BLUE_GREY_700 if e.data == "true" else ft.Colors.BLUE_GREY_600
        page.update()

    # Mensagem de feedback
    dlg_mensagem = ft.Text(
        "",
        color=cor_fonte_escura,
        size=14,
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER
    )

    # Campo Usuário
    dlg_usuarios = ft.TextField(
        label="Usuário",
        on_submit=dlg_clicou,
        bgcolor=ft.Colors.WHITE,
        filled=True,
        border_radius=12,
        border_color=ft.Colors.BLUE_100,
        focused_border_color=ft.Colors.BLUE_400,
        cursor_color=ft.Colors.BLUE_600,
        text_style=ft.TextStyle(color=cor_fonte_escura),
        label_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_600),
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=20, vertical=15),
        password=False
    )

    # Campo Email
    dlg_email = ft.TextField(
        label="Email",
        on_submit=dlg_clicou,
        bgcolor=ft.Colors.WHITE,
        filled=True,
        border_radius=12,
        border_color=ft.Colors.BLUE_100,
        focused_border_color=ft.Colors.BLUE_400,
        cursor_color=ft.Colors.BLUE_600,
        text_style=ft.TextStyle(color=cor_fonte_escura),
        label_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_600),
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        content_padding=ft.padding.symmetric(horizontal=20, vertical=15),
        password=False
    )

    # Campo Senha
    dlg_senha = ft.TextField(
        label="Senha",
        on_submit=dlg_clicou,
        bgcolor=ft.Colors.WHITE,
        filled=True,
        border_radius=12,
        border_color=ft.Colors.BLUE_100,
        focused_border_color=ft.Colors.BLUE_400,
        cursor_color=ft.Colors.BLUE_600,
        text_style=ft.TextStyle(color=cor_fonte_escura),
        label_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_600),
        password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=20, vertical=15)
    )

    # Botão CRIAR CADASTRO
    btn_cadastrar = ft.Container(
        content=ft.Text(
            "Registrar",
            color=cor_fonte_clara,
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        bgcolor=ft.Colors.BLUE_600,
        padding=ft.padding.symmetric(vertical=15, horizontal=30),
        border_radius=12,
        alignment=ft.alignment.center,
        on_click=dlg_clicou,
        animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        on_hover=on_hover_cadastrar,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLUE_200,
            offset=ft.Offset(0, 4)
        )
    )

    # Botão VOLTAR
    btn_voltar = ft.Container(
        content=ft.Text(
            "Login",
            color=cor_fonte_clara,
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        bgcolor=ft.Colors.BLUE_GREY_600,
        padding=ft.padding.symmetric(vertical=15, horizontal=30),
        border_radius=12,
        alignment=ft.alignment.center,
        on_click=lambda _, page_ft=page: login_front(page_ft),
        animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        on_hover=on_hover_voltar,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLUE_GREY_200,
            offset=ft.Offset(0, 4)
        )
    )

    # Container do avatar/ícone
    avatar_container = ft.Container(
        content=ft.Icon(
            ft.Icons.PERSON_ADD,
            size=56,
            color=ft.Colors.BLUE_GREY_400,
        ),
        bgcolor=ft.Colors.BLUE_GREY_100,
        width=120,
        height=120,
        border_radius=40,
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=200)
    )

    # Elementos decorativos
    decorative_elements = ft.Stack([
        ft.Container(
            width=20,
            height=20,
            bgcolor=ft.Colors.BLUE_200,
            border_radius=10,
            left=50,
            top=30
        ),
        ft.Container(
            width=30,
            height=30,
            bgcolor=ft.Colors.CYAN_200,
            border_radius=15,
            right=40,
            top=80
        ),
        ft.Container(
            width=25,
            height=25,
            bgcolor=ft.Colors.LIGHT_BLUE_200,
            border_radius=3,
            left=60,
            bottom=50
        ),
        ft.Container(
            width=15,
            height=15,
            bgcolor=ft.Colors.BLUE_300,
            border_radius=7.5,
            right=60,
            bottom=40
        )
    ])

    # Container principal
    container_main = ft.Container(
        content=ft.Column([
            # Título estilizado
            ft.Text(
                "Realize seu cadastro",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_GREY_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Container(
                padding=15,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(name=ft.Icons.PERSON_ADD,
                                color=ft.Colors.BLUE, size=30),
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
                    btn_voltar,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=450,
        padding=40,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=20,
            color=ft.Colors.BLUE_GREY_300,
            offset=ft.Offset(0, 10)
        ),
        alignment=ft.alignment.center
    )

    # Layout principal
    layout_principal = ft.Container(
        content=ft.Stack([
            decorative_elements,
            ft.Row([
                # Lado esquerdo com avatar
                ft.Container(
                    content=ft.Column([
                        avatar_container,
                        ft.Container(height=20),
                        ft.Icon(ft.Icons.APP_REGISTRATION,
                                color=ft.Colors.BLUE_300, size=30)
                    ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    expand=1,
                    alignment=ft.alignment.center
                ),
                # Lado direito com formulário
                ft.Container(
                    content=container_main,
                    expand=2,
                    alignment=ft.alignment.center
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]),
        width=900,
        height=600,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=25,
        padding=40,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                ft.Colors.BLUE_100,
                ft.Colors.LIGHT_BLUE_50,
                ft.Colors.CYAN_50
            ]
        )
    )

    # Estrutura principal
    principal_row = ft.Row(
        controls=[
            ft.Column(
                controls=[layout_principal],
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
        if not dlg_usuarios.value or not dlg_senha.value:
            dlg_mensagem.value = "Usuário não identificado..."
            dlg_mensagem.color = ft.Colors.RED_400
            page.update()
            return

        dict_acess = Functions_bd.usuario_logado(
            dlg_usuarios.value, dlg_senha.value)
        if not dict_acess["email_existente"]:
            dlg_mensagem.value = "Usuário não cadastrado. Realize o cadastro"
            dlg_mensagem.color = ft.Colors.RED_400
            page.update()

        elif not dict_acess["senha_correta"]:
            dlg_mensagem.value = "Senha incorreta"
            dlg_mensagem.color = ft.Colors.RED_400
            page.update()

        # Senha correta e email existente
        else:
            global nome_usuario
            nome_usuario = dict_acess['nome']
            home_front(page)

    def on_hover_acessar(e):
        btn_acessar.bgcolor = ft.Colors.BLUE_700 if e.data == "true" else ft.Colors.BLUE_600
        page.update()

    def on_hover_registrar(e):
        btn_registrar.bgcolor = ft.Colors.BLUE_700 if e.data == "true" else ft.Colors.BLUE_600
        page.update()

    # Mantendo os nomes originais
    dlg_mensagem = ft.Text(
        "",
        color=cor_fonte_escura,
        size=14,
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER
    )

    dlg_usuarios = ft.TextField(
        label="Email",
        on_submit=dlg_clicou,
        bgcolor=ft.Colors.WHITE,
        filled=True,
        border_radius=12,
        border_color=ft.Colors.BLUE_100,
        focused_border_color=ft.Colors.BLUE_400,
        cursor_color=ft.Colors.BLUE_600,
        text_style=ft.TextStyle(color=cor_fonte_escura),
        label_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_600),
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        content_padding=ft.padding.symmetric(horizontal=20, vertical=15),
        password=False
    )

    dlg_senha = ft.TextField(
        label="Senha",
        on_submit=dlg_clicou,
        bgcolor=ft.Colors.WHITE,
        filled=True,
        border_radius=12,
        border_color=ft.Colors.BLUE_100,
        focused_border_color=ft.Colors.BLUE_400,
        cursor_color=ft.Colors.BLUE_600,
        text_style=ft.TextStyle(color=cor_fonte_escura),
        label_style=ft.TextStyle(color=ft.Colors.BLUE_GREY_600),
        password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        content_padding=ft.padding.symmetric(horizontal=20, vertical=15)
    )

    # Botão ACESSAR reformulado mas mantendo o nome
    btn_acessar = ft.Container(
        content=ft.Text(
            "ACESSAR",
            color=cor_fonte_clara,
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        bgcolor=ft.Colors.BLUE_600,
        padding=ft.padding.symmetric(vertical=15, horizontal=30),
        border_radius=12,
        alignment=ft.alignment.center,
        on_click=dlg_clicou,
        animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        on_hover=on_hover_acessar,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLUE_200,
            offset=ft.Offset(0, 4)
        )
    )

    btn_registrar = ft.Container(
        content=ft.Text(
            "REGISTRAR",
            color=cor_fonte_clara,
            size=16,
            weight=ft.FontWeight.BOLD
        ),
        bgcolor=ft.Colors.BLUE_600,
        padding=ft.padding.symmetric(vertical=15, horizontal=30),
        border_radius=12,
        alignment=ft.alignment.center,
        on_click=lambda _, page_ft=page: registrar(page_ft),
        animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        on_hover=on_hover_registrar,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLUE_200,
            offset=ft.Offset(0, 4)
        )
    )

    # Container do avatar/ícone - elemento adicional
    avatar_container = ft.Container(
        content=ft.Icon(
            ft.Icons.PERSON,
            size=56,
            color=ft.Colors.BLUE_GREY_400,
        ),
        bgcolor=ft.Colors.BLUE_GREY_100,
        width=120,
        height=120,
        border_radius=40,
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=200)  # Adiciona espaço no topo
    )

    # Elementos decorativos - elementos adicionais
    decorative_elements = ft.Stack([
        ft.Container(
            width=20,
            height=20,
            bgcolor=ft.Colors.BLUE_200,
            border_radius=10,
            left=50,
            top=30
        ),
        ft.Container(
            width=30,
            height=30,
            bgcolor=ft.Colors.CYAN_200,
            border_radius=15,
            right=40,
            top=80
        ),
        ft.Container(
            width=25,
            height=25,
            bgcolor=ft.Colors.LIGHT_BLUE_200,
            border_radius=3,
            left=60,
            bottom=50
        ),
        ft.Container(
            width=15,
            height=15,
            bgcolor=ft.Colors.BLUE_300,
            border_radius=7.5,
            right=60,
            bottom=40
        )
    ])

    # Container principal reformulado mantendo o nome
    container_main = ft.Container(
        content=ft.Column([
            # Substituindo a imagem por um título estilizado
            ft.Text(
                "Realize seu login",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_GREY_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Container(
                padding=15,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(name=ft.Icons.KEY,
                                color=ft.Colors.BLUE, size=30),
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
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=450,
        padding=40,
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=20,
            color=ft.Colors.BLUE_GREY_300,
            offset=ft.Offset(0, 10)
        ),
        alignment=ft.alignment.center
    )

    # Layout principal reformulado
    layout_principal = ft.Container(
        content=ft.Stack([
            decorative_elements,
            ft.Row([
                # Lado esquerdo com avatar
                ft.Container(
                    content=ft.Column([
                        avatar_container,
                        ft.Container(height=20),
                        ft.Icon(ft.Icons.PLAY_ARROW,
                                color=ft.Colors.BLUE_300, size=30)
                    ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    expand=1,
                    alignment=ft.alignment.center
                ),
                # Lado direito com formulário
                ft.Container(
                    content=container_main,
                    expand=2,
                    alignment=ft.alignment.center
                )
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]),
        width=900,
        height=600,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=25,
        padding=40,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                ft.Colors.BLUE_100,
                ft.Colors.LIGHT_BLUE_50,
                ft.Colors.CYAN_50
            ]
        )
    )

    # Mantendo a estrutura original principal_row
    principal_row = ft.Row(
        controls=[
            ft.Column(
                controls=[layout_principal],  # Usando o novo layout
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
    # Cores mais suaves e modernas
    COR_PRIMARIA = "#2196F3"      # Azul mais suave
    COR_SECUNDARIA = "#F5F5F5"    # Cinza muito claro
    COR_SUCESSO = "#4CAF50"       # Verde suave
    COR_PERIGO = "#F44336"        # Vermelho suave
    COR_TEXTO_ESCURO = "#212121"  # Quase preto
    COR_TEXTO_CLARO = "#FFFFFF"   # Branco
    COR_FUNDO = "#FAFAFA"         # Branco acinzentado

    # Elementos da interface
    nome_usuario_campo = ft.Text(
        nome_usuario,
        color=COR_TEXTO_ESCURO,
        weight=ft.FontWeight.W_600,
        size=16
    )

    btn_start_diag = ft.ElevatedButton(
        text="Novo Diagnóstico",
        icon=ft.Icons.ADD_CIRCLE_OUTLINE,
        bgcolor=COR_PRIMARIA,
        color=COR_TEXTO_CLARO,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=2,
            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500)
        ),
        on_click=lambda _, page_ft=page: diagnostic_front(page_ft)
    )

    area_ult_diag = ft.ElevatedButton(
        text="Último diagnóstico",
        icon=ft.Icons.HISTORY,
        bgcolor=COR_SECUNDARIA,
        color=COR_TEXTO_ESCURO,
        height=45,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=1,
            text_style=ft.TextStyle(size=13, weight=ft.FontWeight.W_400)
        ),
        on_click=lambda _: pyperclip.copy(_.control.text)
    )

    num_emerg = ft.ElevatedButton(
        text="Emergência - 192",
        icon=ft.Icons.LOCAL_HOSPITAL_OUTLINED,
        bgcolor=COR_PERIGO,
        color=COR_TEXTO_CLARO,
        height=45,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=2,
            text_style=ft.TextStyle(size=13, weight=ft.FontWeight.W_500)
        ),
        on_click=lambda _, page_ft=page: login_front(page_ft)
    )

    btn_logout = ft.ElevatedButton(
        text="Sair",
        icon=ft.Icons.LOGOUT,
        bgcolor=COR_SECUNDARIA,
        color=COR_TEXTO_ESCURO,
        height=40,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=1,
            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.W_400)
        ),
        on_click=lambda _, page_ft=page: login_front(page_ft)
    )

    # Container principal com design mais limpo
    container_main = ft.Container(
        bgcolor=COR_TEXTO_CLARO,
        padding=ft.padding.all(24),
        height=480,
        width=420,
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.1, "#000000"),
            offset=ft.Offset(0, 4)
        ),
        border=ft.border.all(1, ft.Colors.with_opacity(0.1, "#000000")),
        content=ft.Column(
            width=360,
            height=420,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Header com informações do usuário
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.PERSON,
                                    color=COR_PRIMARIA,
                                    size=24
                                ),
                                bgcolor=ft.Colors.with_opacity(
                                    0.1, COR_PRIMARIA),
                                border_radius=20,
                                padding=8
                            ),
                            nome_usuario_campo
                        ],
                        spacing=12,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    padding=ft.padding.only(bottom=16)
                ),

                # Botões principais
                ft.Column(
                    controls=[
                        btn_start_diag,
                        area_ult_diag,
                    ],
                    spacing=16,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=320
                ),

                # Botões secundários
                ft.Column(
                    controls=[
                        num_emerg,
                        btn_logout,
                    ],
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=320
                ),
            ],
            spacing=24
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

    # inicializa o page maximizado
    page.window_maximized = True
    principal_row = ft.Text("inicio")
    page.add(principal_row)

    login_front(page)


if __name__ == '__main__':
    try:
        ft.app(target=main, assets_dir="assets")

    except Exception as ex:
        print(ex, flush=True)
