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
            .select("nome,email_paciente, senha")
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
    
def pega_sintomas(filtro: list[str] = []) -> tuple[list[str], str]:
    connect_db()

    try:
        
        if not filtro:
            resp = supabase\
                .table("sintoma")\
                .select("descricao")\
                .execute()

            descricoes = [row["descricao"] for row in resp.data]
            return list(dict.fromkeys(descricoes)), "sintomas"

        
        resp_d = supabase\
            .table("doenca")\
            .select("id_doenca")\
            .in_("descricao_doenca", filtro)\
            .execute()
        doenca_ids = [r["id_doenca"] for r in resp_d.data]
        if not doenca_ids:
            return ([], "sintomas")

        
        resp_ds = supabase\
            .table("doenca_sintoma")\
            .select("sintoma_id")\
            .in_("doenca_id", doenca_ids)\
            .execute()
        sintoma_ids = [r["sintoma_id"] for r in resp_ds.data]
        if not sintoma_ids:
            return ([], "sintomas")

       
        resp_s = supabase\
            .table("sintoma")\
            .select("descricao")\
            .in_("id_sintoma", sintoma_ids)\
            .execute()
        descricoes = [r["descricao"] for r in resp_s.data]
        #   remover duplicatas
        return list(dict.fromkeys(descricoes)), "sintomas"

    except Exception as e:
        print("Erro em pega_sintomas:", e)
        return ([], "error")

    
if __name__ == "__main__":
    # lista_sintom = pega_sintomas()
    lista_sintom, tipo = pega_sintomas(['dor no peito'])
    print(tipo)
    print(lista_sintom)