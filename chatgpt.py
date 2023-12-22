import requests
import json


def gerarTexto(livro):
    try:
        key_chatgpt = "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"
        headers = {"Authorization": f"Bearer {key_chatgpt}", "Content-Type": "application/json"}
        link = "https://api.openai.com/v1/chat/completions"
        modelo = "gpt-3.5-turbo"
        body = {
            "model": modelo,
            "messages": [{"role": "user", "content": f"me resuma {livro} com no máximo 400 caracteres, caso não conheça o livro, responda com Livro Desconhecido"}]
        }
        body = json.dumps(body)
        requisicao = requests.post(link, headers=headers, data=body)
        resposta = requisicao.json()
        sinopse = resposta["choices"][0]["message"]["content"]
        return sinopse
    except:
        print("Chave API Esta fora no momento!")
        return "Chave API Esta fora no momento!"
    





