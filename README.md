# R2-D20 Discord Bot

R2-D20 é um bot para **Discord** desenvolvido para auxiliar em jogos de RPG, principalmente para rolagem de dados de iniciativa. Ele permite registrar iniciativas dos jogadores e organizá-las de forma prática, respeitando regras como desvantagem, vantagem e rolagens normais.

## Funcionalidades

- **!iniciativa**: Inicia a escuta de mensagens de iniciativa no chat.
  - Registra iniciativas no formato `D+X nome_do_personagem`, `V+X nome_do_personagem` ou `i+X nome_do_personagem`.
  - X é o bônus (ou penalidade) a ser somado ou subtraído da rolagem.
  - `D` e `V` indicam desvantagem e vantagem, respectivamente.
  - `i` indica uma rolagem simples de dado.

- **!stop**: Encerra o registro das iniciativas e exibe a lista de resultados organizados em ordem decrescente.

## Como Usar

1. Adicione o bot ao seu servidor Discord.
2. Use o comando `!iniciativa` para começar a registrar as iniciativas.
3. Os jogadores devem enviar suas iniciativas no formato:

   - `D+X nome_do_personagem` (Desvantagem)
   - `V+X nome_do_personagem` (Vantagem)
   - `i+X nome_do_personagem` (Rolagem normal)

4. Quando todos os jogadores enviarem suas iniciativas, use o comando `!stop` para ver a lista organizada.

## Pré-requisitos

Para rodar o bot localmente, você precisará:

- **Python 3.11** ou superior
- **discord.py** (para interagir com o Discord API)

## Passos de Instalação (Windows)

### 1. Baixe o Repositório

Baixe o repositório diretamente em formato ZIP clicando no botão **Code** na página do GitHub e selecionando **Download ZIP**. [Clique aqui para baixar o arquivo ZIP](https://github.com/caue-r/R2-D20/archive/refs/heads/main.zip).

Após o download, extraia o conteúdo em uma pasta de sua escolha.

### 2. Crie um Ambiente Virtual

No terminal, dentro da pasta onde você extraiu o conteúdo, crie um ambiente virtual:

```bash
python -m venv venv 
```

### 3. Ative o Ambiente Virutal

```bash
.\venv\Scripts\activate
```

Após a ativação do ambiente virtual, você verá o nome do ambiente virtual entre parênteses no terminal, como:
```scss
(venv) C:\caminho\para\o\projeto>
```

### 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 5. Defina o Token do Bot no Código

Abra o arquivo bot.py no editor de sua escolha. No arquivo, você verá uma linha onde o token do bot é carregado. Substitua INSIRA SEU TOKEN pelo seu token real:

```bash
bot.run("INSIRA SEU TOKEN")
```

### 6. Execute o Bot

```bash
python bot.py
```

### Disclaimer

O R2-D20 não coleta nenhuma informação pessoal dos usuários e não está relacionado oficialmente ao Discord ou qualquer sistema de RPG específico. Ele é um projeto de código aberto para fins de entretenimento e aprimoramento da experiência de jogo.





