from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    excerpt = models.TextField(max_length=500, blank=True, verbose_name="خلاصه")
    content = models.TextField(verbose_name="محتوا")
    image = models.ImageField(upload_to='media/blog_images/', blank=True, null=True, verbose_name="تصویر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")
    is_published = models.BooleanField(default=False, verbose_name="منتشر شده")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ['-created_at']