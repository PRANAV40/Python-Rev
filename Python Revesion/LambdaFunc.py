users = [
        {"Name":"Amit","Age":24},
        {"Name":"Harsh","Age":25},
        {"Name":"Aniket","Age":23},
]
sorted_user = sorted(users,key=lambda e: e["Age"])
print(sorted_user)

logs = [
    {"level":"info","msg":"started"},
    {"level":"error","msg":"failed"},
    {"level":"warning","msg":"slow"},
]
errors = list(filter(lambda l:l["level"] == "error",logs))
print(errors)