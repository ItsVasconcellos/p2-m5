# p2-m5

## Como executar?

Para rodar a aplicação, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório em seu ambiente local.
3. Crie um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos no diretório raiz do projeto:

    ```bash
    cd Flask-Htmx/
    python -m venv venv
    ```

4. Ative o ambiente virtual. No Windows, execute o seguinte comando:

    ```bash
    venv\Scripts\activate
    ```

    No macOS, Linux e no Bash, execute o seguinte comando:

    ```bash
    source venv/bin/activate
    ```

5. Instale as dependências do projeto. Execute o seguinte comando:

    ```bash
    pip install -r requirements.txt
    ```

6. Inicie a aplicação. Execute o seguinte comando:

    ```bash
    flask run 
    ```

7. Acesse a aplicação no seu navegador através do seguinte endereço: `http://localhost:5000`.

## Estrutura de pastas
```bash
projeto-pcb/
├── templates/
│   ├── dash.html    
│   └── info.html      
├── .gitignore
├── app.py
├── db.json
├── LICENSE
└── readme.md
```

## Rotas Disponíveis

```python
[Get]/Pong
```
Retorna Pong em formato JSON


```python
[Post]/Echo
```
Retorna em formato JSON, o que o usuário enviou no JSON na chave "Dados"


```python
[Get]/dash
```
Acessa o template html com o botão que traz as rotas

```python
[Get]/info
```
Acessa o template html com uma tabela, contendo todas as informações do banco.

