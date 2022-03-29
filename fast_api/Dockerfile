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
COPY . /code/app

ENV PYTHONPATH "${PYTHONPATH}:/code/app"

# RUN python3.8 /code/app/bdd/mongo-init.py
# 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8585"]
