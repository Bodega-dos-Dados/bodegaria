import httpx
import logging
from pathlib import Path


def download_resource(url, resource_name, output_folder, verbose=False):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    if verbose:
        logging.info(f"Baixando {resource_name} de {url} em {output_folder}...")

    with httpx.stream("GET", url, timeout=60.0) as response:
        logging.info(f"Status code: {response.status_code}")
        response.raise_for_status()

        total_tamanho = int(response.headers.get("content-length", 0))
        baixado = 0

        with open(Path(output_folder) / resource_name, "wb") as arquivo:
            for chunk in response.iter_bytes(chunk_size=8192):
                if chunk:
                    arquivo.write(chunk)
                    baixado += len(chunk)
                    if verbose and total_tamanho > 0:
                        porcentagem = (baixado / total_tamanho) * 100
                        logging.info(
                            f"\rProgresso: {porcentagem:.1f}%", end="", flush=True
                        )
