#!/bin/sh
# Starts up rabbitmq dependency and nameko service on run of container
rabbitmq-server start &
nameko run service