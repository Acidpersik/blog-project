from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='testuser@gmail.com',
            password='testsecret',
        )

        self.post = Post.objects.create(
            title='Test title',
            body='Hello, its test',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='Sample test hey')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test title')
        self.assertEqual(f'{self.post.body}', 'Hello, its test')
        self.assertEqual(f'{self.post.author}', 'test_user')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, its test')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'Wow title',
            'body': 'Wow text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wow title')
        self.assertContains(response, 'Wow text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Hey, updated title',
            'body': 'Hey, updated body'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)