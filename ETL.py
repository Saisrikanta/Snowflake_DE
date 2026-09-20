def clean_data(records):
    #Remove where id is none and make name to lowercase and strip spaces
    cleaned=[]
    for r in records:
        if r.get("id") is None:
            continue
        r["name"]=r["name"].strip().lower()
        cleaned.append(r)
    return cleaned
sample=[{"id":1,"name":"Sai"},
        {"id":None,"name":"bachi"},
        {"id":2,"name":"Sri"}]
print(clean_data(sample))

'''
def clean_data(records):
    cleaned=[]
    for r in records:
        if r.get("id") is None:
            continue
        
        # Create a NEW dict, don't change old one
        new_r = {
            "id": r.get("id"),
            "name": r.get("name", "").strip().lower() if r.get("name") else "unknown"
        }
        cleaned.append(new_r)
    return cleaned
'''