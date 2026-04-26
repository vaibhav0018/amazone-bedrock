

Let’s lock this in properly so you can explain it confidently in interviews and know what to do next.

✅ WHAT YOU HAVE SUCCESSFULLY DONE (BIG DEAL)

You now have:

✅ EC2 instance running Ubuntu

✅ Docker installed & working

✅ Docker Compose orchestration

✅ Two services running:

Admin (PDF upload + FAISS index)

User (RAG chat)

✅ AWS Bedrock for embeddings & LLM

✅ S3 for FAISS persistence

✅ IAM Role attached to EC2

✅ IMDSv2 issue fixed

✅ NO AWS access keys anywhere (best practice)

✅ Production-style deployment

This is NOT beginner-level anymore.

🧠 FINAL INTERVIEW-READY EXPLANATION (MEMORIZE THIS)

I built and deployed a Retrieval-Augmented Generation system on AWS using EC2 and Docker.
The application uses Amazon Bedrock for embeddings and text generation, FAISS for vector search, and S3 for storing vector indexes.
I containerized the admin and user services and orchestrated them using Docker Compose.
For security, I attached an IAM role to the EC2 instance so containers access AWS services using temporary credentials via instance metadata, without hardcoding keys.

If you say this cleanly → strong hire signal.

📂 WHAT YOUR FINAL ARCHITECTURE LOOKS LIKE
Browser
  ├── Admin UI (8083) → Upload PDF → FAISS → S3
  └── User UI  (8084) → Query → FAISS → Bedrock → Answer

EC2
 ├── Docker
 ├── Docker Compose
 ├── admin-app container
 ├── user-app container
 └── IAM Role (Bedrock + S3)

🔐 SECURITY CHECK (YOU DID IT RIGHT)

✔ No .env with secrets
✔ No AWS keys in GitHub
✔ IAM role + metadata
✔ Containers restarted after role attach

This is exactly how AWS wants it.

🚀 WHAT SHOULD YOU DO NEXT? (CHOOSE ONE)

Reply with one number 👇

1️⃣ Add Nginx reverse proxy (single port like /admin, /chat)
2️⃣ Add Elastic IP (static URL)
3️⃣ Add CloudWatch logs & monitoring
4️⃣ Write resume-ready README (I’ll help)
5️⃣ Cost control + auto-shutdown
6️⃣ Move to ECS / ECR (next-level deployment)


vaibhav@LAPTOP-JL099FE3:/mnt/c/Users/Vaibhav/OneDrive/Desktop$ ssh -i ~/rag-key\ -\ Copy.pem ubuntu@13.233.120.103
Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.14.0-1015-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Jan  4 12:35:18 UTC 2026

  System load:  0.04              Processes:             116
  Usage of /:   74.1% of 6.71GB   Users logged in:       0
  Memory usage: 25%               IPv4 address for enX0: 172.31.4.196
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

74 updates can be applied immediately.
28 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

1 additional security update can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


Last login: Sun Jan  4 11:58:36 2026 from 203.192.238.78
ubuntu@ip-172-31-4-196:~$ curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
ubuntu@ip-172-31-4-196:~$ curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
rag-bedrock-roleubuntu@ip-docker stop admin-app user-appmin-app user-app
admin-app
user-app
ubuntu@ip-172-31-4-196:~$ docker rm admin-app user-app
admin-app
user-app
ubuntu@ip-172-31-4-196:~$ docker run -d \
  --name admin-app \
  -e BUCKET_NAME=vaibhav-learning-bucket \
  -e AWS_REGION=ap-south-1 \
  -e AWS_DEFAULT_REGION=ap-south-1 \
  -p 8083:8083 \
  pdf-reader-admin
b1fc6dc44ccbf7eec2061ed5fd1a25ee896951e7431506eee0bed7b68bbf899e
ubuntu@ip-172-31-4-196:~$ docker run -d \
  --name user-app \
  -e BUCKET_NAME=vaibhav-learning-bucket \
  -e AWS_REGION=ap-south-1 \
  -e AWS_DEFAULT_REGION=ap-south-1 \
  -p 8084:8084 \
  pdf-reader-user
59a90468cb5fee2980739db4a86a1147cdb415ff9f57e49b243b63c9aafc6fde
ubuntu@ip-172-31-4-196:~$ cd amazone-bedrock/
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ pwd
/home/ubuntu/amazone-bedrock
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ nano docker-compose.yml
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ nano docker-compose.yml
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker stop admin-app user-app
admin-app
user-app
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker rm admin-app user-app
admin-app
user-app
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker compose up -d --build
unknown shorthand flag: 'd' in -d

Usage:  docker [OPTIONS] COMMAND [ARG...]

Run 'docker --help' for more information
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker-compose up -d --build
Command 'docker-compose' not found, but can be installed with:
sudo snap install docker          # version 28.4.0, or
sudo apt  install docker-compose  # version 1.29.2-6
See 'snap info docker' for additional versions.
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker-compose ps
Command 'docker-compose' not found, but can be installed with:
sudo snap install docker          # version 28.4.0, or
sudo apt  install docker-compose  # version 1.29.2-6
See 'snap info docker' for additional versions.
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ sudo apt update
Hit:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble InRelease
Get:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Get:3 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
Get:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [175 kB]
Get:5 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [377 kB]
Get:6 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]
Get:7 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease
Get:9 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7328 B]
Get:10 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [10.5 kB]
Get:11 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
Get:12 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
Fetched 824 kB in 1s (1056 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
68 packages can be upgraded. Run 'apt list --upgradable' to see them.
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ sudo apt install docker-compose-plugin -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package docker-compose-plugin
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker compose version
docker: unknown command: docker compose

Run 'docker --help' for more information
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ sudo apt update
Hit:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:3 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
68 packages can be upgraded. Run 'apt list --upgradable' to see them.
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ sudo apt install docker-compose -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-compose python3-docker python3-dockerpty python3-docopt python3-dotenv python3-texttable python3-websocket
The following NEW packages will be installed:
  docker-compose python3-compose python3-docker python3-dockerpty python3-docopt python3-dotenv python3-texttable
  python3-websocket
0 upgraded, 8 newly installed, 0 to remove and 68 not upgraded.
Need to get 297 kB of archives.
After this operation, 1589 kB of additional disk space will be used.
Get:1 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-websocket all 1.7.0-1 [38.1 kB]
Get:2 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3-docker all 5.0.3-1ubuntu1.1 [89.1 kB]
Get:3 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dockerpty all 0.4.1-5 [11.4 kB]
Get:4 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-docopt all 0.6.2-6 [26.1 kB]
Get:5 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-dotenv all 1.0.1-1 [22.3 kB]
Get:6 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-texttable all 1.6.7-1 [11.0 kB]
Get:7 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 python3-compose all 1.29.2-6ubuntu1 [84.6 kB]
Get:8 http://ap-south-1.ec2.archive.ubuntu.com/ubuntu noble/universe amd64 docker-compose all 1.29.2-6ubuntu1 [14.0 kB]
Fetched 297 kB in 0s (9979 kB/s)
Selecting previously unselected package python3-websocket.
(Reading database ... 72102 files and directories currently installed.)
Preparing to unpack .../0-python3-websocket_1.7.0-1_all.deb ...
Unpacking python3-websocket (1.7.0-1) ...
Selecting previously unselected package python3-docker.
Preparing to unpack .../1-python3-docker_5.0.3-1ubuntu1.1_all.deb ...
Unpacking python3-docker (5.0.3-1ubuntu1.1) ...
Selecting previously unselected package python3-dockerpty.
Preparing to unpack .../2-python3-dockerpty_0.4.1-5_all.deb ...
Unpacking python3-dockerpty (0.4.1-5) ...
Selecting previously unselected package python3-docopt.
Preparing to unpack .../3-python3-docopt_0.6.2-6_all.deb ...
Unpacking python3-docopt (0.6.2-6) ...
Selecting previously unselected package python3-dotenv.
Preparing to unpack .../4-python3-dotenv_1.0.1-1_all.deb ...
Unpacking python3-dotenv (1.0.1-1) ...
Selecting previously unselected package python3-texttable.
Preparing to unpack .../5-python3-texttable_1.6.7-1_all.deb ...
Unpacking python3-texttable (1.6.7-1) ...
Selecting previously unselected package python3-compose.
Preparing to unpack .../6-python3-compose_1.29.2-6ubuntu1_all.deb ...
Unpacking python3-compose (1.29.2-6ubuntu1) ...
Selecting previously unselected package docker-compose.
Preparing to unpack .../7-docker-compose_1.29.2-6ubuntu1_all.deb ...
Unpacking docker-compose (1.29.2-6ubuntu1) ...
Setting up python3-dotenv (1.0.1-1) ...
Setting up python3-texttable (1.6.7-1) ...
Setting up python3-docopt (0.6.2-6) ...
Setting up python3-websocket (1.7.0-1) ...
Setting up python3-dockerpty (0.4.1-5) ...
Setting up python3-docker (5.0.3-1ubuntu1.1) ...
Setting up python3-compose (1.29.2-6ubuntu1) ...
Setting up docker-compose (1.29.2-6ubuntu1) ...
Processing triggers for man-db (2.12.0-4build2) ...
Scanning processes...
Scanning linux images...

Running kernel seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker-compose --version
docker-compose version 1.29.2, build unknown
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker-compose up -d --build
Creating network "amazone-bedrock_default" with the default driver
Building admin
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  8.192kB
Step 1/7 : FROM python:3.12.3
 ---> 12e5ab9d51c8
Step 2/7 : EXPOSE 8083
 ---> Using cache
 ---> cd513ddf5305
Step 3/7 : WORKDIR /app
 ---> Using cache
 ---> 6844913d8a4a
Step 4/7 : COPY requirements.txt ./
 ---> Using cache
 ---> e4d53a48363d
Step 5/7 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> bbb0b23fe086
Step 6/7 : COPY . ./
 ---> Using cache
 ---> 969deafebdab
Step 7/7 : ENTRYPOINT ["streamlit", "run", "admin.py", "--server.port=8083", "--server.address=0.0.0.0"]
 ---> Using cache
 ---> d17825d68c1e
Successfully built d17825d68c1e
Successfully tagged amazone-bedrock_admin:latest
Building user
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  7.168kB
Step 1/7 : FROM python:3.12.3
 ---> 12e5ab9d51c8
Step 2/7 : EXPOSE 8084
 ---> Using cache
 ---> 91b6c999a491
Step 3/7 : WORKDIR /app
 ---> Using cache
 ---> 48c0e0fb25b3
Step 4/7 : COPY requirements.txt ./
 ---> Using cache
 ---> e9f6fa823bf1
Step 5/7 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 3995f804a4dd
Step 6/7 : COPY . ./
 ---> Using cache
 ---> 0ba9cf0d12d1
Step 7/7 : ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8084", "--server.address=0.0.0.0"]
 ---> Using cache
 ---> ce06ed39953c
Successfully built ce06ed39953c
Successfully tagged amazone-bedrock_user:latest
Creating user-app  ... done
Creating admin-app ... done
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ docker-compose ps
  Name                 Command               State                    Ports
---------------------------------------------------------------------------------------------
admin-app   streamlit run admin.py --s ...   Up      0.0.0.0:8083->8083/tcp,:::8083->8083/tcp
user-app    streamlit run app.py --ser ...   Up      0.0.0.0:8084->8084/tcp,:::8084->8084/tcp
ubuntu@ip-172-31-4-196:~/amazone-bedrock$ cd ..
ubuntu@ip-172-31-4-196:~$ exit
logout
Connection to 13.233.120.103 closed.
vaibhav@LAPTOP-JL099FE3:/mnt/c/Users/Vaibhav/OneDrive/Desktop$