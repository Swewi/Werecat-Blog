from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Post, Comment
from cloudinary.models import CloudinaryField

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post content',
        )

    def test_default_status(self):
        # Test that the default status is Draft (0)
        self.assertEqual(self.post.status, 0)

    def test_slug_uniqueness(self):
        # Test that slugs are unique
        with self.assertRaises(Exception):
            Post.objects.create(
                title='Another Post',
                slug='test-post',  # Same slug as self.post
                author=self.user,
                content='Content with the same slug',
            )

    def test_featured_image_default(self):
        # Test that the default image is 'placeholder'
        self.assertEqual(self.post.featured_image, 'placeholder')

    def test_related_name_for_author(self):
        # Test that the related_name 'blog_posts' works correctly
        self.assertEqual(self.user.blog_posts.first(), self.post)

    def test_ordering(self):
        # Test that the default ordering is by created_on, descending
        post2 = Post.objects.create(
            title='Second Post',
            slug='second-post',
            author=self.user,
            content='Content for the second post',
        )
        posts = Post.objects.all()
        self.assertEqual(posts.first(), post2)  # post2 should come first
        self.assertEqual(posts.last(), self.post)

    def test_slug_generation(self):
        # Test that the slug is generated automatically (if this is implemented)
        new_post = Post.objects.create(
            title='A Unique Title',
            author=self.user,
            content='Some content',
        )
        self.assertEqual(new_post.slug, slugify(new_post.title))

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post content',
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment',
        )

    def test_comment_ordering(self):
        # Test that the default ordering is by created_on, ascending
        comment2 = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Another comment',
        )
        comments = Comment.objects.all()
        self.assertEqual(comments.first(), self.comment)  # First comment
        self.assertEqual(comments.last(), comment2)  # Second comment

    def test_related_name_for_post_comments(self):
        # Test that the related_name 'comments' works correctly
        self.assertEqual(self.post.comments.first(), self.comment)

    def test_related_name_for_author_comments(self):
        # Test that the related_name 'comments_author' works correctly
        self.assertEqual(self.user.comments_author.first(), self.comment)