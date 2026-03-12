# AI Lead Intelligence Agent

An autonomous backend platform that discovers companies exhibiting operational inefficiency signals, scores them as consulting leads, identifies decision makers, generates AI-powered diagnoses, and sends personalized outreach — without human intervention.

## What it does

Runs a 7-stage agent pipeline on a daily schedule:

```
Discovery → Signal Detection → Lead Scoring → Contact Discovery
         → AI Diagnosis → Outreach Generation → Email Delivery
```

1. **Scout Agent** — pulls companies from job boards and news APIs via SerpAPI
2. **Analyst Agent** — detects operational distress signals (hiring patterns, recalls, bad reviews)
3. **Scorer Agent** — assigns a 0–100 lead score and band (HOT / WARM / COOL / COLD)
4. **Researcher Agent** — finds VP/C-suite contacts via Hunter.io and Apollo
5. **Diagnostician Agent** — generates a structured consulting diagnosis via GPT-4o
6. **Copywriter Agent** — generates two personalized cold email variants (A/B) per contact
7. **Sender Agent** — delivers emails via SendGrid with open/reply tracking

## Tech stack

- **FastAPI** — async REST API
- **PostgreSQL** (Supabase) — primary database
- **SQLAlchemy 2.0** — async ORM with Alembic migrations
- **GPT-4o** — operational diagnosis and outreach generation
- **ARQ + Redis** — background task queue for pipeline execution
- **APScheduler** — daily 6am pipeline trigger
- **SendGrid** — email delivery and webhook tracking
- **JWT + bcrypt** — authentication
- **structlog + Sentry** — structured logging and error tracking
- **Docker** — containerized local development

## Project structure

```
app/
├── api/v1/          # REST endpoints (auth, companies, leads, outreach, pipeline)
├── agents/          # 7 autonomous agents + orchestrator
├── services/        # Business logic layer
├── integrations/    # External API clients (OpenAI, SerpAPI, Hunter, SendGrid)
├── models/          # SQLAlchemy ORM models
├── schemas/         # Pydantic request/response schemas
├── db/              # Database session and base
└── core/            # Security, logging, exceptions
```

## Status

Work in progress — foundation layer complete (config, auth utilities, DB session, ORM models, Pydantic schemas). Agent implementations and API routes in progress.

## Environment variables

```bash
DATABASE_URL=postgresql+asyncpg://...
SECRET_KEY=...
OPENAI_API_KEY=...
SERP_API_KEY=...
NEWS_API_KEY=...
HUNTER_API_KEY=...
APOLLO_API_KEY=...
SENDGRID_API_KEY=...
SENDGRID_FROM_EMAIL=...
REDIS_URL=redis://localhost:6379
```
