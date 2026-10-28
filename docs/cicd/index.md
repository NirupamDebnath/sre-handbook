# CI/CD and deployment safety

A delivery pipeline turns a reviewed revision into a verifiable release. Separate build, test, artifact, deploy, and post-deploy verification; record artifact digest and source revision so a rollback is precise.

## Safe release controls

- Use short-lived workload identity and a minimal deployment role.
- Verify provenance, dependency policy, tests, and rendered configuration before promotion.
- Prefer progressive rollout with SLI-based checks and automatic/explicit halt criteria.
- Keep migration compatibility and rollback semantics in the release plan.

Jenkins shared libraries can standardize trusted pipeline behavior; CodeBuild/CodePipeline and GitHub Actions should use isolated identities and explicit artifact boundaries. A failed pipeline may be source, dependency, credentials, runner, artifact, environment, or deployment health—start with the first failing stage and correlate timestamps.

**Interview question:** Why can a green CI build still be unsafe? Unit tests do not validate production configuration, dependencies, permissions, capacity, or user journey. Add environment-aware checks and limited exposure without treating a canary as proof against every failure mode.
