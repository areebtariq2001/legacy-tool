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

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips=*"]
