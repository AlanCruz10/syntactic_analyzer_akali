from pathlib import Path
from lexical.lexer import Lexer
from syntactic.syntactic import analyze_syntax
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\exala\Documents\proyectos\projects-8\python\syntactic_analyzer_grammar_2\src\main\python\com\app\sagt"
    r"\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def analyze(entry_1, entry_2):
    entry_2.delete('1.0', END)
    result = []
    result_show = []
    lexer = Lexer(entry_1.get())
    token = lexer.next_token()
    t, lexeme = token
    format_token = f'TOKEN: {t} - LEXEMA: {lexeme}'
    while t is not None and lexeme is not None:
        result_show.append(format_token)
        result.append((t, lexeme))
        token = lexer.next_token()
        t, lexeme = token
        format_token = f'TOKEN: {t} - LEXEMA: {lexeme}'
    result_syntactic = analyze_syntax(result)
    result_show.insert(0, result_syntactic)
    entry_2.insert(END, "\n".join(map(str, result_show)))


def show_window():
    window = Tk()

    window.geometry("562x418")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(window, bg="#FFFFFF", height=418, width=562, bd=0, highlightthickness=0, relief="ridge")

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(281.0, 209.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(216.0, 114.0, image=image_image_2)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(216.0, 114.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=31.0, y=95.0, width=370.0, height=37.0)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(281.0, 263.0, image=image_image_3)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(281.5, 263.5, image=entry_image_2)
    entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=38.0, y=186.0, width=487.0, height=153.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: analyze(entry_1, entry_2), relief="flat")
    button_2.place(x=445.0, y=102.0, width=95.0, height=25.0)

    window.resizable(False, False)
    window.mainloop()
