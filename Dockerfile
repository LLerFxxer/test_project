FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install pytest allure-pytest pandas
CMD ["pytest", "-v"]