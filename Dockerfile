FROM python:3.6.6-stretch
ADD . .
RUN pip3 install -r requirements.txt
CMD ["python3", "loginator.py"]
