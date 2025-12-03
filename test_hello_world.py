import unittest
from hello_world import app, greet, generate_html

class TestHelloWorld(unittest.TestCase):
    """
    Unit tests for the Hello World Flask application.
    """

    def setUp(self) -> None:
        """
        Sets up the test client for the Flask application.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_greet(self) -> None:
        """
        Tests the greet function to ensure it returns the correct greeting message.
        """
        expected_greeting = 'Welcome to CI/CD 101 using GitHub Actions!'
        self.assertEqual(greet(), expected_greeting)

    def test_generate_html(self) -> None:
        """
        Tests the generate_html function to ensure it generates valid HTML
        containing the message and the expected image structure.
        """
        message = "Test Message"
        html = generate_html(message)
        self.assertIn(message, html)
        self.assertIn('<div style=\'text-align:center;font-size:80px;\'>', html)

    def test_hello_world_route(self) -> None:
        """
        Tests the '/greeting' route to ensure it returns a 200 status code
        and the expected content.
        """
        response = self.app.get('/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to CI/CD 101 using GitHub Actions!', response.data)

if __name__ == '__main__':
    unittest.main()

#Hello