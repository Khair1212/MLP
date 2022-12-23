FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE $PORT
#CMD python ./app.py

#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "wsgi:app" ]
#CMD ["app.py"]

#EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
