from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.

User = get_user_model()


class Post(models.Model):
    """
    This Postm model accepts author, title, and Description
    Created during Django models task in zuri internship programme
    """

    author = models.ForeignKey(User, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=200)
    text = models.TextField(_("Text"))
    created_date = models.DateTimeField(
        _("Created"), auto_now_add=True)
    published_date = models.DateTimeField(_("Published"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
