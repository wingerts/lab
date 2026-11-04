# CP25-CEDAR

## Kubernetes Manifest Inventory

| Filename | Kind | metadata.name | containerPort | service port | targetPort |
|----------|------|---------------|---------------|--------------|------------|
| deploy.yaml | Deployment | test | none | none | none |
| mealie-deploy.yaml | Deployment | mealie | 9000 | none | none |
| mealie-ns.yaml | Namespace | mealie | none | none | none |
| my-namespace.yaml | Namespace | my-namespace | none | none | none |
| nginx-docs.yaml | Pod | nginx-docs | 80 | none | none |
| nginx.yaml | Pod | nginx-yaml | none | none | none |
| pod-storage.yaml | Pod | nginx-storage | none | none | none |
| service.yaml | Service | mealie | none | 9000 | 9000 |
| storage.yaml | PersistentVolumeClaim | mealie-data | none | none | none |
| test.yaml | (non-manifest file) | - | - | - | - |

Review only; do not apply manifests.
