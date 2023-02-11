# Тестовое задание
___

#### Сайт доступен для тестирования - http://185.112.102.55:8000/


```bash
git clone git@github.com:contiinue/shop.git && cd shop
```

#### Необходимо выполнить команду + вставить свои ключи от STRIPE
```shell
mv .env.example .env
```

#### Запускаем проект, админка создаться автоматически данные будут вязты с .env файла
```
docker compose up -d --build 
```