FROM python:3.9

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.2.2
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /home/${USERNAME}/.local/bin:${PATH}

WORKDIR /app

# Copy files
COPY . /app

# RUN pip install fastapi uvicorn
RUN poetry config virtualenvs.create false && poetry install --no-root  --no-interaction


CMD [ "uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]