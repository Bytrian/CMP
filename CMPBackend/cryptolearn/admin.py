# CMPBackend/cryptolearn/admin.py
from django.contrib import admin
from .models import Course, Lesson, Enrollment

# Opcional: Personalizar la vista de los modelos en el panel de administración
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at' # Navegación por fecha

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'video_url')
    list_filter = ('course',)
    search_fields = ('title', 'content')
    raw_id_fields = ('course',) # Util para seleccionar cursos si hay muchos

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at', 'completed', 'completion_date')
    list_filter = ('completed', 'course')
    search_fields = ('user__username', 'course__title')
    raw_id_fields = ('user', 'course') # Util para seleccionar usuarios y cursos

# Registra tus modelos
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)

