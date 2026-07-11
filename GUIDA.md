# Guida a Musik Maker

## Usare l'app (nessuna installazione)

L'app è online su **https://roberto-casale.github.io/musik-maker/** e funziona
da qualunque browser, a PC spento: la generazione avviene sui server GPU
gratuiti di Hugging Face (Space ufficiale Stable Audio 3 di Stability AI).

1. Scrivi la descrizione della musica (in inglese funziona meglio),
   es. `Calm lo-fi hip hop with warm piano, 80 BPM`.
2. Scegli modello e durata: **medium** fino a 6:20 (consigliato),
   **small** fino a 2:00.
3. Premi **Genera musica**: pochi secondi e la traccia è pronta.
4. Scarica in **MP3** (convertito nel browser) o WAV.

### Token (necessario) e quota giornaliera

Il motore GPU gratuito richiede un account Hugging Face: le chiamate anonime
hanno quota zero. Una volta sola: crea un account gratuito su
https://huggingface.co/join, poi un token di tipo **Read** su
https://huggingface.co/settings/tokens, e salvalo nelle **Impostazioni**
della pagina. Il token resta solo nel tuo browser (localStorage) e viene
inviato esclusivamente a Hugging Face.

La quota GPU gratuita è di alcuni minuti al giorno; ogni traccia ne consuma
pochi secondi, quindi bastano per decine di generazioni quotidiane.

**Link personale (token automatico):** puoi salvare nei preferiti un link del
tipo `https://TUO-SITO/#token=hf_xxx` — aprendolo, la pagina salva il token da
sola e lo rimuove dalla barra degli indirizzi. Il fragment (`#...`) non viene
mai inviato ad alcun server: resta nel browser. Tratta quel link come una
password (non condividerlo e non scriverlo nel repo: GitHub revoca
automaticamente i token `hf_` trovati nei repository pubblici).

### Se la generazione fallisce

- "Quota esaurita" → salva un token nelle impostazioni o riprova più tardi.
- Coda lunga → lo Space ufficiale è condiviso: nei momenti di punta si aspetta
  qualche minuto in coda.
- Se lo Space ufficiale venisse spento da Stability, l'app va ripuntata a un
  altro Space (una riga in `docs/index.html`, costante `SPACE`) o si passa al
  piano B qui sotto.

## Piano B: Space Gradio proprio (richiede HF PRO, $9/mese)

Il repo contiene anche l'app Python completa (`app.py`) per ospitare un
proprio Space con il modello `stable-audio-3-small-music`. Da luglio 2026
Hugging Face richiede l'abbonamento PRO per ospitare Space Gradio (anche su
CPU). Con PRO attivo:

1. Accetta la licenza del modello su
   https://huggingface.co/stabilityai/stable-audio-3-small-music
2. Crea un token **Write** su https://huggingface.co/settings/tokens
3. Dalla cartella del progetto:

   ```bash
   pip install huggingface_hub
   python deploy.py --space TUO_USERNAME/musik-maker --token hf_xxx
   ```

   Lo script crea lo Space, imposta il secret `HF_TOKEN` e carica i file. La
   prima build scarica ~3.5 GB di pesi (10–20 minuti). Con PRO conviene poi
   impostare hardware **ZeroGPU** nelle Settings dello Space: la generazione
   passa da minuti (CPU) a secondi.

4. (Facoltativo) Keep-alive: nel repo GitHub aggiungi il secret `HF_TOKEN` e
   la variabile `SPACE_ID` (es. `TUO_USERNAME/musik-maker`) — l'Action inclusa
   riavvia lo Space ogni giorno.

## Promemoria legale (YouTube e uso commerciale)

- La musica generata **ti appartiene** ([Stability AI Community
  License](https://stability.ai/license)): uso commerciale libero sotto 1 M$
  di fatturato annuo, anche in video monetizzati e pubblicità digitale.
- Su YouTube attiva l'etichetta **«contenuto generato con AI»** (non penalizza
  la monetizzazione).
- **Non registrare** le tracce nel Content ID e non distribuirle su
  Spotify/Apple Music come opere protette: la musica puramente AI non ha
  copyright.
- Conserva prompt e seed delle tracce che usi: sono la prova della
  generazione in caso di claim errati.
