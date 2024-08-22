from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Comment

class TestBlogViews(TestCase):

    def setUp(self):
        """Create a superuser and a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com")
        self.post = Post.objects.create(
            title="Blog title", author=self.user,
            slug="blog-title", excerpt="Blog excerpt",
            content="Blog content", status=1
        )

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies a single blog post containing a comment form is returned"""
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is a test comment.', response.content)

    def test_post_list_page(self):
        """Test that the post list page loads correctly and displays posts."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Blog title")
        self.assertEqual(len(response.context['object_list']), 1)

    def test_comment_submission_without_login(self):
        """Test that unauthenticated users cannot submit comments."""
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertRedirects(response, f'/accounts/login/?next=/post/{self.post.slug}/')

    def test_comment_edit(self):
        """Test editing a comment by its author."""
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            post=self.post, author=self.user, body="Original comment")
   
        edit_data = {
            'body': 'Edited comment'
        }
        response = self.client.post(
            reverse('comment_edit', args=['blog-title', comment.id]), edit_data)
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.body, 'Edited comment')

    def test_comment_edit_by_different_user(self):
        """Test that a user cannot edit another user's comment."""
        another_user = User.objects.create_user(
            username="anotherUser", password="anotherPassword", email="another@test.com")
        comment = Comment.objects.create(
            post=self.post, author=self.user, body="Original comment")
   
        self.client.login(username="anotherUser", password="anotherPassword")
        edit_data = {
            'body': 'Malicious edit attempt'
        }
        response = self.client.post(
            reverse('comment_edit', args=['blog-title', comment.id]), edit_data)
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertNotEqual(comment.body, 'Malicious edit attempt')
        self.assertEqual(comment.body, 'Original comment')

    def test_comment_deletion(self):
        """Test that a user can delete their own comment."""
        self.client.login(username="myUsername", password="myPassword")
        comment = Comment.objects.create(
            post=self.post, author=self.user, body="Comment to delete")
   
        response = self.client.post(
            reverse('comment_delete', args=['blog-title', comment.id]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=comment.id)

    def test_comment_deletion_by_different_user(self):
        """Test that a user cannot delete another user's comment."""
        another_user = User.objects.create_user(
            username="anotherUser", password="anotherPassword", email="another@test.com")
        comment = Comment.objects.create(
            post=self.post, author=self.user, body="Comment to delete")
   
        self.client.login(username="anotherUser", password="anotherPassword")
        response = self.client.post(
            reverse('comment_delete', args=['blog-title', comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(id=comment.id).exists())

    def test_post_detail_with_non_existent_slug(self):
        """Test that accessing a post with a non-existent slug returns a 404 error."""
        response = self.client.get(reverse('post_detail', args=['non-existent-slug']))
        self.assertEqual(response.status_code, 404)

    def test_post_list_pagination(self):
        """Test pagination on the post list page."""
        for i in range(4):
            Post.objects.create(
                title=f"Blog title {i+2}", author=self.user,
                slug=f"blog-title-{i+2}", excerpt="Blog excerpt",
                content="Blog content", status=1)
   
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)
        self.assertIn('page_obj', response.context)