from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField('Blog content')
    pub_date = models.DateTimeField('Date published')
    image = models.TextField('Image')

    def __unicode__(self):
        return "%s:%s" % (self.pub_date, self.title)

class HeaderElement(models.Model):
    name = models.CharField(max_length=50)
    link = models.TextField(max_length=100)
    order = models.IntegerField()
    def __unicode__(self):
        return self.name
