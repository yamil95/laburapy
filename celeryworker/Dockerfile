# pull official base image
FROM python:3.12.3-alpine3.19

# set work directory
WORKDIR /app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1  

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./app/
RUN pip install -r ./app/requirements.txt

# copy project
COPY . ./app/