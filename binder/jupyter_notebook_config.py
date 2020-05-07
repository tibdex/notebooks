lab_command = " ".join([
    "jupyter",
    "lab",
    "--debug",
    "--no-browser",
    "--port={port}",
    "--NotebookApp.ip=127.0.0.1",
    "--NotebookApp.token=''",
    # Disable DNS rebinding protection here, since our "Host" header
    # is not going to be localhost when coming from hub.mybinder.org
    "--NotebookApp.allow_remote_access=True"
])

c.ServerProxy.servers = {
    "lab-dev": {
        "command": [
            "/bin/bash", "-c",
            f"{lab_command} >jupyterlab.log 2>&1"
        ],
        "timeout": 60,
        "absolute_url": True
    }
}
