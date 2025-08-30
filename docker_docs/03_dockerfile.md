Dockerfile
==========
  
1. `FROM`: specifies the base image from which to start the build. This is typically the first instruction.

2. `RUN': executes commands in a new layer on top of the current image, committing the result. Used for installing packages, creating directories, etc.

3. `COPY`: copies files or directories from the build context into the image's filesystem

4. `ADD`: similar to `COPY`, but can also handle remote URLs and automatically extract compressed archives

5. `WORKDIR`: sets the working directory for subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` instructions.

6. `EXPOSE`: informs Docker that the container listens on the specified network ports at runtime. This is for documentation and **does not automatically publish** the port.

7. `ENV`: sets environment variables within the image. These variables are **available** to subsequent instructions and at **runtime** within the container.

8. `ARG`: defines build-time variables that can be passed during the docker build command. These are **not available after** the image is **built**.

9. `CMD`: provides default commands or arguments for an executing container. There can **only be one** `CMD` instruction in a Dockerfile.

10. `ENTRYPOINT`: configures a container that will run as an executable. Like `CMD`, there can **only be one** `ENTRYPOINT`. Often used with `CMD` to provide default arguments.

11. `USER`: sets the user name or UID (and optionally group name or GID) to use when running the image and for any `RUN`, `CMD`, and `ENTRYPOINT` instructions that follow

12. `VOLUME`: creates a mount point for external volumes or other containers, allowing data to persist or be shared

13. `LABEL`: adds **metadata** to an image as key-value pairs.

14. `HEALTHCHECK`: defines how to check a container's health.

15. `ONBUILD`: adds a **trigger** instruction to an image that will be **executed** when the image is used **as the base** for another build.

16. `SHELL`: allows overriding the default shell program used for the shell form of `RUN`, `CMD`, and `ENTRYPOINT` instructions.

17. `STOPSIGNAL`: sets the system call signal that will be sent to the container to exit
  
Layers
-------
Docker containers leverage a layered architecture for efficiency and resource optimization.
1. Image layers  
    - Docker images are built from a series of `read-only` layers. Each instruction in a **Dockerfile**, such as `FROM`, `RUN`, `COPY`, or `ADD`, typically creates a **new layer**.
    - These layers are **stacked** on top of each other, forming the complete filesystem of the image.
    - They are **immutable**, meaning once created, they cannot be modified. Any changes result in the creation of a new layer.
    - Docker utilizes a union filesystem (like OverlayFS) to combine these layers into a single, cohesive view for the container.
    - Image layers are **cached** by Docker, enabling faster builds and efficient resource usage, as common layers can be shared between multiple images.
    - Whenever one layer is changed, all upper (or following) layers will be rebuilt
2. Container layer  
    - When a Docker container is launched from an image, Docker adds a thin, **writable** layer on **top** of the image's read-only layers. This is known as the `container layer` or container filesystem.
    - All changes made within the running container, such as creating, modifying, or deleting files, are stored in this writable layer.
    - This ensures that the underlying image layers remain untouched and immutable.
    - The container layer is **ephemeral**; when the container is stopped or removed, this writable layer is discarded, and any changes made within it are lost unless data is persisted using Docker volumes.
