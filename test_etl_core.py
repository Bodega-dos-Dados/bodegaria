import zipfile
import pytest
from bodegaria.etl.core import download_resource
from bodegaria.etl.core import unzip_file


@pytest.fixture
def tmp_path(tmp_path_factory: pytest.TempPathFactory):
    return tmp_path_factory.mktemp("shared_dir")


@pytest.fixture
def zip_file_path(tmp_path):
    # Given
    zip_file_path = tmp_path / "test.zip"

    # Create a sample ZIP file for testing
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        zipf.writestr("test.txt", "This is a test file.")

    return zip_file_path


def test_download_resource_downloads_zip_file_in_specified_folder(tmp_path):
    url = "https://github.com/robots.txt"
    resource_name = "robots.txt"

    download_resource(url, resource_name, tmp_path)

    assert (tmp_path / resource_name).exists()


def test_unzip_file_extracts_zip_file_into_specified_folder(zip_file_path, tmp_path):
    # Given
    output_folder = tmp_path / "extracted"
    output_folder.mkdir(exist_ok=True)

    # When
    unzip_file(zip_file_path, output_folder)

    # Then
    assert (output_folder / "test.txt").exists()


def test_unzip_file_returns_the_correct_names_of_extracted_files(
    zip_file_path, tmp_path
):
    # Given
    output_folder = tmp_path / "extracted"
    output_folder.mkdir(exist_ok=True)

    # When
    extracted_files = unzip_file(zip_file_path, output_folder)

    # Then
    assert extracted_files == ["test.txt"]
