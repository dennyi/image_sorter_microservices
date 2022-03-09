FROM python:3

WORKDIR /app


COPY ./image_sorter/requirements.txt ./
COPY ./libs ./libs
RUN pip install --no-cache-dir -r requirements.txt

COPY ./image_sorter/src ./

COPY ./image_sorter/.env_container ./.env

CMD [ "python", "-u", "./" ]
