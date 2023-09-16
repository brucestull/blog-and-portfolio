from django.test import TestCase

from blog.forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test `blog.forms.CommentForm`.
    """

    def test_author_field(self):
        """
        Test `blog.forms.CommentForm.author`.
        """
        self.assertEqual(
            CommentForm.base_fields["author"].max_length,
            60,
        )
        self.assertEqual(
            CommentForm.base_fields["author"].widget.attrs,
            {
                "class": "form-control",
                "placeholder": "Your Name",
                "maxlength": "60",
            },
        )

    def test_body_field(self):
        """
        Test `blog.forms.CommentForm.body`.
        """
        self.assertEqual(
            CommentForm.base_fields["body"].widget.attrs,
            {
                "cols": "40",
                "rows": "10",
                "class": "form-control",
                "placeholder": "Leave a comment!",
            },
        )
