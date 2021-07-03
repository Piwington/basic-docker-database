FROM python:3

WORKDIR /python

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY python/ .

CMD [ "python", "server.py" ]