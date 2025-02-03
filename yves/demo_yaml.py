import yaml


with open ("test.yaml", "r") as yaml_file:
    content = yaml.safe_load(yaml_file)

print(content)

for c in content["cities_lived"]:
    print(c)