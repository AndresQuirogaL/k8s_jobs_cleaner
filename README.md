# k8s_jobs_cleaner

### Construir imagen

~~~
$ docker build -t k8s_jobs_cleaner:latest .
~~~

### Levantar CronJob

~~~
$ kubectl create -f clear_jobs_cronjob.yaml
~~~
