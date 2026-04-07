FROM python:3.8-slim
COPY . /apKP
WORKDIR /apKP
RUN pip install -r requirements.txt
CMD python app.py