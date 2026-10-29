# Kubernetes Files Summary

- **deploy.yaml**: Deployment of 10 httpd:alpine3.19 replicas with rolling update strategy.
- **mealie-deploy.yaml**: Single-replica Mealie v2.8.0 deployment in mealie namespace with persistent volume mount at /app/data.
- **mealie-ns.yaml**: Namespace definition for mealie.
- **my-namespace.yaml**: Namespace definition for my-namespace.
- **nginx-docs.yaml**: Single nginx:1.14.2 pod with label hello=world.
- **nginx.yaml**: Single nginx pod with labels run=nginx-yaml and method=from-code.
- **pod-storage.yaml**: Pod with nginx and busybox containers sharing a 500M emptyDir volume at /scratch.
- **service.yaml**: LoadBalancer service exposing Mealie on port 9000 in mealie namespace.
- **storage.yaml**: PersistentVolumeClaim for Mealie with 500Mi storage and ReadWriteOnce access mode.
- **test.yaml**: Placeholder file containing only "test yaml file" text.
