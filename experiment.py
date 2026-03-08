from bodegaria.etl.ceaf import extract, transform

OUTPUT_FOLDER = 'data/extract'

if __name__ == "__main__":
    resource_path = extract(OUTPUT_FOLDER)
    # transformed_resource = transform(resource_path)
    
    print(f"Recurso extraído: {resource_path}")
    # print(f"Recurso transformado: {transformed_resource}")