from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Question(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
	subject = models.CharField(max_length=200)
	content = models.TextField()
	create_date = models.DateTimeField()
	modify_date = models.DateTimeField(null=True, blank=True)
	voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가	

	def __str__(self):
		return self.subject


class Answer(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # Question model 외래키로 가져가기 위해설정. on_delete는 질문 삭제시 모든 연관된 답변 삭제 설정=CASCADE
	content = models.TextField()
	create_date = models.DateTimeField()
	modify_date = models.DateTimeField(null=True, blank=True)
	voter = models.ManyToManyField(User, related_name='voter_answer')

