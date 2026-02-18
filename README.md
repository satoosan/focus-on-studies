# 📚 Focus Timer — Foco nos Estudos

Aplicativo simples em **Python + Tkinter** para ajudar no foco durante os estudos utilizando ciclos de **tempo de estudo + descanso**, inspirado na técnica Pomodoro.

A proposta é evitar distrações, controlar pausas inesperadas e incentivar pequenos descansos produtivos.

---

## ✨ Funcionalidades

* ⏱ **Timer de Estudo configurável** (10 a 180 minutos)
* 🧘 **Timer de Descanso configurável** (5 a 60 minutos)
* ⏸ **Pausa com motivo** (registra em log o porquê da interrupção)
* ▶ **Retomar estudo** após pausa
* 🔄 **Resetar sessão**
* 📄 **Log de pausas** salvo automaticamente em `pausas.log`
* 🔔 Avisos visuais para:

  * Início do descanso
  * Retorno ao estudo
* 🖥 Interface gráfica simples e leve (Tkinter)

---

## 🧠 Como Funciona

O aplicativo opera em 4 estados:

| Estado     | Descrição                     |
| ---------- | ----------------------------- |
| `idle`     | Parado, aguardando início     |
| `studying` | Contando tempo de estudo      |
| `paused`   | Estudo pausado por imprevisto |
| `break`    | Período de descanso           |

O descanso **só começa após clicar em OK**, evitando que o tempo corra sem o usuário perceber.

---

## 📷 Interface

A interface possui:

* Campos para definir minutos de estudo e descanso
* Status atual (parado, estudando, pausado, descanso)
* Cronômetro grande
* Botões de ação

---

## 🛠 Requisitos

* Python **3.8+**
* Tkinter instalado (normalmente já vem com Python)

Verificar Tkinter:

```bash
python3 -m tkinter
```

Se abrir uma janelinha, está tudo certo 👍

---

## ▶ Como Executar

### Linux / macOS

```bash
python3 foco.py
```

Ou torne executável:

```bash
chmod +x foco.py
./foco.py
```

### Windows

```bash
python foco.py
```

---

## 📁 Arquivos Gerados

| Arquivo      | Descrição                             |
| ------------ | ------------------------------------- |
| `pausas.log` | Registro das pausas com data e motivo |

Exemplo de log:

```
[2026-02-18 14:32:10] Pausa: Atender ligação
```

---

## 🔄 Fluxo de Uso

1. Defina tempo de estudo e descanso
2. Clique em **Iniciar Estudo**
3. Caso algo aconteça, clique em **Pausar** e informe o motivo
4. Clique em **Retomar** para continuar
5. Ao finalizar o tempo, surgirá aviso de descanso
6. Após o descanso, o ciclo reinicia

---

## 🎯 Objetivo do Projeto

Este projeto foi criado com o intuito de:

* Melhorar produtividade
* Reduzir distrações
* Criar disciplina de pausas saudáveis
* Servir como exemplo de aplicação GUI em Python

---

## 🚀 Possíveis Melhorias Futuras

* Sons de notificação
* Histórico visual de estudos
* Exportação de relatórios
* Tema escuro
* Atalhos de teclado

---

## 📜 Licença

Livre para uso e modificação para fins pessoais ou educacionais.

---

## 🤝 Contribuição

Sinta-se à vontade para abrir *issues*, sugerir melhorias ou enviar *pull requests*.

---
