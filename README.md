# Personal Finance Analytics System

A modular Python application for tracking income and expenses, managing budgets, and analyzing personal spending through data visualization.

Built as a learning project to apply OOP, file handling, exception handling, and data analysis (Pandas/NumPy/Matplotlib) in a real, multi-file application — not a tutorial script.

---

## Features

- **Authentication** — user registration, login, session management (see [Known Limitations](#known-limitations))
- **Income & Expense tracking** — add, categorize, and view records tied to the logged-in user
- **Transactions** — JSON-backed CRUD, filterable by user and attributes
- **Budgets** — set spending limits, track against them, flag overruns
- **Analytics** — total income/expense/savings, category breakdowns, spending patterns
- **Visualization** — income vs. expense, monthly trends, category distribution, budget comparison
- **Reports** — financial summaries prepared for export

---

## Architecture

```text
Personal-Finance-Analytics-System/
├── main.py
├── mypkg/
│   ├── models/       # User, Income, Expense, Transaction, Budget
│   ├── services/      # Auth, Session, Dashboard, Transaction/Budget services, Analytics, File I/O
│   ├── utils/         # Validators, helpers
│   └── data/          # users.json, transactions.json, budgets.json
├── exports/
└── logs/
```

**Flow:** Register/Login → Session created → Dashboard → Income/Expense/Transactions/Budget → Analytics → Graphs & Reports

Each service owns one responsibility — e.g. `analytics.py` never touches raw JSON directly, it consumes data the file manager loads.

---

## Analytics Pipeline

```text
JSON Storage → Pandas DataFrame → Cleaning/Filtering → NumPy Calculations → Matplotlib Visualization
```

---

## Getting Started

```bash
git clone <https://github.com/charanpersoa-a11y/Personal-Finance-Analytics-System.git>
cd Personal-Finance-Analytics-System
pip install -r requirements.txt   # pandas, numpy, matplotlib
python main.py
```

## Usage

```text
====================================
 Personal Finance Analytics System
====================================
1. Register
2. Login
3. Exit
```

After login:

```text
====================================
          DASHBOARD
====================================
1. Add Income
2. Add Expense
3. Transactions
4. Budget
5. Analytics
6. Graphs
7. Reports
8. Logout
```

*(Sample output — expense-vs-budget chart and a category breakdown pie chart — goes here once graphs are finalized.)*

---

## Known Limitations

- **Passwords are stored in plain text**, not hashed. This is a known gap, not an oversight — hashing (bcrypt/argon2) is the top priority before this touches any real financial data.
- Storage is flat JSON, not a database — fine for single-user local use, not concurrent-safe.
- No automated tests yet.

---

## Tech Stack

Python 3 · `json` · `pathlib` · `numpy` · `pandas` · `matplotlib`

---

## Roadmap

- [ ] Password hashing
- [ ] SQLite/PostgreSQL backend
- [ ] Unit + integration tests
- [ ] PDF/CSV export
- [ ] GUI or web front end

---

## License

Created for learning and educational purposes.