.
├── frontend/                # Next.js + Tailwind + Shadcn
│   ├── components/          # The "Lego Bricks" (Aceternity, etc.)
│   ├── app/                 # Next.js App Router logic
│   ├── public/              # Static assets
│   ├── Dockerfile           # Frontend build instructions
│   └── package.json
├── backend/                 # FastAPI + SQLModel
│   ├── app/
│   │   ├── api/             # Endpoints (Industrial monitoring, etc.)
│   │   ├── core/            # db.py, config.py, security.py
│   │   ├── models/          # SQLModel Table definitions
│   │   └── main.py          # Entry point
│   ├── Dockerfile           # Backend build (UV-optimized)
│   └── pyproject.toml       # Modern Python dependencies
├── docker-compose.yml       # Orchestrates everything
├── .gitignore               # The "Shield" (keeps repo clean)
├── .env.example             # Template for local dev
└── STRUCTURE.md             # The map for your future self
