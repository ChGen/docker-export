## docker-export

This scripts allow to export Dockerfile `RUN` commands to shell script file for local/manual use.
There's separate script for Windows Containers dockerfiles.

Usage:

```
./docker-export.py Dockerfile > commands.sh
./docker-export-win32.py Dockerfile_win32 > commands.bat
```
