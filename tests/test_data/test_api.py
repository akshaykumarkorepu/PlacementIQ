from placementiq.api import InternitoAPI

client = InternitoAPI()

raw = client.fetch_interviews()

text = raw[0]["OT_description"]

print("NORMAL PRINT:")
print(text)

print("\n" + "=" * 60)

print("REPR:")
print(repr(text))
