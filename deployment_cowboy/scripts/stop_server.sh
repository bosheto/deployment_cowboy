#!/bin/sh

SERVER_PID=$(lsof -t -itcp:8080 -c java)
kill $SERVER_PID
echo "Stopped java server"