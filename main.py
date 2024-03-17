import tkinter as tk
from tkinter import messagebox
import random

class MathProblemGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Бодлого бодох")
        self.master.geometry("300x200")

        self.low = 1
        self.high = 100
        self.num_questions = 5
        self.current_question = 0
        self.score = 0

        self.label_question = tk.Label(master, text="")
        self.label_question.pack()

        self.entry_answer = tk.Entry(master)
        self.entry_answer.pack()

        self.button_submit = tk.Button(master, text="Илгээх", command=self.check_answer)
        self.button_submit.pack()

        self.label_score = tk.Label(master, text="")
        self.label_score.pack()

        self.generate_question()

    def generate_question(self):
        self.current_question += 1
        if self.current_question > self.num_questions:
            messagebox.showinfo("Хожигдлоо", f"Таны оноо {self.score}/{self.num_questions}")
            self.master.destroy()
            return

        num1 = random.randint(self.low, self.high)
        num2 = random.randint(self.low, self.high)
        operator = random.choice(['+', '-', '*'])
        self.correct_answer = eval(f"{num1}{operator}{num2}")
        
        # Зөв хариулт дээр үндэслэн дараагийн асуултын хязгаарыг тохируулна 
        self.low = min(self.low, self.correct_answer - 10)
        self.high = max(self.high, self.correct_answer + 10)

        self.label_question.config(text=f"Хариуг олно уу {num1} {operator} {num2}?")

    def check_answer(self):
        user_answer = self.entry_answer.get()
        try:
            user_answer = int(user_answer)
        except ValueError:
            messagebox.showerror("Буруу оролт байна", "Бүхэл тоо оруулна уу.")
            return

        if user_answer == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Зөв хариулт", "Таны хариулт зөв байна")

        else:
            messagebox.showerror("Буруу хариулт", f"Уучлаарай, зөв хариу бол {self.correct_answer}")

        self.label_score.config(text=f"Оноо: {self.score}/{self.current_question}")
        self.entry_answer.delete(0, tk.END)
        self.generate_question()

def main():
    root = tk.Tk()
    game = MathProblemGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
