FROM python:2.7-slim

ENV http_proxy http://proxy-chain.xxx.com:911/
ENV https_proxy http://proxy-chain.xxx.com:912/

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libmysqlclient-dev
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD ["python"]