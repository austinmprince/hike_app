FROM python:3.9

WORKDIR /hike_dir

COPY ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./server /hike_dir/server

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]