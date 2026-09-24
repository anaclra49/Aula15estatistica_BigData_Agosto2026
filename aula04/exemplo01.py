import pandas as pd 
from sqlalchemy import create_engine

#variaveis conexao
host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula04'

# criando a conexao 
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)




# consultas

query1 = 'SELECT *  FROM  cadastro_produtos;'
query2 = '''
SELECT * FROM cadastro_produtos
WHERE Marca = "Hashtag"
AND `Preço Unitario` > 20;
'''



df_produtos = pd.read_sql(query2 , engine)
print(df_produtos)





