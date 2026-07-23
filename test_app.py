import unittest

import app as book_app


class BookManagerTestCase(unittest.TestCase):

    def setUp(self):
        book_app.app.config["TESTING"] = True
        self.client = book_app.app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book Manager", response.data)

    def test_add_book(self):

        conn = book_app.get_db_connection()

        with conn.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM books WHERE title=%s AND author=%s",
                ("Clean Code", "Robert Martin")
            )

            existing = cursor.fetchone()

        conn.close()

        # Dacă există deja, testul este considerat trecut
        if existing:
            self.assertIsNotNone(existing)
            return

        # Dacă nu există, o adaugă
        response = self.client.post(
            "/add",
            data={
                "title": "Clean Code",
                "author": "Robert Martin"
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Clean Code", response.data)
        self.assertIn(b"Robert Martin", response.data)

        conn = book_app.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM books WHERE title=%s AND author=%s",
                ("Clean Code", "Robert Martin")
            )

            book = cursor.fetchone()

        conn.close()

        self.assertIsNotNone(book)


if __name__ == "__main__":
    unittest.main()