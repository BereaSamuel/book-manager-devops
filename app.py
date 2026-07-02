from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("books.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():

    conn = get_db_connection()

    books = conn.execute(
        "SELECT * FROM books"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        books=books
    )


@app.route("/add", methods=["POST"])
def add_book():

    title = request.form["title"]
    author = request.form["author"]

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:book_id>")
def delete_book(book_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/edit/<int:book_id>")
def edit_book(book_id):

    conn = get_db_connection()

    book = conn.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        book=book
    )


@app.route("/update/<int:book_id>", methods=["POST"])
def update_book(book_id):

    title = request.form["title"]
    author = request.form["author"]

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE books
        SET title = ?, author = ?
        WHERE id = ?
        """,
        (title, author, book_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)