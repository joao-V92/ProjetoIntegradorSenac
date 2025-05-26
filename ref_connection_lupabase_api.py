import os
from supabase import create_client, Client
from supabase.client import ClientOptions

supabase = None
schema = "public"
url_api = "https://hubmhnxfzksrgcpysjwx.supabase.co"
key_api = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1Ym1obnhmemtzcmdjcHlzand4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc5NjU0NDIsImV4cCI6MjA2MzU0MTQ0Mn0.qIsc9HfD340waUxsCjbukmjErg2B4eVR_Mk09McUCxU"


def connect_db():
    '''FUNÇÃO QUE CONECTA NO BANCO COLOCANDO A CONEXÃO NA VARIAVEL supabase'''
    global supabase
    try:
        '''
        OPTIONS DA CONEXÃO
        schema
        Optional
        string
        The Postgres schema which your tables belong to. Must be on the list of exposed schemas in Supabase. Defaults to 'public'.

        headers
        Optional
        dictionary
        Optional headers for initializing the client.

        auto_refresh_token
        Optional
        bool
        Whether to automatically refresh the token when it expires. Defaults to true.

        persist_session
        Optional
        bool
        Whether to persist a logged in session to storage.

        storage
        Optional
        SyncSupportedStorage
        A storage provider. Used to store the logged in session.

        realtime
        Optional
        string
        Options passed to the realtime-py instance.

        postgrest_client_timeout
        Optional
        number, float, Timeout
        Timeout passed to the SyncPostgrestClient instance.

        storage_client_timeout
        Optional
        number, float, Timeout
        Timeout passed to the SyncStorageClient instance.

        flow_type
        Optional
        AuthFlowType
        flow type to use for authentication.
        '''

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

def select():
    '''
    METODO DE SELECT NO BANCO DO SUPABASE
    RETORNA UMA RESPONSE COM O ELEMENTO DATA. 
    ESSA DATA É UMA LISTA AONDE CADA ITEM É UM DICIONARIO SENDO CHAVE = COLUNA , VALOR = VALOR DA COLUNA NAQUELA LINHA
    '''
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
            .select("*", count="exact") # count (Optional) The property to use to get the count of rows returned.
            .execute()
        )
        '''
        *select com colunas especificas:
        response = (
            supabase.table("planets")
            .select("name")
            .execute()
        )
        
        *select com referencias:
        response = (
            supabase.table("orchestral_sections")
            .select("name, instruments(name)")
            .execute()
        )
        
        *select com join:
        response = (
            supabase.table("orchestral_sections")
            .select("name, instruments(name)")
            .execute()
        )
        
        *select filtrando por valor:
        response = (
            supabase.table("orchestral_sections")
            .select("name, instruments(*)")
            .eq("instruments.name", "guqin")
            .execute()
        )
        
        *select com count em alguma coluna:
        response = (
            supabase.table("orchestral_sections")
            .select("*, instruments(count)")
            .execute()
        )
        '''
        
        return response.data
        
    except Exception as er:
        print(f'Erro no select {er}')
        return None

def insert():
    '''METODO DE INSERT NO BANCO DO SUPABASE'''
    try:
        '''PARAMETROS:
        json
        Required
        dict, list
        The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.

        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.

        returning
        Optional
        ReturnMethod
        Either 'minimal' or 'representation'. Defaults to 'representation'.

        default_to_null
        Optional
        bool
        Make missing fields default to null. Otherwise, use the default value for the column. Only applies for bulk inserts.
        '''
        
        dict_data = {"nome": "joao", "idade": 26}
        response = (
            supabase.table("usuarios")
            .insert(dict_data,)
            .execute()
        )
        '''INSERT MULTIPLOS
        response = (
            supabase.table("characters")
            .insert([
                {"id": 1, "name": "Frodo"},
                {"id": 2, "name": "Sam"},
            ])
            .execute()
        )
        '''

        return True
        
    except Exception as er:
        print(f'Erro no insert: {er}')
        return None

def update():
    '''METODO DE UPDATE NO BANCO DO SUPABASE'''
    try:
        '''PARAMETROS:
        json
        Required
        dict, list
        The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.

        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.
        '''
        response = (
            supabase.table("usuarios")
            .update({"nome": "juca"})
            .eq("nome", "joao") #.eq é o WHERE
            .execute()
        )
        '''UPDATE DE UM CAMPO COM JSON/OBJETO
        response = (
            supabase.table("users")
            .update({"address": {"street": "Melrose Place", "postcode": 90210}})
            .eq("address->postcode", 90210)
            .execute()
        )
        '''
        
        return True
    
    except Exception as er:
        print(f'Erro no update: {er}')
        return False
    
def upsert():
    '''METODO DE UPSERT NO BANCO DO SUPABASE
    UPSERT é um método que insere e atualiza um registro
    então caso o registro não existe ele será inserido
    caso já exita, será atualizado com as novas informações
    '''
    try:
        '''PARAMETROS:
        json
        Required
        dict, list
        The values to insert. Pass an dict to insert a single row or an list to insert multiple rows.

        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.

        returning
        Optional
        ReturnMethod
        Either 'minimal' or 'representation'. Defaults to 'representation'.

        ignore_duplicates
        Optional
        bool
        Whether duplicate rows should be ignored.

        on_conflict
        Optional
        string
        Specified columns to be made to work with UNIQUE constraint.

        default_to_null
        Optional
        bool
        Make missing fields default to null. Otherwise, use the default value for the column. Only applies for bulk inserts.
        '''
        response = (
            supabase.table("instruments")
            .upsert({"id": 1, "name": "piano"})
            .execute()
        )
    
    except Exception as er:
        print(f'Erro no upsert: {er}')
        return False

def delete():
    '''METODO DE DELETE NO BANCO DO SUPABASE'''
    try:
        '''PARAMETROS:
        count
        Optional
        CountMethod
        The property to use to get the count of rows returned.

        returning
        Optional
        ReturnMethod
        Either 'minimal' or 'representation'. Defaults to 'representation'.
        '''
        response = (
            supabase.table("countries")
            .delete()
            .eq("id", 1)
            .execute()
        )
        '''APAGAR MULTIPLOS REGISTROSs
        response = (
            supabase.table("countries")
            .delete()
            .in_("id", [1, 2, 3])
            .execute()
        )
        '''
        
        return True
    
    except Exception as er:
        print(f'Erro no delete: {er}')
        return False

def filtros():
    '''FUNÇÃO PARA COLOCAR COMO USAR OS FILTROS'''
    '''
    EM SUPABASE O FILTRO É EQ (EQUAL OU WHERE)
    # Correct
    response = (
        supabase.table("instruments")
        .select("name, section_id")
        .eq("name", "flute")
        .execute()
    )

    # Incorrect
    response = (
        supabase.table("instruments")
        .eq("name", "flute")
        .select("name, section_id")
        .execute()
    )
    
    FILTRO NEQ: NÃO IGUAL / != / FIFERENTE:
    
    response = (
        supabase.table("planets")
        .select("*")
        .neq("name", "Earth")
        .execute()
    )
    
    FILTRO GT: MAIOR DO QUE
    
    response = (
        supabase.table("planets")
        .select("*")
        .gt("id", 2)
        .execute()
    )
    
    FILTRO GTE: MAIOR DO QUE OU IGUAL A
    
    response = (
        supabase.table("planets")
        .select("*")
        .gte("id", 2)
        .execute()
    )
    
    FILTRO LT: MENOR DO QUE
    
    response = (
        supabase.table("planets")
        .select("*")
        .lt("id", 2)
        .execute()
    )
    
    FILTRO LTE: MENOR OU IGUAL A
    
    response = (
        supabase.table("planets")
        .select("*")
        .lte("id", 2)
        .execute()
    )
    
    FILTRO LIKE: BUSCA POR SEMELHANÇA (CASE-SENSITIVE)
    
    response = (
        supabase.table("planets")
        .select("*")
        .like("name", "%Ea%")
        .execute()
    )
    
    FILTRO ILIKE: BUSCA POR SEMELHANÇA (CASE-INSENSITIVE)
    
    response = (
        supabase.table("planets")
        .select("*")
        .ilike("name", "%ea%")
        .execute()
    )
    
    FILTRO IS: BUSCA DE UM TERMO QUE É TAL VALOR
    
    response = (
        supabase.table("planets")
        .select("*")
        .is_("name", "null")
        .execute()
    )
    
    FILTRO IN: PEGA REGISTROS AONDE TAIS ELEMENTOS EM TAL COLUNA:
    
    response = (
        supabase.table("planets")
        .select("*")
        .in_("name", ["Earth", "Mars"])
        .execute()
    )
    
    FILTRO RANGE_GT: REGISTROS MAIOR A QUALQUER UM DOS ELEMENTOS NO RANGE:
    
    response = (
        supabase.table("reservations")
        .select("*")
        .range_gt("during", ["2000-01-02 08:00", "2000-01-02 09:00"])
        .execute()
    )
    
    FILTRO RANGE_GTE: REGISTROS MAIOR OU IGUAL A QUALQUER UM DOS ELEMENTOS NO RANGE:
    
    response = (
        supabase.table("reservations")
        .select("*")
        .range_gte("during", ["2000-01-02 08:30", "2000-01-02 09:30"])
        .execute()
    )
    
    FILTROS RANGE_LT: REGISTROS MENOR A QUALQUER UM DOS ELEMENTOS NO RANGE:
    
    response = (
        supabase.table("reservations")
        .select("*")
        .range_lt("during", ["2000-01-01 15:00", "2000-01-01 16:00"])
        .execute()
    )
        
    FILTROS RANGE_LTE: REGISTROS MENOR OU IGUAL A QUALQUER UM DOS ELEMENTOS NO RANGE:
    
    response = (
        supabase.table("reservations")
        .select("*")
        .range_lte("during", ["2000-01-01 14:00", "2000-01-01 16:00"])
        .execute()
    )
        
        
    
    '''
    pass

def modificador_order():
    '''FUNÇÃO PARA COLOCAR COMO USAR OS FILTROS'''
    '''
    ORDENANDO RESULTADOS:
    
    PARAMETROS:
    
    column
    Required
    string
    The column to order by

    desc
    Optional
    bool
    Whether the rows should be ordered in descending order or not.

    foreign_table
    Optional
    string
    Foreign table name whose results are to be ordered.

    nullsfirst
    Optional
    bool
    Order by showing nulls first
    
    
    response = (
        supabase.table("planets")
        .select("*")
        .order("name", desc=True)
        .execute()
    )
    
    
    Limit the number of rows returned
    response = (
        supabase.table("planets")
        .select("name")
        .limit(1)
        .execute()
    )
    
    Limit the query to a range ( 0 conta )
    response = (
        supabase.table("planets")
        .select("name")
        .range(0, 1)
        .execute()
    )
    
    Create a new user
    **Sign up with an email and password
    response = supabase.auth.sign_up(
        {
            "email": "email@example.com", 
            "password": "password",
        }
    )
    **Sign up with a phone number and password (whatsapp)
    response = supabase.auth.sign_up(
        {
            "phone": "123456789",
            "password": "password",
            "options": {"channel": "whatsapp"},
        }
    )
    **Sign up with additional user metadata
    response = supabase.auth.sign_up(
        {
            "email": "email@example.com",
            "password": "password",
            "options": {"data": {"first_name": "John", "age": 27}},
        }
    )
    
    '''
    pass

if connect_db():
    print(f'Conectado ao banco de dados')
    # dados = select()
    # dados = insert()
    # dados = update()
    # dados = upsert()
    # print(dados)
else:
    print(f'Sem sucesso na conexão ao banco de dados')