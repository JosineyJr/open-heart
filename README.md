# Passo a Passo para Executar o Projeto

Este guia descreve como configurar e executar o projeto localmente.

## Pré-requisitos

1. **Python**: Certifique-se de ter o Python 3.9 ou superior instalado. [Baixe aqui](https://www.python.org/downloads/).
2. **Pip**: O gerenciador de pacotes do Python, geralmente incluído na instalação do Python.

## Instruções

### 1. Clone o Repositório

Use o seguinte comando para clonar o repositório do projeto:

```bash
https://github.com/JosineyJr/open-heart-api
```

Navegue até a pasta do projeto:

```bash
cd open-heart-api
```

### 2. Ative o Ambiente Virtual

Como o projeto já possui um ambiente virtual configurado, basta ativá-lo:

- **Linux/MacOS**:

  ```bash
  source .venv/bin/activate
  ```

- **Windows**:
  
  ```bash
  .venv\Scripts\activate
  ```

### 3. Instale as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
### 5. Execute o Servidor

Inicie o servidor FastAPI usando o Uvicorn:

```bash
uvicorn main:app --reload
```

O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 6. Teste os Endpoints

- Acesse a documentação interativa do FastAPI em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- Utilize ferramentas como **Postman** ou **curl** para testar os endpoints manualmente.

### 7. Encerrando o Ambiente Virtual

Quando terminar, desative o ambiente virtual com:

```bash
deactivate
```
