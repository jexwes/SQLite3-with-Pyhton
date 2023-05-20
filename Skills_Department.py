import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

# Como a tabela funcionarios tem 8 atributos, é necessario declarar o 8
exp_sql = 'INSERT INTO competencias values (?, ?, ?)'

competencias = [
    (1, 'Configurar linha de Produção', 'PRODUÇÃO'),
    (2, 'Elaborar plano de Marketing', 'MARKETING'),
    (3, 'Vender para o Mercosul', 'VENDAS'),
    (4, 'Realizar manutenção de linha de Produção', 'PRODUÇÃO'),
    (5, 'Operar CAD e CAM', 'ENGENHARIA')
]


for competencia in competencias:
    con.execute(exp_sql, competencia)


con.commit()
con.close()
