# SCROPY

## Author

Tadala N. Kapengule

## Setup

1. Create gunicorn daemon: `/etc/systemd/system/gunicorn.service`

- `sudo systemctl start gunicorn`

- `sudo systemctl enable gunicorn`

- `sudo systemctl status`

    - stat scropy.sock in present proj directory.

2. After modifying nginx conf in sites-av*, enable w : `sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled`

- Test `nginx` syntax w `sudo nginx -t`.

- `sudo systemctl restart nginx`