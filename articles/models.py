from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    ceated_at = models.DateTimeField(auto_now_add=True) # 수정 할때 자동으로 업데이트
    updatee_at = models.DateTimeField(auto_now=True)  # 생성이 될때 자동으로 업데이트
    

