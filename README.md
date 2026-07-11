---
title: Musik Maker
emoji: 🎵
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 6.20.0
app_file: app.py
python_version: "3.11"
license: mit
pinned: false
short_description: Musica AI da testo con Stable Audio 3 small
startup_duration_timeout: 1h
suggested_hardware: cpu-basic
models:
  - stabilityai/stable-audio-3-small-music
---

# 🎵 Musik Maker

Genera musica strumentale da un prompt testuale e scaricala in MP3 — gratis,
con output **di tua proprietà** anche per uso commerciale (video YouTube
monetizzati, spot, ecc., sotto 1 M$ di fatturato annuo).

**▶️ App online: https://roberto-casale.github.io/musik-maker/**

## Come funziona

La pagina (statica, su GitHub Pages) chiama via API lo
[Space ufficiale Stable Audio 3](https://huggingface.co/spaces/stabilityai/stable-audio-3)
di Stability AI, che gira su GPU gratuite (ZeroGPU). Nessun server proprio,
nessuna chiave nel codice: la generazione usa la quota GPU gratuita
giornaliera del visitatore (anonima per IP, più ampia salvando un proprio
token Hugging Face nelle impostazioni della pagina — resta nel browser).

- Modelli: **medium** (fino a 6:20, qualità migliore) e **small** (fino a 2:00).
- Output: WAV dal motore, **MP3 convertito direttamente nel browser**.
- Generazione tipica: pochi secondi.

## Struttura del repo

- [docs/index.html](docs/index.html) — l'app web (tutto in un file: UI, chiamata
  API via `@gradio/client`, conversione MP3 con lamejs).
- [app.py](app.py) + [requirements.txt](requirements.txt) +
  [deploy.py](deploy.py) — **piano B**: la stessa app come Space Gradio
  self-hosted con `stable-audio-3-small-music`. Pronta e revisionata, ma da
  luglio 2026 ospitare uno Space Gradio proprio richiede Hugging Face PRO
  ($9/mese); istruzioni in [GUIDA.md](GUIDA.md).
- [.github/workflows/keep-alive.yml](.github/workflows/keep-alive.yml) —
  keep-alive giornaliero dello Space (solo per il piano B, inattivo senza
  secret).

## Licenza della musica generata

Modello distribuito con la
[Stability AI Community License](https://stability.ai/license): gli output
appartengono a chi li genera, uso commerciale libero sotto 1 M$ di fatturato
annuo, addestramento su dati interamente licenziati. La musica puramente
generata da AI non è coperta da copyright: non registrarla nel Content ID e
usa l'etichetta «contenuto generato con AI» su YouTube.

Codice del progetto: licenza MIT ([LICENSE](LICENSE)).
