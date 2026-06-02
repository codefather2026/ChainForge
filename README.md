<p align="center">
  <img src="assets/soter-logo.png" width="160" alt="Soter logo" />
</p>

# Soter

Soter is a testnet-first humanitarian aid distribution platform built on the Stellar ecosystem (Soroban). It combines on-chain escrow + auditable events with off-chain verification and field-ready client apps.

## What’s in this repo

- Backend (NestJS): APIs, orchestration, persistence, on-chain adapter, observability ([backend README](app/backend/README.md))
- Smart Contracts (Soroban/Rust): AidEscrow escrow + claim flows ([onchain README](app/onchain/README.md))
- Frontend (Next.js): admin/donor UI, dashboards, wallet flows ([frontend README](app/frontend/README.md))
- Mobile (Expo): field operations + pilot flows ([mobile README](app/mobile/README.md))
- AI Service (FastAPI): OCR/anonymization/fraud checks for verification flows ([ai-service README](app/ai-service/README.md))

## Quick start (local dev)

Prereqs:
- Node.js 18+
- Python 3.11+
- Rust toolchain + Soroban CLI (for contracts)

### Backend (NestJS)

```bash
cd app/backend
npm ci
cp .env.example .env
npm run prisma:migrate
npm run start:dev
```

### Frontend (Next.js)

```bash
cd app/frontend
pnpm install
cp .env.example .env.local
pnpm dev
```

### AI service (FastAPI)

```bash
cd app/ai-service
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Mobile (Expo)

```bash
cd app/mobile
pnpm install
cp .env.example .env
pnpm start
```

## Testnet setup (high level)

- Deploy the Soroban contracts to testnet and capture contract IDs.
- Configure the backend to target testnet RPC + network passphrase + contract ID(s).
- Configure frontend/mobile environment variables to point at the backend and set the testnet network + contract IDs.

Helpful starting points:
- Backend Soroban integration notes: [SOROBAN_INTEGRATION.md](app/backend/src/onchain/SOROBAN_INTEGRATION.md)
- Contract docs and method/event reference: [onchain README](app/onchain/README.md)

## Contributing

We review contributor branches frequently. Keep PRs small and focused, and include:
- A clear problem statement + acceptance criteria
- Tests or a short manual test plan
- No secrets committed (keys, tokens, seed phrases)

For component-specific contribution details, follow the README in each folder linked above.
