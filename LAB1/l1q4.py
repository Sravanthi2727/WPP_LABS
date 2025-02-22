d = {
    "name" : "Sravanthi",
    "class" : "B tech 1st yeear",
    "branch" : "CSE",
    "college" : "at NIT - SURAT",
}

print("Dictionary Items :", d)
print("Student Name :", d["name"])
print("Student branch :", d.get("branch"))
d["college"] = "NIT,Surat"
print("College Name :", d["college"])
print("Length of dictionary is :", len(d))