<h1>Pf Python</h1>

<h3><strong>Proposta:</strong></h3>
<p>........</p>
<hr noshade />

<h2>[201] Criar usuários </h2>
<h3>POST - /users/</h3>

<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 150 chars.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email e máximo 127 chars.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 30 chars.</li>
    <li><strong>address: </strong>Entrada obrigatória do tipo dicionario.</li>
    <li><strong>is_superuser: </strong>Entrada opcional do tipo boolean com default false.</li>
    <li><strong>is_seller: </strong>Entrada opcional do tipo boolean com default false.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
    "id": "146c8c8b-fef1-4487-8641-cff3ef748c7a",
    "username": "Mariano Lopes",
    "email": "ml123@gmail.com",    
    "address": {
        "street": "Floriano arroba",
        "distric": "Jardim das flores",
        "zipCode": 12341231,
        "state": "Ba",
        "city": "Jacobina",
        "number": 12,
    },
    "is_seller": False,
    "is_superuser": False,
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto/vazio:</p>
<pre>
{
  "username": [
    "This field is required."
  ],
  "email": [
    "This field is required."
  ],
  "password": [
    "This field is required."
  ],
  "address": [
    "This field is required."
  ]
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para email/username já existente:</p>
<pre>
{
  "email": [
    "email already registered."
  ],
  "username": [
    "username already taken."
  ]
}
</pre>
<hr noshade />

<h2>[200] Listar usuários.</h2>
<h3> GET -/users/</h3>

<strong>Essa rota necessita autenticação bearer token sem request body:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem bem sucedida:</p>
<pre>
[
    {
        "id": "146c8c8b-fef1-4487-8641-cff3ef748c7a",
        "username": "Mariano Lopes",
        "email": "ml123@gmail.com",    
        "address": {
            "street": "Floriano arroba",
            "distric": "Jardim das flores",
            "zipCode": 12341231,
            "state": "Ba",
            "city": "Jacobina",
            "number": 12,
        },
        "is_seller": False,
        "is_superuser": False,
    },
    {
        "id": "fae43b77-1c12-4fb4-af8e-4fb13fab5e26",
        "username": "Ronaldo Algusto Moreira Alves",
        "email": "ramalves@email.com",
        "address": {
            "street": "Saltante das figueiras",
            "distric": "Oliveiras amarelas",
            "zipCode": 12341231,
            "state": "SP",
            "city": "Guarulhos",
            "number": 14,
        },
        "is_seller": False,
        "is_superuser": False,
    }
]
</pre>
<hr noshade />

<h2>[200] Listar um usuário específico</h2>
<h3>GET - /users/:user_id/</h3>

<strong>Essa rota não necessita autenticação bearer token nem request body, mas é preciso enviar o id do autor como parâmetro:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para retorno bem sucedido:</p>
<pre>
    {
        "id": "146c8c8b-fef1-4487-8641-cff3ef748c7a",
        "username": "Mariano Lopes",
        "email": "ml123@gmail.com",    
        "address": {
            "street": "Floriano arroba",
            "distric": "Jardim das flores",
            "zipCode": 12341231,
            "state": "Ba",
            "city": "Jacobina",
            "number": 12,
        },
        "is_seller": False,
        "is_superuser": False,
    },
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para autor inexistente ou não encontrado:</p>
<pre>
{
    "detail": "User not found"
}
</pre>
<hr noshade />

<h2>[200] Atualizar um usuário específico</h2>
<h3>PATCH - /users/:user_id/</h3>

<strong>Essa rota necessita autenticação bearer token, é preciso enviar o id do usuário como parâmetro:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para atualização realizada com sucesso:</p>
<pre>
    {
        "id": "146c8c8b-fef1-4487-8641-cff3ef748c7a",
        "username": "Mariano Lopes",
        "email": "ml123@gmail.com",    
        "address": {
            "street": "Floriano arroba",
            "distric": "Jardim das flores",
            "zipCode": 12341231,
            "state": "Ba",
            "city": "Jacobina",
            "number": 12,
        },
        "is_seller": False,
        "is_superuser": False,
    },
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para usuário inexistente ou não encontrado:</p>
<pre>
{
    "detail": "User not found"
}
</pre>
<hr noshade />





<h2>[201] Criar Produtos </h2>
<h3>POST - /products/</h3>

<strong>Essa rota necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>name: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>stock: </strong>Entrada obrigatória do tipo number.</li>
    <li><strong>category: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>is_active: </strong>Entrada opcional do tipo boolean.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
	"id": "009bc657-2704-4593-9c3a-17c2e74f15c1",
	"name": "Coca-cola",
	"stock": 80,
	"category": "Bebidas",
	"is_active": true
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto/vazio:</p>
<pre>
{
	"name": [
        "This field is required."
    ],
	"stock": [
        "This field is required."
    ],
	"category": [
        "This field is required."
    ],
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para ausência de autenticação por token:</p>
<pre>
{
	"detail": "Authentication credentials were not provided."
}
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para usuário sem permissão de acesso:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />

<h2>[200] Listar Produtos.</h2>
<h3> GET -/products/</h3>

<strong>Essa rota necessita autenticação bearer token sem request body:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem bem sucedida:</p>
<pre>
[
    {
        "id": "009bc657-2704-4593-9c3a-17c2e74f15c1",
        "name": "Coca-cola",
        "stock": 80,
        "category": "Bebidas",
        "is_active": true
    },
    {
        "id": "5as8f351-2104-4493-9ab23a-123astf15a5",
        "name": "Red bull",
        "stock": 120,
        "category": "Bebidas",
        "is_active": true
    },
]
</pre>
<hr noshade />

<h2>[200] Listar um produto específico</h2>
<h3>GET - /products/:product_id/</h3>

<strong>Essa rota não necessita autenticação bearer token nem request body, mas é preciso enviar o id do usuário como parâmetro:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para retorno bem sucedido:</p>
<pre>
    {
        "id": "009bc657-2704-4593-9c3a-17c2e74f15c1",
        "name": "Coca-cola",
        "stock": 80,
        "category": "Bebidas",
        "is_active": true
    },
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para produto inexistente ou não encontrado:</p>
<pre>
{
    "detail": "Product not found"
}
</pre>
<hr noshade />

<h2>[200] Atualizar um produto específico</h2>
<h3>PATCH - /products/:product_id/</h3>

<strong>Essa rota necessita autenticação bearer token, é preciso enviar o id do usuário como parâmetro:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para atualização realizada com sucesso:</p>
<pre>
    {
        "id": "009bc657-2704-4593-9c3a-17c2e74f15c1",
        "name": "Coca-cola",
        "stock": 80,
        "category": "Bebidas",
        "is_active": true
    },
</pre>

<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para produto inexistente ou não encontrado:</p>
<pre>
{
    "detail": "Product not found"
}
</pre>
<hr noshade />
