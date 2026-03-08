from bodegaria.etl.core import download_resource


def ceaf(output_folder, custom_date=""):
    BASE_URL = (
        "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/ceaf"
    )
    DOWNLOAD_URL = f"{BASE_URL}/20260306_CEAF.zip"

    if custom_date:
        DOWNLOAD_URL = f"{BASE_URL}/{custom_date}_CEAF.zip"

    download_resource(DOWNLOAD_URL, "ceaf.zip", output_folder)
