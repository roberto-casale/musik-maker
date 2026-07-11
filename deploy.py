"""Crea (o aggiorna) lo Space su Hugging Face e carica i file del progetto.

Uso:
    python deploy.py --space TUO_USERNAME/musik-maker --token hf_xxx

Il token deve essere di tipo Write e appartenere a un account che ha
accettato la licenza del modello su
https://huggingface.co/stabilityai/stable-audio-3-small-music
"""

import argparse
import os
import sys

from huggingface_hub import HfApi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--space",
        required=True,
        help="ID dello Space, es. tuo-username/musik-maker",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("HF_TOKEN"),
        help="Token Hugging Face (Write); in alternativa esporta HF_TOKEN",
    )
    args = parser.parse_args()

    if not args.token:
        sys.exit("Errore: passa --token oppure esporta la variabile HF_TOKEN.")

    api = HfApi(token=args.token)

    print(f"Creazione dello Space {args.space} (se non esiste)...")
    api.create_repo(
        repo_id=args.space,
        repo_type="space",
        space_sdk="gradio",
        exist_ok=True,
    )

    print("Impostazione del secret HF_TOKEN dello Space (per il modello gated)...")
    api.add_space_secret(repo_id=args.space, key="HF_TOKEN", value=args.token)

    print("Caricamento dei file del progetto...")
    api.upload_folder(
        folder_path=os.path.dirname(os.path.abspath(__file__)),
        repo_id=args.space,
        repo_type="space",
        ignore_patterns=[".git*", ".claude*", "deploy.py", "__pycache__*"],
    )

    print(
        f"\nFatto! Lo Space sta partendo: https://huggingface.co/spaces/{args.space}\n"
        "Il primo avvio scarica ~3.5 GB di pesi: attendi 10-20 minuti.\n"
        "Se la build fallisce, controlla i log nella scheda 'Logs' dello Space."
    )


if __name__ == "__main__":
    main()
