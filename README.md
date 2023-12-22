## Projeto CRUD Livraria

Desafio oferecido pela [Python Brasil](https://www.instagram.com/python_brasil/), este projeto consiste em um CRUD (Create - Read - Update - Delete) de um sistema de livraria. Como desafio adicional, integrei a aplicação com o ChatGPT, permitindo que ele gere uma sinopse sobre o livro cadastrado.

### Autores

- **Código**: [Marcos Paulo](https://github.com/MarcosP-Costa)
- **Desafio**: [Python Brasil](https://www.instagram.com/python_brasil/)

### Informações Adicionais

Para gerar a sinopse com o ChatGPT, siga estes passos:

- Gerar uma chave de acesso à API da OpenAI [aqui](https://platform.openai.com/api-keys) (é necessário ter uma conta).
![image](https://github.com/MarcosP-Costa/CRUD_Biblioteca/assets/44422455/ec03a1b7-3d31-487c-ae4c-66f45879088e)
- No arquivo `pass_w.py`, substitua a variável `key_chatgpt` pela sua chave.
- Para instalar todos os requisitos, utilize o comando:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

### Código 1: Interface com PySimpleGUI
O código usa a biblioteca PySimpleGUI para criar uma interface gráfica amigável para o CRUD da livraria. Algumas funcionalidades notáveis incluem:

- **Adicionar Livro:** Permite adicionar novos livros com informações como nome, autor e ano de publicação.
- **Atualizar ou Deletar Livro:** Permite a atualização e exclusão de livros existentes com base no ID.
- **Gerar Sinopse com ChatGPT:** Gera sinopses para os livros usando a API do ChatGPT.
- **Repositório do Projeto no GitHub:** Abre o repositório do projeto no GitHub.

### Código 2: Integração com ChatGPT
Este código usa a API do ChatGPT para gerar sinopses de livros. Alguns pontos-chave:

- Utiliza a chave da API da OpenAI (substitua-a no arquivo `pass_w.py`).
- Envia uma solicitação para a API com o título do livro para obter uma sinopse.
- Manipula a resposta JSON da API para extrair a sinopse.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias ou relatar problemas por meio de issues ou pull requests. Lembre-se de seguir as instruções para configurar a chave da API do ChatGPT e os requisitos do projeto.

