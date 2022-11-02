# Django_Rest_Project

SQL script для создания схемы БД:

CREATE TABLE "Rest_project_registerview" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "phone" varchar(12) NOT NULL, 
  "login" varchar(24) NOT NULL, 
  "password" varchar(24) NOT NULL, 
  "name" varchar(18) NOT NULL, 
  "birth" date NOT NULL, 
  "tg" varchar(24) NOT NULL, 
  "email" varchar(254) NOT NULL
);

База данных: DBeaver 22.2.0

Проект запускаеться командами:
- venv\scripts\activate
- cd project
- python manage.py runserver
