from django.db import models

#class Author(models.Model):
#    name = models.CharField(db_index=True)
#
#    def __str__(self):
#                return self.name
#    class Meta:
#        verbose_name_plural = 'Materials'
#        ordering = ('name')


class Material(models.Model):
    PAPER = 'PAPER'
    BOOK = 'BOOK'
    AUDIO = 'AUD'
    VIDEO = 'VID'
    ARTWORK = 'ART'
    POST = 'POST'

    MATERIAL_KIND = (
        (PAPER, 'paper'),
        (BOOK, 'book'),
        (AUDIO, 'audio'),
        (VIDEO, 'video'),
        (POST, 'post'),
        (ARTWORK, 'artwork')
    )
    title = models.CharField(max_length=120, unique=True)
    subtitle = models.CharField(max_length=120, blank=True, null=True)
    summary = models.TextField(blank=True)
    publication = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=120, blank=True)
#    author = models.ForeignKey('Author', related_name='paper_authors')
    authors = models.CharField(max_length=120, blank=True)
    artists = models.CharField(max_length=120, blank=True)
    original_language = models.CharField(max_length=60, null=True, blank=True)
    kind = models.CharField(max_length=5, choices=MATERIAL_KIND,
                            default=PAPER, db_index=True)
    url = models.URLField(blank=True)
    year = models.PositiveIntegerField(db_index=True)
    original_year = models.PositiveIntegerField(null=True, blank=True)
    read = models.BooleanField(default=False)

    def fields(self):
        return '.\n'.join([f.name for f in self.field_set.all()])

    def __str__(self):
                return self.title
    class Meta:
        verbose_name_plural = 'Materials' 
        ordering = ('title', 'kind', 'year')


class Field(models.Model):
    name = models.CharField(max_length=120, unique=True, db_index=True)
    materials = models.ManyToManyField(Material)

    def related_materials(self):
        from django.urls import reverse
        from django.utils.html import format_html
        return '.\n'.join([format_html("<a href='{}'>{}</a>", reverse('admin:phd_material_change', args=(m.id,)), m.title) for m in self.materials.all()])
#        materials = []
#        for m in self.materials.all():
#            url = reverse('admin:phd_material_change', args=(m.id,))
#            material = format_html("<a href='{}'>{}</a>", url, m.title)
#            materials.append(material)
#        return materials

    def __str__(self):
                return self.name

    class Meta:
        verbose_name_plural = 'Fields'
        ordering = ('name',)


class Concept(models.Model):
    subject = models.CharField(max_length=120, unique=True, db_index=True)
    method = models.TextField(blank=True)
    meterials = models.ManyToManyField(Material)
    fields = models.ManyToManyField(Field)
    community = models.CharField(max_length=120, blank=True)

    def __str__(self):
                return self.subject

    class Meta:
        verbose_name_plural = 'Concepts'
        ordering = ('subject',)


class Note(models.Model):
    paragraph = models.TextField()
    material = models.ForeignKey(Material, models.SET_NULL,
                                 blank=True, null=True,
                                 related_name='notes')

    def __str__(self):
                return 'fron {}'.format(self.material)
    class Meta:
        verbose_name_plural = 'Notes'


class Chapter(models.Model):
    title = models.CharField(max_length=120, unique=True, db_index=True)
    materials = models.ManyToManyField(Material)
    notes = models.ManyToManyField(Note)
    fields = models.ManyToManyField(Field)

    def __str__(self):
                return self.title

    class Meta:
        verbose_name_plural = 'Chapters'
        ordering = ('title',)
