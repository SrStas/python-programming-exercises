import pandas as pd
import random

# List of sample names to choose from
first_names = [
    "John",
    "Jane",
    "Michael",
    "Sarah",
    "Robert",
    "Emily",
    "William",
    "Jessica",
    "David",
    "Laura",
    "Richard",
    "Megan",
    "Joseph",
    "Sophia",
    "Thomas",
    "Olivia",
    "Charles",
    "Emma",
    "Daniel",
    "Ava",
    "Matthew",
    "Isabella",
    "Anthony",
    "Mia",
    "Mark",
    "Amelia",
    "Steven",
    "Evelyn",
    "Paul",
    "Harper",
    "Andrew",
    "Abigail",
    "Joshua",
    "Emily",
    "George",
    "Elizabeth",
    "Kenneth",
    "Sofia",
    "Kevin",
    "Ella",
    "Brian",
    "Madison",
    "Edward",
    "Avery",
    "Ronald",
    "Lily",
    "Timothy",
    "Grace",
    "Jason",
    "Chloe",
]
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "Hernandez",
    "King",
    "Wright",
    "Lopez",
    "Hill",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Gonzalez",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
]

# generate 50 random names
names = []
for _ in range(50):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    names.append(f"{first_name} {last_name}")

# create dataFrame
df = pd.DataFrame(names, columns=["Name"])

# Save to CSV
# csv_file_path = "~/Desktop/src/random_names.csv"
csv_file_path = "GeneralTraining/random_names.csv"
df.to_csv(csv_file_path, index=False)
