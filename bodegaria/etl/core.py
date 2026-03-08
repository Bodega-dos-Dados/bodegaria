import zipfile

import httpx
import logging
from pathlib import Path

MEGABYTE = 2 * 1024 * 1024


def build_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


LOGGER = build_logger()


def download_resource(url, resource_name, output_folder, verbose=False):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    global LOGGER

    if verbose:
        LOGGER.info(f"Baixando {resource_name} de {url} em {output_folder}...")

    with httpx.stream("GET", url, timeout=60.0) as response:
        if verbose:
            LOGGER.info(f"Status code: {response.status_code}")

        response.raise_for_status()

        total_tamanho = int(response.headers.get("content-length", 0))
        baixado = 0

        with open(Path(output_folder) / resource_name, "wb") as arquivo:
            for chunk in response.iter_bytes(chunk_size=10 * MEGABYTE):
                if chunk:
                    arquivo.write(chunk)
                    baixado += len(chunk)
                    if verbose and total_tamanho > 0:
                        porcentagem = (baixado / total_tamanho) * 100
                        LOGGER.info(f"Progresso: {porcentagem:.1f}%")


def unzip_file(zip_file_path, output_folder, verbose=False):
    global LOGGER

    try:
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(output_folder)

        if verbose:
            LOGGER.info(
                f"Arquivo '{zip_file_path}' descompactado com sucesso em '{output_folder}'!"
            )

        return zip_ref.namelist()

    except FileNotFoundError:
        LOGGER.error(f"Erro: Arquivo '{zip_file_path}' não encontrado.")
    except zipfile.BadZipFile:
        LOGGER.error(f"Erro: '{zip_file_path}' não é um arquivo ZIP válido.")
    except Exception as e:
        LOGGER.error(f"Erro ao descompactar: {e}")
