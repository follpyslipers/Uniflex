# FROM python:3.11

# ENV http_proxy http://proxy-chain.xxx.com:911/
# ENV https_proxy http://proxy-chain.xxx.com:912/

# WORKDIR /app

# COPY requirements.txt.

# RUN pip install --no-cache-dir -r requirements.txt

# COPY..

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]