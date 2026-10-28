# GitOps with Argo CD and Helm

GitOps declares desired state in version control; a controller continuously reconciles it with a target environment. Argo CD sync status reports comparison/sync outcomes, while health reports resource health—neither replaces application SLOs.

Helm packages templates and values. Keep values environment-specific but secrets outside plain Git (for example, an approved external-secret pattern). Render and validate charts in CI; a syntactically valid manifest can still be operationally wrong.

## Drift and rollback

Investigate drift before forcing sync: it may be an emergency mitigation, another controller, a defaulted field, or an unauthorized change. Revert the Git revision for a declarative rollback, confirm reconciliation, then validate service behavior. Avoid automated prune until ownership and deletion blast radius are understood.

**Interview question:** An app is OutOfSync after a manual hotfix. Preserve the change details, decide whether it is the intended emergency state, commit the intended desired state or revert it safely, then reconcile. Improve the emergency-change process rather than normalizing drift.
