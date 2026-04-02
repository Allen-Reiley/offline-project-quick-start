
Below is the **PROJECT_SCOPE.md**. This is the definitive blueprint for our factory.


---

# PROJECT_SCOPE.md: AuraWorks Master Seed

## 1. Project Intent & Philosophy
The **Master Seed** is a high-performance, offline-capable "Project Factory." Its purpose is to allow the rapid generation of new industrial-grade applications (Industrial Intelligence, B2B, Market Analysis) without needing a stable internet connection once the seed is "hydrated."

* **Atomic Design:** UI is built using "Lego Bricks" (Shadcn, Aceternity, Tailark, Kokonut).
* **Infrastructure-as-Code:** Entire environments (DB, API, Web) are orchestrated via Docker.
* **Industrial Scale:** Backend is designed for heavy data processing (Pandas) and professional reporting (ReportLab) targeting the R100k+ contract sectors.

---

## 2. Core Architecture
The project follows a "Strict Fence" directory structure to avoid OS-level permission errors (like the Wine `.node` error) and to ensure Docker build-context efficiency.

```text
aura-master-seed/
├── frontend/                # Next.js 14+ (App Router)
│   ├── components/          # Hydrated UI Library (The "Warehouse")
│   ├── app/                 # Frontend Routes & Logic
│   └── Dockerfile           # Node-Alpine Optimized Build
├── backend/                 # FastAPI (Python 3.11)
│   ├── app/                 # core/, api/, models/, services/
│   ├── Dockerfile           # UV-Accelerated Build
│   └── pyproject.toml       # Modern dependency management (uv)
├── docker-compose.yml       # System Orchestrator (DB + API + Web)
├── .env                     # Local Environment Secrets
├── .gitignore               # Deployment & Git Shield
└── STRUCTURE.md             # File system manifest
```

---

## 3. Technical Stack (The "Engine" Packages)

### **Backend (FastAPI + SQLModel)**
* **`fastapi[all]`**: The high-performance web framework.
* **`sqlmodel`**: Combines SQLAlchemy & Pydantic for the database layer.
* **`alembic`**: Database migrations (version control for your schema).
* **`psycopg2-binary`**: PostgreSQL adapter.
* **`pydantic-settings`**: Environment variable management.
* **`python-jose[cryptography]` & `passlib[bcrypt]`**: Security and JWT authentication.
* **`pandas`**: High-leverage data analysis for industrial leads.
* **`reportlab`**: Generating PDF invoices and technical specs offline.
* **`loguru`**: Advanced logging for monitoring system health.

### **Frontend (Next.js + Tailwind)**
* **`framer-motion`**: For the high-end Aceternity animations.
* **`lucide-react`**: Standardized iconography.
* **`clsx` & `tailwind-merge`**: Dynamic styling utilities.
* **`axios` / `tanstack-query`**: For robust data fetching from the Backend.
* **`date-fns`**: Handling industrial timestamps and scheduling.
* **`recharts`**: Data visualization for market analysis.

---

## 4. Operational Bash Suite
These are the custom scripts that turn the Seed into a Factory:

* **`aura-init.sh`**: The "Scaffolder." Creates a new project by copying the Seed and using `fzf` (Fuzzy Finder) to pick specific UI components. It uses an "Iron Fence" logic to stay within the local filesystem.
* **`aura-add.sh`**: The "Hydrator." Downloads single components into the Master Seed via Verdaccio (local registry) for offline availability.
* **Verdaccio (PM2)**: Acts as the local "Warehouse" for all `npm` packages.

---

## 5. Implementation Roadmap

---

This updated **PROJECT_SCOPE.md** shifts our strategy to a **Local-First, Offline-Reliant Development** model. We are pivoting to ensure the core Python and Next.js logic is 100% functional on your Pop!_OS machine before we wrap it in Docker "armor."

Copy and paste this entire block into your `PROJECT_SCOPE.md` file.

---

# PROJECT_SCOPE.md: AuraWorks Master Seed

## 1. Project Intent & Philosophy
The **Master Seed** is a high-performance "Project Factory" designed for the East Rand industrial B2B market. It prioritizes **Local-First Development** to ensure 100% offline stability, with Docker orchestration as the final deployment and environment-locking phase.

* **Atomic Design:** UI built via "Lego Bricks" (Shadcn, Aceternity, Tailwind).
* **Local-First Engine:** Development happens directly on the host (Pop!_OS) using `uv` and `npm` for instant feedback.
* **Industrial Scale:** Built to process R100k+ contract data using Pandas and professional PDF reporting.

---

## 2. Core Architecture (Local-First)
The project is a decoupled Monorepo. All logic is strictly separated to ensure portability.

```text
aura-master-seed/
├── frontend/                # Next.js 14+ (App Router)
│   ├── components/          # Hydrated UI Warehouse (Aceternity, etc.)
│   ├── app/                 # Routes & Logic
│   └── package.json         # Engine: framer-motion, lucide, tanstack-query
├── backend/                 # FastAPI (Python 3.11)
│   ├── app/                 # core/, api/, models/, services/
│   ├── pyproject.toml       # Engine: sqlmodel, pandas, reportlab
│   └── aura_local.db        # Local SQLite (Offline Dev Database)
├── docker-compose.yml       # Orchestrator (DEFERRED TO PHASE 4)
├── .env                     # Local Environment Secrets
└── STRUCTURE.md             # File system manifest
```

---

## 3. Implementation Roadmap (The Law)

### **Phase 1: Local Environment Sync (Current)**
* **Backend:** Initialize `uv venv` and install the "Heavy Machinery" (FastAPI, SQLModel, Pandas).
* **Frontend:** Install "Atomic" packages (Framer Motion, Lucide, Axios).
* **Database:** Utilize SQLite (`aura_local.db`) for zero-config offline development.

### **Phase 2: The Industrial Lead Engine**
* **Schema:** Define `IndustrialClient` models in `backend/app/models/`.
* **Data Logic:** Implement Pandas scripts to analyze East Rand industrial sectors.
* **API:** Build CRUD endpoints for lead management and PDF generation via ReportLab.

### **Phase 3: The Scaffolding Scripts (Aura-CLI)**
* **`aura-init`**: Clones the seed into a new project directory.
* **`aura-add`**: Injects UI components from the local warehouse into the project.

### **Phase 4: Docker Hardening**
* Synchronize `Dockerfiles` with the final local code.
* Migrate from SQLite to PostgreSQL via `docker-compose`.
* Conduct final "Internet-Off" build test.

---

## 4. Technical Stack Manifest

| Domain | Backend (Python/UV) | Frontend (Next.js/TS) |
| :--- | :--- | :--- |
| **Core** | `fastapi`, `uvicorn` | `next`, `react`, `typescript` |
| **Data** | `sqlmodel`, `pandas`, `openpyxl` | `@tanstack/react-query`, `recharts` |
| **UI/UX** | N/A | `framer-motion`, `lucide-react`, `clsx` |
| **Industrial** | `reportlab`, `loguru` | `date-fns`, `tailwind-merge` |
| **Config** | `pydantic-settings`, `python-dotenv` | `.env.local` |

---

## 5. Instructions for Gemini AI
* **Supreme Authority:** This document overrides all other file suggestions.
* **Context Sync:** Read the GitHub repo ([Allen-Reiley/offline-project-quick-start](https://github.com/Allen-Reiley/offline-project-quick-start)) before every response.
* **Logic First:** Prioritize local execution (`uv`, `npm`) over Docker commands until Phase 4.

