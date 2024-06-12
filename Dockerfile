FROM python:3.11

WORKDIR /app

ENV OSS_ACCESS_KEY_ID='LTAI5tCub24r8bcgejLVfLZf'
ENV OSS_ACCESS_KEY_SECRET='UZDCPmE9PL7JIFg2q148T6agZitSdB'
ENV OSS_BUCKET_NAME='uniabujaflexUnmodifiable'
ENV OSS_ENDPOINT='oss-us-west-1.aliyuncs.com'

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]