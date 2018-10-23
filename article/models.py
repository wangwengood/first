from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=False, default=1)
    is_delete = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)
    def __str__(self):
        return '<Article: %s>' % self.content