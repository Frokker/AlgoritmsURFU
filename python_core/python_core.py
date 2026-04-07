import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    s1 = 'Hello'
    s2 = "world"
    s3 = '''Привет'''
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    name = "Alice"
    age = 30
    message = "Привет, меня зовут %s и мне %s лет." % (name, age)
    print(message)  # Вывод: Привет, меня зовут Alice и мне 30 лет.
    return


@app.cell
def _():
    import string
    string.ascii_uppercase
    return


@app.cell
def _():
    import unicodedata 

    return (unicodedata,)


@app.cell
def _(unicodedata):
    unicodedata.name('Z')
    return


app._unparsable_cell(
    r"""
    unicodedata.
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
