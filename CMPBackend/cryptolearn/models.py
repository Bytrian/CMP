# CMPBackend/cryptolearn/models.py
from django.db import models
from django.conf import settings # Para referenciar al AUTH_USER_MODEL

class Course(models.Model):
    """
    Modelo para representar un curso de aprendizaje.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    # Imagen de portada del curso (opcional)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True, verbose_name="Miniatura")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    is_published = models.BooleanField(default=False, verbose_name="Publicado")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['title'] # Ordenar cursos por título por defecto

    def __str__(self):
        return self.title

class Lesson(models.Model):
    """
    Modelo para representar una lección dentro de un curso.
    """
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, verbose_name="Curso")
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido de la Lección")
    order = models.PositiveIntegerField(verbose_name="Orden de la Lección") # Para definir el orden de las lecciones
    video_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="URL del Video (opcional)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Lección"
        verbose_name_plural = "Lecciones"
        ordering = ['course', 'order'] # Ordenar por curso y luego por orden
        unique_together = ('course', 'order') # No puede haber dos lecciones con el mismo orden en el mismo curso

    def __str__(self):
        return f"{self.course.title}: {self.title}"

class Enrollment(models.Model):
    """
    Modelo para registrar la inscripción de un usuario en un curso.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Usuario")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Curso")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    completed = models.BooleanField(default=False, verbose_name="Completado")
    completion_date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Finalización")

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ('user', 'course') # Un usuario solo puede inscribirse una vez en un curso
        ordering = ['enrolled_at']

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

