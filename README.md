### Banco de Dados com Python

O projeto tinha como objetivo **conectar o Python a um banco de dados** e manipular as informações nele contidas. Um **banco de dados** é uma tecnologia que permite armazenar informações de forma organizada em tabelas no disco. Eles são amplamente utilizados em diversas áreas, como empresas, instituições governamentais, organizações de pesquisa e outros setores, para gerenciar informações, como recursos, registros de funcionários, registros médicos e comércio eletrônico, entre outras aplicações.

O tipo de banco de dados utilizado no projeto foi o **banco de dados relacionais**, que permite realizar consultas e manipulações usando a linguagem SQL (Structured Query Language). Esse tipo de banco de dados é comum em aplicações empresariais, sites e aplicativos de comércio eletrônico, pois oferece uma estrutura robusta e flexível para o armazenamento e gerenciamento eficiente de dados, garantindo a integridade e consistência dos mesmos.

No projeto, foi utilizado o **SQLite**, uma biblioteca C que fornece um banco de dados leve baseado em disco, não requerendo um processo de servidor separado e permitindo o acesso ao banco de dados usando uma variante não padrão da linguagem de consulta SQL. O SQLite é útil para prototipar aplicativos, e posteriormente, o código pode ser portado para um banco de dados maior, como PostgreSQL ou Oracle.

Para facilitar o trabalho, foi utilizado o **DB Browser for SQLite** , uma ferramenta visual de código aberto que permite criar, projetar e editar arquivos de banco de dados compatíveis com o SQLite. Essa ferramenta possui uma interface familiar semelhante a uma planilha, dispensando a necessidade de aprender comandos SQL complicados. Ao final do projeto, foi possível criar uma tabela, conectar-se ao banco de dados e executar operações como enviar, inserir e trazer valores na tabela. Site da documentação oficial: https://docs.python.org/3/library/sqlite3.html .




