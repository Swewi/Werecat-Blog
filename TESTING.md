# Werecat Blog Testing

## Blog Page Testing

I conducted both automated and manual testing for the blog posts/comments page:

### Automated Testing:

In total I constructed 21 tests to test the majority of the functions within the Blog, broken down into 3 sections:

| Catagory | Test description | Expected outcome | Notes |
| --- | --- | --- | --- |
| Model Testing: | | | |
| Post Model Testing | | | |
| | test_default_status | Verifies the default status value for a Post is Draft | Pass |
| | test_slug_uniqueness | Ensures that each Post must have a unique slug | Pass |
| | test_featured_image_default | Checks that the default value for featured_image is 'placeholder' | Pass |
| | test_related_name_for_author | Verifies the related_name attribute blog_posts allows access to posts by the author | Pass |
| | test_ordering | Ensures Post instances are ordered by created_on in descending order | Pass |
| | test_slug_generation | Confirms that the slug is automatically generated based on the title if not provided | Pass |
| Comment Model Testing | | | |
| | test_comment_ordering | Verifies that comments are ordered by created_on in ascending order | Pass |
| | test_related_name_for_post_comments | Checks that the related_name attribute comments allows access to comments on a post | Pass |
| | test_related_name_for_author_comments | Ensures that the related_name attribute comments_author allows access to comments authored by a specific user | Pass |
| | | | |
| Form Testing: | | | |
| Test Comment Form | | | |
| | test_form_is_valid | Checks that the form is valid when a non-empty comment body is provided | Pass |
| | test_form_is_invalid | Ensures the form is invalid when the comment body is empty | Pass |
| | | | |
| View Testing: | | | |
| Post Detail and List Views | | | |
| | test_render_post_detail_page_with_comment_form | Verifies that the post_detail view renders the post with the comment form | Pass |
| | test_post_list_page | Ensures that the home view (post list) loads correctly and displays posts | Pass |
| | test_post_list_pagination | Tests pagination on the post list page | Pass |
| | test_post_detail_with_non_existent_slug | Verifies that accessing a post with a non-existent slug returns a 404 error | Pass |
| Comment Submission and Editing | | | |
| | test_successful_comment_submission | Verifies that a logged-in user can successfully submit a comment | Pass |
| | test_comment_submission_without_login | Ensures that unauthenticated users cannot submit comments and are redirected to the login page | Pass |
| | test_comment_edit | Checks that a user can edit their own comment | Pass |
| | test_comment_edit_by_different_user | Ensures that a user cannot edit another user's comment | Pass |
| Comment Deletion | | | |
| | test_comment_deletion | Verifies that a user can delete their own comment | Pass |
| | test_comment_deletion_by_different_user | Ensures that a user cannot delete another user's comment | Pass |

---

| ![Image 1](static/images/readme/testing/blog-tests.png) | ![Image 2](static/images/readme/testing/blog-models-test.png) |
|:-------------------------------------------:|:-------------------------------------------:|
| **Overall Blog Test output** | **Blog Model Test Output** |
| ![Image 3](static/images/readme/testing/blog-form-test.png) | ![Image 4](static/images/readme/testing/blog-veiws-test.png) |
| **Blog Form Test Output** | **Blog Veiw Test Output** |

### Manual Testing:

