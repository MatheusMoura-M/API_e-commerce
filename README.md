<h1>Pf Python</h1>

<h3><strong>Proposta:</strong></h3>
<p>........</p>
<hr noshade />

<h2>[201] Aderir usuários </h2>
<h3>POST - /users</h3>

<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email e máximo 100 chars.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>address: </strong>Entrada obrigatória do tipo dicionario.</li>
    <li><strong>isAdm: </strong>Entrada opcional do tipo boolean com padrão falso.</li>
    <li><strong>isSeller: </strong>Entrada opcional do tipo boolean com padrão falso.</li>
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
    "isSeller": False,
    "isAdm": False,
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
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">409</strong> para email/username já existente:</p>
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
<h3> GET -/users</h3>

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
        "isSeller": False,
        "isAdm": False,
        "updatedAt": "2023-01-18T18:50:16.343Z",
        "createdAt": "2023-01-18T18:50:16.343Z",
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
        "isSeller": False,
        "isAdm": False,
        "updatedAt": "2023-01-18T18:50:16.343Z",
        "createdAt": "2023-01-18T18:50:16.343Z",
    }
]
</pre>
<hr noshade />

<h2>[200] Listar um usuário específico</h2>
<h3>GET - /users/:id</h3>

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
        "isSeller": False,
        "isAdm": False,
        "updatedAt": "2023-01-18T18:50:16.343Z",
        "createdAt": "2023-01-18T18:50:16.343Z",
    },
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">404</strong> para autor inexistente ou não encontrado:</p>
<pre>
{
    "detail": "User not found"
}
</pre>
<hr noshade />
