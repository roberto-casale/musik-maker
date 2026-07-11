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

Genera musica strumentale da un prompt testuale e scaricala in MP3.
Frontend Gradio + modello open-weight
[stable-audio-3-small-music](https://huggingface.co/stabilityai/stable-audio-3-small-music)
di Stability AI, in esecuzione su uno Space Hugging Face gratuito (CPU).

## Come funziona

1. Scrivi un prompt che descrive la musica (in inglese funziona meglio),
   es. `Calm lo-fi hip hop with warm piano, 80 BPM`.
2. Scegli la durata (10–120 secondi).
3. Premi **Genera** e scarica l'MP3.

Sulla CPU gratuita la generazione può richiedere diversi minuti; la coda e
l'avanzamento sono mostrati nella pagina.

## Deploy del tuo Space (riassunto)

Istruzioni complete in [GUIDA.md](GUIDA.md). In breve:

1. Account Hugging Face (gratuito).
2. Accetta la licenza sulla
   [pagina del modello](https://huggingface.co/stabilityai/stable-audio-3-small-music)
   (il repo è *gated*: senza questo passaggio il download fallisce).
3. Crea un [token di accesso](https://huggingface.co/settings/tokens) di tipo
   **Write**.
4. Dalla cartella del progetto:

   ```bash
   pip install huggingface_hub
   python deploy.py --space TUO_USERNAME/musik-maker --token hf_xxx
   ```

   Lo script crea lo Space, imposta il secret `HF_TOKEN` e carica i file.
   Il primo avvio scarica ~3.5 GB di pesi: attendi 10–20 minuti.

## Licenza della musica generata

Il modello è distribuito con la
[Stability AI Community License](https://stability.ai/license): **gli output
appartengono a te** e l'uso commerciale (video YouTube monetizzati, spot,
ecc.) è consentito finché il fatturato annuo resta sotto 1 M$. Il modello è
addestrato solo su dati licenziati o Creative Commons. Nota: la musica
puramente generata da AI non è coperta da copyright — non registrarla nel
Content ID e ricorda l'etichetta "contenuto generato con AI" su YouTube.

Il codice di questo progetto è rilasciato sotto licenza MIT (vedi
[LICENSE](LICENSE)).
