# Kubernetes Files Summary

- **deploy.yaml**: Deployment of 10 replicas of httpd:alpine3.19 with rolling update strategy (max 1 unavailable, max 1 surge).
- **mealie-deploy.yaml**: Deployment of Mealie recipe application (v2.8.0) with 1 replica in mealie namespace, mounting persistent volume at /app/data.
- **mealie-ns.yaml**: Namespace definition for the mealie application.
- **my-namespace.yaml**: Namespace definition for my-namespace.
- **nginx-docs.yaml**: Pod running nginx:1.14.2 with label hello=world and port 80 exposed.
- **nginx.yaml**: Pod running nginx image with labels run=nginx-yaml and method=from-code.
- **pod-storage.yaml**: Pod with nginx and busybox containers sharing an emptyDir volume (500M limit) mounted at /scratch.
- **service.yaml**: LoadBalancer service for mealie application in mealie namespace, exposing port 9000.
- **storage.yaml**: PersistentVolumeClaim for mealie-data with 500Mi storage and ReadWriteOnce access mode in mealie namespace.
- **test.yaml**: Placeholder test yaml file.
