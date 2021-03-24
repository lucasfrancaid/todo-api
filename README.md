[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="center">
  <p align="center">
    <h1 align="center">Todo API</h1>
    <p align="center">
			Construído para desenvolvedores front-end produtivos.<br/>
      <a href="https://drf-todoapi.herokuapp.com/api/docs/"><strong>Documentação com Swagger (DEMO)</strong></a>
    </p>
  </p>
</p>

<br/>

<p align="center">
  <a href="#-tecnologias">💻 Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%EF%B8%8F-sobre-o-projeto">🕵️ Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-iniciando-o-projeto">🚀 Iniciando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">🆙 Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contato">📬 Contate-me</a>
</p>


<br>


## 💻 Tecnologias
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Swagger](https://drf-yasg.readthedocs.io/en/stable/)
* [PostgreSQL](https://www.postgresql.org/)




<br>

## 🕵️ Sobre o projeto
Todo API, é um projeto criado com Django Rest Framework na intenção de aumentar a produtividade de desenvolvedores front-end. Dado que um desenvolvedor quer treinar suas habilidades ou experimentar uma nova tecnologia (no front-end), pode reaproveitar essa API focando apenas no necessário.

O que você pode construir utilizando essa API:
- <b>Criação de usuários</b> (Users Endpoint)
- <b>Autenticação de usuários via JWT</b> (Auth Endpoint)
- <b>Ler, criar, atualizar e deletar tarefas</b> (Task Endpoint)

<br>

## 🚀 Iniciando o projeto
Para iniciar vamos utilizar o Docker, então garanta que você tem instalado em sua máquina o Docker e o Docker Compose. Tudo certinho? Então execute na pasta raíz do projeto:
```bash
cp .env.sample .env
sudo docker-compose up
```

API disponível nas seguintes URL:
<br>
- <b>Documentação com Swagger:</b> http://localhost:8000/api/docs/
- <b>Documentação com Redoc:</b> http://localhost:8000/api/redoc/
- <b>Auth Endpoint [POST]:</b> http://localhost:8000/api/auth/token/
- <b>Users Endpoint [POST]:</b> http://localhost:8000/api/users/
- <b>Tasks Endpoint [GET, POST, PUT, DELETE]:</b> http://localhost:8000/api/tasks/
- <b>Painel de Admin:</b> http://localhost:8000/admin/
	```
	[ADMIN LOGIN]
	user: admin
	pass: 123
	```

Caso prefira, utilize as rotas pré-definidas com o Postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ab48013b4c23ceb3666c)

<br>

## Observações 
- O CORS já está configurado para aceitar as requisições do front-end
- Crie um usuário na rota Users, e o utilize na rota de autenticação
- Para criar tasks, é necessário que o usuário esteja autenticado, para isso é só enviar no <b>Header</b> de cada requisição:
	```js
	'Authorization': 'Bearer (token)'
	```
- Todos os dados serão persistidos na base de dados (PostgreSQL)
- Você pode gerenciar os dados do banco utilizando a interface de admin
- A API possui Rate Limit por IP, sendo o número de requisições para anônimos 100/dia e autenticados 5000/dia

<br>

## 🆙 Como contribuir

- Faça um fork desse repositório
- Crie uma branch com sua feature, para isso execute ```git checkout -b nome-feature```
- Desenvolva sua implementação, adicione seus commits e execute ```git push origin nome-feature```
- Abra um Pull Request explanando sua implementação

<br>

## 📬 Contato

<b>Lucas França</b> <br/>
https://lucasfrancaid.com.br/

<br>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lucasfrancaid
