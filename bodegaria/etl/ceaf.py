from pathlib import Path
from bodegaria.etl.core import download_resource, unzip_file


def extract(output_folder, custom_date=""):
    BASE_URL = (
        "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/ceaf"
    )
    DOWNLOAD_URL = f"{BASE_URL}/20260306_CEAF.zip"

    if custom_date:
        DOWNLOAD_URL = f"{BASE_URL}/{custom_date}_CEAF.zip"

    resource_path = Path(output_folder) / "ceaf.zip"

    if not resource_path.exists():
        download_resource(DOWNLOAD_URL, "ceaf.zip", output_folder, verbose=True)

    unzipped_files = ["20260306_Expulsoes.csv"]

    if not (Path(output_folder) / "20260306_Expulsoes.csv").exists():
        unzipped_files = unzip_file(str(resource_path), output_folder, verbose=True)

    return unzipped_files


def transform(): ...


def load(): ...
