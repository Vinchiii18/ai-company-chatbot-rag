def greet(name: str) -> str:
    return f"Hello, {name}!"


user = {
    "name": "Alvin",
    "role": "AI Engineer"
}

skills = [
    "Python",
    "FastAPI",
    "Azure AI"
]

print(greet(user["name"]))

for skill in skills:
    print(skill)