from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Sua chave da API
API_KEY = "320d71c7bc6e6485b016638cc8a5b1ab"

# URL base para a API do TMDb
BASE_URL = "https://api.themoviedb.org/3"

# Função para buscar um filme pelo nome
async def search_movie_by_name(movie_name: str, page: int = 1):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}&page={page}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Levanta erro em caso de falha
        return response.json()

# Função para buscar detalhes de um filme com base no ID
async def get_movie_details(movie_id: int):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Levanta erro em caso de falha
        return response.json()

# Função para obter filmes mais bem avaliados com paginação
async def get_top_rated_movies(page: int = 1):
    url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&page={page}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Função para obter filmes populares com paginação
async def get_popular_movies(page: int = 1):
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&page={page}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Função para obter filmes em cartaz com paginação
async def get_now_playing_movies(page: int = 1):
    url = f"{BASE_URL}/movie/now_playing?api_key={API_KEY}&page={page}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Função para obter próximos lançamentos com paginação
async def get_upcoming_movies(page: int = 1):
    url = f"{BASE_URL}/movie/upcoming?api_key={API_KEY}&page={page}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Função para obter gêneros de filmes
async def get_movie_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

# Endpoint para pesquisar filmes e obter informações sobre um filme específico
@app.get("/movie_info/{movie_name}")
async def movie_info(movie_name: str, page: int = 1):
    # Buscar filme pelo nome
    search_result = await search_movie_by_name(movie_name, page)
    
    # Verificar se filmes foram encontrados
    if not search_result["results"]:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    # Pegar o primeiro filme da lista de resultados
    movie = search_result["results"][0]
    movie_id = movie["id"]
    
    # Obter detalhes do filme
    movie_details = await get_movie_details(movie_id)
    
    # Retornar detalhes do filme
    return movie_details

# Endpoint para filmes mais bem avaliados
@app.get("/top_rated_movies")
async def top_rated_movies(page: int = 1):
    top_rated = await get_top_rated_movies(page)
    total_results = top_rated["total_results"]  # Total de resultados
    return {
        "total_results": total_results,
        "results": top_rated["results"]
    }

# Endpoint para filmes populares
@app.get("/popular_movies")
async def popular_movies(page: int = 1):
    popular = await get_popular_movies(page)
    total_results = popular["total_results"]  # Total de resultados
    return {
        "total_results": total_results,
        "results": popular["results"]
    }

# Endpoint para filmes em cartaz
@app.get("/now_playing_movies")
async def now_playing_movies(page: int = 1):
    now_playing = await get_now_playing_movies(page)
    total_results = now_playing["total_results"]  # Total de resultados
    return {
        "total_results": total_results,
        "results": now_playing["results"]
    }

# Endpoint para próximos lançamentos
@app.get("/upcoming_movies")
async def upcoming_movies(page: int = 1):
    upcoming = await get_upcoming_movies(page)
    total_results = upcoming["total_results"]  # Total de resultados
    return {
        "total_results": total_results,
        "results": upcoming["results"]
    }

# Endpoint para gêneros de filmes
@app.get("/movie_genres")
async def movie_genres():
    genres = await get_movie_genres()
    return genres["genres"]

# Endpoint para retornar KPIs sobre filmes (melhores avaliados, populares, etc)
@app.get("/movie_kpis")
async def movie_kpis(page: int = 1):
    # Obter filmes mais bem avaliados
    top_rated = await get_top_rated_movies(page)
    
    # Obter filmes mais populares
    popular = await get_popular_movies(page)

    # Obter filmes em cartaz
    now_playing = await get_now_playing_movies(page)

    # Obter próximos lançamentos
    upcoming = await get_upcoming_movies(page)

    # Obter gêneros de filmes
    genres = await get_movie_genres()

    return {
        "top_rated": {
            "total_results": top_rated["total_results"],
            "results": top_rated["results"]
        },
        "popular": {
            "total_results": popular["total_results"],
            "results": popular["results"]
        },
        "now_playing": {
            "total_results": now_playing["total_results"],
            "results": now_playing["results"]
        },
        "upcoming": {
            "total_results": upcoming["total_results"],
            "results": upcoming["results"]
        },
        "genres": genres["genres"]
    }
