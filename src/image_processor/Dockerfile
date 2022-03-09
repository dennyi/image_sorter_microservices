FROM python:3

WORKDIR /app


COPY ./image_processor/requirements.txt ./
COPY ./libs ./libs
RUN pip install --no-cache-dir -r requirements.txt

COPY ./image_processor/src ./

COPY ./image_processor/.env_container ./.env

CMD [ "python", "-u", "./" ]
