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

## Configuration Appendix

### deploy.yaml

**Kind**: Deployment  
**Labels**: `app: test` (metadata.labels)  
**Selector**: `matchLabels: app: test`  
**Replicas**: 10  
**Image**: `httpd:alpine3.19`  
**Container Name**: `httpd`  
**Rollout Settings**: `strategy.type: RollingUpdate`, `maxUnavailable: 1`, `maxSurge: 1`  
**Template Labels**: `app: test`  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: none

### mealie-deploy.yaml

**Kind**: Deployment  
**Namespace**: mealie  
**Labels**: `app: mealie` (metadata.labels)  
**Selector**: `matchLabels: app: mealie`  
**Replicas**: 1  
**Image**: `ghcr.io/mealie-recipes/mealie:v2.8.0`  
**Container Name**: `nginx`  
**Rollout Settings**: `strategy: {}` (empty declaration)  
**Template Labels**: `app: mealie`  
**Commands**: none  
**Mounts**: `volumeMounts` with `mountPath: /app/data`, `name: mealie-data`  
**Volumes**: `volumes` with `name: mealie-data`, `persistentVolumeClaim.claimName: mealie-data`  
**PVC/Storage**: References PVC `mealie-data`  
**Ports**: `containerPort: 9000`

### mealie-ns.yaml

**Kind**: Namespace  
**Name**: mealie  
**Labels**: none  
**Selectors**: none  
**Replicas**: none  
**Images/Container Names**: none  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: none  
**Spec**: `spec: {}` (empty declaration)  
**Status**: `status: {}` (empty declaration)

### my-namespace.yaml

**Kind**: Namespace  
**Name**: my-namespace  
**Labels**: none  
**Selectors**: none  
**Replicas**: none  
**Images/Container Names**: none  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: none  
**Spec**: `spec: {}` (empty declaration)  
**Status**: `status: {}` (empty declaration)

### nginx-docs.yaml

**Kind**: Pod  
**Labels**: `hello: world` (metadata.labels)  
**Selectors**: none  
**Replicas**: none  
**Image**: `nginx:1.14.2`  
**Container Name**: `nginx`  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: `containerPort: 80`

### nginx.yaml

**Kind**: Pod  
**Labels**: `run: nginx-yaml`, `method: from-code` (metadata.labels)  
**Selectors**: none  
**Replicas**: none  
**Image**: `nginx`  
**Container Name**: `nginx`  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: none

### pod-storage.yaml

**Kind**: Pod  
**Labels**: `run: nginx-storage` (metadata.labels)  
**Selectors**: none  
**Replicas**: none  
**Images/Container Names**: Container 1: `nginx` image, `nginx-storage` name; Container 2: `busybox` image, `busybox` name  
**Rollout Settings**: none  
**Commands**: Container 2 (busybox): `command: ["/bin/sh", "-c"]`, `args: ["sleep 1000"]`  
**Mounts**: Both containers have `volumeMounts` with `mountPath: /scratch`, `name: scratch-volume`  
**Volumes**: `volumes` with `name: scratch-volume`, `emptyDir.sizeLimit: 500M`  
**PVC/Storage**: emptyDir volume (ephemeral storage)  
**Ports**: none

### service.yaml

**Kind**: Service  
**Namespace**: mealie  
**Labels**: `app: mealie` (metadata.labels)  
**Selector**: `app: mealie`  
**Replicas**: none  
**Images/Container Names**: none  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: `port: 9000`, `protocol: TCP`, `targetPort: 9000`  
**Type**: LoadBalancer

### storage.yaml

**Kind**: PersistentVolumeClaim  
**Namespace**: mealie  
**Name**: mealie-data  
**Labels**: none  
**Selectors**: none  
**Replicas**: none  
**Images/Container Names**: none  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: `accessModes: [ReadWriteOnce]`, `resources.requests.storage: 500Mi`  
**Ports**: none

### test.yaml

**Kind**: (non-manifest file)  
**Content**: Plain text file containing "test yaml file"  
**Labels**: none  
**Selectors**: none  
**Replicas**: none  
**Images/Container Names**: none  
**Rollout Settings**: none  
**Commands**: none  
**Mounts**: none  
**Volumes**: none  
**PVC/Storage**: none  
**Ports**: none

## Documentation Summary

### README.md

**Purpose**: Project description  
**Key Facts**: Repository title is "lab"; contains "Course lab examples" (2 lines total)

### docs/services.md

**Purpose**: Service inventory table  
**Key Facts**: Lists all Kubernetes Services in kubernetes/ directory; documents one service: mealie (LoadBalancer type, port 9000:9000/TCP, namespace mealie)

### docs/forge-squash-e2e-1793368148.md

**Purpose**: Forge test marker file  
**Key Facts**: Contains single line "Forge squash merge UI test 1793368148."
