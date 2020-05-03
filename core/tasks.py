# Create your tasks here
from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task

from .models import Job, Run


@shared_task
def launch_the_jobs(run_pk):
    do_a_job.delay(run_pk, 'python:3.4-alpine')
    do_a_job.delay(run_pk, 'python:3.5-alpine')
    do_a_job.delay(run_pk, 'python:3.6-alpine')
    do_a_job.delay(run_pk, 'python:3.7-alpine')
    do_a_job.delay(run_pk, 'python:3.8-alpine')
    do_a_job.delay(run_pk, 'python:rc-alpine')
    do_a_job.delay(run_pk, 'pypy:3-slim', 'pypy3')
    do_a_job.delay(run_pk, 'pypy:2-slim', 'pypy')


@shared_task
def do_a_job(run_pk, python_version, executable='python'):
    run = Run.objects.get(pk=run_pk)
    code = run.code

    job = Job.objects.create(
        run=run,
        python_version=python_version,
    )

    os.mkdir(f'jobs/{job.pk}')
    filename_code = f'jobs/{job.pk}/code.py'
    output_file = f'jobs/{job.pk}.out'
    open(filename_code, 'w').write(code)
    job_dir = os.path.abspath(f"jobs/{job.pk}")
    cmd = f'docker run -it --rm -v {job_dir}:/usr/src/myapp -w /usr/src/myapp {python_version} {executable} code.py > {output_file}'
    print('cmd', cmd)
    os.system(cmd)

    output = open(output_file).read()
    print('output', output)

    job.output = output
    job.finished = True
    job.save()
