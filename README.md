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




## Authors

- [@nelassump](https://github.com/nelassump)
