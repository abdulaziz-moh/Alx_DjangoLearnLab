# Security Best Practices Documentation for bookshelf App

## Settings

- `DEBUG = False` in production to prevent sensitive data leaks.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser XSS protection.
- `X_FRAME_OPTIONS = 'DENY'` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME-type sniffing.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` ensure cookies are sent over HTTPS only.

## Templates

- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## Views

- All user input is handled via Django ORM and validated in views.
- No raw SQL queries are used, preventing SQL injection.

## Content Security Policy (CSP)

- To further reduce XSS risk, add a CSP header using django-csp or middleware (not shown here for brevity).

## Testing

- Manually tested forms and input fields for CSRF and XSS vulnerabilities.
- Verified that only safe, validated data is processed.

---

**Note:** Always review Django's security checklist before deploying to production.
