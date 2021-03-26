FROM python:3.9
WORKDIR /code
#ENV CI=1
COPY . .
RUN pip install -r requirements.txt
RUN pip install -e src
CMD pytest ./tests
