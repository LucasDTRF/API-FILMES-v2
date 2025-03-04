Documentação dos Endpoints da API
1. Pesquisar Filme pelo Nome
Endpoint: /movie_info/{movie_name}

Método: GET

Descrição: Pesquisa um filme pelo nome e retorna os detalhes completos do filme.

Parâmetros:

movie_name: Nome do filme a ser pesquisado (obrigatório).
page: Número da página para paginar os resultados (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: Detalhes do filme.
json
Copiar
Editar
{
    "adult": false,
    "backdrop_path": "/path/to/backdrop.jpg",
    "id": 12345,
    "original_title": "Movie Title",
    "overview": "Movie overview",
    "release_date": "2025-01-01",
    "runtime": 120,
    "genres": [ ... ],
    ...
}
2. Filmes Mais Bem Avaliados
Endpoint: /top_rated_movies

Método: GET

Descrição: Retorna a lista de filmes mais bem avaliados.

Parâmetros:

page: Número da página (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: Lista de filmes mais bem avaliados e total de resultados.
json
Copiar
Editar
{
    "total_results": 1000,
    "results": [
        {
            "id": 12345,
            "title": "Top Rated Movie",
            "overview": "Movie overview",
            "rating": 8.5,
            ...
        }
    ]
}
3. Filmes Populares
Endpoint: /popular_movies

Método: GET

Descrição: Retorna a lista de filmes mais populares.

Parâmetros:

page: Número da página (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: Lista de filmes populares e total de resultados.
json
Copiar
Editar
{
    "total_results": 500,
    "results": [
        {
            "id": 54321,
            "title": "Popular Movie",
            "overview": "Movie overview",
            "rating": 7.5,
            ...
        }
    ]
}
4. Filmes em Cartaz
Endpoint: /now_playing_movies

Método: GET

Descrição: Retorna a lista de filmes em cartaz nos cinemas.

Parâmetros:

page: Número da página (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: Lista de filmes em cartaz e total de resultados.
json
Copiar
Editar
{
    "total_results": 300,
    "results": [
        {
            "id": 98765,
            "title": "Now Playing Movie",
            "overview": "Movie overview",
            "rating": 6.8,
            ...
        }
    ]
}
5. Próximos Lançamentos
Endpoint: /upcoming_movies

Método: GET

Descrição: Retorna a lista de filmes que serão lançados em breve.

Parâmetros:

page: Número da página (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: Lista de próximos lançamentos e total de resultados.
json
Copiar
Editar
{
    "total_results": 150,
    "results": [
        {
            "id": 11223,
            "title": "Upcoming Movie",
            "overview": "Movie overview",
            "rating": 9.0,
            ...
        }
    ]
}
6. Gêneros de Filmes
Endpoint: /movie_genres
Método: GET
Descrição: Retorna a lista de gêneros de filmes disponíveis na API.
Parâmetros: Nenhum.
Resposta (sucesso):
Código HTTP: 200
Corpo: Lista de gêneros.
json
Copiar
Editar
{
    "genres": [
        {
            "id": 28,
            "name": "Action"
        },
        {
            "id": 35,
            "name": "Comedy"
        },
        ...
    ]
}
7. KPIs sobre Filmes
Endpoint: /movie_kpis

Método: GET

Descrição: Retorna KPIs (indicadores chave de desempenho) sobre filmes, como os mais bem avaliados, populares, em cartaz, próximos lançamentos e gêneros.

Parâmetros:

page: Número da página (opcional, padrão é 1).
Resposta (sucesso):

Código HTTP: 200
Corpo: KPIs de filmes com total de resultados e lista de filmes para cada categoria.
json
Copiar
Editar
{
    "top_rated": {
        "total_results": 1000,
        "results": [
            {
                "id": 12345,
                "title": "Top Rated Movie",
                "overview": "Movie overview",
                "rating": 8.5,
                ...
            }
        ]
    },
    "popular": {
        "total_results": 500,
        "results": [
            {
                "id": 54321,
                "title": "Popular Movie",
                "overview": "Movie overview",
                "rating": 7.5,
                ...
            }
        ]
    },
    "now_playing": {
        "total_results": 300,
        "results": [
            {
                "id": 98765,
                "title": "Now Playing Movie",
                "overview": "Movie overview",
                "rating": 6.8,
                ...
            }
        ]
    },
    "upcoming": {
        "total_results": 150,
        "results": [
            {
                "id": 11223,
                "title": "Upcoming Movie",
                "overview": "Movie overview",
                "rating": 9.0,
                ...
            }
        ]
    },
    "genres": [
        {
            "id": 28,
            "name": "Action"
        },
        {
            "id": 35,
            "name": "Comedy"
        },
        ...
    ]
}
Considerações Adicionais
Paginação:

A API do TMDb retorna total_results para indicar o número total de filmes, e total_pages para indicar o número total de páginas.
Cada resposta inclui um campo page que indica a página atual da consulta.
Parâmetros de Pesquisa:

Todos os endpoints que lidam com listas de filmes (como os mais bem avaliados, populares, etc.) aceitam o parâmetro page para permitir a navegação entre as páginas de resultados.
Respostas de Erro:

Caso um filme não seja encontrado ou haja algum erro na solicitação, a API retornará um erro HTTP adequado (por exemplo, 404 Not Found ou 500 Internal Server Error).
Como Visualizar a Documentação Interativa:
O FastAPI automaticamente gera uma interface de documentação interativa usando o Swagger. Para visualizar essa documentação, basta rodar sua aplicação e acessar:

URL da Documentação: http://localhost:8000/docs
Aqui você pode testar os endpoints diretamente e ver os exemplos de resposta. Além disso, o FastAPI também gera uma documentação alternativa em formato de ReST (ReStructuredText), acessível em:

URL Alternativa da Documentação: http://localhost:8000/redoc