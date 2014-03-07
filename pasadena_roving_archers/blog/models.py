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
        return "%s:%s" % (self.order, self.name)


class ArcheryClassType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ArcheryClass(models.Model):
    date = models.DateTimeField("Date of class")
    type = models.ForeignKey(ArcheryClassType)

    def __unicode__(self):
        return "%s @ %s" % (self.type, self.date.date())