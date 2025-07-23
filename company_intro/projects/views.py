from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Project, Category

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        queryset = Project.objects.filter(is_published=True).order_by('-created_at')
        category_slug = self.request.GET.get('category')
        search_query = self.request.GET.get('search')
        if category_slug:
            queryset = queryset.filter(categories__slug=category_slug)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.filter(is_published=True)