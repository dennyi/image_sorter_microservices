FROM python:3

WORKDIR /app


COPY ./image_loader/requirements.txt ./
COPY ./libs ./libs
RUN pip install --no-cache-dir -r requirements.txt

COPY ./image_loader/src ./

COPY ./image_loader/.env_container ./.env

CMD [ "python", "-u", "./" ]
