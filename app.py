from flask import Flask, render_template, request, redirect
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "book_manager")
DB_USER = os.getenv("DB_USER", "bookuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "bookpass")


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )


def init_db():
    conn = get_db_connection()

    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL
            )
        """)

    conn.close()


@app.route("/")
def home():

    conn = get_db_connection()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

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

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (%s, %s)",
            (title, author)
        )

    conn.close()

    return redirect("/")


@app.route("/delete/<int:book_id>")
def delete_book(book_id):

    conn = get_db_connection()

    with conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM books WHERE id = %s",
            (book_id,)
        )

    conn.close()

    return redirect("/")


@app.route("/edit/<int:book_id>")
def edit_book(book_id):

    conn = get_db_connection()

    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM books WHERE id = %s",
            (book_id,)
        )

        book = cursor.fetchone()

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

    with conn.cursor() as cursor:
        cursor.execute(
            """
            UPDATE books
            SET title = %s,
                author = %s
            WHERE id = %s
            """,
            (title, author, book_id)
        )

    conn.close()

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)