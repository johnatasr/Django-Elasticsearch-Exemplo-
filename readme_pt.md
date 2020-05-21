# Django Elasticsearch  ( Em desenvolvimento )

Projeto testando Elasticsearch com Django

## Requisitos

* Docker
* Docker-compose
* Python 3.7

## Começando

Migrando de arquivos JSON na pasta fixtures e rodando o projeto:

### Via Docker

1. `docker-compose build`
2. `docker-compose run --service-ports --rm django python manage.py bootstrap`
3. `docker-compose up`

### Via Docker/ Servidor Local (Opção de DEBUG)

1. `docker pull docker.elastic.co/elasticsearch/elasticsearch:6.8.9`
2. `docker run --name django_elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.8.9`
3. `docker pull postgres:10`
4. `docker run --name django_postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=django_elastic -d -p 5432:5432 postgres:10`
5. `python manage.py bootstrap`
6. `python manage.py runserver`

Rodando o elastic e o postgres é possivel debugar e implementar novos modelos e indices.


Teste o Elasticsearch com o shell:
1. `docker-compose up`
2. `docker-compose exec django python manage.py shell`

## Exemplos de uso

```
cars = CarDocument.search().query('match', color='black')
for car in cars:
    print(car.color)

cars = CarDocument.search().extra(size=0)
cars.aggs.bucket('points_count', 'terms', field='points')
result = cars.execute()
for point in result.aggregations.points_count:
    print(point)
```

- http://localhost:8000/cars/?search=description|is - procura uma descricao em todos os carros
- http://localhost:8000/cars/?id__gte=7 - procura um carro com o ID igual a 7 ou maior
- http://localhost:8000/cars/suggest/?name_suggest__completion=cor - procura sugestões para frases


