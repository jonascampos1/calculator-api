FROM python:3.9-alpine

RUN mkdir -p /home/app

COPY . /home/app

RUN pip install --no-cache-dir -r home/app/requirements.txt

EXPOSE 3000

CMD ["python","-u","/home/app/setup.py"]