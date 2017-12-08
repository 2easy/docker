Exercise 3 done on sight.

$ docker build -t 2easy/flask:v5 ex2/src && docker push 2easy/flask:v5
// login and change version of the image on the serwer in docker-compose.yml
$ ssh ubuntu@$GCP_INSTANCE_IP "docker-compose down && docker-compose up"


