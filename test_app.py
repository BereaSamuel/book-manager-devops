import unittest
import os
import tempfile

import app as book_app


class BookManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()

        book_app.DATABASE = self.db_path
        book_app.app.config["TESTING"] = True

        book_app.init_db()

        self.client = book_app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book Manager", response.data)

    def test_add_book(self):
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


if __name__ == "__main__":
    unittest.main()