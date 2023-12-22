from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

# Tetsing Post Model
class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
        username='testuser1', password='user!123')
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1,
            title='I am the title', 
            body='I am a body...'
        )
        test_post.save()

    # Test blog content
    def test_blog_content(self):
        post = Post.objects.get(id=1)

        # Variables that store post content
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        slug = f'{post.slug}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'I am the title')
        self.assertEqual(body, 'I am a body...')
        self.assertEqual(slug, 'i-am-the-title')