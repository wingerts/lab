# Kubernetes YAML Files

This directory contains Kubernetes manifest files for various deployments and configurations. All YAML files have been validated and are syntactically correct.

## File Documentation

### Namespace Files

#### `mealie-ns.yaml`
- **Kind**: Namespace
- **Purpose**: Creates a dedicated namespace named `mealie` for the Mealie recipe application
- **Details**: Provides namespace isolation for Mealie-related resources

#### `my-namespace.yaml`
- **Kind**: Namespace
- **Purpose**: Creates a custom namespace named `my-namespace`
- **Details**: General-purpose namespace for organizing resources

### Pod Files

#### `nginx.yaml`
- **Kind**: Pod
- **Purpose**: Simple Nginx pod for testing
- **Image**: `nginx:latest`
- **Labels**: `run: nginx-yaml`, `method: from-code`
- **Details**: Basic pod definition created from code

#### `nginx-docs.yaml`
- **Kind**: Pod
- **Purpose**: Nginx pod with documentation/example configuration
- **Image**: `nginx:1.14.2`
- **Port**: 80 (HTTP)
- **Labels**: `hello: world`
- **Details**: Example pod with explicit port configuration

#### `pod-storage.yaml`
- **Kind**: Pod
- **Purpose**: Multi-container pod demonstrating shared storage
- **Containers**:
  - `nginx-storage`: Nginx container mounting shared volume at `/scratch`
  - `busybox`: Busybox container for testing, also mounting the shared volume
- **Storage**: EmptyDir volume named `scratch-volume` with 500M size limit
- **Details**: Demonstrates inter-pod communication through shared volumes

### Deployment Files

#### `deploy.yaml`
- **Kind**: Deployment
- **Purpose**: Test deployment with rolling update strategy
- **Image**: `httpd:alpine3.19`
- **Replicas**: 10
- **Strategy**: RollingUpdate with maxUnavailable=1, maxSurge=1
- **Labels**: `app: test`
- **Details**: High-availability deployment with controlled rollout

#### `mealie-deploy.yaml`
- **Kind**: Deployment
- **Purpose**: Mealie recipe application deployment
- **Namespace**: `mealie`
- **Image**: `ghcr.io/mealie-recipes/mealie:v2.8.0`
- **Replicas**: 1
- **Port**: 9000
- **Storage**: Mounts PersistentVolumeClaim `mealie-data` at `/app/data`
- **Details**: Production deployment with persistent storage for recipe data

### Service Files

#### `service.yaml`
- **Kind**: Service
- **Purpose**: LoadBalancer service for Mealie application
- **Namespace**: `mealie`
- **Type**: LoadBalancer
- **Port**: 9000 (TCP)
- **Selector**: Routes traffic to pods with label `app: mealie`
- **Details**: Exposes Mealie deployment externally via LoadBalancer

### Storage Files

#### `storage.yaml`
- **Kind**: PersistentVolumeClaim
- **Purpose**: Storage claim for Mealie application data
- **Namespace**: `mealie`
- **Name**: `mealie-data`
- **Access Mode**: ReadWriteOnce
- **Storage Size**: 500Mi
- **Details**: Provides persistent storage for Mealie recipe database and files

### Test Files

#### `test.yaml`
- **Purpose**: Placeholder test file
- **Details**: Contains only text content, not a valid Kubernetes manifest

## Validation

All YAML files in this directory have been validated using Python's `pyyaml` library. To validate the files:

```bash
python3 ../validate_yaml.py
```

## Deployment Order

For a complete Mealie deployment, apply resources in this order:

1. `mealie-ns.yaml` - Create namespace
2. `storage.yaml` - Create PersistentVolumeClaim
3. `mealie-deploy.yaml` - Deploy Mealie application
4. `service.yaml` - Expose service

## Related Files

- `../validate_yaml.py` - Python script for YAML validation
