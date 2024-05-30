FROM python:3.11

RUN apt update && apt install iproute2 iputils-ping -y

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backendserver.py ./
COPY docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh

RUN touch init.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
