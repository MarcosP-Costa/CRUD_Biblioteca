import PySimpleGUI as sg
import sqlite3
import webbrowser
import chatgpt


def abrir_link():
    # URL que você deseja abrir
    url = "https://github.com/MarcosP-Costa"

    # Abrir o navegador padrão com a URL fornecida
    webbrowser.open(url)

rows = []

def gerarSinopse(titulo_livro):
    if titulo_livro == "":
        return("Selecione um livro antes!")
    else:
        return(chatgpt.gerarTexto(titulo_livro))

def janela_menu():
    sg.theme('Dark')
    toprow = ['ID', 'Titulo', "Autor", "Ano de Publicação"]
    me_de_imagens = sg.Image(filename="./img/LIVRARIABanner.png")
    global rows 
    rows = listar_livros(ler_livros())
    layout = [
        [sg.Column([[me_de_imagens]], justification='center')],
        [sg.Column([[sg.Button('Adicionar'), sg.Button('Atualizar ou Deletar', key='Atualizar')]], justification='center')],
        
        [sg.Table(values=rows, headings=toprow,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='center', key='-TABLE-',
            selected_row_colors='red on yellow',
            enable_events=True,
            expand_x=True,
            expand_y=True,
            enable_click_events=True)],
        [sg.Column([[sg.Button('Gerar Sinopse com ChatGPT', key="Gerar Sinopse"), sg.Button('Repositório do Projeto no GitHub', key="abrir_github")],[ sg.Text("Clique no livro e depois clique no botão de gerar a sinopse!", key="sinopse_gpt", expand_x=True, expand_y=True, size=(80, 10))]], justification='center')]       
        
    ]
    
    return sg.Window('Livraria da Python Brasil', layout=layout, finalize=True, size=(800, 500), resizable=True)

def janela_create():
    sg.theme('DarkAmber')
    layout = [
        [[sg.Text('Nome:*')], [sg.Input(key="nome", tooltip="Nome do Livro")]],
        [[sg.Text('Autor:*')], [sg.Input(key="autor", tooltip="Nome do Autor")]],
        [[sg.Text('Ano:*')], [sg.Input(key="ano", tooltip="Ano da Publicação")]],
        [sg.Column([[sg.Button("Salvar")]], justification='center')]
    ]
    return sg.Window('Adicionar Livros', layout=layout, finalize=True, modal=True)

def janela_delete():
    #sg.theme('') Pesquisar tema q combina
    layout = [
        [[sg.Input(key="id_del", tooltip="ID do Livro")],[sg.Column([[sg.Button("Pesquisar Livro pelo ID", key="buscar")]], justification='center')]],
        [[sg.Text('Nome:*')], [sg.Input(key="nome_del", tooltip="Nome do Livro")]],
        [[sg.Text('Autor:*')], [sg.Input(key="autor_del", tooltip="Nome do Autor")]],
        [[sg.Text('Ano:*')], [sg.Input(key="ano_del", tooltip="Ano de Publicação")]],
        [sg.Column([[sg.Button("Deletar Livro", key="salvar_del")]], justification='center')]
    ]
    return sg.Window('Deletar Livros', layout=layout, finalize=True, modal=True)

def janela_att():
    #sg.theme('') Pesquisar tema q combina
    layout = [
        [[sg.Input(key="id_att", tooltip="ID do Livro")],[sg.Column([[sg.Button("Pesquisar Livro pelo ID", key="buscar")]], justification='center')]],
        [[sg.Text('Nome:*')], [sg.Input(key="nome_att", tooltip="Nome do Livro")]],
        [[sg.Text('Autor:*')], [sg.Input(key="autor_att", tooltip="Nome do Autor")]],
        [[sg.Text('Ano:*')], [sg.Input(key="ano_att", tooltip="Ano de Publicação")]],
        [sg.Column([[sg.Button("Salvar Alterações", key="salvar_att"), sg.Button("Deletar", key="salvar_del")]], justification='center')]
    ]
    return sg.Window('Atualizar Livros', layout=layout, finalize=True, modal=True)

def sinopse():
    #sg.theme('') Pesquisar tema q combina
    layout = [
        [sg.Column([[sg.Text("Gerando sua Sinopse, por favor aguarde...")], [sg.Button("OK", key="ok")]], justification='center')],
        [sg.Text("", key="msg_confirmacao")]
    ]
    return sg.Window('Gerar Sinopse de Livros', layout=layout, finalize=True, modal=True)

def listar_livros(livrosParam):

    livros = []
    for l in livrosParam:
        aux = []
        aux.append(l[0])
        aux.append(l[1])
        aux.append(l[2])
        aux.append(l[3])
        livros.append(aux)
    return livros

def janela_inf(text, titulo):
    layout = [
        [sg.Text(f"{text}", key='inf')],
    ]
    return sg.Window(f"{titulo}", layout=layout, finalize=True, modal=True)
    
# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('livraria.db')

# Função para inserir um novo livro
def inserir_livro(titulo, autor, ano_publicacao):
    
    
        conexao = conectar()
        cursor = conexao.cursor()
        comando_inserir = '''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
        '''
        cursor.execute(comando_inserir, (titulo, autor, ano_publicacao))
        conexao.commit()
        conexao.close()


# Função para ler todos os livros
def ler_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conexao.close()
    return livros

def pesquisar_livros(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conexao.close()
    for l in livros:
        if(l[0] == id):
            return l

    return ("", "", "")
    

# Função para deletar um livro pelo ID
def deletar_livro(livro_id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando_deletar = 'DELETE FROM livros WHERE id = ?'
    cursor.execute(comando_deletar, (livro_id,))
    conexao.commit()
    conexao.close()

# Função para atualizar informações de um livro pelo ID
def atualizar_livro(livro_id, novo_titulo, novo_autor, novo_ano):
    conexao = conectar()
    cursor = conexao.cursor()
    comando_atualizar = '''
    UPDATE livros
    SET titulo = ?, autor = ?, ano_publicacao = ?
    WHERE id = ?
    '''
    cursor.execute(comando_atualizar, (novo_titulo, novo_autor, novo_ano, livro_id))
    conexao.commit()
    conexao.close()    
    
#Janela Criada
janela1, janela2, janela3 = janela_menu(), None, None
titulo_livro = ""
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if event == sg.WIN_CLOSED and window == janela1:
        break
    if event == sg.WIN_CLOSED and window != janela1:
        window.close()
    if event == sg.WIN_CLOSED and window != janela2:
        janela1 = janela_menu()
    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Adicionar':
        janela2 = janela_create()

    if window == janela1 and event == 'Atualizar':
        janela2 = janela_att()
    if event == 'buscar' and values['id_att'] != '':
        try: 
            livros = pesquisar_livros(int(values['id_att']))
            window['nome_att'].update(livros[1])
            window['autor_att'].update(livros[2])
            window['ano_att'].update(livros[3])
        except ValueError:
            janela3 = janela_inf(text="Você colocou um caractere errado", titulo="erro!")
        except IndexError:
            janela3 = janela_inf(text="Você colocou um ID inexistente!", titulo="erro!")


        except:
            janela3 = janela_inf(text="Você colocou um valor errado!", titulo="erro!")
    if event == 'salvar_att' and values['id_att'] != '':
        atualizar_livro(livro_id=values['id_att'], novo_titulo=values['nome_att'], novo_autor=values['autor_att'], novo_ano=values['ano_att'])
        janela3 = janela_inf("Livro Atualzado com Sucesso!", "Sucesso")
    if event == 'salvar_del' and values['id_att'] != '':
        #mudar para deletar
        deletar_livro(livro_id=values['id_att'])
        janela3 = janela_inf("Livro Deletado com Sucesso!", "Sucesso")
        

    if window == janela1 and event == 'Gerar Sinopse':
        window['sinopse_gpt'].update(gerarSinopse(titulo_livro=titulo_livro))
    if window == janela2 and event == 'Salvar':
        nome = values['nome']
        autor = values['autor']
        ano = values['ano']
        if(nome == '') or (autor == '') or (ano == ''):
            janela3 = janela_inf("Faltou Informações!", "Erro!")
        else:
            inserir_livro(titulo=nome,autor=autor,ano_publicacao=ano)
            janela3 = janela_inf("Livro Adicionado com Sucesso!", "Sucesso")
            
    if window == janela1 and event == '-TABLE-':
    # Verifica se há uma célula clicada
        index = values[event][0]
        titulo_livro = rows[index][1]
        
    if window == janela1 and event == 'abrir_github':
        abrir_link()
        

