## FastAPI Weather API

Clone this repo
```bash
git clone https://github.com/danieladupusamezgaile/weather-api.git
cd weather-api
```

Create an .env file using the .env.example

Start the containers:
```bash
docker-compose up -d --build
```

Create database tables:
```bash
docker exec -it weather-api python -m app.db.init_db
```

Visit the API at http://localhost:8000
Swagger docs: http://localhost:8000/docs
