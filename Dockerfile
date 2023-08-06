FROM python:3.11.3

RUN apt-get upgate -y

RUN apt-get install tk -y

CMD ["/app/tkinter_app.py"]
ENTRYPOINT ["python3"]