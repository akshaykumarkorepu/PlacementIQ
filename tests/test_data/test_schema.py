from placementiq.database.schema import DatabaseSchema


schema = DatabaseSchema()

schema.create_database()

print("Database created successfully!")

print("Schema verified!")
