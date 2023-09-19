#!/bin/bash

env >> /etc/environment
S_ADDRESS='0.0.0.0'
PORT='8000'

exit_with_error(){
    echo "Something went wrong"
    exit 1
}

start_server(){
    echo "Starting server..."
    DEBUG=True python manage.py runserver $S_ADDRESS:$PORT
    exit_with_error
}

wait_for_db(){
    echo "Waiting for PG to become online..."
    sleep 5
}

start_cron(){
  echo "Starting cron..."
  cron
  sleep 1
}

default_start(){
    wait_for_db
    #start_cron
    start_server
    exit_with_error
}

main(){
  default_start
}


main