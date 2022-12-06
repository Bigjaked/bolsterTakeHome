FROM python:3.10-slim-bullseye

# Create a directory to run the app from
WORKDIR /app

# Copy requirements.txt file into container and run pip install
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# expose port 8081 for external binding.
EXPOSE 8081

# copy the application into the docker container.
COPY ./candidate_api /app/candidate_api


# start the uvicorn wsgi server hosting the candidate_api app in reload mode so it will
# pick up code changes if we use volume mounts to overwrite the candidate_api directory.
CMD ["uvicorn", "candidate_api.main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
