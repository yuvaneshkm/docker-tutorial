# use an official python runtime as a parent image
FROM python:3.10

# set the working directory in the container
WORKDIR /app

# copy the current directory contents to the container at /app
COPY . /app

# install any required packages
RUN pip install -r requirements.txt

# run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]