# Using lightweight alpine image
FROM python:3.8-alpine

COPY requirements.txt .

# Installing packages
RUN apk update
RUN pip install --no-cache-dir -r requirements.txt

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY bootstrap.sh ./
COPY box ./box


# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
