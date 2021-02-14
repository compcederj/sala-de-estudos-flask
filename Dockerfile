FROM python:3.9.1


WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN mv pyproject.toml py.toml && \
    pip install -U pip && \
    pip install -e . && \
    mv py.toml pyproject.toml

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]
