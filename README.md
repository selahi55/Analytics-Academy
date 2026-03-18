# 📊 Analytics Academy and the VSAE

The **Analytics Academy** is the web platform for [VSAE](https://vsae.nl/en/companies)'s flagship educational initiative that connects econometrics students from the University of Amsterdam with non-profit organizations.

> **Mission:** Bridge the gap between data-savvy students and NGOs/social organisations that lack access to high-quality data analytics — creating real impact for non-profits while giving students hands-on consultancy experience.

---

## About the Analytics Academy Project

Each project round, teams of 3-5 motivated students working 4–6 hours per week over 10–15 weeks to deliver data-driven insights to a partner organisation. Projects kick off with a pitch event where organisations present their challenges, and conclude with a final presentation of findings and recommendations.

**Parthner for this Project:** Global Human Rights Defence (GHRD)
**Project contributors:** Kiril - Team Lead, Shayaan and Nastya - Team Members

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3 / Django 5.1 |
| **Database** | PostgreSQL (via `psycopg2`) |
| **Frontend** | HTML / CSS / JavaScript with Django Templates |
| **Forms** | django-crispy-forms + Bootstrap 5 |
| **Payments** | Stripe |
| **Static Files** | WhiteNoise |
| **WSGI Server** | Gunicorn |
| **Config** | python-dotenv |

---

## Project Structure

```
Analytics-Academy/
├── config/             # Django project settings & WSGI config
├── dashboard/          # Dashboard app (admin/management views)
├── events/             # Events app (project rounds, kick-offs, etc.)
├── front/              # Public-facing frontend app
├── templates/          # Shared HTML templates
├── static/             # Source static assets (CSS, JS, images)
├── staticfiles/        # Collected static files for production
├── manage.py           # Django management entry point
├── requirements.txt    # Python dependencies
└── Procfile            # Heroku/PaaS deployment config
```
