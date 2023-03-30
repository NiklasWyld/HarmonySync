import json

app_path = str(__file__).split(r"\builder.py")[0]

json_structure = {
    "app_path": str(app_path),
    "app_version": "",
    "profiles": [],
    "settings": {}
}
save_file = open(f"{app_path}\save_data.json", "w")


save_file.write(json.dumps(json_structure, indent=3))
save_file.close()

