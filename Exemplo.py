import customtkinter as ctk
from customtkinter import *
from PIL import Image
import sqlite3
from tkinter import messagebox
from CTkTable import CTkTable

'''
Exemplo de uma interface para o sistema de livraria
Foi utilizado a lib CustomtkInter apenas para criar essa interface
Para rodas esse script execute em seu terminal

# > pip install -r requirements.txt

E consulte se a pasta "img" esta no mesmo diretório do script Exemplo.py
'''






class Livraria:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('550x450')
        self.root.resizable(False,False)
        self.root.title('Livraria Python Brasil')
        
        self.img_banner = Image.open('img\LIVRARIABanner.png')
        # person_img_data = Image.open("person_icon.png")
        self.img_banner_ctk = CTkImage(dark_image=self.img_banner, light_image=self.img_banner,size=(500, 50))
        self.containers()
        self.root.mainloop()
    
    def containers(self):
        
        self.lb_img_banner = ctk.CTkLabel(
            master=self.root,
            text='',
            image=self.img_banner_ctk,
        )
        
        self.btn_add_new = ctk.CTkButton(
            master=self.root,
            text='Add novo Livro',
            fg_color='green',
            command=self.janela_add_new_livro
        )
        
        self.btn_delete = ctk.CTkButton(
            master=self.root,
            text='Deletar Livro',
            fg_color='red',
            command=self.janela_deletar_livro
        )
        
        self.btn_update = ctk.CTkButton(
            master=self.root,
            text='Atualizar Livro',
            command=self.janela_atualizar_livro
        )
        
        self.lb_title_table = ctk.CTkLabel(
            master=self.root,
            text='LIVROS',
            bg_color=self.root.cget('bg'),
            font=('Verdana', 20)
        )
        
        self.fr_container_table = ctk.CTkFrame(
            master=self.root,
            width=460,
            height=300,
        )
        
        header = (['ID', 'Titulo', 'Autor', 'Ano'])
        
        self.tabela_livros = self.ler_livros()
        
        self.tabela_livros.insert(0,header)
        
        self.table_frame = CTkScrollableFrame(
            master=self.fr_container_table, 
            fg_color="transparent"
            )
        
        self.table = CTkTable(
            master=self.table_frame, 
            values=self.tabela_livros, 
            header_color="#007FBB", 
            hover_color="#04567D",
            )
        
        self.lb_img_banner.place(x=25,y=10)
        self.btn_add_new.place(x=50,y=70)
        self.btn_delete.place(x=205,y=70)
        self.btn_update.place(x=360,y=70)
        self.lb_title_table.place(x=50,y=110)
        
        self.fr_container_table.propagate(0)
        self.fr_container_table.place(x=50,y=140)
        
        self.table_frame.pack(expand=True, fill="both")
        self.table.edit_row(0, text_color="#fff", hover_color="#04567D")
        self.table.pack(expand=True)

    def janela_add_new_livro(self):
        self.root_new_livro = ctk.CTk()
        self.root_new_livro.geometry('300x220')
        self.root_new_livro.resizable(False,False)
        self.root_new_livro.title('Add new Livro')
        
        lb_title = ctk.CTkLabel(
            master=self.root_new_livro,
            text='ADICIONAR NOVO REGISTRO',
            bg_color=self.root_new_livro.cget('bg'),
            font=('Verdana', 15)
        )
        
        self.en_nome_livro = ctk.CTkEntry(
            master=self.root_new_livro,
            placeholder_text='Nome do Livro...',
            border_color="green", 
            border_width=1,
            width=350
        )
        
        self.en_autor_livro = ctk.CTkEntry(
            master=self.root_new_livro,
            placeholder_text='Autor do Livro...',
            border_color="green", 
            border_width=1,
            width=350
        )
        
        self.en_ano_livro = ctk.CTkEntry(
            master=self.root_new_livro,
            placeholder_text='Ano do Livro...',
            border_color="green", 
            border_width=1,
            width=350
        )
        
        btn_salvar = ctk.CTkButton(
            master=self.root_new_livro,
            text='salvar',
            fg_color='green',
            command=self.inserir_livro
        )
        
        
        lb_title.pack(pady=(0,15))
        self.en_nome_livro.pack(anchor=W, padx=15)
        self.en_autor_livro.pack(anchor=W, padx=15, pady=15)
        self.en_ano_livro.pack(anchor=W, padx=15)
        btn_salvar.pack(anchor=W, padx=15,pady=15)
        
        self.root_new_livro.mainloop()
        
    def janela_atualizar_livro(self):
        self.root_atualizar_livro = ctk.CTk()
        self.root_atualizar_livro.geometry('300x220')
        self.root_atualizar_livro.resizable(False,False)
        self.root_atualizar_livro.title('Add new Livro')
        
        lb_title = ctk.CTkLabel(
            master=self.root_atualizar_livro,
            text='ATUALIZAR REGISTRO',
            bg_color=self.root_atualizar_livro.cget('bg'),
            font=('Verdana', 15)
        )
        
        self.en_id_livro_up = ctk.CTkEntry(
            master=self.root_atualizar_livro,
            placeholder_text='ID do Livro...',
            border_color="blue", 
            border_width=1,
            width=100
        )
        
        btn_procurar = ctk.CTkButton(
            master=self.root_atualizar_livro,
            text='Procurar',
            command=self.procurar_livro
        )
        
        self.en_nome_livro_up = ctk.CTkEntry(
            master=self.root_atualizar_livro,
            placeholder_text='Nome do Livro...',
            border_color="blue", 
            border_width=1,
            width=250
        )
        
        self.en_autor_livro_up  = ctk.CTkEntry(
            master=self.root_atualizar_livro,
            placeholder_text='Autor do Livro...',
            border_color="blue", 
            border_width=1,
            width=250
        )
        
        self.en_ano_livro_up  = ctk.CTkEntry(
            master=self.root_atualizar_livro,
            placeholder_text='Ano do Livro...',
            border_color="blue", 
            border_width=1,
            width=250
        )
        
        btn_salvar = ctk.CTkButton(
            master=self.root_atualizar_livro,
            text='salvar',
            fg_color='green',
            command=self.atualizar_livro
        )
        
        
        lb_title.place(x=70, y=5)
        
        self.en_id_livro_up.place(x=30, y=35)
        btn_procurar.place(x=140, y=35)
        self.en_nome_livro_up.place(x=30, y=70)
        self.en_autor_livro_up.place(x=30, y=105)
        self.en_ano_livro_up.place(x=30, y=140)
        btn_salvar.place(x=30, y=175)
        
        self.root_atualizar_livro.mainloop()
        
    def janela_deletar_livro(self):
        self.root_deletar_livro = ctk.CTk()
        self.root_deletar_livro.geometry('300x150')
        self.root_deletar_livro.resizable(False,False)
        self.root_deletar_livro.title('Deletar Livro')
        
        lb_title = ctk.CTkLabel(
            master=self.root_deletar_livro,
            text='DELETAR REGISTRO',
            bg_color=self.root_deletar_livro.cget('bg'),
            font=('Verdana', 15)
        )
        
        self.en_id_livro = ctk.CTkEntry(
            master=self.root_deletar_livro,
            placeholder_text='Id do Livro...',
            border_color="red", 
            border_width=1,
            width=350
        )
        
        btn_deletar = ctk.CTkButton(
            master=self.root_deletar_livro,
            text='Deletar',
            fg_color='red',
            command=self.deletar_livro
        )  
        
        lb_title.pack(pady=(0,15))
        self.en_id_livro.pack(anchor=W, padx=15)
        btn_deletar.pack(anchor=W, padx=15,pady=15)
        
        self.root_deletar_livro.mainloop()
        
    # Função para conectar ao banco de dados
    def conectar(self):
        return sqlite3.connect('livraria.db')
    
    # Função para inserir um novo livro
    def inserir_livro(self):
        #Pegando valores das entrys
        nome = self.en_nome_livro.get()
        autor = self.en_autor_livro.get()
        ano = self.en_ano_livro.get()
    
        if (nome != '') | (autor != '') | (ano != ''):
            conexao = self.conectar()
            cursor = conexao.cursor()
            comando_inserir = '''
            INSERT INTO livros (titulo, autor, ano_publicacao)
            VALUES (?, ?, ?)
            '''
            cursor.execute(comando_inserir, (nome, autor, ano))
            conexao.commit()
            conexao.close()
            messagebox.showinfo('Sucesso', f'O livro {nome} foi inserido com sucesso!')
            header = (['ID', 'Titulo', 'Autor', 'Ano'])
        
            self.tabela_livros = self.ler_livros()
            
            self.tabela_livros.insert(0,header)
            self.table.configure(values = self.tabela_livros)
        else:
            messagebox.showinfo('Campos vazios', 'Existem campos vazios obrigatórios')

    # Função para ler todos os livros
    def ler_livros(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM livros')
        livros = cursor.fetchall()
        conexao.close()
        return livros
    
    # Função para deletar um livro pelo ID
    def deletar_livro(self):
        
        livro_id = self.en_id_livro.get()
        if livro_id != '':
            try:
                conexao = self.conectar()
                cursor = conexao.cursor()
                comando_deletar = 'DELETE FROM livros WHERE id = ?'
                cursor.execute(comando_deletar, (livro_id,))
                conexao.commit()
                conexao.close()   
                messagebox.showinfo('Sucesso', f'O Livro de Id {livro_id} foi deletado com sucesso')
                header = (['ID', 'Titulo', 'Autor', 'Ano'])
        
                self.tabela_livros = self.ler_livros()
                
                self.tabela_livros.insert(0,header)
                self.table.configure(values = self.tabela_livros)
            except:
                messagebox.showinfo('Erro', 'Um ou mais erro ocorreu ao deletra o livro\nCertifique-se de que o livro exista no banco de dados')
        else:
            messagebox.showinfo('Campos vazios', 'Preencha o campo de Id para deletar')
    
    #Função para procurar registro
    def procurar_livro(self):
        self.lista_livros = self.ler_livros()
        id_livro = self.en_id_livro_up.get()
        
        if id_livro != '':
            id_livro = int(id_livro)
            for i in self.lista_livros:
                if int(id_livro) == i[0]:
                    self.en_nome_livro_up.delete(0, END)
                    self.en_autor_livro_up.delete(0, END)
                    self.en_ano_livro_up.delete(0, END)
                    
                    self.en_nome_livro_up.insert(0, i[1])
                    self.en_autor_livro_up.insert(0, i[2])
                    self.en_ano_livro_up.insert(0, i[3])
                    
            if self.en_autor_livro_up.get() == '':
                messagebox.showinfo('Nenhuma registro', f'Nenhuma informção foi encontrada com esse id {id_livro}')
            
    # Função para atualizar informações de um livro pelo ID
    def atualizar_livro(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        comando_atualizar = '''
        UPDATE livros
        SET titulo = ?, autor = ?, ano_publicacao = ?
        WHERE id = ?
        '''
        novo_titulo = self.en_nome_livro_up.get()
        novo_autor = self.en_autor_livro_up.get()
        novo_ano = self.en_ano_livro_up.get()
        livro_id = self.en_id_livro_up.get()
        
        cursor.execute(comando_atualizar, (novo_titulo, novo_autor, novo_ano, livro_id))
        conexao.commit()
        conexao.close()    
        messagebox.showinfo('Sucesso', f'O Livro de Id {livro_id} foi atualizado com sucesso')
        header = (['ID', 'Titulo', 'Autor', 'Ano'])

        self.tabela_livros = self.ler_livros()
        
        self.tabela_livros.insert(0,header)
        self.table.configure(values = self.tabela_livros)
                     
if __name__ == '__main__':
    Livraria()