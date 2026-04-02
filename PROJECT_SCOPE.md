
Below is the **PROJECT_SCOPE.md**. This is the definitive blueprint for our factory.

Instruction: Read into REMEMBER.md, scan the file to read the prompt conversation that was had in the creation of the project, to when it worked and to when things got messy. It's to serve as a reference for what worked an what didn't, the errors we encountered and the fixes that were made, it's to inspire the highest level of quality in attempt to reduce the number of failures we encounter in the process of creating this project. For consistency purposeses, after every prompt and project modification, this code base will be uploaded to git, including having the conversations being included into the REMEMBER.md, so don't cache the link and/or information you find in the repo, the data will always be updated, so always update your context accordingly. Read into the errors and logs sent to you in the Gemini chat, ensure that once you've read the entire repo, refer back to all the files that hold significance to the problem at hand, read them, modify and load them into your response.

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

## **I. Project Overview & Strategic Intent**
The **AuraWorks Master Seed** is designed as a portable, Docker-orchestrated development environment.
* **Structure:** A decoupled Monorepo (Frontend/Backend).
* **Intent:** To eliminate "environment drift" and enable zero-latency development for industrial clients in the East Rand by having all "Lego Bricks" (UI components) and "Heavy Machinery" (Python processing) pre-baked into local containers.

---

## **II. Phase 1: Infrastructure Synchronization (Immediate)**
The priority is fixing the "File Not Found" errors by aligning the Docker Volume mappings and Build Contexts.

### **1. Backend "UV" Engine Setup**
We are using `uv` for 10x faster dependency resolution.
* **Target:** `backend/Dockerfile`
* **Logic:** Move `uv` binary to `/usr/local/bin` and ensure `pyproject.toml` is the source of truth.
* **Packages to Add:** * `sqlmodel`, `alembic` (Database)
    * `pandas`, `openpyxl` (Industrial Data)
    * `reportlab` (PDF generation)
    * `pydantic-settings`, `python-dotenv` (Config)
    * `loguru` (Diagnostics)

### **2. Frontend "Atomic" Setup**
* **Target:** `frontend/Dockerfile`
* **Logic:** Ensure the `build context` includes the `components/` folder moved from the root.
* **Packages to Add:** * `framer-motion`, `clsx`, `tailwind-merge` (UI Core)
    * `lucide-react` (Icons)
    * `axios`, `@tanstack/react-query` (Data Bridge)
    * `recharts` (Analytics)

---

## **III. Phase 2: The Industrial Lead Engine**
Building the first functional logic for the B2B market analysis.

1.  **Schema Definition:** Create `backend/app/models/industrial.py`.
2.  **Seeding Logic:** Create a `seed.py` script to inject local East Rand industrial data (Companies, Sector, Contract Value) into the Postgres DB.
3.  **The API Layer:** Build CRUD endpoints in `backend/app/api/v1/`.

---

## **IV. Phase 3: The Scaffolding Scripts (Aura-CLI)**
This turns the repository from a "Project" into a "Factory."

* **`aura-init <project-name>`**:
    * Clones the Seed.
    * Renames the Docker containers.
    * Generates a new `.env` with unique keys.
* **`aura-pull <component-name>`**: 
    * Queries the local "Warehouse" (Verdaccio).
    * Injects the code into `frontend/components/`.

---

## **V. Phase 4: Verification & Hardening**
1.  **Offline Build Test:** Disable networking and run `docker compose build --no-cache`.
2.  **Health Check:** Implement a `/health` route that checks DB latency and Disk I/O.
3.  **Documentation:** Generate automated API docs via FastAPI `/docs`.

---

### **Summary Table: Package Manifest**

| Domain | Backend (Python/UV) | Frontend (Next.js/TS) |
| :--- | :--- | :--- |
| **Core** | `fastapi`, `uvicorn` | `next`, `react`, `typescript` |
| **Data** | `sqlmodel`, `pandas` | `tanstack-query`, `recharts` |
| **UI/UX** | N/A | `framer-motion`, `lucide-react` |
| **Industrial** | `reportlab`, `openpyxl` | `date-fns` |
| **Security** | `python-jose`, `passlib` | `next-auth` (Planned) |



