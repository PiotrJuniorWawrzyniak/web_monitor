# Etap 1: Budowanie aplikacji React
FROM node:18 AS build

# Ustawienie katalogu roboczego dla Reacta
WORKDIR /frontend

# Skopiowanie plików konfiguracyjnych i instalacja zależności
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Skopiowanie wszystkich plików aplikacji i budowanie Reacta
COPY frontend/ ./
RUN npm run build

# Etap 2: Konfiguracja środowiska Django
FROM python:3.12-slim

# Zmniejszenie użycia zasobów
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ustawienie katalogu roboczego dla Django
WORKDIR /app

# Skopiowanie całego projektu do kontenera
COPY . /app/

# Skopiowanie plików z folderu build Reacta do odpowiedniego miejsca w projekcie Django
COPY --from=build /frontend/build /app/frontend/build

# Instalacja zależności Pythona
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Zbieranie plików statycznych
RUN python manage.py collectstatic --noinput

# Sprawdzenie, czy pliki statyczne są poprawnie zebrane
RUN ls -l /app/staticfiles

# Uruchomienie aplikacji Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
