from django.db import models

class Articles(models.Model):
    title = models.CharField('Назавание', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст',)
    date = models.DateTimeField('Дата публикации')
    image = models.FileField(upload_to='img/')

    def get_absolute_url(self):
        return f'/News/{self.id}'

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Articles', on_delete=models.CASCADE)


