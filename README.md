<h1 align="center"> Games API</h1>

<p align="center"><img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/></p>

:construction: Projeto em construção :construction:

Projeto em andamento, visando a prática com a linguagem Python e frameworks da linguagem.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python``
- ``Django``
- ``DRF``
- ``Paradigma de orientação a objetos``

## 🛠️ Como rodar o projeto

No terminal executar os comandos:


```bash
  pip install poetry
  poetry install
  python manage.py runserver
```


Após a execução a mesma estará rodando em: http://localhost:8000/

Para gerar um token é necessário acessar http://localhost:8000/admin com as credenciais:
```bash
user: admin
password: admin
```

Ou por padrão utilizar este:
```bash
4e8c65b8d9ef369c5337c0ee66c369a8dab6a278
```

Como pensei que esse processo seria feito em outra camada de aplicação deixei este modelo simples para testar recursos.


## API Reference

#### Get all games

```http
  GET http://localhost:8000//api/v2/games/
```
#### Get game

```http
  GET http://localhost:8000//api/v2/games/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of game to fetch |

#### Get all evaluations

```http
  GET http://127.0.0.1:8000/api/v2/evaluations/
```
#### Get evaluation

```http
  GET http://127.0.0.1:8000/api/v2/evaluations/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of evaluation to fetch |

#### Get all evaluations from a game

```http
  GET http://127.0.0.1:8000/api/v2/games/{id}/evaluations/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of game to fetch |

#### Get a specific evaluation from a game

```http
  GET http://127.0.0.1:8000/api/v2/games/{game_id}/evaluations/{evaluation_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `game_id`      | `int` | **Required**. Id of game to fetch |


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `evaluation_id`      | `int` | **Required**. Id of evaluation_id to fetch |

#### Recursos  POST,PUT, DELETE 
- É necessário estar logado via HTML ou utilizar Token de authorização.

### Throttling
- Foi implementado um limite de throttle rate de 10 requisições por segundo para usuários não autenticados e de 50 por segundo para usuários autenticados, somente para fins de imitar o uso de um Redis.


## A ser feito
- Implementar documentação automática.
- Implementar conexão a algum banco relacional com Docker.

## Authors

- [@nelassump](https://github.com/nelassump)
