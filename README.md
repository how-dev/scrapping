## Introdução

O projeto consiste numa aplicação feita para ‘Web’ Scraping.

O foco do sistema foi usar da Arquitetura Limpa para possibilitar modularizações. Por exemplo:

Se eu quiser trocar de Flask para Django, ou para Chalice, depois voltar para Flask... 
As regras, interações e apresentações de dados do sistema não preciarão ser reescritos.
As únicas coisas que precisarão ser trabalhas são: criar uma classe herdando de `BasicResponse`
e sobrescrever os métodos de resposta, e recriar o arquivo que disponibiliza as rotas. Até mesmo
o conteúdo das funções atuais serão reaproveitadas, com mínimos ajustes.

## Instalação

> 💡 Ter instalado o make no terminal ajudará:

```cmd
sudo apt install make
```

### Buildar o projeto

```cmd
make build
```

ou:

```cmd
export DOCKER_BUILDKIT=1;docker-compose build
```

### Rodar o projeto

```cmd
make run
```

ou:

```cmd
docker-compose up
```

## API

### Endpoints

Buscar dados: `/search?keyword=<pesquisa>`

Este endpoint traz os 5 primeiros links da sua pesquisa.

### Exemplo

```cmd
curl -X GET "http://localhost:5000/search?keyword=test123"
```

### Retorno:

```json
{
  "links": [
    "https://test123.com.br/",
    "https://test123.com.br/",
    "https://br.linkedin.com/company/test123br",
    "https://www.instagram.com/test123br/",
    "https://www.metaventures.com.br/startups/test123-plataforma-de-automacao-e-inteligencia-de-dados/"
  ]
}
```

status: 200

### Exemplo

```cmd
curl -X GET "http://localhost:5000/search"
```

### Retorno:

```json
{
  "error": "Query parameter not found"
}
```

status: 400

Métricas: `/metrics`

Este endpoint traz as métricas das requisições feitas no endpoint `/search`.

### Exemplo

```cmd
curl -X GET "http://localhost:5000/metrics"
```

### Retorno:

```json
{
  "average_response_time": 1.1460609436035156,
  "search_queries": [
    "test123"
  ]
}
```

status: 200


> Caso não tenha sido feita nenhuma requisição, retornada algo como: 
```json
{
  "average_response_time": 0,
  "search_queries": []
}
```
