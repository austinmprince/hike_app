FROM python:3.9

WORKDIR /hike_dir

COPY ./requirements.txt hike_dir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r hike_dir/requirements.txt

COPY ./app /hike_dir/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]