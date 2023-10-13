FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install Compilers for UWSGI
RUN apk add --no-cache gcc musl-dev linux-headers

# Install Poetry
RUN pip install poetry

# Copy Poetry files
COPY pyproject.toml /app/

# Install dependencies with poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --extras "production"

# Copy entrypoint
COPY ./entrypoint.sh /app/entrypoint.sh
# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh
# Copy UWSGI config
COPY ./uwsgi.ini /app/uwsgi.ini

# Copy project. Adding folders manually to avoid copying things we don't want in the image
COPY ./manage.py /app
COPY ./app /app/app
COPY ./red_mascotera /app/red_mascotera

# Entry point
ENTRYPOINT ["/app/entrypoint.sh"]

# Main command
CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]

