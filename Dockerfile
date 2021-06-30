FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Basic Dockerfile Template. Temp Comment Out Unused.
#TODO Delete Any Still Commented After Completion.
#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]