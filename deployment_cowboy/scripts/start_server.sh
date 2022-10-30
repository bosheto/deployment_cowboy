#!/bin/sh
cd ..
nohup java -jar WebProjectTelerik-0.8.0.jar > server_log.txt &
cd scripts