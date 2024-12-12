# **_Genetic tests_**
RESTful API, ĸоторое позволяет сохранять данные генетичесĸих тестов животных, а таĸже выполнять подсчет агрегированной статистиĸи. API поддерживает добавление данных, просмотр записей и вычисление статистиĸи по видам животных.                                                          

Стек: python, Django, DRF, PostgreSQL, Docker-compose.                                                                          
                                           
**Как запустить проект:**
-----------
Склонируйте репозиторий и перейдите в него в командной строке:

```
https://github.com/TatianaSharova/Genetic-tests.git
```
**_Запуск через Docker-compose:_**                                                 

Запустите проект:          
```
docker compose up --build
```
                                                   
**Примеры запросов:**
-----------
1. Добавление теста:
```
POST http://127.0.0.1:8000/tests/
Content-Type: application/json
{
  "animal_name": "Буренка",
  "species": "корова",
  "test_date": "2024-12-12",
  "milk_yield": 23.5,
  "health_status": "good"
}

```
Ответ:
```
{
  "message": "Данные успешно добавлены.",
  "id": 4
}
```
2. Просмотр всех тестов:
                                                         
```
GET http://127.0.0.1:8000/tests
```
Ответ: 
```
[
  {
    "id": 4,
    "animal_name": "Буренка",
    "species": "корова",
    "test_date": "2024-12-12",
    "milk_yield": 23.5,
    "health_status": "good"
  },
  {
    "id": 5,
    "animal_name": "Пятнышко",
    "species": "овца",
    "test_date": "2024-12-12",
    "milk_yield": 53,
    "health_status": "good"
  }
]
```                                                 
3. Просмотр теста по id:
```
GET http://127.0.0.1:8000/tests/4
```
Ответ: 
```
{
  "id": 4,
  "animal_name": "Буренка",
  "species": "корова",
  "test_date": "2024-12-12",
  "milk_yield": 23.5,
  "health_status": "good"
}

```
4.Просмотр списка тестов с фильтрацией по виду животного.  /tests?species=ĸорова    
```
GET http://127.0.0.1:8000/tests?species=корова
``` 
Ответ: 
```
[
  {
    "id": 4,
    "animal_name": "Буренка",
    "species": "корова",
    "test_date": "2024-12-12",
    "milk_yield": 23.5,
    "health_status": "good"
  },
]

```
5. Вывод статистики по видам животных:
```
GET http://127.0.0.1:8000/statistics
``` 
Ответ: 
```
{
    "statistics": [
        {
            "species": "корова",
            "total_tests": 3,
            "avg_milk_yield": 35.0,
            "max_milk_yield": 76.5,
            "good_health_percentage": 66.0
        },
        {
            "species": "овца",
            "total_tests": 1,
            "avg_milk_yield": 53.0,
            "max_milk_yield": 53.0,
            "good_health_percentage": 100.0
        }
    ]
}

```

**Документация:**                                      
Документацию к API после запуска проекта можно посмотреть по адресам:
```
http://127.0.0.1:8000/schema/redoc/
```
```
http://127.0.0.1:8000/schema/swagger-ui/
```

### Автор
[Татьяна Шарова](https://github.com/TatianaSharova)