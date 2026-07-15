#!/bin/bash

echo -e "==Building docker image ==\n"
docker build -t demo .

echo -e "Completed Docker Build Sucessfully!\n"
