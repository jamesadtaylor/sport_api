FROM python:3.8
WORKDIR code
COPY  requirements.txt .
COPY sports/*.py .
RUN  pip install -r requirements.txt
CMD  ["python", "main.py"]