# Contributing to ChainForge Mobile

Thank you for contributing to the ChainForge mobile application. This guide covers the development setup, workflow, and conventions for the mobile module.

---

## Quick start

```bash
pnpm install
cp .env.example .env
# Edit .env with your configuration
pnpm start
```

---

## Development workflow

### Running tests

```bash
pnpm test
```

Runs the Jest test suite covering all screens, services, and utility functions.

### Running linting

```bash
pnpm lint
```

ESLint with Expo configuration. Fix all warnings before opening a pull request.

### Starting the dev server

```bash
pnpm start
```

- Metro server starts on `http://localhost:8081` by default
- Scan the QR code with Expo Go on a physical device
- Press `a` for Android emulator, `i` for iOS simulator
- Use `--clear` to clear Metro cache: `expo start --clear`

### Platform commands

- **Android**: `pnpm android`
- **iOS**: `pnpm ios`
- **Web**: `pnpm web`

---

## Environment configuration

```bash
cp .env.example .env
```

### Required variables

```bash
EXPO_PUBLIC_API_URL=http://localhost:3000
EXPO_PUBLIC_NETWORK=testnet
```

### Finding your local IP

**Windows:**
```bash
ipconfig
# Look for IPv4 Address under your active adapter
```

**macOS/Linux:**
```bash
ifconfig | grep "inet "
# Look for 192.168.x.x or 10.x.x.x
```

---

## Branching and workflow

- Create feature branches from `main`
- Use descriptive kebab-case names: `feature/mobile-auth`, `fix/scanner-crash`
- Keep branches focused on a single feature or fix

## Commit conventions

Follow conventional commits:

- `feat(mobile): ...` — New features
- `fix(mobile): ...` — Bug fixes
- `docs(mobile): ...` — Documentation
- `test(mobile): ...` — Test additions or changes
- `refactor(mobile): ...` — Code restructuring
- `chore(mobile): ...` — Tooling, dependencies, config

---

## Code standards

- **TypeScript** — All source files must use TypeScript. No plain `.js`.
- **Functional components** — Use hooks and functional patterns. No class components.
- **Named exports** — Prefer named exports over default exports.
- **Accessibility** — Every interactive element must have an `accessibilityLabel` and `accessibilityHint`.
- **Minimum tap target** — 44x44 pt per WCAG 2.5.5.
- **Dark mode** — Every screen must support both light and dark themes via `useTheme()`.

### Style guide

- Use `StyleSheet.create()` for component styles — no inline styles for layout.
- Import theme colors from `useTheme()` hook: `const { colors } = useTheme()`.
- Follow existing naming conventions and file organization.

---

## Architecture

```
src/
├── screens/           # Screen-level components (one per route)
├── components/        # Reusable UI components
├── services/          # API clients, cache, sync, wallet
├── contexts/          # React Context providers
├── theme/             # Brand colors, typography, navigation themes
├── navigation/        # Stack navigator configuration
├── hooks/             # Custom React hooks
├── types/             # TypeScript interfaces and definitions
├── config/            # Environment configuration and validation
└── __tests__/         # Test files co-located by feature
```

---

## Troubleshooting

### Metro bundler issues

```bash
expo start --clear              # Clear Metro cache
rm -rf node_modules && pnpm install  # Full reinstall
```

### Connectivity issues

- Physical device: Update `EXPO_PUBLIC_API_URL` to your machine's LAN IP
- Android Emulator: Use `http://10.0.2.2:3000`
- iOS Simulator: Use `http://localhost:3000`
- Ensure device and development machine are on the same network

### Common issues

| Issue | Solution |
|---|---|
| Hot reloading not working | Shake device | Reload, or press `r` in Metro terminal |
| App crashes on startup | Check Metro logs, verify env variables, reinstall deps |
| Bundle errors | Check import paths, restart Metro with `--clear` |

---

## Pull request checklist

Before submitting a PR:

- [ ] Branch is up to date with `main`
- [ ] All tests pass: `pnpm test`
- [ ] Linting passes: `pnpm lint`
- [ ] New features include tests
- [ ] No hardcoded API endpoints (use `.env`)
- [ ] Environment variables documented in `.env.example`
- [ ] Screenshots included for UI changes
- [ ] Code follows existing style patterns
- [ ] Accessibility labels added for new interactive elements

---

## Getting help

1. Check existing GitHub Issues
2. Review the [Root README](../../README.md) for project context
3. Open a new issue with detailed reproduction steps
