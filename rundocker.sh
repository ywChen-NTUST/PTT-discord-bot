docker build -t discordbot_python .
docker run -dt --name discordbot --env-file=.env -v $(pwd)/app:/app discordbot_python
docker exec -it discordbot python /app/app.py