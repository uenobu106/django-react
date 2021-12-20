from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=50)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __srt__(self):
    return self.title