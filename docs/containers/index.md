# Containers

An image is an immutable filesystem plus metadata; a container is a runtime process with namespaces and cgroup resource controls. Containers share the host kernel, so isolation is not equivalent to a virtual machine.

Use small, pinned base images, non-root users, read-only filesystems when possible, minimal capabilities, and image scanning/signing. Set CPU and memory limits with workload testing; a limit is a safety boundary, not a capacity plan.

```dockerfile
FROM python:3.13-slim
RUN useradd --create-home app
USER app
WORKDIR /app
COPY --chown=app:app app.py .
CMD ["python", "app.py"]
```

**Troubleshooting:** compare exit code, stderr, image architecture, mounted configuration, process PID 1 behavior, and cgroup OOM events. Do not solve a crash by granting privileged mode without understanding the requirement.
