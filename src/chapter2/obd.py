obd = {
    "P0001": {
        "description": "jkdjlfkm jdsf jkmldjfklds",
        "causes": [
            "abc",
            "def"
        ],
        "symptoms": [
            "sdqjklm",
            "jkml",
            "kjmklm"
        ]
    }
}

problem = "P0001"

print (f"There are {len (obd[problem]["causes"])} causes for {problem}.")

for c in obd[problem]["causes"]:
    print (c)
