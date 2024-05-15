import os
import subprocess

color_off = "\033[0m"
b_green = "\033[1;32m"
b_red = "\033[0;31m"


def push_image_to_dockerhub(service):
    print(f"{b_green} Pushing {service} docker image to DockerHub... {color_off}")
    subprocess.run(f"docker image push tonivrd/over-the-top-{service}", shell=True, check=True)
    print(f"{b_green} Successfuly pushed {service} image {color_off}")


DOCKER_USERNAME = os.environ["DOCKER_USERNAME"]
DOCKER_ACCESS_TOKEN = os.environ["DOCKER_ACCESS_TOKEN"]

print(f"{b_green} Logging into DockerHub... {color_off}")
subprocess.run(f"""docker login --username {DOCKER_USERNAME} --password {DOCKER_ACCESS_TOKEN}""",
               shell=True,
               check=True)

push_image_to_dockerhub("client")
push_image_to_dockerhub("worker")
push_image_to_dockerhub("server")
push_image_to_dockerhub("nginx")