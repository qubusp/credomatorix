FROM python:3.6.6-stretch
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "loginator.py"]