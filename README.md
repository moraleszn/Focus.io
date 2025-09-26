
# Focus.io 🤖✨

Um bot de produtividade pessoal com bom humor, feito em Python!

## Sobre o projeto

O **Focus.io** é um bot que te ajuda a organizar o seu dia, gerenciar tarefas, enviar lembretes e te motivar com frases engraçadas. Ideal para quem quer ser mais produtivo sem perder o bom humor!

### Funcionalidades

- **Lista de tarefas (To-Do):** Adicione, remova e marque tarefas como concluídas.
- **Lembretes:** Receba alertas para estudar, beber água, descansar, etc.
- **Frases motivacionais:** Mensagens engraçadas e motivacionais para animar seu dia.
- **Pomodoro simples:** Controle o tempo dedicado a cada tarefa.
- **Relatórios de produtividade:** Veja seu progresso e receba feedback divertido.

### Tecnologias utilizadas

- Python 3
- discord.py (para bots no Discord)
- sqlite3 ou TinyDB (para armazenar tarefas)
- requests (para buscar frases motivacionais de APIs externas)
- (Opcional) Tkinter ou PyQt para interface gráfica

### Como usar

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/focusito.git
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Configure o token do seu bot no arquivo `main.py`.
4. Execute o bot:
   ```
   python main.py
   ```
5. Interaja com o bot no Discord usando comandos como `.addtask`, `.lembrete`, `.pomodoro`, `.motivacao`, etc.

### Exemplos de comandos

- `.addtask Estudar Python`
- `.lembrete Beber água em 30 minutos`
- `.motivacao`
- `.pomodoro 25`
