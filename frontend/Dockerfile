# Używamy obrazu z Node.js
FROM node:16

# Tworzymy katalog aplikacji
WORKDIR /app

# Kopiujemy plik package.json i package-lock.json
COPY package*.json ./

# Instalujemy zależności
RUN npm install

# Kopiujemy resztę aplikacji
COPY . .

# Otwieramy port 3000 dla aplikacji React
EXPOSE 3000

# Komenda startująca aplikację React w trybie deweloperskim
CMD ["npm", "start"]
