import json
from collections import Counter

def remove_specific_keywords(data, keywords_to_remove):
    """Remove specific keywords from all games regardless of frequency."""
    removed_count = 0
    for game in data.values():
        if 'keywords' in game and isinstance(game['keywords'], list):
            original_length = len(game['keywords'])
            game['keywords'] = [kw for kw in game['keywords'] if kw not in keywords_to_remove]
            removed_count += original_length - len(game['keywords'])
    
    print(f"\nRemoved {removed_count} instances of specified keywords")

def process_game_details():
    # Read the JSON file
    with open('game_details.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # List of keywords to remove
    keywords_to_remove = [
        "vore",
        "male protagonist",
        "protagonist's name in the title",
        "boss fight",
        "treasure chest",
        "trilogy",
        "greatest hits",
        "collectibles",
        "prequel",
        "single-player only",
        "platform exclusive",
        "new game plus",
        "the game awards - nominee",
        "the game awards 2016",
        "split-screen multiplayer",
        "licensed game",
        "steam trading cards",
        "steam achievements",
        "original soundtrack release",
        "optional boss",
        "crowdfunding - kickstarter",
        "nintendo switch online",
        "wii u virtual console",
        "nintendo 3ds virtual console",
        "fan translation - spanish",
        "fan translation - italian",
        "fan translation - korean",
        "fan translation - french",
        "fan translation - tagalog",
        "fan translation - galician",
        "fan translation - romanian",
        "fan translation - greek",
        "fan translation - ancient greek",
        "fan translation - indonesian",
        "fan translation - arabic",
        "fan translation - irish",
        "fan translation - dutch",
        "fan translation - norwegian",
        "fan translation - german",
        "fan translation - swedish",
        "fan translation - english",
        "fan translation - polish",
        "virtual console",
        "female antagonist",
        "nintendo gateway system",
        "e3 2005",
        "e3 2017",
        "pax west 2017",
        "mod support",
        "nintendo switch online - expansion pack",
        "wii virtual console",
        "player's choice",
        "4 player co-op",
        "unlockable difficulty level",
        "interquel",
        "nintendo 64 exclusive",
        "60 fps on consoles",
        "cheat code",
        "downloadable content",
        "fictional currencies",
        "high score",
        "multi-phase boss",
        "non-player character",
        "online",
        "open-source",
        "steam cloud",
        "super game boy enhancement",
        "transforming boss",
        "unlockables",
        "unofficial",
        "young protagonist",
        "e3 1997",
        "e3 2001",
        "steam",
        "e3 2000",
        "e3 2002",
        "e3 2003",
        "e3 2004",
        "e3 2006",
        "e3 2008",
        "in-game anti-piracy effects",
        "leaderboard",
        "level selection",
        "played for charity",
        "playstation trophies",
        "post-credits plot twist",
        "pre-release public testing",
        "promo vhs",
        "xbox controller support for pc",
        
    ]
    
    # Print initial keyword statistics
    total_keywords = 0
    keyword_counts = Counter()
    for game in data.values():
        if 'keywords' in game and isinstance(game['keywords'], list):
            total_keywords += len(game['keywords'])
            keyword_counts.update(game['keywords'])
    
    print(f"\nInitial statistics:")
    print(f"Total unique keywords: {len(keyword_counts)}")
    print(f"Total keyword occurrences: {total_keywords}")
    
    # Remove specified keywords
    remove_specific_keywords(data, keywords_to_remove)
    
    # Print final keyword statistics and list all remaining keywords with counts
    total_keywords = 0
    keyword_counts = Counter()
    for game in data.values():
        if 'keywords' in game and isinstance(game['keywords'], list):
            total_keywords += len(game['keywords'])
            keyword_counts.update(game['keywords'])
    
    print(f"\nFinal statistics:")
    print(f"Total unique keywords: {len(keyword_counts)}")
    print(f"Total keyword occurrences: {total_keywords}")
    
    print("\nRemaining unique keywords (alphabetically sorted with counts):")
    for keyword in sorted(keyword_counts.keys()):
        print(f"  '{keyword}': {keyword_counts[keyword]}")

    # Save unique keywords and their counts to a JSON file
    keywords_with_counts = {kw: count for kw, count in sorted(keyword_counts.items())}
    with open('unique_keywords.json', 'w', encoding='utf-8') as file:
        json.dump(keywords_with_counts, file, indent=4)
    print("\nSaved unique keywords and their counts to 'unique_keywords.json'")

    # Write the updated data back to the file
    with open('game_details.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    process_game_details() 