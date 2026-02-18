#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class FocusTimerApp:
    def __init__(self, root):
        self.root = root
        root.title("Foco nos Estudos")

        # Config padrão (você pode mudar na tela)
        self.study_minutes = tk.IntVar(value=50)     # 30 ou 60, etc.
        self.break_minutes = tk.IntVar(value=15)

        # Estado
        self.mode = "idle"   # idle | studying | paused | break
        self.study_elapsed = 0.0       # segundos estudados desde o último descanso (float)
        self.break_remaining = 0.0     # segundos restantes do descanso (float)
        self.last_tick = None

        # UI
        top = tk.Frame(root)
        top.pack(padx=12, pady=10)

        tk.Label(top, text="Estudar (min):").grid(row=0, column=0, sticky="e")
        tk.Spinbox(top, from_=10, to=180, textvariable=self.study_minutes, width=6).grid(row=0, column=1, padx=6)

        tk.Label(top, text="Descanso (min):").grid(row=0, column=2, sticky="e")
        tk.Spinbox(top, from_=5, to=60, textvariable=self.break_minutes, width=6).grid(row=0, column=3, padx=6)

        self.status_label = tk.Label(root, text="Status: parado", font=("Arial", 12))
        self.status_label.pack(pady=(6, 2))

        self.timer_label = tk.Label(root, text="00:00", font=("Arial", 32))
        self.timer_label.pack(pady=(0, 10))

        btns = tk.Frame(root)
        btns.pack(pady=8)

        tk.Button(btns, text="Iniciar Estudo", width=16, command=self.start_study).grid(row=0, column=0, padx=6)
        tk.Button(btns, text="Pausar (imprevisto)", width=16, command=self.pause_with_reason).grid(row=0, column=1, padx=6)
        tk.Button(btns, text="Retomar", width=16, command=self.resume).grid(row=0, column=2, padx=6)
        tk.Button(btns, text="Resetar", width=16, command=self.reset).grid(row=0, column=3, padx=6)

        self.root.after(250, self.tick)

    def format_mmss(self, seconds: int) -> str:
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    def start_study(self):
        if self.mode in ("studying", "break"):
            return
        self.mode = "studying"
        self.last_tick = time.time()
        self.status_label.config(text="Status: estudando")
        self.update_display()

    def pause_with_reason(self):
        if self.mode not in ("studying",):
            return

        reason = simpledialog.askstring("Pausa - motivo", "Qual o motivo da pausa?")
        if reason is None:
            return  # cancelou

        self.log_pause(reason)
        self.mode = "paused"
        self.status_label.config(text="Status: pausado (imprevisto)")
        self.last_tick = None
        self.update_display()

    def resume(self):
        if self.mode not in ("paused",):
            return
        self.mode = "studying"
        self.status_label.config(text="Status: estudando")
        self.last_tick = time.time()

    def start_break(self):
    # entra em modo descanso, mas o tempo só começa DEPOIS do OK
        self.mode = "break"
        self.status_label.config(text="Status: descanso")

        messagebox.showinfo(
            "Hora do descanso",
            f"Descanso de {self.break_minutes.get()} min! Levanta, água, alonga 👌\n\n"
            "Clique em OK para iniciar o descanso."
        )

        # Só agora inicia a contagem do descanso
        self.break_remaining = float(int(self.break_minutes.get()) * 60)
        self.last_tick = time.time()
        self.update_display()


    def finish_break(self):
        # avisa, mas só volta a contar estudo DEPOIS do OK
        messagebox.showinfo("Voltar", "Bora voltar a estudar! 💪\n\nClique em OK para retomar.")

        self.mode = "studying"
        self.study_elapsed = 0.0
        self.last_tick = time.time()
        self.status_label.config(text="Status: estudando")
        self.update_display()


    def reset(self):
        self.mode = "idle"
        self.study_elapsed = 0.0
        self.break_remaining = 0.0
        self.last_tick = None
        self.status_label.config(text="Status: parado")
        self.timer_label.config(text="00:00")

    def log_pause(self, reason: str):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("pausas.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] Pausa: {reason}\n")

    def update_display(self):
        if self.mode == "studying":
            limit = int(self.study_minutes.get()) * 60
            remaining = max(0, int(limit - self.study_elapsed))
            self.timer_label.config(text=self.format_mmss(remaining))
        elif self.mode == "break":
            self.timer_label.config(text=self.format_mmss(max(0, int(self.break_remaining))))
        elif self.mode == "paused":
            self.timer_label.config(text="PAUSA")
        else:
            self.timer_label.config(text="00:00")

    def tick(self):
        now = time.time()

        if self.mode == "studying" and self.last_tick is not None:
            dt = now - self.last_tick
            self.last_tick = now
            self.study_elapsed += dt  # soma frações de segundo

            limit = float(int(self.study_minutes.get()) * 60)
            if self.study_elapsed >= limit:
                self.start_break()

            self.update_display()

        elif self.mode == "break" and self.last_tick is not None:
            dt = now - self.last_tick
            self.last_tick = now
            self.break_remaining -= dt  # decrementa frações de segundo

            if self.break_remaining <= 0:
                self.finish_break()

            self.update_display()

        self.root.after(250, self.tick)

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimerApp(root)
    root.mainloop()
