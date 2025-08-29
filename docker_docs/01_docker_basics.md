# Docker
  
in case of errors: `sudo chmod 666 /var/run/docker.sock`  
  
1. **Container**
    - A **container** is a standars unit of SW that can run a particular app and its associated processes
    - A **container** is **portable** and contains the SW dependencies for a given app
    - It is common to run several containers at once on a single host machine
    - **Containers** are **self-contained** and do not alter the host system they are running on
    - **Docker** is lightweight
    - **Containers** provide **reproducible** and **consistent** environments. If it works in development, it will work in production
    - **Containers** have a smaller footprint than virtual machines
  
    Docker isolates containers from each other. Isolation techniques: cgroups and namespaces  
    Orchestartors can be used to manage multiple containers  
  
    Container vs VM  
    - **Containers** are used for a `single process` or task, while **VM** may run `multiple processes` or tasks
    - **Container** boot times are **much quicker** than VM
  
    Multiple containers on the host machine will always share the kernel of the host machine  

    Docker uses a layered filesystem, so that you can add to a base image  

2. Microservices  
    - Microservices is an architectural style that structures an application as a collection of loosely coupled services
    - Microservices are easier t ofix and test
    - Each microservice can be deployed without the need to deploy the whole app
    - Docker containers are ideal for microservices

3. Basic Docker Commands  
    1. Download & Run  
        `docker run -dit debian`  
        Options:  
        - `-d' or '--detach': Runs the container in detached mode, meaning it runs in the background and does not tie up your terminal
        - `-it`: Combines -i (interactive) and -t (pseudo-TTY). This allows you to interact with the container's shell, typically used for debugging or running interactive commands
        - `--name <container-name>`: Assigns a specific name to the container, making it easier to reference later
        - `-p <host-port>:<container-port>`: Publishes a container's port to a host port, allowing external access to services running inside the container
        - `-e <key>=<value>` or `--env <key>=<value>`: Sets environment variables inside the container, useful for configuring applications
        - `-v <host-path>:<container-path>` or `--volume <host-path>:<container-path>`: Mounts a host volume into the container, enabling persistent storage or sharing files between the host and container.
        - `--rm`: Automatically removes the container when it exits, keeping your system clean
        - `--restart <policy>`: Sets a restart policy for the container (e.g., `always`, `on-failure`, `no`), determining how Docker should handle container restarts
        - `--network <network-name>`: Connects the container to a specific Docker network, enabling communication with other containers on that network
        - `--privileged`:Grants extended privileges to the container, allowing it to access host devices and potentially perform more actions. Use with caution as it can pose security risks

    2. Display info about running containers  
        `docker ps`  
        By default, it only shows containers that are currently in a "running" state.  
        ```
        CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
        ea6fa5aaadd3   debian    "bash"    6 seconds ago   Up 5 seconds             zen_wilson
        ```
        Options:  
        - `-a` or `--all`: Displays all containers, including those that are stopped, exited, or paused.
        - `-s` or `--size`: Shows the on-disk size of the container's writable layer and the virtual size (total disk space used by the image and writable layer).
        - `-q` or `--quiet`: Only displays the container IDs.
        - `-n <number>` or `--last <number>`: Shows the last `<number>` created containers, regardless of their state.
        - `-l` or `--latest`: Shows the latest created container, regardless of its state.
        - `--filter "key=value"`: Filters the output based on specific criteria (e.g., `docker ps --filter "status=exited"`).
        - `--format "Go template"`: Allows for custom formatting of the output using Go templates.
        - `--no-trunc`: Prevents truncation of output, showing the full command or other long strings.

    3. Stop container  
        ```
        docker stop my_container_name
        docker stop a0c59618bf9e
        ```
        To stop multiple containers:  
        `docker stop container1_name container2_id`  

        To stop all running containers:  
        `docker stop $(docker ps -q)`  

        By default, docker stop sends a SIGTERM signal to the container's main process and waits for a default grace period (usually 10 seconds) for the process to exit gracefully. If the process does not exit within this period, a SIGKILL signal is sent to forcefully terminate it. You can customize this timeout using the -t or --time flag:  
        `docker stop -t 30 my_container_name # waits for 30 seconds`  

    4. Show Docker images
        `docker images`  
        Output:  
        ```
        REPOSITORY                                                  TAG       IMAGE ID       CREATED         SIZE
        abertowyregistrydft.azurecr.io/devops-abertowy-test-repo    latest    eb5a26ffaa02   11 days ago     257MB
        mcr.microsoft.com/dotnet/sdk                                9.0       0103c4d7b67b   2 weeks ago     849MB
        mcr.microsoft.com/dotnet/aspnet                             9.0       8b54a45733eb   2 weeks ago     224MB
        debian                                                      latest    047bd8d81940   2 weeks ago     120MB
        ```
          
        Options:  
        - `-a` or `--all`: Show all images (default hides intermediate images).
        - -`-digests`: Show digests.
        - `-f` or `--filter "filter"`: Filter output based on conditions provided. Common filters include:
            - `dangling=true` (or `false`): Show only dangling images (images not associated with any tagged image).
            - `label=<key>` or `label=<key>=<value>`: Filter by image label.
            - `before=<image_name|image_id>`: Show images created before a specific image.
            - `since=<image_name|image_id>`: Show images created since a specific image.
            - `reference=<pattern>`: Filter by image name and tag (e.g., ubuntu:latest).
        - `--format "FORMAT"`: Pretty-print images using a Go template. This allows for custom output formats, accessing various image attributes like .ID, .Repository, .Tag, .Size, .CreatedAt, etc.
        - `--no-trunc`: Don't truncate output.
        - `-q` or `--quiet`: Only show numeric IDs.

    5. Show detailed info  
        `docker inspect [OPTIONS] NAME|ID [NAME|ID...]`  
        Options:  
        - `-f` or `--format`: This option allows you to format the output using a Go template. This is particularly useful for extracting specific fields from the detailed JSON output.  
        `docker inspect -f '{{.State.Status}}' my_container`  
        - `-s` or `--size`: This option displays the total file sizes if the object being inspected is a container. It adds size information to the output, including the size of the writable layer and the total size of the container.  
        `docker inspect -s my_container`  
        - -`-type`: This option allows you to explicitly specify the type of Docker object you are inspecting (e.g., `container`, `image`, `network`, `volume`). This can be helpful when a name or ID might be ambiguous (e.g., a `container` and an `image` have the same name).  

    6. Docker download image  
        `docker pull [OPTIONS] NAME[:TAG|@DIGEST]`  

    7. Docker tag  
        `docker tag container_name:origin_tag container_name:my_tag`  

    8. Build docker image
        `docker build -t myimage:latest .`  
        The command typically ends with a **path to the build context**, often `.` to indicate the **current** directory.  
        **Options**: 
        - `-t`, `--tag <name>:<tag>`: Assigns a name and optionally a `tag` to the built `image`. This allows for easier identification and versioning of images.  
            `docker build -t myapp:1.0 . `
        - `-f`, `--file <path/to/Dockerfile>`: Specifies the path to the Dockerfile to use for the build. If not specified, Docker searches for a file named Dockerfile in the build context.  
            `docker build -f custom_dockerfile . `
        - `--build-arg <name>=<value>`: Sets build-time variables that can be used within the Dockerfile using the ARG instruction. This allows for dynamic customization during the build process.  
            `docker build --build-arg VERSION=2.0 . `  
        - `--no-cache`: Forces Docker to ignore cached layers and perform a fresh build, re-executing all instructions in the Dockerfile. This is useful when changes might not be detected by Docker's caching mechanism.
        - `--target <stage_name>`: Specifies a specific build stage to build in a multi-stage Dockerfile. This allows for building only a subset of the image if different stages are defined.  
            `docker build --target builder_stage . `
        - `--pull`: Always attempts to pull a newer version of the base image specified in the `FROM` instruction before building. This ensures you are building on the most up-to-date base image.
        - `--rm`: Removes intermediate containers after a successful build. This is true by default; setting false keeps them for debugging.
    9. Some other cmds:
        ```
        docker system df                # show space used by docker
        docker run -dit container-name  # run in background
        docker logs -t container-id     # show logs for background container
        ```

