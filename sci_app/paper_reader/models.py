from django.db import models


class Author(models.Model):
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50, default='N/A')
    l_name = models.CharField(max_length=50)
    scopus_author_id = models.IntegerField(default=0)
    staff_member = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name+" "+self.l_name


class PType(models.Model):
    type_name = models.CharField(max_length=30, default='N/A')
    description = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.type_name


class Source(models.Model):
    name = models.TextField(null=True)
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    year_published = models.IntegerField(default=2019)
    p_type = models.ForeignKey(PType, models.CASCADE, blank=False)

    def __str__(self):
        result = self.name

        if self.volume:
            result += " (V."+str(self.volume)

        if self.number:
            result += ", No."+str(self.number)+")"

        return result


class Paper(models.Model):
    title = models.TextField(max_length=150, blank=False)
    source = models.ForeignKey(Source, models.CASCADE, blank=False)
    start_page = models.IntegerField(null=True)
    end_page = models.IntegerField(null=True)
    doi = models.TextField(max_length=15, blank=True)
    file = models.FileField(upload_to="papers/", null=True, blank=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Authored(models.Model):
    p_title = models.ForeignKey(Paper, on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)

