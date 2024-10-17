# Projeto: Agente SQL com LangChain

Este projeto é um exemplo de como usar LangChain para criar um agente SQL que se conecta a um banco de dados SQLite e responde a perguntas usando o modelo OpenAI.

## Pré-requisitos

- Python 3.8 ou superior
- Chave de API da OpenAI
- Biblioteca SQLite

## Instalação

1. Clone este repositório.
2. Instale as dependências do projeto:

   ```sh
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

- `sql_agent.py`: Script principal que cria e executa o agente SQL.
- `requirements.txt`: Arquivo com as dependências necessárias para executar o projeto.
- `.gitignore`: Arquivo que especifica arquivos e pastas a serem ignorados pelo Git, incluindo `key.txt`.
- `key.txt`: Arquivo onde você pode salvar a sua chave de API da OpenAI (opcional, mas é recomendável não versionar este arquivo).

## Uso

1. Execute o script Python:

   ```sh
   python sql_agent.py
   ```

2. Quando solicitado, insira sua chave de API da OpenAI.

3. O agente responderá a perguntas sobre o banco de dados SQLite "Chinook.db".

## Consultas de Exemplo

O script realiza as seguintes consultas SQL:

1. **Qual o artista que possui mais álbuns?**
2. **Quantos álbuns começam com a letra 'T'?**
3. **Qual o total de músicas do Led Zeppelin?**

## Banco de Dados

- O banco de dados utilizado é o `Chinook.db`, que é um banco de dados de exemplo popular para práticas com SQL.

## Notas

- **Segurança**: Nunca compartilhe sua chave de API públicamente.
- **Personalização**: Você pode modificar o script para utilizar outros bancos de dados ou realizar diferentes consultas.

## Autor

Felipe Bossolani

## Licença

Este projeto está sob a licença MIT.

