#!/usr/bin/env bash
./manage.py collectstatic
tmux new-session "./manage.py runserver 8001"
