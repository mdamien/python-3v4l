# Create your tasks here
from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task

from .models import Job, Run

versions = [
    ('python:3.4-alpine',),
    ('python:3.5-alpine',),
    ('python:3.6-alpine',),
    ('python:3.7-alpine',),
    ('python:3.8-alpine',),
    ('python:3.9-rc-alpine',),
    ('pypy:3-slim', 'pypy3'),
    ('pypy:2-slim', 'pypy'),
]


def launch_the_jobs(run):
    for version in versions:
        job = Job.objects.create(
            run=run,
            python_version=version[0],
        )
        do_a_job.delay(job.pk, *version)


@shared_task
def do_a_job(job_pk, python_version, executable='python'):
    job = Job.objects.get(pk=job_pk)
    python_version = job.python_version
    code = job.run.code

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
