# Note
If you feel difficulty to set up the Environment. So, you can use any environment Docker and Python virtual to set up the project.

# Setup Through Docker



### Installation
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Clone this repo `https://github.com/arslan578/resize-image-app.git`
3. Update .env file `DATABASE_URL` with your  `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.
    
### Getting Started
- Run `docker image build -t resize-image-app .`
- Run `docker run  -p 5000:5000 -d resize-image-app` (Run In Detach Mode)
- Run `docker run  -p 5000:5000 resize-image-app`
- Visit `http://0.0.0.0:5000`



# SetUp With Python

#### Python
Install Python v3.7.3.
A list of releases can be found [here](https://www.python.org/downloads/)

Installation can be verified by running the command
`python` in a terminal.


##### Virtual Environment
Once Python is installed, create a virtual environment to store any 
Python-specific dependencies. If the default
version of Python is the appropriate version, this can be done with `python -m
venv venv`. If multiple versions of Python are installed, a more specific
command is required:

With an alias:
```
python36 -m venv venv
```
or with a path to the executable: 
```
/usr/bin/python3.6 -m venv venv
```

Once created, activate the venv with the `activate` script:

On Linux:
```
source venv/bin/activate
```

On Windows (Git Bash):
```
source venv/Scripts/activate
```

On Windows (Powershell):
```
.\venv\Scripts\activate
```

On Windows (Command Prompt):
```
venv\Scripts\activate
```

An indicator (something like `(venv)`) should appear before the terminal
prompt. If this is missing, the venv has not been activated.

_Creating_ the venv only needs to be done once, unless it is removed.
_Activating_ the venv should be done whenever running code or installing
dependencies, if it is not already active. It can be deactivated with the command `deactivate`.

#### Git
If not already installed, download Git from [here](https://git-scm.com/) or
from an appropriate package manager.

NOTE: Mac/Linux users can skip this next section

While PowerShell or CMD _can_ work, the environment setup process is much
easier with a shell that supports UNIX-style commands and paths. Therefore, it
is recommended to use Git Bash instead. Git Bash is included in the [Git For
Windows](https://gitforwindows.org/) suite, which also includes a graphical
user interface.

### Application Dependencies
To quickly install all app dependencies, run
```
make dependencies
```

#### Python Libraries
First, ensure that the virtual environment is active.
To install the required python dependencies, run 

```
pip install -r requirements.txt
```

### Run Command

```

python3 app.py
```

