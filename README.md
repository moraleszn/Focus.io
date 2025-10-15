<p align="center">

  <img width="250" alt="Mascote Focus.io" src="https://github.com/user-attachments/assets/65c370e9-f92c-4821-8046-68329634f304" />
</p>

<h1 align="center">Focus.io</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Project Status">
</p>

<p align="center">
  Seu assistente pessoal de produtividade para o Discord, combinando organização com uma dose de bom humor!
</p>

---

### 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades Principais](#-funcionalidades-principais)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🎮 Exemplos de Comandos](#-exemplos-de-comandos)

---

## 🤖 Sobre o Projeto

> O **Focus.io** é mais do que um simples bot. Ele foi criado para ser seu parceiro na jornada de organização e estudos, ajudando a gerenciar tarefas, criar lembretes úteis e, claro, te motivar com frases divertidas quando você mais precisar. Ideal para quem quer ser mais produtivo sem perder a leveza do dia a dia!

<br>

## ✨ Funcionalidades Principais

- **✅ Lista de Tarefas (To-Do):** Adicione, remova, liste e marque tarefas como concluídas diretamente do Discord.
- **🔔 Lembretes Personalizados:** Configure alertas para estudar, beber água, fazer uma pausa ou qualquer outra atividade importante.
- **🍅 Timer Pomodoro:** Gerencie seu tempo de foco e descanso com um timer Pomodoro simples e eficaz.
- **📊 Relatórios de Produtividade:** Acompanhe seu progresso com relatórios divertidos sobre as tarefas concluídas.

<br>

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **discord.py** (para a integração com a API do Discord)
- **python-dotenv** (para gerenciar variáveis de ambiente, como o token do bot)

<br>

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/focus.io.git](https://github.com/seu-usuario/focus.io.git)
    cd focus.io
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas variáveis de ambiente:**
    - Crie um arquivo chamado `.env` na pasta raiz do projeto.
    - Dentro dele, adicione seu token do bot da seguinte forma:
      ```
      DISCORD_TOKEN=SEU_TOKEN_SECRETO_VAI_AQUI
      ```
    - *Garanta que o arquivo `main.py` está configurado para ler esta variável.*

5.  **Execute o bot:**
    ```bash
    python main.py
    ```

<br>

## 🎮 Exemplos de Comandos

Uma vez que o bot esteja online no seu servidor, você pode interagir com ele:

-   **Adicionar uma tarefa:** `.addtask Estudar Python por 1 hora`
-   **Criar um lembrete:** `.remindme 30m Beber água!`
-   **Iniciar um ciclo Pomodoro:** `.pomodoro 25`
-   **Ver suas tarefas:** `.tasks`

<br>
