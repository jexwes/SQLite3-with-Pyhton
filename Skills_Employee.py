import sqlite3
con = sqlite3.connect('empresa.db')
cur = con.cursor()

# Como a tabela funcionarios tem 8 atributos, é necessario declarar os 8
exp_sql = 'INSERT INTO funcionarios_competencias values (?, ?, ?)'

f_comptencias = [
    (1001, 1, '10/10/2022'),
    (1002, 3, '20/11/2022'),
    (1003, 1, '24/03/2021'),
    (2001, 2, '27/04/2022'),
    (2002, 3, '22/04/2022'),
    (1001, 4, '15/07/2022'),
    (1003, 4, '21/11/2022')
]


for f_comptencia in f_comptencias:
    con.execute(exp_sql, f_comptencia)


con.commit()
con.close()
