FROM python:3.9
WORKDIR /code

COPY . .
RUN pip install -r requirements.txt
RUN pip install -e src
ENV FLASK_APP=/code/src/entrypoints/server.py
EXPOSE ${FLASK_RUN_PORT}
CMD python3 ${FLASK_APP}
