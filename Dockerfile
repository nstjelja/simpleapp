FROM python:3.12.11
WORKDIR /app
EXPOSE 5555
ADD requirements.txt requirements.txt
ADD app.py app.py
RUN pip install -r requirements.txt
CMD python app.py