import itertools

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.object.job_set.all()
        finished_jobs = [job for job in jobs if job.finished]
        context['finished'] = all([job.finished for job in jobs])
        context['n_finished'] = len(finished_jobs)
        context['n_jobs'] = len(jobs)
        context['progress'] = context['n_finished'] / context['n_jobs'] * 100

        sorted_jobs = sorted(finished_jobs, key=lambda job:job.output)
        groups = itertools.groupby(sorted_jobs, key=lambda job:job.output)
        context['outputs'] = [{'output':k, 'jobs': list(v)} for k, v in groups]
        print(context['outputs'])
        return context