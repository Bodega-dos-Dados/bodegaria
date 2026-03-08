import pytest
from bodegaria.etl.core import download_resource
from bodegaria.etl.extract import ceaf


@pytest.fixture
def tmp_path(tmp_path_factory: pytest.TempPathFactory):
    return tmp_path_factory.mktemp("shared_dir")


def test_download_resource_downloads_zip_file_in_specified_folder(tmp_path):
    url = "https://github.com/robots.txt"
    resource_name = "robots.txt"

    download_resource(url, resource_name, tmp_path)

    assert (tmp_path / resource_name).exists()


def test_ceaf_extraction_downloads_data_into_specified_folder(tmp_path):
    # Given
    output_folder = tmp_path / "ceaf_data"
    output_folder.mkdir()

    # When
    ceaf(output_folder)

    # Then
    assert (output_folder / "ceaf.zip").exists()
