# steps-to-deploy-locally-on-docker

## https://hub.docker.com/_/ubuntu

## download image

```bash
docker pull ubuntu
```

## Create and start docker container interactive and detach with code mapping for ubuntu image
```bash
docker run -dit -p 8080:8080 ubuntu /bin/bash
```

## to list all containers 
```bash
docker ps -a
```

## to go into docker conatiner 
```bash
docker exec -it <container_id> /bin/bash
```

## update container
```bash
apt-get update -y
```
```bash
apt-get upgrade -y
```
## install aws cli 
```bash
apt install awscli -y   
```
# choose you region and country when prompt

## configure aws configuration
```bash
aws configure
```

## Since model upload after training and application will download model from s3, hence we need to configure
```bash
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_DEFAULT_REGION=us-east-1
```

## install python      
```bash
apt-get install python3
```

## install pip      
```bash
apt-get install pip -y
```

```bash
apt-get install libgl1-mesa-glx -y
```

```bash
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```
## install git
```bash
apt-get install git -y
```

## install nano
```bash
apt-get install nano
```

## install vi
```bash
apt-get install vi
```

## install unzip
```bash
apt-get install unzip
```

## git clone
```bash
git clone https://github.com/mayankchugh-learning/Industry-Safety-Detection-using-Yolov7.git
```

## change directory to clonned repository
```bash
cd Industry-Safety-Detection-using-Yolov7
```

## install all requirement
```bash
pip install -r requirements.txt
```

## to check if aws cli is installed
```bash
aws --version
```

## execute application
```bash
python3 app.py
```

# docker image

https://docs.docker.com/engine/reference/commandline/image/#examples


## to list all images
```bash
docker image ls
```

# docker command line interface (cli)

```bash
https://docs.docker.com/engine/reference/commandline/


 AWS_ACCESS_KEY_ID=
 AWS_SECRET_ACCESS_KEY=
 AWS_DEFAULT_REGION=
```

## to stop all running container (reference only)
```bash
docker stop $(docker ps -a -q)
```

## to remove all stopped container (reference only)
```bash
docker rm $(docker ps -a -q)
```

## to remove all images
```bash
docker rmi $(docker images -a -q)
```

## to list all containers (reference only)
```bash
docker ps -a
```

## to list all images (reference only)
```bash
docker image ls
```

# docker-compose

https://docs.docker.com/compose/


# dockerfile

```bash
https://docs.docker.com/engine/reference/builder/#run
```


