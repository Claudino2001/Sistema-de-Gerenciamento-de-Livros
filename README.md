### Sistema de Gerenciamento de Livros

Este projeto é um sistema simples para gerenciar um catálogo de livros, permitindo adicionar, atualizar, remover e listar livros. O sistema é dividido em dois serviços principais: Auth Service e Books Service. Cada serviço é responsável por uma parte específica do sistema e se comunicam entre si usando JWT para autenticação e autorização.

## Estrutura do Projeto

- **auth_service/**: Serviço de autenticação e autorização.
- **books_service/**: Serviço de gerenciamento de livros.
- **data/**: Contém os bancos de dados SQLite.
- **docker-compose.yml**: Arquivo de configuração do Docker Compose.
- **.gitignore**: Arquivo para ignorar arquivos desnecessários no Git.
- **README.md**: Documentação do projeto.

## Bibliotecas e Frameworks Utilizados

### Flask
Flask é um microframework para Python baseado em Werkzeug e Jinja2. É simples, mas extensível, permitindo a construção de aplicações web robustas.

### Flask-JWT-Extended
Flask-JWT-Extended estende o Flask com suporte para JWT (JSON Web Tokens) para autenticação. Ele permite a criação de endpoints protegidos que requerem um JWT válido para acesso.

### SQLAlchemy
SQLAlchemy é um ORM (Object-Relational Mapping) para Python, que facilita a comunicação com bancos de dados relacionais. Ele permite definir os modelos de dados como classes Python, mapeando-as para tabelas no banco de dados.

### SQLite
SQLite é um banco de dados relacional leve, ideal para desenvolvimento e testes de pequenos projetos. Ele armazena os dados em um único arquivo, tornando-o fácil de usar e distribuir.

## Arquitetura do Sistema

### Auth Service
O Auth Service é responsável por gerenciar a autenticação e autorização dos usuários. Ele oferece endpoints para registro, login e validação de tokens JWT. Quando um usuário se registra ou faz login, um token JWT é gerado e deve ser usado para acessar os endpoints protegidos no Books Service.

### Books Service
O Books Service gerencia o catálogo de livros. Ele oferece endpoints para listar, adicionar, atualizar e remover livros. A maioria dos endpoints deste serviço está protegida por JWT, garantindo que apenas usuários autenticados possam realizar operações de escrita.

## Endpoints do Auth Service

- **POST /register**: Registra um novo usuário.
- **POST /login**: Autentica um usuário e retorna um token JWT.

### Exemplo de Uso

#### Registro de Usuário
```bash
curl -X POST http://localhost:5001/register -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'
```

#### Login de Usuário
```bash
curl -X POST http://localhost:5001/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'
```

## Endpoints do Books Service

- **GET /books**: Lista todos os livros.
- **POST /books**: Adiciona um novo livro (Requer JWT).
- **PUT /books/<id>**: Atualiza um livro existente (Requer JWT).
- **DELETE /books/<id>**: Remove um livro existente (Requer JWT).

### Exemplo de Uso

#### Listar Livros
```bash
curl -X GET http://localhost:5002/books
```

#### Adicionar Livro
```bash
curl -X POST http://localhost:5002/books -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"title": "Novo Livro", "author": "Autor Desconhecido"}'
```

#### Atualizar Livro
```bash
curl -X PUT http://localhost:5002/books/1 -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"title": "Livro Atualizado", "author": "Autor Famoso"}'
```
#### Remover Livro
```bash
curl -X DELETE http://localhost:5002/books/1 -H "Authorization: Bearer <TOKEN>"
```

### Como Executar
1. Clone o repositório
```bash
git clone https://github.com/Claudino2001/Sistema-de-Gerenciamento-de-Livros
cd Sistema-de-Gerenciamento-de-Livros
```
2. Execute os serviços
```bash
python auth_service/auth_service.py
python books_service/books_service.py
```
3. Acesse os serviços nos seguintes URLs:
   - Auth Service: http://localhost:5001
   - Books Service: http://localhost:5002

## Fluxo do Usuário

1. Registro/Login: O usuário acessa o Auth Service para se registrar ou fazer login. Após a autenticação, o usuário recebe um token JWT.

3. Acesso ao Books Service: O usuário usa o token JWT para acessar os endpoints protegidos no Books Service, onde pode listar, adicionar, atualizar e remover livros.

## Observações
- Certifique-se de que as portas 5001 e 5002 estejam livres no seu ambiente.

- Utilize ferramentas como Postman ou cURL para testar os endpoints facilmente.

- Mantenha o token JWT seguro, pois ele é essencial para a autenticação nos endpoints protegidos.
