FROM python:3.11

WORKDIR /DemandForecast

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "demand_forecaster.py" ]

