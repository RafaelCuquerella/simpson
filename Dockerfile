FROM python:3.9.12

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/ 

RUN mkdir Lisa
RUN mkdir Homer
RUN mkdir General

RUN pip3 install -r ./requirements.txt

CMD ["python","main.py"]