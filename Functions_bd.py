import os
from supabase import create_client, Client
from supabase.client import ClientOptions


supabase = None
schema = "public"
url_api = "https://rawtcrjzfjyexchuzhge.supabase.co"
key_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJhd3Rjcmp6Zmp5ZXhjaHV6aGdlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc2NjU3NTUsImV4cCI6MjA2MzI0MTc1NX0.TFlTNNmY5L3onBzpbHzA7hYafkeRCvykkUroLnZClrQ"


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
            supabase.table("usuarios")
            .select("nome, senha")
            .eq("email", email_informado) #.eq é o WHERE
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
        
        dict_data = {"nome": usuario, "email": email, "senha": senha}
        response = (
            supabase.table("usuarios")
            .insert(dict_data)
            .execute()
        )

        return True
        
    except Exception as er:
        print(f'Erro no insert: {er}')
        return None
    
if __name__ == "__main__":
    if connect_db():
        print('Conexão com o banco realizada com sucesso')
        usuario_logado('rroba@gmail.com','235432')
    else:
        print('Erro na conexão com o banco')