# Terraform and infrastructure as code

Terraform plans desired resource changes against configuration and state. State is sensitive operational data; use remote encrypted storage, locking where supported, restricted access, and backups. Never hand-edit state as a first response to drift.

```bash
terraform fmt -check
terraform validate
terraform plan -out=tfplan     # review before applying
terraform show tfplan
```

Modules should expose small, stable interfaces and avoid implicit provider configuration where that obscures ownership. Imports adopt existing resources but do not make configuration correct automatically. Drift can be an emergency change, a provider behavior, or a modeling gap: inspect it before deciding whether to reconcile or intentionally update configuration.

**Interview question:** Two applies conflict. Stop concurrent writers, identify the backend lock/state owner, avoid force-unlock until the holder is proven stale, refresh/replan from a known revision, and add CI serialization or reviewed change controls.
