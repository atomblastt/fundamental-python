bio = {
    "name":"Thomas",
    "age":27,
    "gender":"Laki Laki"
}

bio["addition"] = "test"

del bio["addition"]

for key, value in bio.items():
    print(f"{key}:{value}")

print(f"nama saya {bio["name"]}, saya berumur {bio["age"]}, saya berjenis kelamin {bio["gender"]}")