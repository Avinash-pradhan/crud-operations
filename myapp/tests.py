from django.test import TestCase
from django.urls import reverse

from myapp.models import ArticleModel


class ArticleViewsTests(TestCase):
    def test_create_article_redirects_to_articles_list(self):
        response = self.client.post(
            reverse('form'),
            {
                'title': 'First Article',
                'description': 'Testing create flow',
                'author': 'Avinash',
                'date': '2026-03-28',
            },
        )

        self.assertRedirects(response, reverse('articles'))
        self.assertEqual(ArticleModel.objects.count(), 1)

    def test_update_article_saves_changes(self):
        article = ArticleModel.objects.create(
            title='Old title',
            description='Old description',
            author='Old author',
            date='2026-03-28',
        )

        response = self.client.post(
            reverse('update', args=[article.id]),
            {
                'title': 'New title',
                'description': 'New description',
                'author': 'New author',
                'date': '2026-03-29',
            },
        )

        article.refresh_from_db()
        self.assertRedirects(response, reverse('articles'))
        self.assertEqual(article.title, 'New title')
        self.assertEqual(article.author, 'New author')

    def test_delete_article_removes_record(self):
        article = ArticleModel.objects.create(
            title='Delete me',
            description='Delete description',
            author='Author',
            date='2026-03-28',
        )

        response = self.client.post(reverse('delete', args=[article.id]))

        self.assertRedirects(response, reverse('articles'))
        self.assertFalse(ArticleModel.objects.filter(id=article.id).exists())
