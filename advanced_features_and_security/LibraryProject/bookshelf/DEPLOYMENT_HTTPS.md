# Deployment Configuration for HTTPS

To serve your Django application securely over HTTPS, you must configure your web server (e.g., Nginx or Apache) with SSL/TLS certificates. Below is an example for Nginx:

## Example Nginx Configuration

```
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/ssl/certs/your_cert.crt;
    ssl_certificate_key /etc/ssl/private/your_key.key;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

- Replace `yourdomain.com`, `your_cert.crt`, and `your_key.key` with your actual domain and certificate paths.
- Make sure your Django `settings.py` has `SECURE_SSL_REDIRECT = True` and other security settings enabled.

---

**Note:** Always test your deployment in a staging environment before going live.
