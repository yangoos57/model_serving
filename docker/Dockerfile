
FROM python:3.9.16-slim-bullseye

ENV DIR model_server

RUN apt-get update -y && apt-get install -y gcc

COPY ./docker/requirements.txt ${DIR}/

COPY ./App ${DIR}/app

COPY ./data ${DIR}/data

COPY ./models ${DIR}/models

WORKDIR /${DIR}

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

WORKDIR /${DIR}/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
