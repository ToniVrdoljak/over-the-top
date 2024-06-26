import os
import subprocess

color_off = "\033[0m"
b_green = "\033[1;32m"
b_red = "\033[0;31m"


DOCKER_USERNAME = os.environ["DOCKER_USERNAME"]
DOCKER_ACCESS_TOKEN = os.environ["DOCKER_ACCESS_TOKEN"]

def push_image_to_repo(service):
    print(f"{b_green} Pushing {service} docker image to repo... {color_off}")
    subprocess.run(f"docker image push {DOCKER_USERNAME}/over-the-top-{service}", shell=True, check=True)
    print(f"{b_green} Successfuly pushed {service} image {color_off}\n")

print(f"{b_green} Logging into DockerHub... {color_off}")
subprocess.run(f"""docker login --username {DOCKER_USERNAME} --password {DOCKER_ACCESS_TOKEN}""",
               shell=True,
               check=True)

push_image_to_repo("client")
push_image_to_repo("worker")
push_image_to_repo("server")
push_image_to_repo("nginx")