# ERP-requisitos-dos-clientes-
Trabalho do primeiro semestre analise e desenvolvimento de sitemas
resumo do projeto:funcionalidades essenciais de um de estoques
o projeto deve ter 
01- cadastro de produtos,
nome, categoria, preço, quantidade inicial e especificações técnicas 
02 -registro de movimentações 
entradas (compras, devoluções e saídas (vendas transferências perdas)
03 -consulta em tempo real 
visualização instantânea do saldo atual de todos os produtos 
04 -alerta inteligente 
notifica se o estoque está com baixa ou sem estoque 




contribuiçoes:

sou PEDRO DA SILVA VASCONCELOS E fiquei responsável pela estrutura inicial do sistema, modelagem do banco de dados e a lógica de escrita com validação de segurança.

1. Configuração do Banco de Dados (Célula 01)
Desenvolvi o módulo de infraestrutura utilizando a biblioteca sqlite3 para garantir o armazenamento permanente dos dados do marketplace.

Modelagem: Criação das tabelas produtos (armazenamento dos itens com nome, categoria, preço, quantidade inicial e especificações) e movimentacoes (histórico de fluxos).

Controle: Uso da cláusula IF NOT EXISTS para que o banco e as tabelas sejam gerados dinamicamente sem sobrescrever dados existentes.

2. Módulo de Escrita e Validação de Saída (Célula 02)
coloquei as funções modulares que alteram os dados do estoque, inserindo regras de negócio para proteger a integridade dos saldos.

cadastrar_produto(): coloca novos itens utilizando consultas parametrizadas para evitar vulnerabilidades de segurança (SQL Injection).

registrar_movimentacao(): Gerencia a lógica de entradas e saídas do estoque.

Validação de Saída: Implementação de uma trava de segurança que realiza uma consulta prévia do saldo antes de efetuar qualquer baixa. Se a quantidade solicitada for maior que o estoque atual, a função exibe um erro e interrompe a operação imediatamente, impedindo saldos negativos no banco de dados.

Meu nome é Danilo Arthur Rodrigues da Silva e fiquei responsável pela parte de estruturação lógica do sistema, consultas inteligentes e geração de relatórios do projeto de controle de estoque.

Atuei no desenvolvimento do módulo de consultas e monitoramento do sistema, utilizando Python com a biblioteca sqlite3 para leitura e gerenciamento das informações armazenadas no banco de dados.

Na Célula 03 desenvolvi o módulo de consultas e relatórios, responsável por interpretar os dados do estoque e gerar informações úteis para o funcionamento do marketplace.

Implementei o sistema de consulta em tempo real, permitindo a visualização instantânea do saldo atual dos produtos cadastrados no banco de dados. Esse processo é realizado através de comandos SQL utilizando SELECT, possibilitando o acompanhamento atualizado das quantidades disponíveis.

Também participei da criação do Alerta Inteligente de Estoque, funcionalidade responsável por identificar automaticamente produtos com quantidade baixa ou indisponível. O sistema realiza verificações automáticas no banco e informa quais itens precisam de reposição, ajudando no controle e na prevenção da falta de produtos.

Além disso, desenvolvi o Relatório Gerencial utilizando JOIN entre tabelas, conectando informações de produtos e movimentações para gerar uma visualização mais completa das entradas, saídas e situação atual do estoque.

Na Célula 04 participei da área de testes e execução do fluxo do sistema. Como o projeto foi desenvolvido de forma modularizada, as funções já permanecem carregadas na memória do Google Colab, permitindo executar apenas os módulos principais para simular o funcionamento real do marketplace de forma organizada e limpa.

Também auxiliei na identificação e correção de erros durante os testes, especialmente problemas relacionados à criação de tabelas, consultas SQL e validações de execução, garantindo maior estabilidade e funcionamento correto do sistema.
