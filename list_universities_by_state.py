def list_universities_by_state(data, state_name):
    for item in data:
        university = item['university']
        if university['state'].lower() == state_name.lower():
            print(f"{university['name']} in {university['city']}")
