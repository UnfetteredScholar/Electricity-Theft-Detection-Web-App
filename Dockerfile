# app/Dockerfile

FROM python:3.9-slim

WORKDIR /Electricity-Theft-Detection-Web-App

RUN mkdir -p /Electricity-Theft-Detection-Web-App
RUN mkdir -p /Electricity-Theft-Detection-Web-App/pages
RUN mkdir -p /Electricity-Theft-Detection-Web-App/dependencies
RUN mkdir -p /Electricity-Theft-Detection-Web-App/models
RUN mkdir -p /Electricity-Theft-Detection-Web-App/resources

COPY ./dependencies /Electricity-Theft-Detection-Web-App/dependencies

COPY ./models /Electricity-Theft-Detection-Web-App/models

COPY ./pages /Electricity-Theft-Detection-Web-App/pages

COPY ./resources /Electricity-Theft-Detection-Web-App/resources

COPY ./Login.py /Electricity-Theft-Detection-Web-App

COPY ./.env /Electricity-Theft-Detection-Web-App

COPY ./requirements.txt /Electricity-Theft-Detection-Web-App

RUN pip3 install -r /Electricity-Theft-Detection-Web-App/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Login.py", "--server.port=8501", "--server.address=0.0.0.0"]
