# Contributing to Lab

Thank you for your interest in contributing to this project! This guide will help you set up, run, and test the project.

## Project Overview

This is a Kubernetes lab repository containing example YAML configuration files for various Kubernetes resources including deployments, services, namespaces, and storage configurations.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** - For version control
- **Python 3.6+** - For YAML validation
- **pip** - Python package manager (usually comes with Python)

Optional but recommended:
- **kubectl** - Kubernetes command-line tool (for applying configurations to a cluster)
- **A Kubernetes cluster** - To test the configurations (local or remote)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/wingerts/lab.git
cd lab
```

### 2. Install Dependencies

Install yamllint for YAML validation:

```bash
pip install yamllint
```

## Running the Project

### Viewing Configuration Files

The Kubernetes YAML files are located in the `kubernetes/` directory. You can view them with:

```bash
ls -la kubernetes/
cat kubernetes/deploy.yaml
```

### Applying Configurations to a Kubernetes Cluster

If you have a Kubernetes cluster running and `kubectl` configured:

```bash
# Apply all configurations
kubectl apply -f kubernetes/

# Apply a specific configuration
kubectl apply -f kubernetes/deploy.yaml

# View deployed resources
kubectl get deployments
kubectl get services
kubectl get namespaces
```

### Viewing Configuration Details

To understand what each configuration does:

```bash
# View deployment configuration
cat kubernetes/deploy.yaml

# View service configuration
cat kubernetes/service.yaml

# View namespace configuration
cat kubernetes/my-namespace.yaml
```

## Testing

### Validate YAML Syntax

Validate all YAML files for syntax errors:

```bash
yamllint kubernetes/
```

### Validate YAML Structure

Check that all Kubernetes resource files have required fields:

```bash
# Check for apiVersion field
find kubernetes -name "*.yaml" -exec grep -l "apiVersion:" {} \;

# Check for kind field
find kubernetes -name "*.yaml" -exec grep -l "kind:" {} \;
```

### Manual Validation

You can also manually inspect files to ensure they follow Kubernetes conventions:

```bash
# View a specific file
cat kubernetes/deploy.yaml

# Check file structure
grep -E "^(apiVersion|kind|metadata|spec):" kubernetes/deploy.yaml
```

## Project Structure

```
lab/
├── README.md                 # Project overview
├── CONTRIBUTING.md          # This file
└── kubernetes/              # Kubernetes configuration files
    ├── deploy.yaml          # Deployment configuration
    ├── service.yaml         # Service configuration
    ├── nginx.yaml           # Nginx deployment
    ├── nginx-docs.yaml      # Nginx documentation deployment
    ├── mealie-deploy.yaml   # Mealie application deployment
    ├── mealie-ns.yaml       # Mealie namespace
    ├── my-namespace.yaml    # Custom namespace
    ├── pod-storage.yaml     # Pod storage configuration
    ├── storage.yaml         # Storage configuration
    └── test.yaml            # Test file
```

## Making Changes

### Before Committing

1. **Validate YAML syntax:**
   ```bash
   yamllint kubernetes/
   ```

2. **Review your changes:**
   ```bash
   git diff
   ```

3. **Test in a cluster (if available):**
   ```bash
   kubectl apply -f kubernetes/ --dry-run=client
   ```

### Commit Guidelines

- Write clear, descriptive commit messages
- Reference issue numbers if applicable
- Keep commits focused on a single change

Example:
```bash
git add kubernetes/deploy.yaml
git commit -m "Update deployment replicas to 10"
git push origin your-branch-name
```

## Troubleshooting

### YAML Validation Errors

If `yamllint` reports errors:
- Check indentation (YAML is whitespace-sensitive)
- Ensure proper use of colons and dashes
- Verify field names match Kubernetes API specifications

### Kubernetes Deployment Issues

If `kubectl apply` fails:
- Verify the YAML syntax with `yamllint`
- Check that required fields are present (apiVersion, kind, metadata, spec)
- Ensure your cluster has the necessary resources
- Check cluster logs: `kubectl describe pod <pod-name>`

## Additional Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes YAML Reference](https://kubernetes.io/docs/concepts/configuration/overview/)
- [yamllint Documentation](https://yamllint.readthedocs.io/)

## Questions or Issues?

If you have questions or encounter issues:
1. Check existing issues on GitHub
2. Review the Kubernetes documentation
3. Open a new issue with a clear description of the problem

Thank you for contributing!
