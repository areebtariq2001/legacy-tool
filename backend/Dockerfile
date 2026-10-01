FROM python:3.11-slim

# Bug (reported by the user, secondary/minor, 29th bug report): without this, Python's stdout
# is block-buffered (not line-buffered) when it isn't attached to a real terminal - which is
# always true inside a Docker container. main.py uses plain print() in a few places for
# warnings (e.g. around line 969), and Docker/`docker compose logs` captures stdout, so those
# warnings could sit in Python's internal buffer and appear late, out of order, or not at all
# if the process is killed before the buffer flushes - undermining the point of having
# structured logging in the first place (nginx's own JSON access log has no such gap, but the
# backend's own print()-based warnings did). PYTHONUNBUFFERED=1 forces stdout/stderr to be
# unbuffered so every print() reaches the container logs immediately.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Bug/gap (reported by the user): this container ran as root the whole time - the default for
# any Dockerfile with no USER directive. This process doesn't need root for anything it
# actually does (it binds to port 8000, not a privileged port below 1024, and installs no
# packages at runtime - pip install above already ran earlier in the build, while still root,
# so switching users here doesn't block that). If the FastAPI app or a dependency were ever
# exploited via a code-execution bug, a root process inside the container has a meaningfully
# easier path to escalate further (container-escape CVEs, anything mounted into the
# container) than an unprivileged one would - this is defense in depth, not a fix for any
# specific known vulnerability. The one thing this app writes to disk at runtime
# (approval_log.json, a relative path under WORKDIR /app - confirmed via the only local
# "open(..., 'w')" call in main.py; everything else goes to an external Postgres DB via
# DATABASE_URL) still needs to be writable, so /app is chown'd to the new user before
# switching to it.
RUN useradd --create-home --shell /usr/sbin/nologin appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips=*"]
