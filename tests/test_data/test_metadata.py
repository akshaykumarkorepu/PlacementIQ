from placementiq.pipeline.metadata import MetadataGenerator


generator = MetadataGenerator()

metadata = generator.generate()

print()
print("PlacementIQ Metadata")
print("--------------------")

for key, value in metadata.items():
    print(f"{key}: {value}")
