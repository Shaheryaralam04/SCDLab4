while True:
    data = input("Enter data (or 'q' to quit): ")
    if data.lower() == 'q':
        break
    user_data.append(data)

print("User Data:")
for i, data in enumerate(user_data, 1):
    print(f"{i}. {data}")