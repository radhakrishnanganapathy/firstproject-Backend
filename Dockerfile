# set python version
FROM python:3.9

# set working directory
WORKDIR /code

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy to docker cache
COPY ./requirements.txt /code/requirements.txt

# install all requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy codebase to working directory
COPY ./app /code

# ENV PYTHONPATH = /code

# make directories for uploads
# RUN  mkdir -p /uploads/depots /uploads/suppliers

# run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
