I have processed the entire history of our architectural "Phoenix" build. I have synthesized your background as a self-taught full-stack developer in the East Rand, your transition to Pop!_OS, the requirement for an offline-first "Master Seed," and the specific "Lego Set" philosophy we are using for AuraWorks.

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

### **Phase 1: The Integrity Fix (CURRENT)**
* Ensure `docker-compose.yml` points to the correct subdirectory Dockerfiles.
* Synchronize `.env` with `backend/app/core/config.py`.
* Validate the `uv` binary path in the Backend Dockerfile.

### **Phase 2: Data & Intelligence**
* Initialize SQLModel tables for "Industrial Clients."
* Create a Seed script to populate the DB with local Gauteng market data.

### **Phase 3: The Frontend Bridge**
* Set up a global API client in Next.js.
* Build the "Industrial Dashboard" using the hydrated components.

### **Phase 4: Full Offline Test**
* Disconnect internet and run `aura-init.sh` to confirm a 100% offline project build.

---