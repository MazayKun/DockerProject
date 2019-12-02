from fabric import Connection, Config

config = Config(overrides={'sudo': {'password': '123'} , 'Password' : '123'})
connect = Connection ("192.168.1.51", config = config)

try:
    connect.run("git clone https://github.com/MazayKun/DockerProject.git")
except BaseException:
    print("already cloned")

connect.sudo("docker-compose -f DockerProject/docker-compose.yml up")

connect.close()