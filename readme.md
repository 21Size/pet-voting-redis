## Тестовое задание: **Голосование в Redis**

> Docker: Для запуска в контенейре ```docker compose up -d```. 

#### Endpoints

Создание голосования:
```sh
POST http://localhost:8080/api/voting/
Accept: application/json
Content-Type: application/json

{
  "title": "test",
  "options": [
    {"name": "o1"},
    {"name": "o2"},
    {"name": "o3"}
  ]
}

Return: {
  "voting_id": "993706f9-f2df-4299-bdfb-ed9a8069a8d9" # voting_id
}
```

Получение голосования 
```sh
GET http://localhost:8080/api/voting/{voting_id}
Accept: application/json

Return: {
  "data": [
    {
      "name": "o1",
      "stat": 3,
      "percent": 37.5
    },
    {
      "name": "o2",
      "stat": 5,
      "percent": 62.5
    },
    {
      "name": "o3",
      "stat": 0,
      "percent": 0.0
    }
  ]
}
```

Голосование
```sh
GET http://localhost:8080/api/voting/{voting_id}
Accept: application/json

Return: null
```

