import tkinter as tk
from tkinter import messagebox, RIDGE, RAISED, NSEW



class Login:
    def __init__(self, master):
        self.janelalogin = master
        self.janelalogin.title('')
        self.janelalogin.geometry("310x330")
        self.janelalogin.configure(background="#20b2aa")
        self.janelalogin.resizable(width=False, height=False)

        # Dividindo a janela
        self.frame_cima = tk.Frame(self.janelalogin, width=310, height=50, bg="#20b2aa", relief="flat")
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        self.frame_baixo = tk.Frame(self.janelalogin, width=310, height=350, bg="#20b2aa", relief="flat")
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        # configurando o fram cima
        self.lbl_cima = tk.Label(self.frame_cima, text="LOGIN", font=("Ivy 25"), bg="#20b2aa", fg="#111111")
        self.lbl_cima.place(x=5, y=5)

        self.lbl_linha = tk.Label(self.frame_cima, text="", width=280, font=("Ivy 1"), bg="#ffa500")
        self.lbl_linha.place(x=10, y=45)

        self.credenciais = ["Carlos", "12345", "Luiz", "12345"]


        # configurando frame baixo
        lbl_nome = tk.Label(self.frame_baixo, text="Nome *", font=("Ivy 13"), bg="#20b2aa", fg="#111111")
        lbl_nome.place(x=10, y=20)

        self.entry_nome = tk.Entry(self.frame_baixo, width=20, justify="left", font=("", 15), highlightthickness=1, relief="solid")
        self.entry_nome.place(x=14, y=50)

        self.lbl_senha = tk.Label(self.frame_baixo, text="Senha *", font=("Ivy 13"), bg="#20b2aa", fg="#111111")
        self.lbl_senha.place(x=10, y=95)

        self.entry_senha = tk.Entry(self.frame_baixo, width=20, justify="left", font=("", 15), highlightthickness=1, relief="solid")
        self.entry_senha.place(x=14, y=130)

        botao_confirmar = tk.Button(self.frame_baixo, command=self.verifica_senha, text="Entrar", width=34, height=2,
                                 font=("Ivy 8 bold"), bg="#ffa500", fg="#111111", relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=15, y=180)


        botao_cadastrar = tk.Button(self.frame_baixo, command=self.cadastramento, text="Cadastrar", width=6, height=1,
                                 font=("Ivy 8 bold"), bg="#20b2aa", fg="#111111", highlightbackground = "#20b2aa", relief=tk.FLAT)
        botao_cadastrar.place(x=115, y=230)

    def verifica_senha(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

    def cadastramento(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        sql_verifica = 'SELECT Usuario, Senha FROM Login'
        a = db_consultar(sql_verifica)
        print(a)
        parsed_sql_verifica = ''.join(map(str, (a[0])))
        print(parsed_sql_verifica)

        # sql_insert_cadas = f'INSERT INTO Login VALUES(NULL, "{nome}", "{senha}");'


#criar um arquivo separado só pra isso
import sqlite3
from sqlite3 import Error


def conexao():
    caminho = "bd_login"
    try:
        con = None
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_insert = 'INSERT INTO produtos VALUES(2, "Teste2", 1, 1.9);'

sql_tabela = """
             CREATE TABLE produtos(
             código INT(10) PRIMARY KEY NOT NULL,
             nomes VARCHAR(100) NOT NULL,
             preço INT(20),
             estoque INT(20))
             """

sql_update = 'UPDATE cliente SET nome = "Elias Charizard" WHERE id = 8'
sql_delete = 'DELETE FROM produtos WHERE estoque = "";'
sql_consutar = "SELECT * FROM produtos;"
# print(conexao())

def db_consultar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)

def db_inserir(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Registros inseridos")
    except Error as er:
        print(er)

def db_tabela(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Tabela inserida")
    except Error as er:
        print(er)

def db_atualizar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print("Atualiza funcionando")
    except Error as er:
        print(er)

def db_deletar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print("Deletado com Sucesso!")
    except Error as er:
        print(er)

# db_tabela(sql_tabela)
# db_deletar(sql_delete)
# atualizar(sql_update)
# db_inserir(sql_insert)
# for i in db_consultar(sql_consutar):
#     print(i)

janela = tk.Tk()
Login(janela)
janela.mainloop()
