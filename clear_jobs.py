import os

from datetime import datetime

from kubernetes import client
from kubernetes import config
from kubernetes.client.rest import ApiException

namespace = os.environ.get('NAMESPACE')

config.load_incluster_config()
k8s_batch_client = client.BatchV1Api()

# corp-datascience-dev-pre
try:
    api_response = k8s_batch_client.list_namespaced_job(namespace)
    for job in api_response.items:
        status = job.status
        job_name = job.metadata.labels['job-name']

        if status.failed:
            k8s_batch_client.delete_namespaced_job(
                name=job_name,
                namespace=namespace,
                body=client.V1DeleteOptions(
                    propagation_policy='Foreground',
                )
            )

        if status.succeeded:
            now = datetime.now()
            completion_time = status.completion_time
            secconds_diff = (now - completion_time.replace(tzinfo=None)).total_seconds()

            if secconds_diff >= 60:
                k8s_batch_client.delete_namespaced_job(
                    name=job_name,
                    namespace=namespace,
                    body=client.V1DeleteOptions(
                        propagation_policy='Foreground',
                    )
                )

except ApiException as e:
    print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)
