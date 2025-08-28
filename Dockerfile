# Base Image

FROM python:3.12.3

# workdir
WORKDIR /main

# copy
COPY requirements.txt .


# run
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the application code
COPY . .

# port
EXPOSE 8000

# command to run fast api file
CMD [ "uvicorn","app:app","--host","0.0.0.0","--port","8000" ]