from django.views.generic import CreateView, DetailView

from .tasks import launch_the_jobs
from .models import Run


class HomeView(CreateView):
    model = Run
    template_name = "home.html"
    fields = ['code']

    def form_valid(self, form):
        response = super().form_valid(form)
        launch_the_jobs.delay(self.object.pk)
        return response

class RunView(DetailView):
    model = Run