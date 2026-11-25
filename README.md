# 🛡️ DIO Agent como mentor de Cibersegurança

> **Um laboratório prático de AppSec com Hermes:** análise de vulnerabilidades, avaliação de riscos, orientação defensiva e validação de correções.

Este projeto demonstra como especializar o **DIO Agent** para atuar como um mentor de cibersegurança. Em vez de apenas entregar respostas ou comandos, o agente é orientado a compreender o cenário, fazer perguntas quando faltam informações, explicar os riscos e recomendar correções de forma didática.

O trabalho parte do repositório-base da Digital Innovation One e acrescenta a skill `vulnerability-analysis`, uma base de conhecimento de segurança, ajustes na persona e exercícios práticos com **SQL Injection** e **Path Traversal**.

---

## 📚 Índice

- [Objetivo](#-objetivo)
- [O que foi desenvolvido](#-o-que-foi-desenvolvido)
- [Tecnologias e requisitos](#-tecnologias-e-requisitos)
- [Preparação do ambiente](#-preparação-do-ambiente)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Etapa 1 — Análise de SQL Injection](#-etapa-1--análise-de-sql-injection)
- [Etapa 2 — Criação da skill](#-etapa-2--criação-da-skill)
- [Etapa 3 — Base de conhecimento](#-etapa-3--base-de-conhecimento)
- [Etapa 4 — Especialização da persona e registro da skill](#-etapa-4--especialização-da-persona-e-registro-da-skill)
- [Etapa 5 — Teste do comportamento de mentor](#-etapa-5--teste-do-comportamento-de-mentor)
- [Etapa 6 — Laboratório de Path Traversal](#-etapa-6--laboratório-de-path-traversal)
- [Segurança e uso responsável](#-segurança-e-uso-responsável)
- [Aprendizados e conclusão](#-aprendizados-e-conclusão)

---

## 🎯 Objetivo

O desafio propõe transformar o DIO Agent em um mentor capaz de analisar vulnerabilidades seguindo uma abordagem semelhante à utilizada por profissionais de segurança.

A especialização deve orientar o agente a:

1. Entender o contexto antes de sugerir ações.
2. Identificar e explicar vulnerabilidades.
3. Avaliar impacto, probabilidade e severidade.
4. Recomendar medidas de correção e prevenção.
5. Validar se a correção resolveu o problema.
6. Ensinar o raciocínio por trás da análise, em vez de fornecer somente uma resposta pronta.

O foco deste repositório é **educacional e defensivo**. Os testes são realizados em aplicações e ambientes de laboratório.

## ✨ O que foi desenvolvido

| Componente | Finalidade |
|---|---|
| `skills/vulnerability-analysis/` | Skill que define o roteiro de análise de vulnerabilidades seguido pelo agente. |
| `agent/knowledge/security-basics.md` | Conceitos fundamentais: vulnerabilidade, ameaça, risco e tríade CIA. |
| `agent/persona.md` | Complemento da persona para orientar o agente como mentor de segurança. |
| `AGENTS.md` | Registro da skill e indicação de quando utilizá-la. |
| Exercício de SQL Injection | Demonstração de uma consulta vulnerável e sua correção com parâmetros. |
| Laboratório de Path Traversal | Aplicação local para observar a falha e testar uma validação de caminho. |

## 🧰 Tecnologias e requisitos

- **DIO Agent** — repositório-base do desafio.
- **Hermes Agent** — agente utilizado para interagir com os arquivos e executar o fluxo de orientação.
- **Python 3** e **pip** — necessários para os exemplos em Python.
- **Flask** — dependência do laboratório de Path Traversal.
- **SQLite** — banco utilizado no exemplo de login com SQL Injection.
- **bcrypt** — biblioteca usada no exemplo corrigido para verificação de senha com hash.
- Git ou a opção de baixar o repositório em ZIP.

Documentação e repositórios:

- [DIO Agent — repositório-base](https://github.com/digitalinnovationone/dio-agent)
- [Hermes Agent — documentação oficial](https://hermes-agent.nousresearch.com/)

> **Importante:** instale e configure o Hermes seguindo a documentação oficial. Os comandos e requisitos de instalação podem variar conforme o sistema operacional e a versão utilizada.

## 🚀 Preparação do ambiente

### 1. Obtenha o repositório-base

Com Git:

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
cd dio-agent
```

Ou baixe o ZIP do repositório-base e extraia os arquivos.

### 2. Configure o Hermes

Siga as instruções da [documentação do Hermes](https://hermes-agent.nousresearch.com/) para instalar e configurar o agente.

### 3. Abra o terminal na pasta correta

Antes de iniciar o Hermes, abra o terminal **na raiz do projeto `dio-agent/`**. Isso é importante para que o agente encontre os arquivos e diretórios que serão analisados.

> ⚠️ Executar o Hermes em outro diretório pode fazer com que ele não encontre os arquivos do projeto ou trabalhe sobre um caminho diferente do esperado.

### 4. Adicione os arquivos deste projeto

Copie os arquivos e diretórios deste repositório para a estrutura correspondente do DIO Agent. Preserve os arquivos originais que não fazem parte das alterações e revise os caminhos antes de iniciar os testes.

## 🗂️ Estrutura do projeto

A organização utilizada neste projeto é:

```text
dio-agent/
├── AGENTS.md
├── agent/
│   ├── app.py
│   ├── app_corrigido.py
│   ├── persona.md
│   ├── knowledge/
│   │   └── security-basics.md
├── path_traversal_lab/
│   ├── app.py
│   ├── app_nao_corrigido.py
│   ├── README.md
│   ├── requirements.txt
│   ├── public_files/
│   │   └── welcome.txt
│   └── templates/
│       └── index.html
└── skills/
    └── vulnerability-analysis/
        ├── README.md
        └── SKILL.md

Images/
├── 00_Aplicacao_insegura.png
├── 01_prompt_correcao_app_py.png
├── 02_prompt_correcao_app_py_resultado.png
├── 03_Hermes_correcao_app_py.png
├── 04_Aplicacao_corrigida.png
├── 05_Hermes_validando_correcao_app_py.png
├── 06_Adicionando_especializacao_ao_persona_md.png
├── 07_Adicionando_skill_ao_agent_md.png
├── 08_Hermes_comportamento_alterado.png
├── 09_Hermes_comportamento_mentor.png
├── 10_Site_comprometido.png
├── 11_Site_comprometido_manipulando_diretorio.png
├── 12_Site_comprometido_analise.png
├── 13_Site_comprometido_corrigido.png
└── 14_Site_aprovacao_do_hermes.png
```

A pasta `Images/` fica na raiz deste repositório, no mesmo nível do `README.md`, para que as capturas de tela abaixo sejam exibidas corretamente no GitHub.

---

## 🔎 Etapa 1 — Análise de SQL Injection

O primeiro exercício consiste em criar uma aplicação de login intencionalmente vulnerável e solicitar ao Hermes que analise o código, explique o risco e proponha uma correção.

### Código inicial: consulta vulnerável

O exemplo abaixo concatena diretamente os valores fornecidos pelo usuário na instrução SQL:

```python
import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"

    cursor.execute(query)
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."
```

O problema é que a entrada pode alterar a estrutura da consulta SQL, em vez de ser tratada apenas como dado. Esse comportamento caracteriza uma possibilidade de **SQL Injection**.

![Aplicação com consulta vulnerável](Images/00_Aplicacao_insegura.png)

### Solicitação de análise ao Hermes

Com o arquivo `agent/app.py` no diretório do projeto, foi utilizado o seguinte prompt:

```text
Atue como um especialista em AppSec. Leia o arquivo app.py nesta pasta.
Identifique se existe alguma vulnerabilidade crítica, explique como um atacante poderia explorá-la, cite a técnica correspondente no MITRE ATT&CK e
reescreva o código corrigindo a falha de forma segura.
```

![Prompt de análise enviado ao Hermes](Images/01_prompt_correcao_app_py.png)

![Resultado da análise do Hermes](Images/02_prompt_correcao_app_py_resultado.png)

### Correção proposta

Após a identificação do problema, foi solicitado que o agente corrigisse a aplicação.

![Hermes realizando a correção](Images/03_Hermes_correcao_app_py.png)

A versão corrigida utiliza uma consulta parametrizada. O exemplo também utiliza `bcrypt` para verificar senhas armazenadas como hash:

```python
import sqlite3
import bcrypt

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # Os placeholders tratam a entrada como dado, não como SQL.
    query = "SELECT password FROM usuarios WHERE username = ?"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado and bcrypt.checkpw(senha.encode(), resultado[0]):
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."


def cadastrar_usuario(usuario, senha):
    """Cadastra usuário armazenando o hash da senha."""
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        (usuario, hash_senha)
    )
    conexao.commit()
    conexao.close()
```

![Aplicação após a correção](Images/04_Aplicacao_corrigida.png)

### Validação

Depois da alteração, foi solicitado ao Hermes que analisasse novamente o arquivo para verificar se a falha havia sido mitigada.

![Validação da correção pelo Hermes](Images/05_Hermes_validando_correcao_app_py.png)

**Ponto de aprendizado:** a correção principal contra SQL Injection é utilizar consultas parametrizadas. O armazenamento e a verificação de senhas também devem seguir práticas próprias de autenticação, como o uso de funções de hash apropriadas para senhas.

### Sobre CWE e MITRE ATT&CK

SQL Injection é uma categoria de fraqueza descrita pela **CWE-89**. MITRE ATT&CK, por sua vez, descreve técnicas e comportamentos de adversários. A técnica aplicável depende do contexto do cenário e do objetivo do ataque; por isso, não se deve associar automaticamente toda ocorrência de SQL Injection a uma técnica ATT&CK específica. O prompt do exercício solicita que o agente faça essa correlação e justifique a escolha.

Referências: [CWE-89 — Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html) · [MITRE ATT&CK](https://attack.mitre.org/).

---

## 🧠 Etapa 2 — Criação da skill

A skill é o roteiro que orienta o Hermes sobre como agir diante de solicitações relacionadas à análise de vulnerabilidades.

Crie o diretório:

```text
skills/vulnerability-analysis/
```

Dentro dele, mantenha dois arquivos:

- `README.md` — explica a finalidade da skill para pessoas que consultam o projeto.
- `SKILL.md` — contém as instruções que orientam o comportamento do agente.

### Finalidade da skill

A skill `vulnerability-analysis` foi criada para ajudar estudantes a compreender:

- conceitos de segurança;
- identificação de vulnerabilidades e riscos;
- impacto e probabilidade;
- avaliação de severidade;
- investigação e correção defensiva;
- prevenção e aprendizado contínuo.

### Fluxo de análise

1. **Entender o cenário:** identificar sistema, ambiente, tecnologia e objetivo da análise.
2. **Coletar informações:** perguntar o que estiver faltando, sem assumir fatos.
3. **Explicar a vulnerabilidade:** apresentar a falha e o princípio de segurança afetado.
4. **Avaliar o risco:** descrever impacto, probabilidade e severidade, justificando a classificação.
5. **Recomendar melhorias:** orientar correções e medidas preventivas.
6. **Verificar o aprendizado:** resumir o problema e explicar o raciocínio utilizado.

O `SKILL.md` também estabelece regras defensivas: não incentivar ataques contra sistemas reais, não tratar hipóteses como certezas e priorizar ambientes de laboratório autorizados.

---

## 📖 Etapa 3 — Base de conhecimento

Na pasta `agent/knowledge/`, foi criado o arquivo `security-basics.md`.

Ele fornece ao agente uma referência introdutória sobre:

### Conceitos fundamentais

- **Vulnerabilidade:** falha em um sistema, aplicação ou processo que pode permitir comportamentos indesejados.
- **Ameaça:** algo que pode explorar uma vulnerabilidade.
- **Risco:** combinação de probabilidade e impacto.

### Tríade CIA

| Princípio | Significado |
|---|---|
| **Confidencialidade** | Garantir que somente pessoas autorizadas tenham acesso às informações. |
| **Integridade** | Proteger informações contra alterações indevidas. |
| **Disponibilidade** | Manter sistemas e informações acessíveis quando necessário. |

### Boas práticas registradas

- Manter sistemas atualizados.
- Aplicar o princípio do menor privilégio.
- Monitorar eventos e atividades relevantes.
- Realizar backups.
- Corrigir vulnerabilidades conhecidas.

---

## 🎭 Etapa 4 — Especialização da persona e registro da skill

### Atualização de `agent/persona.md`

Foi acrescentada uma seção de especialização em segurança para que o agente, além de mentor educacional, adote uma postura de orientação defensiva quando identificar perguntas relacionadas à segurança da informação.

A orientação acrescentada determina que o agente:

- assuma postura de mentor;
- explique os conceitos envolvidos;
- faça perguntas antes de responder quando faltar contexto;
- recomende boas práticas defensivas;
- ajude a desenvolver o pensamento de um analista de segurança.

![Especialização adicionada à persona](Images/06_Adicionando_especializacao_ao_persona_md.png)

### Atualização de `AGENTS.md`

Também foi registrada a skill `vulnerability-analysis` na documentação de skills do agente. A descrição indica quando ela deve ser utilizada, por exemplo, em perguntas sobre vulnerabilidades, riscos, falhas de segurança e análise defensiva.

![Skill registrada no AGENTS.md](Images/07_Adicionando_skill_ao_agent_md.png)

---

## 💬 Etapa 5 — Teste do comportamento de mentor

Com a skill, a base de conhecimento e os arquivos de orientação configurados, foi realizado um teste para verificar se o Hermes perguntaria sobre o contexto antes de sugerir ações.

### Primeiro cenário: servidor Ubuntu

Prompt utilizado:

```text
Quero analisar uma vulnerabilidade.

Tenho um servidor Ubuntu exposto na internet.
Não sei por onde começar.
```

![Hermes solicitando contexto](Images/08_Hermes_comportamento_alterado.png)

Durante o teste, foi observado que o agente não deveria partir diretamente para comandos ou conclusões. O objetivo era obter informações sobre o ambiente antes de orientar a investigação.

### Complementando o contexto

Em seguida, foi fornecido um cenário mais detalhado:

```text
É um servidor meu, de laboratório, usado para hospedar um site de testes. Tenho acesso administrativo por SSH. Não recebi alertas nem observei comportamento estranho; quero fazer uma avaliação inicial. Sou iniciante em segurança. Com essas informações, me guie como um mentor: diga o que já sabemos, o que ainda precisamos descobrir e quais seriam as três primeiras verificações defensivas. Explique o motivo de cada uma em uma linguagem simples. Não presuma que exista uma vulnerabilidade e não execute nenhuma ação; quero entender o raciocínio primeiro.
```

![Hermes atuando como mentor](Images/09_Hermes_comportamento_mentor.png)

### Observação sobre o carregamento da skill

Durante a experiência, o Hermes não carregou a skill automaticamente. Foi necessário orientá-lo a adicionar ou localizar a skill, informando o caminho em que ela estava disponível.

Esse comportamento foi registrado como uma dificuldade encontrada no processo. O carregamento deve ser conferido na versão e na configuração do Hermes utilizadas, pois a existência do arquivo no repositório, por si só, não comprova que ele foi carregado pelo agente.

---

## 🧪 Etapa 6 — Laboratório de Path Traversal

Como melhoria além do exercício de SQL Injection, foi incluído um segundo cenário para testar a especialização em uma vulnerabilidade diferente: **Path Traversal**.

O laboratório está em `path_traversal_lab/` e possui uma aplicação Flask com:

- uma rota intencionalmente vulnerável, usada para demonstrar o problema;
- uma rota com validação de caminho, usada como exemplo de mitigação;
- arquivos de teste dentro de `public_files/`.

O diretório possui um `README.md` próprio com instruções de instalação e execução.

### Executar o laboratório

No terminal, entre na pasta do laboratório:

```bash
cd path_traversal_lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Depois, acesse localmente:

```text
http://127.0.0.1:5000
```

O laboratório foi configurado para escutar em `127.0.0.1`. **Não o exponha à rede ou à internet.**

### Observando a falha

A vulnerabilidade ocorre quando a aplicação permite que referências de caminho fornecidas pelo usuário sejam utilizadas sem validação adequada. Isso pode permitir que arquivos fora do diretório pretendido sejam acessados.

![Laboratório de Path Traversal](Images/10_Site_comprometido.png)

![Demonstração de manipulação de caminho](Images/11_Site_comprometido_manipulando_diretorio.png)

### Solicitando análise ao Hermes

Foi utilizado o seguinte prompt:

```text
Quero analisar uma vulnerabilidade.

Alguns usuários estão tendo acesso a arquivos que eles não deveriam ter no site de teste disponibilizado na pasta path_traversal_lab/
```

![Análise do laboratório pelo Hermes](Images/12_Site_comprometido_analise.png)

Após a análise, a aplicação foi modificada conforme as recomendações para restringir o acesso aos arquivos permitidos.

![Aplicação após a correção](Images/13_Site_comprometido_corrigido.png)

### Validando a mitigação

Por fim, foi solicitado ao Hermes que verificasse a nova versão:

```text
Criei uma nova versão do site chamada app.py na pasta path_traversal_lab/. A ameaça foi mitigada?
```

![Hermes avaliando a correção do Path Traversal](Images/14_Site_aprovacao_do_hermes.png)

**Ponto de aprendizado:** validar caminhos recebidos do usuário é essencial. A aplicação deve garantir que o arquivo solicitado permaneça dentro do diretório autorizado, além de tratar erros e permissões adequadamente.

---

## 🔐 Segurança e uso responsável

Este repositório contém exemplos intencionalmente vulneráveis para fins didáticos. Para utilizá-los com segurança:

- Execute os exercícios somente em ambientes próprios, isolados e autorizados.
- Mantenha o laboratório de Path Traversal vinculado a `127.0.0.1`.
- Não exponha aplicações vulneráveis à internet ou a redes compartilhadas.
- Utilize dados fictícios e arquivos de teste.
- Não utilize credenciais reais nos exemplos.
- Revise as alterações propostas pelo agente antes de utilizá-las em qualquer projeto.
- Faça cópias de segurança antes de modificar arquivos importantes.
- Não interprete a resposta de uma IA como garantia de que uma aplicação está segura.

As demonstrações são educativas e não substituem uma avaliação profissional de segurança, testes automatizados ou revisão de código.

## 🎓 Aprendizados e conclusão

O projeto demonstra como um agente de IA pode ser orientado para assumir um papel mais especializado por meio de instruções, skills, arquivos de conhecimento e ajustes de persona.

Ao longo da experiência, foram trabalhados conceitos e práticas importantes:

- identificação de SQL Injection;
- uso de consultas parametrizadas;
- armazenamento e verificação de senhas com hash;
- análise de risco e orientação defensiva;
- criação de uma skill reutilizável;
- organização de uma base de conhecimento;
- importância de compreender o contexto antes de sugerir ações;
- identificação e mitigação de Path Traversal;
- validação das mudanças realizadas.

A principal lição é que uma IA pode ir além de responder perguntas: quando recebe contexto e instruções bem estruturadas, pode atuar como apoio ao aprendizado, ajudando o estudante a compreender o problema, avaliar consequências e desenvolver um raciocínio mais próximo do trabalho de um profissional de segurança.

---

## 👤 Autor

Projeto desenvolvido como atividade prática de estudos em cibersegurança da **Digital Innovation One (DIO)**, utilizando o DIO Agent e o Hermes Agent.

