
# uers = {"name":"Alok","email":"alok@gmail.com","age":24}
# required = ["name","enail","age"]

# if all("filed in user for field in required"):
#     print("Valid User✔")
# else:
#     print("Missing value *")


cpu,mem,disk = 92,65,88

if any(x > 90 for x in [cpu,mem,disk]):
    print("ALERT: Resource usege high🚨")