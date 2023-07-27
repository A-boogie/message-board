from django.test import TestCase
from django.urls import reverse

from .models import Post


"""Using the hook setUpTestData(), a classmethod, to create the test data: it is much faster than using the
setUp() hook from Python’s unittest because it creates the test data only once per test case
rather than per test. Create test class called PostTests that extends TestCase, this will use the method SetUpTestData to develop initial data. 
Note that the second function is the actual test and the first one is to prepare data before all tests on that class are run"""


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    """The following functions are to test the URLs, views and templates. 
    It will check if URL exists by returnunf a 200 HTTP status code, if the URL is available at home, 
    the correct template home.html is correct and the homepage content matches what should be in the database"""

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
