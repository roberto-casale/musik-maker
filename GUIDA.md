# Guida passo-passo: mettere online Musik Maker

Tempo stimato: 15 minuti di lavoro tuo + 10–20 minuti di attesa per la build.
Costo: **zero**.

## 1. Crea l'account Hugging Face

Vai su https://huggingface.co/join e registrati (gratuito). Hugging Face è la
piattaforma che ospiterà l'app: gira sui loro server, quindi funziona anche a
PC spento.

## 2. Accetta la licenza del modello

Vai su https://huggingface.co/stabilityai/stable-audio-3-small-music da
loggato. Vedrai un modulo ("gated model"): compila nome, email, paese e uso
previsto, e accetta la **Stability AI Community License** (più i termini Gemma
per il componente di testo). L'approvazione è automatica.

Questo passaggio è ciò che ti dà il diritto di **usare commercialmente la
musica generata** (valido finché il tuo fatturato annuo resta sotto 1 M$).
Senza questo passaggio, lo Space non riuscirà a scaricare il modello.

## 3. Crea un token di accesso

Vai su https://huggingface.co/settings/tokens → "Create new token" → tipo
**Write** → dagli un nome (es. `musik-maker`) e copialo. Trattalo come una
password: non incollarlo in file che finiscono su GitHub.

## 4. Lancia il deploy

Dal terminale, nella cartella del progetto:

```bash
pip install huggingface_hub
python deploy.py --space TUO_USERNAME/musik-maker --token hf_xxx
```

(sostituisci `TUO_USERNAME` con il tuo username Hugging Face e `hf_xxx` con il
token). Lo script:

- crea lo Space `TUO_USERNAME/musik-maker` (SDK Gradio, hardware CPU gratuito);
- imposta il token come secret `HF_TOKEN` dello Space (serve per scaricare il
  modello gated);
- carica tutti i file del progetto.

## 5. Attendi la prima build

Apri `https://huggingface.co/spaces/TUO_USERNAME/musik-maker`. La prima build
installa le dipendenze e scarica ~3.5 GB di pesi del modello: **10–20 minuti**.
Puoi seguire i log nella scheda **Logs**. Quando lo stato diventa "Running",
l'app è online e pubblica.

## 6. Prova e misura i tempi

Genera una prima traccia corta (20–30 secondi) e cronometra. Su CPU gratuita
(2 vCPU) i tempi non sono documentati da nessuno: potrebbero essere minuti per
traccia. Se per te è troppo lento, le alternative (a pagamento) sono:

- **ZeroGPU**: abbonamento Hugging Face PRO ($9/mese), poi nello Space imposti
  hardware ZeroGPU — genera in secondi;
- hardware CPU/GPU dedicato a ore, sempre da Hugging Face.

## 7. (Facoltativo) Tieni sveglio lo Space

Lo Space gratuito si addormenta dopo 48 ore senza visite e si risveglia da
solo alla prima visita (con qualche minuto di attesa e nuovo download del
modello). Se vuoi evitarlo, nel repo **GitHub** vai su Settings →

- **Secrets and variables → Actions → New repository secret**: nome
  `HF_TOKEN`, valore il tuo token;
- **Variables → New repository variable**: nome `SPACE_ID`, valore
  `TUO_USERNAME/musik-maker`.

La GitHub Action inclusa (`.github/workflows/keep-alive.yml`) riavvierà lo
Space una volta al giorno.

## 8. Aggiornamenti futuri

Per modificare l'app: cambia i file, poi rilancia `python deploy.py ...` (o
committa direttamente sul repo dello Space). Il repo GitHub e lo Space sono
due copie separate: GitHub è la vetrina del codice, lo Space è ciò che gira.

## Promemoria legale (per YouTube e uso commerciale)

- La musica generata **ti appartiene** (Stability AI Community License) e puoi
  usarla in video monetizzati e pubblicità finché fatturi meno di 1 M$/anno.
- Su YouTube attiva l'etichetta **"contenuto generato con AI"** (non penalizza
  la monetizzazione).
- **Non registrare** le tracce nel Content ID e non distribuirle su
  Spotify/Apple Music come se fossero opere protette: la musica puramente AI
  non ha copyright.
- Conserva i prompt e i parametri (seed) delle tracce che usi: sono la prova
  della generazione in caso di claim errati.
