# CP25-MAPLE

## Manifest Inventory

| Filename | Kind | metadata.name | Namespace | containerPort | Service port | targetPort |
|----------|------|---------------|-----------|---------------|--------------|------------|
| deploy.yaml | Deployment | test | none | none | none | none |
| mealie-deploy.yaml | Deployment | mealie | mealie | 9000 | none | none |
| mealie-ns.yaml | Namespace | mealie | none | none | none | none |
| my-namespace.yaml | Namespace | my-namespace | none | none | none | none |
| nginx-docs.yaml | Pod | nginx-docs | none | 80 | none | none |
| nginx.yaml | Pod | nginx-yaml | none | none | none | none |
| pod-storage.yaml | Pod | nginx-storage | none | none | none | none |
| service.yaml | Service | mealie | mealie | none | 9000 | 9000 |
| storage.yaml | PersistentVolumeClaim | mealie-data | mealie | none | none | none |
| test.yaml | (non-manifest: plain text file) | none | none | none | none | none |

Review only; do not apply manifests.
