FROM redhat/usi8
RUN yum install python3- y
RUN pip3install flask
COPY app.py /app.py
CMD ["python3","/app.py"]
