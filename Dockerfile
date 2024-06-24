FROM python:3.9.1

EXPOSE 80
WORKDIR /app
COPY . .


RUN apt-get update && apt-get install -y curl

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

ARG VERSION
ENV APP_VERSION=$VERSION
RUN echo "APP_VERSION = $APP_VERSION"

ARG STACK
ENV STACK=${STACK}
RUN echo "STACK = $STACK"

ENTRYPOINT ["python", "main.py"]
