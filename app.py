"""Musik Maker — genera musica strumentale da un prompt testuale.

Gira su uno Space Hugging Face gratuito (cpu-basic) con il modello
stabilityai/stable-audio-3-small-music. Il repo del modello è "gated":
lo Space deve avere un secret HF_TOKEN di un account che ha accettato
la licenza sulla pagina del modello.
"""

import os

# 2 vCPU sullo Space gratuito: evita l'oversubscription dei thread BLAS.
os.environ.setdefault("OMP_NUM_THREADS", "2")

import torch  # noqa: E402
import gradio as gr  # noqa: E402
from stable_audio_3 import StableAudioModel  # noqa: E402

if not os.getenv("HF_TOKEN"):
    print(
        "ATTENZIONE: HF_TOKEN non impostato. Il download del modello fallira'\n"
        "perche' il repo e' gated. Aggiungi il secret HF_TOKEN nelle impostazioni"
        " dello Space."
    )

print("Caricamento di stable-audio-3-small-music (al primo avvio scarica ~3.5 GB)...")
# Su CPU la libreria forza automaticamente fp32 (fp16 su CPU si blocca).
model = StableAudioModel.from_pretrained("small-music")

SAMPLE_RATE = int(model.model.sample_rate)  # 44100
MAX_SECONDS = int(model.model_config["sample_size"]) // SAMPLE_RATE  # 120
STEPS = 8  # default ufficiale per i modelli post-trained della famiglia SA3

print(f"Modello pronto: {SAMPLE_RATE} Hz, durata massima {MAX_SECONDS}s.")


def genera(prompt, durata, seed, progress=gr.Progress(track_tqdm=True)):
    if not prompt or not prompt.strip():
        raise gr.Error("Scrivi un prompt che descriva la musica da generare.")

    durata = float(max(5, min(int(durata), MAX_SECONDS)))
    try:
        seed = int(seed)
    except (TypeError, ValueError):
        seed = -1

    try:
        audio = model.generate(
            prompt=prompt.strip(),
            duration=durata,
            steps=STEPS,
            seed=seed,
            sample_size=int(model.model_config["sample_size"]),
        )
    except Exception as exc:  # noqa: BLE001
        raise gr.Error(f"Generazione fallita: {exc}") from exc

    # (batch, canali, campioni) float32 in [-1, 1], gia' troncato a `durata`.
    track = audio[0]
    peak = track.abs().max().clamp(min=1e-9)
    track = (track / peak).clamp(-1, 1).mul(32767).to(torch.int16).cpu().numpy()

    # gr.Audio (numpy) vuole (campioni, canali); format="mp3" fa la conversione.
    return (SAMPLE_RATE, track.T)


DESCRIZIONE = f"""
Scrivi una descrizione della musica (in **inglese** funziona meglio), scegli la
durata e premi **Genera**: ottieni una traccia **strumentale** stereo a 44.1 kHz
scaricabile in MP3.

- Durata massima: **{MAX_SECONDS} secondi**; sotto i 20 secondi la qualita' cala.
- Questo Space gira su CPU gratuita: la generazione puo' richiedere **diversi
  minuti**. La pagina mostra la coda e l'avanzamento.
- La musica generata **ti appartiene** (Stability AI Community License): uso
  commerciale consentito sotto 1 M$ di fatturato annuo. Niente copyright sugli
  output puramente AI: non registrarli nel Content ID.
"""

ESEMPI = [
    ["Calm lo-fi hip hop with warm piano and vinyl crackle, 80 BPM", 60],
    ["Uplifting corporate background music, acoustic guitar and light percussion", 45],
    ["Epic cinematic orchestral trailer with big drums and strings, 110 BPM", 90],
    ["Ambient electronic soundscape, soft pads, no drums, dreamy", 120],
]

with gr.Blocks(title="Musik Maker") as demo:
    gr.Markdown("# 🎵 Musik Maker")
    gr.Markdown(DESCRIZIONE)

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Prompt",
                placeholder="Es.: Calm lo-fi hip hop with warm piano, 80 BPM",
                lines=3,
            )
            durata = gr.Slider(
                minimum=10,
                maximum=MAX_SECONDS,
                value=60,
                step=5,
                label="Durata (secondi)",
                info="Consigliati almeno 20 secondi",
            )
            with gr.Accordion("Opzioni avanzate", open=False):
                seed = gr.Number(
                    value=-1,
                    precision=0,
                    label="Seed",
                    info="-1 = casuale; un valore fisso rende il risultato riproducibile",
                )
            btn = gr.Button("Genera", variant="primary")
        with gr.Column():
            uscita = gr.Audio(
                label="Traccia generata (scaricabile in MP3)",
                type="numpy",
                format="mp3",
            )

    gr.Examples(examples=ESEMPI, inputs=[prompt, durata])

    btn.click(genera, inputs=[prompt, durata, seed], outputs=uscita)

    gr.Markdown(
        "Modello: [stabilityai/stable-audio-3-small-music]"
        "(https://huggingface.co/stabilityai/stable-audio-3-small-music) — "
        "[Stability AI Community License](https://stability.ai/license)"
    )

demo.queue(max_size=10)

if __name__ == "__main__":
    demo.launch()
