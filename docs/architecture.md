# Architecture

This document describes the high-level architecture of Copilot Log Analyzer.

- CLI sends logs to backend via HTTP or WebSocket
- Backend persists logs to DB, computes metrics, and calls an LLM to generate summaries
- Frontend shows session list, session details, live logs, metrics and AI summaries

logpilot-ai/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ docker-compose.yml          # Local run backend + db + frontend
├─ pyproject.toml / requirements.txt
├─ package.json                # for root scripts
│
├─ backend/
│  ├─ app/
│  │  ├─ __init__.py
│  │  ├─ main.py              # FastAPI entrypoint, WS + REST endpoints
│  │  ├─ config.py            # settings (env, DB URL, etc.)
│  │  ├─ models.py            # SQLAlchemy models: Session, LogEvent, Summary
│  │  ├─ schemas.py           # Pydantic schemas (LogEventIn, SessionOut, SummaryOut)
│  │  ├─ database.py          # DB connection, sessionmaker
│  │  ├─ services/
│  │  │  ├─ ingestion_service.py   # logic for receiving and storing logs
│  │  │  ├─ metrics_service.py     # p90/p99, aggregations
│  │  │  ├─ summarizer_service.py  # working with LLM for summary
│  │  │  └─ sessions_service.py    # creating/updating sessions
│  │  ├─ routers/
│  │  │  ├─ logs.py           # /api/logs, /api/logs/batch
│  │  │  ├─ sessions.py       # /api/sessions, /api/sessions/{id}
│  │  │  ├─ summaries.py      # /api/sessions/{id}/summaries
│  │  │  └─ metrics.py        # /api/sessions/{id}/metrics
│  │  └─ ws/
│  │     └─ logs_ws.py        # /ws/logs WebSocket endpoint
│  │
│  ├─ tests/
│  │  ├─ test_sessions.py
│  │  ├─ test_logs.py
│  │  ├─ test_metrics.py
│  │  └─ test_summarizer.py
│  │
│  └─ Dockerfile              # backend container for Cloud Run
│
├─ frontend/
│  ├─ public/
│  ├─ src/
│  │  ├─ main.tsx / index.tsx
│  │  ├─ App.tsx
│  │  ├─ api/                 # wrappers over REST API
│  │  │  ├─ sessions.ts
│  │  │  ├─ logs.ts
│  │  │  ├─ summaries.ts
│  │  │  └─ metrics.ts
│  │  ├─ components/
│  │  │  ├─ SessionList.tsx       # list of sessions
│  │  │  ├─ SessionDetails.tsx    # logs + summary
│  │  │  ├─ LiveLogView.tsx       # live tail via WebSocket
│  │  │  ├─ SummaryPanel.tsx      # AI summary block
│  │  │  ├─ MetricsCharts.tsx     # charts for p90/p99 etc.
│  │  │  └─ Layout.tsx
│  │  ├─ hooks/
│  │  │  └─ useWebSocketLogs.ts   # custom hook for WS logs
│  │  ├─ types/
│  │  │  ├─ session.ts
│  │  │  ├─ log.ts
│  │  │  └─ summary.ts
│  │  └─ styles/
│  └─ Dockerfile              # frontend in a separate container (will see, mb Cloud Run)
│
├─ cli/
│  ├─ logwatch/
│  │  ├─ __init__.py
│  │  ├─ main.py              # entrypoint: `logwatch ...`
│  │  ├─ commands/
│  │  │  ├─ run.py            # `logwatch run "mvn test"`
│  │  │  └─ tail.py           # `logwatch tail app.log`
│  │  ├─ client.py            # WebSocket/HTTP client for sending logs
│  │  └─ config.py            # backend address, token, etc.
│  └─ pyproject.toml / setup.cfg  # to install cli via pip (`pip install -e .`)
│
├─ infra/
│  ├─ docker/
│  │  └─ backend.env.example
│  ├─ cloudrun/
│  │  ├─ backend.service.yaml
│  │  └─ frontend.service.yaml
└─ docs/
   ├─ architecture.md          # textual architecture description
   ├─ api.md                   # API endpoints documentation
   └─ diagrams/
      ├─ architecture.mmd      # Mermaid diagram
      └─ sequence-logs.mmd     # sequence: CLI → backend → DB → AI → UI
