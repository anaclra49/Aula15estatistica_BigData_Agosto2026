import pandas as pd 
from sqlalchemy import create_engine

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula04'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

query1 = 'SELECT * FROM materiais_construcao;'
query2 = 'SELECT preco, produto FROM materiais_construcao;'
query3 = '''
    SELECT * FROM materiais_construcao;
    WHERE categoria = 'cimento'
'''
query4 = '''
    SELECT * FROM materiais_construcao
    WHERE preco > 200;
'''

df_construcao = pd.read_sql(query4, engine)
print(df_construcao)
