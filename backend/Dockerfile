FROM Python:3.11-slim

WORKDIR /app

COPY requiremtents.txt .
RUN pip install -r requiremtents.txt

COPY . .

RUN python manage.py collectstatic --noinput