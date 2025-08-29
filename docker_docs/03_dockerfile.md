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
