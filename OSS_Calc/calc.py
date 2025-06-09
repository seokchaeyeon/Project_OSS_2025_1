import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.silent_mode = False

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=','Silent']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char, b=btn: self.on_click(ch, b)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char,button):
        if char == 'Silent':
            self.silent_mode = not self.silent_mode
            if self.silent_mode:
                button.config(bg="gray")  # 무음모드 ON 표시
            else:
                button.config(bg="SystemButtonFace")  # 무음모드 OFF 표시
            return

        if not self.silent_mode:
            button.config(bg="yellow")
            button.after(100, lambda: button.config(bg="SystemButtonFace"))

        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



