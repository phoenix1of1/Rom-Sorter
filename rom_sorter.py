import os
import re

# Define the folder path and keywords
folder_path = 'path/to/your/folder'

keywords = ['Asia', 'Pirate', 'Japan', 'Brazil', 
            'Spain', 'Korea', 'Russia', 'Unl', 'Evercade', 'Beta', 
            'Virtual Console', 'Arcade', 'World', 'Sample', 'Proto', 'Beta',
            'Rev', 'Germany', 'Italy', 'France', 'Netherlands', 'Demo', 'Tech Demo', 
            'Switch online', 'Switch Online', 'Sega Channel', 'Genisis Mini']

# List all items in the folder
items = os.listdir(folder_path)

# Counter for removed items
removed_count = 0

# Dictionary to track game titles and their corresponding countries
game_dict = {}

# Regular expression to extract the country from the title
country_pattern = re.compile(r'\((.*?)\)')

# Iterate through the list of items
for item in items:
    item_path = os.path.join(folder_path, item)
    # Check if any keyword is in the item's name
    if any(keyword in item for keyword in keywords):
        # Remove the item
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f'Removed file: {item_path}')
            removed_count += 1
        elif os.path.isdir(item_path):
            os.rmdir(item_path)
            print(f'Removed directory: {item_path}')
            removed_count += 1
    else:
        # Extract the game title and country
        match = country_pattern.search(item)
        if match:
            country = match.group(1)
            title = country_pattern.sub('', item).strip()
            if title not in game_dict:
                game_dict[title] = item_path
            else:
                # Favor (Europe) over (USA)
                if 'Europe' in item:
                    os.remove(game_dict[title])
                    game_dict[title] = item_path
                    print(f'Removed duplicate (USA): {game_dict[title]}')
                    removed_count += 1
                elif 'USA' in item:
                    os.remove(item_path)
                    print(f'Removed duplicate (USA): {item_path}')
                    removed_count += 1

# Output the number of removed items
print(f'Total items removed: {removed_count}')

# Keep the terminal open
input("Press Enter to exit...")