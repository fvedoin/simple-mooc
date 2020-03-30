from django.db import models

#tem que rodar python manage.py makemigrations courses antes da migration
#ou sem o courses para fazer a migration em tudo
class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(description__icontains=query)
        )

class Course(models.Model):

    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    #campo pode ser em branco (nível de formulário)
    description = models.TextField(
        'Descrição', blank=True
    )
    about = models.TextField(
        'Sobre o curso', blank=True
    )
    #pode ser nulo (nível de bd)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    #precisa dar easy_install Pillow
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        #-name para ser decrescente
        ordering = ['name']
