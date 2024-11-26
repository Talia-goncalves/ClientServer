# Exemplo de Arquitetura Client x Server - Adicionar Itens 

Este é um projeto simples de gerenciamento de itens que exemplifica a **arquitetura Client x Server**. No projeto, o back-end é implementado utilizando **Flask** (Python), enquanto o front-end é feito com **HTML**, **CSS** e **JavaScript**. O exemplo mostra como os dados são manipulados no **client-side** e como o servidor pode ser estruturado para servir os recursos.

## Arquitetura: Client x Server

Neste projeto, temos a separação entre **client-side** (front-end) e **server-side** (back-end):

- **Client-side**: O front-end é responsável por interagir com o usuário, exibir o formulário para adicionar itens e manipular as interações. Ele também gerencia a exibição e remoção de itens da lista diretamente na interface.

- **Server-side**: O back-end, que é implementado com o Flask, serve o arquivo HTML e os recursos estáticos (CSS, JS). A manipulação de dados no servidor, como armazenamento permanente, não está incluída neste exemplo (mas seria possível integrar com banco de dados se necessário).

Este exemplo ilustra como a comunicação entre o **client** e o **server** pode ser estruturada, embora a manipulação dos dados seja feita no lado do cliente para este projeto simples.

## Funcionalidades

- **Adicionar Itens**: O usuário preenche um formulário e clica em "Adicionar", o item é então exibido na lista abaixo.

- **Excluir Itens**: O botão de "Excluir" permite que o usuário remova itens da lista.

- **Interface Dinâmica**: Os itens adicionados e removidos são refletidos instantaneamente na interface do usuário.

- **Armazenamento Local**: Não há banco de dados no servidor, os itens são mantidos apenas enquanto a página estiver aberta. Ao recarregar a página, os dados são perdidos.

## Tecnologias Utilizadas

- **Flask** (Back-end)
- **HTML**, **CSS**, **JavaScript** (Front-end)
- Arquitetura **Client x Server**

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
/meu_projeto 
│ 
├── server.py # Código do servidor Flask 
│ 
└── static/ 
   ├── index.html # Arquivo HTML com a interface 
   ├── script.js # Script JavaScript para interatividade 
   └── style.css # Arquivo CSS com estilos personalizados
```

## Como Executar o Projeto

### Pré-requisitos

Antes de começar, você precisa ter o **Python 3.x** instalado no seu sistema. Além disso, o Flask precisa ser instalado para rodar o servidor.

### Passos para executar:

1. **Clone o repositório** ou baixe o projeto para sua máquina local:

```
   git clone https://github.com/Talia-goncalves/ClientServer.git 
   cd ClientServer
```

2. **Instalar as dependências:**

Caso o Flask não esteja instalado, instale-o com o seguinte comando:

```
    pip install flask
```

3. **Rodar o servidor Flask:**

Navegue até o diretório onde está o arquivo "server.py" e execute o seguinte comando:

```
    python server.py 
```


iniciará o servidor Flask na URL http://127.0.0.1:5000/.

4. **Acesse a aplicação:**

Abra seu navegador e acesse "http://127.0.0.1:5000/" para ver a aplicação funcionando.

## Detalhes do Código

- server.py:
    - O servidor Flask serve o arquivo HTML (index.html) com a interface do projeto.
    - Este exemplo não armazena os dados permanentemente, mas é possível adicionar funcionalidades de persistência utilizando um banco de dados, como MySQL ou SQLite.

- index.html:
    - Contém o formulário de entrada de dados e a estrutura da lista de itens.
    - O arquivo HTML é o responsável por exibir o conteúdo da página e interagir com o usuário.

- script.js:
    - Responsável por adicionar e remover itens da lista diretamente no front-end.
    - O código manipula os dados inseridos pelo usuário e os exibe dinamicamente na página sem a necessidade de comunicação constante com o back-end.

- style.css:
    - Estiliza a interface, deixando a experiência do usuário mais agradável com um layout organizado.

## Como Funciona a Arquitetura Client x Server

- Client-side:
    - O front-end (HTML, CSS e JavaScript) é responsável por capturar a entrada do usuário, exibir os itens na lista e permitir a exclusão deles.

    - O JavaScript lida com a lógica de adição e remoção de itens diretamente na página. Não há comunicação com o servidor para manipulação dos dados no momento, o que significa que os dados são manipulados diretamente no cliente.

- Server-side:
    - O Flask serve o conteúdo HTML e os arquivos estáticos (CSS e JavaScript).

    - O servidor não realiza operações de CRUD no banco de dados neste exemplo. Caso seja necessário persistir os dados, seria possível integrar um banco de dados no back-end, onde o Flask receberia as requisições do front-end para armazenar, buscar ou deletar dados.
