This **README.md** is designed for the **AuraWorks Master Seed**. It acts as the "Operation Manual" for your project factory, ensuring that any developer (or your future self) understands how to use the `aura-init` CLI and the Dockerized architecture.

-----

# 🚀 AuraWorks Master Seed

The **AuraWorks Master Seed** is a high-performance, white-label project factory. It is designed to be a "Mother Mold" for rapidly spinning up decoupled monorepos (Next.js + FastAPI) with zero environment drift, powered by Docker and `uv`.

## 🏗️ Project Architecture

The seed is split into two primary engines, pre-linked and ready for industrial-grade data processing.

  * **Frontend:** Next.js 14+ (App Router) with Tailwind CSS, Framer Motion, and TanStack Query.
  * **Backend:** FastAPI (Python 3.12) using `uv` for dependency management and `SQLModel` for ORM.
  * **Database:** PostgreSQL (Dockerized) or local SQLite for rapid prototyping.

-----

## 🛠️ The Aura-CLI (Factory Tools)

This repository includes a suite of automation scripts to turn the seed into a unique project in seconds.

### **1. Initialize a New Project**

Clone the seed and rename all internal references (Docker containers, environment variables, and directories).

```bash
aura-init <your-project-name>
```

### **2. Component Picker (Lego Bricks)**

During initialization, a fuzzy finder (`fzf`) will allow you to select specific UI components from the `frontend/components` warehouse to hydrate your new project.

### **3. Surgical Pull**

Need to grab a specific component from the Master Seed into an existing project?

```bash
aura-pull <path/to/component.tsx>
```

-----

## 📦 Getting Started (Development)

### **Local-First Setup**

Ensure you have the "Heavy Machinery" installed on your host (Pop\!\_OS):

1.  **Backend:** `cd backend && uv venv && source .venv/bin/activate && uv pip install .`
2.  **Frontend:** `cd frontend && npm install && npm run dev`

### **Docker Hardening**

To run the full stack in a production-ready containerized environment:

```bash
docker compose up --build
```

  * **Frontend:** [http://localhost:3000](https://www.google.com/search?q=http://localhost:3000)
  * **API Docs:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
  * **Database:** `localhost:5432`

-----

## 📜 Technical Manifest

| Layer | Technology | Key Packages |
| :--- | :--- | :--- |
| **Frontend** | Next.js 14 | `framer-motion`, `lucide-react`, `tanstack-query` |
| **Backend** | FastAPI | `sqlmodel`, `pandas`, `loguru` |
| **Environment** | Docker | `docker-compose`, `uv` |
| **Database** | PostgreSQL | `asyncpg`, `alembic` |

-----

## 🛡️ Maintenance & Warehouse

To add new high-performance UI components or backend patterns to the "Mother Mold":

1.  Add the file to `frontend/components/` or `backend/app/models/` in the **Master Seed** repo.
2.  Run `git commit` to ensure the factory is updated for future projects.

-----

> **Note:** This project is governed by the `PROJECT_SCOPE.md`. Refer to that document for the core implementation roadmap and constitutional logic.