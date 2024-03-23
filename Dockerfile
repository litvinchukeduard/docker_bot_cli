FROM python:3.12

ENV APP_HOME /app

WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN python -m venv .venv
RUN pip install .


# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["my-bot-cli"]