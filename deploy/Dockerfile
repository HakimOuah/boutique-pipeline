FROM python:3.12-slim

RUN useradd --create-home --uid 10001 dropilot
WORKDIR /app

COPY pyproject.toml README.md ./
COPY dropilot ./dropilot
COPY broyeur ./broyeur
COPY config ./config
RUN pip install --no-cache-dir .

USER dropilot
EXPOSE 8787
CMD ["dropilot", "serve", "--host", "0.0.0.0", "--port", "8787"]

