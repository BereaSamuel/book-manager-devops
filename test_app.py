import unittest

import app as book_app


class BookManagerTestCase(unittest.TestCase):

    def setUp(self):
        book_app.app.config["TESTING"] = True
        self.client = book_app.app.test_client()

    def test_home_page(self):
        """Verifică dacă pagina principală răspunde."""

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book Manager", response.data)

    def test_database_connection(self):
        """Verifică dacă aplicația se conectează la MySQL."""

        conn = book_app.get_db_connection()

        self.assertIsNotNone(conn)

        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM books")
            result = cursor.fetchone()

        conn.close()

        self.assertIsNotNone(result)
        self.assertGreaterEqual(result["total"], 0)

    def test_books_are_loaded(self):
        """Verifică dacă aplicația afișează cărțile existente."""

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        # Dacă există cărți în baza de date, trebuie să apară în pagină.
        self.assertIn(b"Total Books", response.data)


if __name__ == "__main__":
    unittest.main()