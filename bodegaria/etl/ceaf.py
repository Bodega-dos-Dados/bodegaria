from pathlib import Path
from datetime import datetime
from bodegaria.etl.core import download_resource, unzip_file


def extract(output_folder, custom_date=""):
    TODAY = datetime.now().strftime("%Y%m%d")

    BASE_URL = (
        "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/ceaf"
    )
    DOWNLOAD_URL = f"{BASE_URL}/{TODAY}_CEAF.zip"

    if custom_date:
        DOWNLOAD_URL = f"{BASE_URL}/{custom_date}_CEAF.zip"

    resource_path = Path(output_folder) / "ceaf.zip"

    if not resource_path.exists():
        download_resource(DOWNLOAD_URL, "ceaf.zip", output_folder, verbose=True)

    unzipped_files = [f"{TODAY}_Expulsoes.csv"]

    if not (Path(output_folder) / f"{TODAY}_Expulsoes.csv").exists():
        unzipped_files = unzip_file(str(resource_path), output_folder, verbose=True)

    return unzipped_files


def transform(): ...


def load(): ...
