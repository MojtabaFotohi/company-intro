from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام پروژه")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='media/project_images/', blank=True, null=True, verbose_name="تصویر")
    categories = models.ManyToManyField(Category, related_name='projects', verbose_name="دسته‌بندی‌ها")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")
    is_published = models.BooleanField(default=False, verbose_name="منتشر شده")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-created_at']