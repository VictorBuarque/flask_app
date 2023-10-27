-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Set-2023 às 01:46
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `crm_victor`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nome_cliente` varchar(75) DEFAULT NULL,
  `cpf_cliente` varchar(13) DEFAULT NULL,
  `email_cliente` varchar(100) DEFAULT NULL,
  `data_ultima_interacao` date DEFAULT NULL,
  `status_follow_up` varchar(45) DEFAULT NULL,
  `data_proximo_followup` date DEFAULT NULL,
  `descricao_ultima_interacao` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes_produtos`
--

CREATE TABLE `clientes_produtos` (
  `id_cliente` int(11) DEFAULT NULL,
  `id_produto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `estoque`
--

CREATE TABLE `estoque` (
  `id_produto` int(11) DEFAULT NULL,
  `cod_estoque` int(11) DEFAULT NULL,
  `qtd_produto` int(11) DEFAULT NULL,
  `status_estoque` varchar(75) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `id_funcionario` int(11) NOT NULL,
  `nome_funcionario` varchar(75) DEFAULT NULL,
  `cpf_funcionario` varchar(13) DEFAULT NULL,
  `email_funcionario` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario_tarefa`
--

CREATE TABLE `funcionario_tarefa` (
  `id_tarefa` int(11) DEFAULT NULL,
  `id_funcionario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `galpoes`
--

CREATE TABLE `galpoes` (
  `cod_estoque` int(11) NOT NULL,
  `local_estoque` varchar(75) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `historico_compra`
--

CREATE TABLE `historico_compra` (
  `id_compra` int(11) NOT NULL,
  `data_compra` date NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_produto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE `produto` (
  `id_produto` int(11) NOT NULL,
  `nome_produto` varchar(75) DEFAULT NULL,
  `preco_produto` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_interacao`
--

CREATE TABLE `registro_interacao` (
  `id_interacao` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_funcionario` int(11) DEFAULT NULL,
  `data_interacao` date DEFAULT NULL,
  `tipo_interacao` varchar(45) DEFAULT NULL,
  `descricao_interacao` varchar(45) DEFAULT NULL,
  `registro_interacaocol` varchar(45) DEFAULT NULL,
  `etapa_followup` varchar(45) DEFAULT NULL,
  `status_followup` varchar(45) DEFAULT NULL,
  `data_prox_followup` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tarefas`
--

CREATE TABLE `tarefas` (
  `id_tarefa` int(11) NOT NULL,
  `data_tarefa` date NOT NULL,
  `nome_tarefa` varchar(75) DEFAULT NULL,
  `status_tarefa` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Índices para tabela `clientes_produtos`
--
ALTER TABLE `clientes_produtos`
  ADD KEY `fk_id_cliente` (`id_cliente`),
  ADD KEY `fk_id_produto` (`id_produto`);

--
-- Índices para tabela `estoque`
--
ALTER TABLE `estoque`
  ADD KEY `fk_id_produto2` (`id_produto`),
  ADD KEY `fk_cod_estoque` (`cod_estoque`);

--
-- Índices para tabela `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`id_funcionario`);

--
-- Índices para tabela `funcionario_tarefa`
--
ALTER TABLE `funcionario_tarefa`
  ADD KEY `fk_id_funcionario` (`id_funcionario`),
  ADD KEY `fk_id_tarefas` (`id_tarefa`);

--
-- Índices para tabela `galpoes`
--
ALTER TABLE `galpoes`
  ADD PRIMARY KEY (`cod_estoque`);

--
-- Índices para tabela `historico_compra`
--
ALTER TABLE `historico_compra`
  ADD PRIMARY KEY (`id_compra`,`data_compra`),
  ADD KEY `fk_id_cliente3` (`id_cliente`),
  ADD KEY `fk_id_produto3` (`id_produto`);

--
-- Índices para tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`);

--
-- Índices para tabela `registro_interacao`
--
ALTER TABLE `registro_interacao`
  ADD PRIMARY KEY (`id_interacao`),
  ADD KEY `id_funcionario` (`id_funcionario`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Índices para tabela `tarefas`
--
ALTER TABLE `tarefas`
  ADD PRIMARY KEY (`id_tarefa`,`data_tarefa`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `clientes_produtos`
--
ALTER TABLE `clientes_produtos`
  ADD CONSTRAINT `fk_id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_id_produto` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `estoque`
--
ALTER TABLE `estoque`
  ADD CONSTRAINT `fk_cod_estoque` FOREIGN KEY (`cod_estoque`) REFERENCES `galpoes` (`cod_estoque`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_id_produto2` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `funcionario_tarefa`
--
ALTER TABLE `funcionario_tarefa`
  ADD CONSTRAINT `fk_id_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionarios` (`id_funcionario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_id_tarefas` FOREIGN KEY (`id_tarefa`) REFERENCES `tarefas` (`id_tarefa`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `historico_compra`
--
ALTER TABLE `historico_compra`
  ADD CONSTRAINT `fk_id_cliente3` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_id_produto3` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `registro_interacao`
--
ALTER TABLE `registro_interacao`
  ADD CONSTRAINT `id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_funcionario` FOREIGN KEY (`id_funcionario`) REFERENCES `funcionarios` (`id_funcionario`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
