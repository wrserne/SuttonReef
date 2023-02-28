Reef-pi and Robo-Tank Controller Monitoring Website

This project aims to create a web application that monitors the temperature and pH levels of a robo-tank using the Reef-pi API. The website will allow users to view real-time data on the temperature and pH levels in the robo-tank, as well as view historical data over time.

API Selection
For this project, we have chosen to use the Reef-pi API to monitor the temperature and pH levels in the robo-tank. We chose this API because it is free to access and provides easy-to-use data in JSON format.

Schema Design
Our schema design includes two tables:

User Table
user_id (primary key)
username
password
email
This table is used to store user authentication information.

Temperature Reading Table
event_id (primary key)
event_time (foreign key)
temperature_reading
pH_reading
timestamp




Crow's Foot Notation Diagram can be seen in .sql file

Conclusion
Our database schema is designed to allow us to store and retrieve temperature and pH readings from the robo-tank using the Reef-pi API, and to also store user login information. We believe this schema will allow us to easily track and analyze data over time, and provide a rich user experience for monitoring the robo-tank.
