# 
FROM python:3.8.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN python3.8 -m pip install --upgrade pip

#

RUN python3.8 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./imdb_api /code/app

# 
CMD ["uvicorn", "app.imdb_api:app", "--host", "0.0.0.0", "--port", "80"]
