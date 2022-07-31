FROM python:3.10.5

VOLUME vol1

ADD main.py .
ADD get.py .
ADD csvMaker.py .
ADD listMaker.py .

RUN pip install requests

CMD [ "python", "./main.py" ]

