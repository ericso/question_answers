from django.db import models

class Question(models.Model):
  """
  """
  text = models.TextField()

  def __str__(self):
    return(self.text)


class Answer(models.Model):
  """
  """
  text = models.TextField()
  count = models.IntegerField(default=0)
  question = models.ForeignKey(Question)

  def __str__(self):
    return("%s | %s times selected" % (self.text, self.count))
