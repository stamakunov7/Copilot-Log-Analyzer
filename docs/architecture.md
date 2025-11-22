# Architecture

This document describes the high-level architecture of Copilot Log Analyzer.

- CLI sends logs to backend via HTTP or WebSocket
- Backend persists logs to DB, computes metrics, and calls an LLM to generate summaries
- Frontend shows session list, session details, live logs, metrics and AI summaries
