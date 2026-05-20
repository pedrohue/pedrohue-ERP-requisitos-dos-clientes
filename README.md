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
