FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR ${APP_ROOT}

COPY ./requirements.txt ${APP_ROOT}
RUN pip install -r requirements.txt

COPY . ${APP_ROOT}
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0", "config.wsgi:application"]

