# Contributing to ChainForge Frontend

Thank you for contributing to the ChainForge frontend. This document covers the development workflow, code standards, and conventions for submitting changes.

---

## Table of contents

- [Getting started](#getting-started)
- [Development workflow](#development-workflow)
- [Branching strategy](#branching-strategy)
- [Commit conventions](#commit-conventions)
- [Code standards](#code-standards)
- [Validation checklist](#validation-checklist)
- [Pull request process](#pull-request-process)
- [UI/UX guidelines](#uiux-guidelines)
- [Common tasks](#common-tasks)
- [Troubleshooting](#troubleshooting)
- [Getting help](#getting-help)

---

## Getting started

### Prerequisites

| Tool | Minimum version | Notes |
|---|---|---|
| Node.js | 18.x | Use [nvm](https://github.com/nvm-sh/nvm) or [fnm](https://github.com/Schniz/fnm) |
| pnpm | 9.x | `npm install -g pnpm` or [standalone installer](https://pnpm.io/installation) |
| Freighter | latest | [Browser extension](https://www.freighter.app/) for wallet testing |

**Why pnpm?** This repository uses pnpm workspaces. Using `npm` or `yarn` inside `app/frontend/` directly will produce a mismatched lockfile and can break other workspace packages. Always use `pnpm`.

### Initial setup

1. **Fork and clone** the repository:

```bash
git clone https://github.com/YOUR_USERNAME/chainforge.git
cd chainforge
```

2. **Install dependencies** from the monorepo root:

```bash
pnpm install
```

This installs dependencies for all workspace packages at once using the shared lockfile. Never edit the lockfile manually.

3. **Set up environment variables:**

```bash
cd app/frontend
cp .env.example .env.local
# Edit .env.local with your configuration
```

Key variables to configure:

```bash
NEXT_PUBLIC_API_URL=http://localhost:4000
NEXT_PUBLIC_STELLAR_NETWORK=testnet
NEXT_PUBLIC_STELLAR_HORIZON_URL=https://horizon-testnet.stellar.org
NEXT_PUBLIC_STELLAR_SOROBAN_RPC_URL=https://soroban-testnet.stellar.org
NEXT_PUBLIC_AID_ESCROW_CONTRACT_ID=your_contract_id
```

The navbar displays a network and environment indicator so you always know which Stellar network and app environment you are targeting.

4. **Start the dev server:**

```bash
pnpm dev
# or from the monorepo root:
pnpm --filter frontend dev
```

Open [http://localhost:3000](http://localhost:3000).

---

## Development workflow

### 1. Create a feature branch

Always work on a branch, never directly on `main`:

```bash
git checkout -b feature/your-feature-name
```

### 2. Make your changes

- Follow the [code standards](#code-standards) below
- Add or update tests as needed
- Update documentation if you change APIs or add features
- Run the [validation checklist](#validation-checklist) locally before pushing

### 3. Commit your changes

```bash
git add .
git commit -m "feat(ui): add campaign creation dialog"
```

### 4. Push and open a PR

```bash
git push origin feature/your-feature-name
```

---

## Branching strategy

| Branch | Purpose |
|---|---|
| `main` | Production-ready code |
| `develop` | Integration branch for features |
| `feature/*` | New features |
| `bugfix/*` | Bug fixes |
| `hotfix/*` | Urgent production fixes |
| `release/*` | Release preparation |

Branch names should be descriptive and kebab-case:

```bash
# Good
feature/wallet-integration
bugfix/map-marker-positioning

# Bad
new-feature
fix
myBranch
```

---

## Commit conventions

We follow [Conventional Commits](https://www.conventionalcommits.org/).

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Use for |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructuring, no feature change |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `chore` | Maintenance (deps, config) |
| `ci` | CI/CD changes |

### Scopes

Use the affected feature or area: `ui`, `api`, `wallet`, `maps`, `campaign`, `claim`, `auth`.

### Examples

```bash
# Good
git commit -m "feat(wallet): add Freighter wallet connection"
git commit -m "fix(maps): resolve marker icon not displaying in production"
git commit -m "docs(contributing): add environment variable instructions"

# Bad
git commit -m "update stuff"
git commit -m "WIP"
```

---

## Code standards

### TypeScript

- **Always use TypeScript.** No `.js` or `.jsx` files in `src/`.
- **Define explicit interfaces** for component props and data structures.
- **Avoid `any`.** Use `unknown` or a proper type. If `any` is unavoidable, add an inline comment explaining why.
- **Use type inference** where it does not sacrifice clarity.

```tsx
// Good
interface CampaignCardProps {
  title: string;
  amount: number;
  onClaim: () => void;
}

export function CampaignCard({ title, amount, onClaim }: CampaignCardProps) {
  return <div onClick={onClick}>{title}: {amount} XLM</div>;
}
```

### React components

- **Use functional components** with hooks. No class components.
- **Use named exports.** Default exports make refactoring harder.
- **Destructure props** in function parameters.
- **Use fragment shorthand** (`<>` not `<React.Fragment>`).

### Styling

- **Use Tailwind CSS 4 utilities.** Avoid custom CSS unless Tailwind cannot achieve the result.
- **Never use inline `style` props** for layout or spacing.
- **Always support dark mode** with the `dark:` prefix.
- Use responsive modifiers (`sm:`, `md:`, `lg:`) for adaptive layouts.
- For conditional class logic, use `clsx` or a `cn` helper.

### File and naming conventions

| Thing | Convention | Example |
|---|---|---|
| Component name | PascalCase | `CampaignCard` |
| File name | kebab-case | `campaign-card.tsx` |
| Hook name | camelCase with `use` prefix | `useCampaigns` |
| Types / Interfaces | PascalCase | `CampaignData` |
| Constants | SCREAMING_SNAKE_CASE | `API_BASE_URL` |

### File organization

```
src/components/
├── ui/                   # Reusable Radix UI primitives
├── features/             # Feature-specific components
│   ├── campaign/
│   └── wallet/
└── layout/               # Layout components
```

### Import order

1. React and Next.js
2. External libraries
3. Internal components and utilities
4. Types
5. Styles

### Leaflet / Map components

Leaflet requires a real DOM and cannot render server-side. Any component that imports from `leaflet` or `react-leaflet` must use a dynamic import with `ssr: false`.

```tsx
const AidMap = dynamic(() => import("@/components/features/maps/aid-map"), {
  ssr: false,
  loading: () => <MapSkeleton />,
});
```

### Stellar / Freighter integration

- Freighter API calls are **browser-only**. Guard them with `typeof window !== "undefined"` or call them inside `useEffect`.
- **Never log or store a user's private key or seed phrase.**
- Always target **testnet** during development.

### State management

| State type | Tool |
|---|---|
| Server / async state | React Query (`useQuery`, `useMutation`) |
| Local component state | `useState`, `useReducer` |
| Shared client state | React Context (if needed) |

### Environment variables

- All client-side variables must be prefixed with `NEXT_PUBLIC_`.
- Document every new variable in `.env.example` with a comment explaining its purpose.
- Never commit real secrets. `.env.local` is gitignored.

---

## Validation checklist

Run these checks locally before pushing. CI runs the same steps.

### 1 — Type check

```bash
pnpm type-check
```

### 2 — Lint

```bash
pnpm lint
```

Zero-warning policy — any warning is treated as an error.

```bash
pnpm lint --fix   # Auto-fix what you can
```

### 3 — Tests

```bash
pnpm test
```

Testing conventions:
- Co-locate test files with the source they cover
- Query by role, label, or visible text — in that order
- Wrap renders in a fresh `QueryClientProvider` per test
- Mock Stellar/Freighter API calls at the module boundary

### 4 — Production build

```bash
pnpm build
```

Always run this locally before opening a PR if you have:
- Added or changed environment variables
- Added a new dependency or changed import paths
- Modified `next.config.ts` or Tailwind config
- Added a new page, route, or Leaflet component

### Pre-push checklist

- [ ] `pnpm type-check` — no errors
- [ ] `pnpm lint` — no warnings or errors
- [ ] `pnpm test` — all tests pass
- [ ] `pnpm build` — build succeeds
- [ ] Manually tested in the dev environment
- [ ] Tested in both light and dark modes
- [ ] Tested responsive layout on mobile / tablet / desktop

---

## Pull request process

### Before opening a PR

- [ ] Branch is up-to-date with `develop`
- [ ] All validation checks pass locally
- [ ] New features include tests where applicable
- [ ] Documentation updated (README, inline comments, `.env.example`)
- [ ] Screenshots attached for any UI changes

### PR description template

```markdown
## Description

Brief summary of the change and why it's needed.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [ ] Tested locally
- [ ] Added unit tests
- [ ] Tested on Stellar Testnet (for wallet/contract changes)

## Related Issues

Closes #
```

### Review process

1. **Automated CI** runs `type-check`, `lint`, `test`, and `build` on every push.
2. **Code review** — at least one maintainer reviews your PR.
3. **Address feedback** — push changes to the same branch.
4. **Merge** — maintainer merges once approved.

---

## UI/UX guidelines

### Core principles

- **Accessibility first** — Use semantic HTML, ARIA labels, and keyboard navigation.
- **Mobile-first** — Design for mobile, enhance for desktop.
- **Dark mode always** — Every new component must support `dark:` variants.
- **Performance** — Lazy-load images, use `next/image`, and use `dynamic` imports for heavy components.

### Component states

Every interactive component should handle:

| State | What to show |
|---|---|
| Loading | Skeleton or spinner |
| Error | Clear message with a retry option |
| Empty | Helpful guidance, not a blank space |
| Destructive action | Confirmation dialog before proceeding |

### Accessibility

- Use semantic HTML (`<button>`, `<nav>`, `<main>`, `<section>`).
- Add descriptive `alt` text to all images.
- Ensure color contrast meets WCAG AA.
- Test keyboard navigation (Tab, Enter, Escape, arrow keys).
- Prefer Radix UI primitives — they ship with accessibility built in.

---

## Common tasks

### Adding a new page

Create a file in `src/app/your-route/page.tsx`. Note that Next.js App Router requires a **default export** for page files:

```tsx
export default function CampaignsPage() {
  return <main>Campaigns</main>;
}
```

### Adding a new component

1. Create the file in `src/components/ui/` (primitive) or `src/components/features/<feature>/` (feature-specific).
2. Define a props interface.
3. Implement with a named export.

### Adding a new API route

```tsx
export async function GET() {
  return NextResponse.json({ data: "value" });
}
```

### Installing a new library

```bash
pnpm add library-name            # runtime dependency
pnpm add -D @types/library-name  # types if needed
```

### Adding or updating environment variables

1. Add to `.env.example` with a placeholder value and a comment.
2. Document in `README.md` under environment setup.
3. Update the Vercel dashboard for staging and production.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Hydration errors | Wrap Leaflet/Freighter components with `dynamic(..., { ssr: false })` |
| Freighter returns `undefined` | Guard calls with `typeof window !== "undefined"` and use `useEffect` |
| ENV vars undefined | Must start with `NEXT_PUBLIC_`; restart dev server after changes |
| Build fails after adding Leaflet | Import with `ssr: false` |
| Port 3000 in use | `pnpm dev -- -p 3001` |
| Stale builds | `rm -rf .next && pnpm install` |

---

## Getting help

- **Questions:** Open a [GitHub Discussion](https://github.com/your-org/chainforge/discussions)
- **Bugs:** Open a [GitHub Issue](https://github.com/your-org/chainforge/issues) with steps to reproduce
- **Docs:** Check the [README](./README.md) and [project docs](../../README.md) first

---

## Code of conduct

Be respectful, inclusive, and constructive. We are building this for humanitarian impact — every contribution matters.
