Python Project Setup with Docker Compose
This repository contains a Birthday Mail project setup with Docker Compose, allowing you to easily run and manage your application environment.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Docker
Docker Compose

Getting Started
To set up and run the Python project, follow these steps:

Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/ziasultan2/birthday-mail.git
Navigate to the project directory:
bash
Copy code
cd birthday-mail
1. Build the Docker images and start the containers:
docker compose up

This command will build the Docker images specified in the docker-compose.yml file and start the containers.
Once the containers are up and running, you can access the Python application at http://localhost:8000.

2. Go to the following endpooint it'll Seed some dummy data for testing purposes
http://127.0.0.1:8000/api/seed


3. I could extend the celery and celery beat in docker compose. But I didn't add it in docker compose so that you can check out the logs by running the following command.
    N.B[I run the daily birthday mail at 6am it's the early morning and most of the user will receive mail in top of their mail box that makes users feeling pleased. If you want to change it for testing you can change it from celery.py which is inside [birthday] folder. Go to line 24 and change the hour as per your will]


  Celery        -   celery -A birthdaymail worker -l info
  Celery-beat   -   celery -A birthdaymail beat -l info 

  Just run the above 2 commands and you can see the logs. 



Conclusion
I've tested it locally and seems it's working fine for any reason if it doesn't work you can contact me any time. Will be glad to help you to fix the issues you are facing.


Without docker environment you can run the following command to run the project
 - You will need to have redis installed as it's required to run celery

1. pip install -r requirements.txt
2. python manage.py runserver 0.0.0.0:8000
3. celery -A birthdaymail worker -l info
4. celery -A birthdaymail beat -l info 

Thanks
Zia sultan






