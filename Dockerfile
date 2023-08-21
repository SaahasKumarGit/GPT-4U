FROM python:3.9

WORKDIR /webapp

COPY ./ /webapp

RUN pip install -r Requirements.txt

CMD ["python", "webapp-launch.py"]