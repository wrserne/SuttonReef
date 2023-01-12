**Setup**

1. Install docker using the tutorial found <a href="https://docs.docker.com/engine/install/">here</a>
2. Create a `.env` file at the root directory that looks like this
   with actual secret values. This will be used to log in to the sql
   database

```.dotenv
DB_PASSWORD=super_secret_password
DB_USERNAME=super_secret_username
````

3. Run `docker-compose up` at the root directory

