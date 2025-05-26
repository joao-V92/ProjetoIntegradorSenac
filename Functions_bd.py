import os
from supabase import create_client, Client
from supabase.client import ClientOptions


supabase = None
schema = "public"
url_api = "https://hubmhnxfzksrgcpysjwx.supabase.co"
key_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1Ym1obnhmemtzcmdjcHlzand4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc5NjU0NDIsImV4cCI6MjA2MzU0MTQ0Mn0.qIsc9HfD340waUxsCjbukmjErg2B4eVR_Mk09McUCxU"


def connect_db():
    global supabase
    try:
        supabase = create_client(
            url_api, 
            key_api,
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
                schema=schema,
            )
        )
        return True
    
    except Exception as er:
        print(f'Erro na conexão: {er}')
        return False

def usuario_logado(email_informado, senha_informada):
    connect_db()
    try:
        '''PARAMETROS
        columns
        Optional
        string
        The columns to retrieve, defaults to *.

        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.
        '''
        
        response = (
            supabase.table("paciente")
            .select("nome, email_paciente, senha")
            .eq("email_paciente", email_informado) #.eq é o WHERE
            .execute()
        )
        
        res = {
            "nome": "desconhecido",
            "email_existente": False,
            "senha_correta": False,
        }
        
        if not response.data:
            res["email_existente"] = False
        
        else:
            for registro in response.data:
                if registro['senha'] != senha_informada:
                    res["email_existente"] = True
                    res["senha_correta"] = False
                    
                else:
                    res["nome"] = registro["nome"]
                    res["email_existente"] = True
                    res["senha_correta"] = True
                    break

        return res
        
    except Exception as er:
        print(f'Erro no select {er}')
        return {
            "email_existente": False,
            "senha_correta": False,
        }

def cadastrar_usuario(usuario, email, senha):
    connect_db()
    
    try:
        
        dict_data = {"nome": usuario, "email_paciente": email, "senha": senha}
        response = (
            supabase.table("paciente")
            .insert(dict_data)
            .execute()
        )

        return True
        
    except Exception as er:
        print(f'Erro no insert: {er}')
        return None
    
def pega_sintomas(filtro: list[str] = []) -> tuple[list[dict], str]:
    
    connect_db()
    
    try:
        '''PARAMETROS
        columns
        Optional
        string
        The columns to retrieve, defaults to *.

        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.
        '''
        
        # descricao : nome da doença ; doenca : breve descriçao sobre ela ; sintomas : uma str grande com cada elemento sendo separado por virgula
        if filtro:
            #modelo de pesquisa: "sintomas.ilike.%{filtro}%,sintomas.ilike.%{filtro}%,sintomas.ilike.%{filtro}%"
            or_filter = ",".join([f"sintomas.ilike.%{f}%" for f in filtro])
            response = (
                supabase.table("doenca")
                .select("descricao, doenca, sintomas")
                .or_(or_filter)
                .execute()
            )
            
        else:
            response = (
                supabase.table("doenca")
                .select("descricao, doenca, sintomas")
                .execute()
            )
        
        sintomas_doencas = []
        tipo = "sintomas"
        
        if not response.data:
            sintomas_doencas = [
                {
                    "sintoma": "sem doenças registradas", 
                    "nome_doenca": "sem doenças registradas", 
                    "descricao": "sem doenças registradas",
                }
            ]
        
        else:
            # descricao : nome da doença ; doenca : breve descriçao sobre ela ; sintomas : uma str grande com cada elemento sendo separado por virgula
            
            for registro in response.data:
                    dict_doenca = {
                        "sintomas": registro["sintomas"].split(','),
                        "nome_doenca": registro["descricao"],
                        "descricao": registro["doenca"],
                    }
                    
                    if dict_doenca not in sintomas_doencas:
                        sintomas_doencas.append(dict_doenca)
            
            if len(response.data) > 3:
                tipo = "sintomas"

            else:
                tipo = "nome_doenca"

        return sintomas_doencas, tipo
        
    except Exception as er:
        print(f'Erro no select {er}')
        return [], "sintomas"
    
    
if __name__ == "__main__":
    # lista_sintom, tipo = test_bd(['dor no peito'])
    # lista_sintom, tipo = pega_sintomas(['dor no peito'])
    lista_sintom = test_bd(['dor articular', 'rigidez', 'perda de flexibilidade', 'inchaço'])
    for sint in lista_sintom:
        print(sint)