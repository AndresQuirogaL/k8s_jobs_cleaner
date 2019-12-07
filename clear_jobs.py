from kubernetes import client
from kubernetes import config
from kubernetes.client.rest import ApiException


config.load_incluster_config()
k8s_batch_client = client.BatchV1Api()

# corp-datascience-dev-pre
try:
    api_response = k8s_batch_client.list_namespaced_job('api')
    for job in api_response.items:
        status = job.status
        job_name = job.metadata.labels['job-name']

        if status.failed:
            k8s_batch_client.delete_namespaced_job(
                name=job_name,
                namespace='api',
                body=client.V1DeleteOptions(
                    propagation_policy='Foreground',
                )
            )

            print("Deleted job %s\n. Status Failed" % job_name)

except ApiException as e:
    print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)
