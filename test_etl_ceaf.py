import pytest
from bodegaria.etl.ceaf import extract, transform


@pytest.fixture
def tmp_path(tmp_path_factory: pytest.TempPathFactory):
    return tmp_path_factory.mktemp("shared_dir")


def test_ceaf_extraction_downloads_data_into_specified_folder(tmp_path):
    # Given
    output_folder = tmp_path / "ceaf_data"
    output_folder.mkdir()

    # When
    resource_path = extract(output_folder)

    # Then
    assert (output_folder / "ceaf.zip").exists()
    assert (output_folder / "20260306_Expulsoes.csv").exists()


def test_ceaf_transform_unzips_resource_and_generates_csv(tmp_path): ...
