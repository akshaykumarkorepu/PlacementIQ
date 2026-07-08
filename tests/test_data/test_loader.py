from placementiq.database.loader import SQLiteLoader

loader = SQLiteLoader()

interviews = loader.load()

print()
print("First Interview")
print("----------------")
print(interviews[0]["company"])
