
A container is an isolated (namespaces) and restricted (cgroups, capabilities, seccomp) process.

Namespaces: mnt, pid, net, ipc, uts, user, time and cgroup (syslog is not implemented)

    clone(2) system call with CLONE_NEW* flags
    unshare(2) system call with CLONE_NEW* flags
    setns(2)

docker history
docker diff

ENTRYPOINT [""]
CMD [""]

ENTRYPOINT + CMD (CMD is overridden while running the container) 
docker run --entrypoint <>

docker image build --squash

WRONG
COPY some-file .
RUN chown www-data:www-data some-file
RUN chmod 644 some-file
RUN mv some-file /var/www

RIGHT 
COPY --chown=1000 some-file .
COPY --chown=1000:1000 some-file .
COPY --chown=www-data:www-data some-file .

Debugging crashed container (that can't be started)
docker commit <container_id> debugimage
docker run -ti --entrypoint sh debugimage


what happens if a container is started with multiple networks?

docker buildx build … \
       --platform linux/amd64,linux/arm64,linux/arm/v7,linux/386 \
       [--tag pkali/hello --push]


Kubernetes does not expose that --init option.

However, we can achieve the same result with Process Namespace Sharing.

When Process Namespace Sharing is enabled, PID 1 will be pause.

That pause process takes care of reaping zombies.

Process Namespace Sharing is available since Kubernetes 1.16.

If you're using an older version of Kubernetes ...

... you might have to add tini explicitly to your Docker image.





Control groups provide resource metering and limiting.

Avoiding the OOM killer

For some workloads (databases and stateful systems), killing processes because we run out of memory is not acceptable.

The "oom-notifier" mechanism helps with that.

When "oom-notifier" is enabled and a hard limit is exceeded:

all processes in the cgroup are frozen,

a notification is sent to user space (instead of killing processes),

user space can then raise limits, migrate containers, etc.,

once the memory usage is below the hard limit, unfreeze the cgroup.





Namespaces are materialized by pseudo-files in /proc/<pid>/ns.

ls -l /proc/self/ns



sudo unshare --pid --fork --mount-proc
    setns(2) 


cgroups (/sys/fs/cgroup)

    fork-bomb prevented by PID cgroup.
    a process inherits the cgroups of its parent.
