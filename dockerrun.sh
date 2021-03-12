#!/bin/sh
rabbitmq-server start &
nameko run service