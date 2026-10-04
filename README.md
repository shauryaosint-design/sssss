# SHAURYA OSINT — Number Intelligence Web

Cyberpunk-style number lookup UI + Python serverless backend, ready for **Vercel**.

## Local preview

Just open `public/index.html` in a browser (API calls will fail without backend).

Or run a tiny static server:

```bash
cd public && python3 -m http.server 3000
```

## Deploy to Vercel

### Option A — Vercel CLI (fastest)

```bash
npm i -g vercel
cd shaurya-osint-web
vercel
```

Follow prompts → production deploy:

```bash
vercel --prod
```

### Option B — GitHub

1. Create a new GitHub repo
2. Push this folder
3. Go to [vercel.com/new](https://vercel.com/new)
4. Import the repo → Deploy

## Project layout

```
shaurya-osint-web/
├── api/
│   └── lookup.py      # Python serverless function (proxies upstream API)
├── public/
│   └── index.html     # Cyberpunk UI
├── vercel.json        # Routes + builds
├── requirements.txt
└── README.md
```

## API

```
GET /api/lookup?n=9876543210
```

Returns upstream JSON or `{ "status": "error", "message": "..." }`.

## Notes

- Backend is pure Python stdlib (no pip packages needed).
- Upstream API: `srahitek-num-info-api-xi.vercel.app`
- Use only for numbers you are authorized to query.
