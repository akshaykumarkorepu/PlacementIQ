from placementiq.database.repository import InterviewRepository


repo = InterviewRepository()

total = repo.count()

print("PlacementIQ Repository Test")
print("---------------------------")
print(f"Total Interviews : {total}")
