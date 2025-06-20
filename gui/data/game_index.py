from typing import Dict, Set, Any

class GameIndex:
    """
    Pre-generated search index for games. This index is built during the build process
    and included in the final executable.
    """
    def __init__(self):
        # The search index is pre-populated during build
        self.games: Dict[str, dict] = GAMES_DATA  # Generated during build
        self.search_index: Dict[str, Set[str]] = SEARCH_INDEX  # Generated during build
    
    def search(self, query: str) -> dict:
        """
        Search for games matching the query.
        
        Args:
            query: The search query string
            
        Returns:
            Dictionary of matching games
        """
        if not query:
            return {}
            
        query_terms = query.lower().split()
        matching_games = set()
        
        # First try exact matches from the search index
        for term in query_terms:
            if term in self.search_index:
                if not matching_games:
                    matching_games = set(self.search_index[term])
                else:
                    matching_games &= set(self.search_index[term])
        
        # If no exact matches found, try partial matches
        if not matching_games:
            for game_name, game_data in self.games.items():
                # First check if any query term is in the game title
                if any(term in game_name.lower() for term in query_terms):
                    matching_games.add(game_name)
                    continue
                
                # Then check other searchable fields
                searchable_fields = {
                    'genres': game_data.get('genres', []),
                    'themes': game_data.get('themes', []),
                    'keywords': game_data.get('keywords', []),
                    'player_perspectives': game_data.get('player_perspectives', []),
                    'rating': [game_data.get('rating', '')],
                    'release_date': [str(game_data.get('release_date', ''))]
                }
                
                # Check if any query term is contained in any searchable field
                for field_values in searchable_fields.values():
                    if isinstance(field_values, list):
                        for value in field_values:
                            if isinstance(value, str) and any(term in value.lower() for term in query_terms):
                                matching_games.add(game_name)
                                break
                    elif isinstance(field_values, str) and any(term in field_values.lower() for term in query_terms):
                        matching_games.add(game_name)
                        break
                    
                    if game_name in matching_games:
                        break
        
        # Return only matching games
        return {name: self.games[name] for name in matching_games}
    
    def get_game(self, game_name: str) -> dict:
        """
        Get full game data for a specific game.
        
        Args:
            game_name: The name of the game to retrieve
            
        Returns:
            Dictionary containing all game data
        """
        return self.games.get(game_name, {})
    
    def get_all_games(self) -> dict:
        """
        Get all game data.
        
        Returns:
            Dictionary containing all games and their data
        """
        return self.games.copy()

# These constants will be generated during build
GAMES_DATA = {
    "Adventure": {
        "igdb_id": "12239",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/qzcqrjruhpuge5egkzgj.jpg",
        "world_name": "Adventure",
        "igdb_name": "adventure",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "adventure"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "bbc microcomputer system",
            "acorn electron"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "1983"
    },
    "Against the Storm": {
        "igdb_id": "147519",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7j13.jpg",
        "world_name": "Against the Storm",
        "igdb_name": "against the storm",
        "rating": [
            "mild blood",
            "alcohol reference",
            "use of tobacco",
            "language",
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "real time strategy (rts)",
            "simulator",
            "strategy",
            "indie"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5",
            "nintendo switch"
        ],
        "storyline": "the rain is your ally and the greatest enemy. it cycles in three seasons requiring you to stay flexible and adapt to changing conditions. in drizzle, the season of regrowth, natural resources replenish themselves, and it\u2019s time for construction and planting crops. the clearance is the season of harvest, expansion, and preparations for the last, most unforgiving season of them all. a true test of your city\u2019s strength comes with the storm when bolts of lightning tear the sky, nothing grows and resources are scarce.",
        "keywords": [
            "roguelite"
        ],
        "release_date": "2023"
    },
    "A Hat in Time": {
        "igdb_id": "6705",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pl5.jpg",
        "world_name": "A Hat in Time",
        "igdb_name": "a hat in time",
        "rating": [
            "blood",
            "fantasy violence"
        ],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "time travel",
            "spaceship",
            "female protagonist",
            "action-adventure",
            "cute",
            "snow",
            "wall jump",
            "3d platformer",
            "swimming",
            "steam greenlight",
            "crowdfunding",
            "crowd funded",
            "collection marathon"
        ],
        "release_date": "2017"
    },
    "A Link Between Worlds": {
        "igdb_id": "2909",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3p0j.jpg",
        "world_name": "A Link Between Worlds",
        "igdb_name": "the legend of zelda: a link between worlds",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "historical",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "nintendo 3ds"
        ],
        "storyline": "after capturing princess zelda and escaping through a rift into the parallel world of lorule, the evil sorcerer yuga plan to use the power of the seven mages to resurrect the demon king ganon. the young adventurer link is called out to restore peace to the kingdom of hyrule and is granted the ability to merge into walls after obtaining a magic bracelet from the eccentric merchant ravio, which allows him to reach previously inaccessible areas and travel between the worlds of hyrule and lorule.",
        "keywords": [
            "medieval",
            "magic",
            "minigames",
            "2.5d",
            "archery",
            "action-adventure",
            "fairy",
            "bird",
            "princess",
            "snow",
            "sequel",
            "swimming",
            "sword & sorcery",
            "darkness",
            "digital distribution",
            "anthropomorphism",
            "polygonal 3d",
            "bow and arrow",
            "damsel in distress",
            "upgradeable weapons",
            "disorientation zone",
            "descendants of other characters",
            "save point",
            "stereoscopic 3d",
            "side quests",
            "potion",
            "real-time combat",
            "self-referential humor",
            "multiple gameplay perspectives",
            "rpg elements",
            "mercenary",
            "coming of age",
            "dimension travel",
            "androgyny",
            "fast traveling",
            "context sensitive",
            "living inventory",
            "bees"
        ],
        "release_date": "2013"
    },
    "A Link to the Past": {
        "igdb_id": "1026",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3vzn.jpg",
        "world_name": "A Link to the Past",
        "igdb_name": "the legend of zelda: a link to the past",
        "rating": [
            "mild violence",
            "mild animated violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "satellaview",
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "the wizard agahnim has been abducting descendants of the seven sages, intent on using their power to obliterate the barrier leading to the dark world. one of the descendants happens to be princess zelda, who informs link of her plight. armed with a trusty sword and shield, link begins a journey that will take him through treacherous territory.",
        "keywords": [
            "ghosts",
            "magic",
            "mascot",
            "death",
            "maze",
            "archery",
            "action-adventure",
            "fairy",
            "backtracking",
            "undead",
            "campaign",
            "princess",
            "pixel art",
            "easter egg",
            "teleportation",
            "sequel",
            "giant insects",
            "silent protagonist",
            "swimming",
            "sword & sorcery",
            "darkness",
            "explosion",
            "block puzzle",
            "monkey",
            "nintendo power",
            "world map",
            "human",
            "shopping",
            "bow and arrow",
            "damsel in distress",
            "disorientation zone",
            "ice stage",
            "saving the world",
            "side quests",
            "potion",
            "real-time combat",
            "secret area",
            "shielded enemies",
            "walking through walls",
            "liberation",
            "mercenary",
            "coming of age",
            "conveyor belt",
            "villain",
            "recurring boss",
            "been here before",
            "sleeping",
            "merchants",
            "dimension travel",
            "fetch quests",
            "kidnapping",
            "poisoning",
            "time paradox",
            "fast traveling",
            "context sensitive",
            "living inventory",
            "status effects",
            "hidden room",
            "another world",
            "damage over time",
            "monomyth",
            "buddy system",
            "retroachievements",
            "bees",
            "popular"
        ],
        "release_date": "1991"
    },
    "ANIMAL WELL": {
        "igdb_id": "191435",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4hdh.jpg",
        "world_name": "ANIMAL WELL",
        "igdb_name": "animal well",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "horror",
            "survival",
            "mystery"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5",
            "nintendo switch"
        ],
        "storyline": "it is dark. it is lonely. you don't belong in this world. it's not that it\u2019s a hostile world... it's just... not yours. as you uncover its secrets, the world grows on you. it takes on a feel of familiarity, yet you know that you've only probed the surface. the more you discover, the more you realize how much more there is to discover. secrets leading to more secrets. you recall the feeling of zooming closer and closer in on a very high-resolution photo. as you hone your focus, the world betrays its secrets.",
        "keywords": [
            "exploration",
            "retro",
            "2d",
            "metroidvania",
            "cute",
            "atmospheric",
            "pixel art",
            "pixel graphics",
            "relaxing"
        ],
        "release_date": "2024"
    },
    "Ape Escape": {
        "igdb_id": "3762",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2gzc.jpg",
        "world_name": "Ape Escape",
        "igdb_name": "ape escape",
        "rating": [
            "mild animated violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "playstation 3",
            "playstation",
            "playstation portable"
        ],
        "storyline": "the doctors trustfull test apes have escaped and it's up to you to get out there and retrieve all of them.",
        "keywords": [
            "anime",
            "dinosaurs",
            "time travel",
            "collecting",
            "minigames",
            "multiple endings",
            "amnesia",
            "easter egg",
            "digital distribution",
            "anthropomorphism",
            "monkey",
            "voice acting",
            "human",
            "polygonal 3d",
            "psone classics",
            "moving platforms",
            "spiky-haired protagonist",
            "time trials"
        ],
        "release_date": "1999"
    },
    "Sudoku": {
        "igdb_id": "",
        "world_name": "Sudoku",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer",
            "puzzle"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "hints",
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Aquaria": {
        "igdb_id": "7406",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1r7r.jpg",
        "world_name": "Aquaria",
        "igdb_name": "aquaria",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "fantasy",
            "drama"
        ],
        "platforms": [
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "the world of aquaria hides the secrets of creation within its depths. the currents that buffet the many diverse plants and animals that live there also carry with them stories of long lost civilizations; of love and war, change and loss.\n\nfrom lush, green kelp forests to dark caves, exploring will be no easy task. but the splendor of the undersea world awaits naija... and you.\n\nopen waters\ncrystalline blue\n\nthe glassy waters of the open sea let you peer far into the distance, and fish and other creatures play beneath the wide canopies of giant, undersea mushrooms.\n\nhere, ruins serve as a clue to aquaria's long past. will they lead naija to the truth?\n\nthe kelp forest\nthe natural world\n\nthe kelp forest teems with life. as light from above pours across the multitudes of strange plants and animals that live here, one cannot help but marvel at the dynamic landscape.\n\nbut beware, its beauty belies the inherent danger inside. careful not to lose your way.\n\nthe abyss\ndarkness\n\nas you swim deeper, to where sight cannot reach, the abyss begins to swallow you whole. the deeper waters of aquaria have spawned legends of frightening monstrosities that lurk where few things can survive. are they true?\n\nbeyond\n???\n\nwhat lies beyond? are there areas deeper than the abyss? or as we swim ever upward, can we find the source of the light?\n\nonly those with great fortitude will come to know and understand the mysteries of aquaria.",
        "keywords": [
            "exploration",
            "magic",
            "metroidvania",
            "action-adventure",
            "amnesia",
            "swimming",
            "darkness",
            "alternate costumes",
            "world map",
            "humble bundle",
            "save point",
            "underwater gameplay",
            "shape-shifting",
            "plot twist"
        ],
        "release_date": "2007"
    },
    "ArchipIDLE": {
        "igdb_id": "",
        "world_name": "ArchipIDLE",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "An Untitled Story": {
        "igdb_id": "72926",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2nok.jpg",
        "world_name": "An Untitled Story",
        "igdb_name": "an untitled story",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "metroidvania",
            "action-adventure",
            "bird"
        ],
        "release_date": "2007"
    },
    "Balatro": {
        "igdb_id": "251833",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9f4g.jpg",
        "world_name": "Balatro",
        "igdb_name": "balatro",
        "rating": [
            "simulated gambling"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "strategy",
            "turn-based strategy (tbs)",
            "indie",
            "card & board game"
        ],
        "themes": [],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "android",
            "pc (microsoft windows)",
            "ios",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "roguelike"
        ],
        "release_date": "2024"
    },
    "Banjo-Tooie": {
        "igdb_id": "3418",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6c1w.jpg",
        "world_name": "Banjo-Tooie",
        "igdb_name": "banjo-tooie",
        "rating": [
            "crude humor",
            "animated violence",
            "comic mischief",
            "cartoon violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "quiz/trivia",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "nintendo 64"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "dinosaurs",
            "collecting",
            "flight",
            "action-adventure",
            "witches",
            "bird",
            "backtracking",
            "achievements",
            "easter egg",
            "sequel",
            "talking animals",
            "swimming",
            "digital distribution",
            "anthropomorphism",
            "breaking the fourth wall",
            "cameo appearance",
            "ice stage",
            "underwater gameplay",
            "rpg elements",
            "villain",
            "recurring boss",
            "invisible wall",
            "shape-shifting",
            "temporary invincibility",
            "gliding",
            "collection marathon",
            "lgbtq+",
            "retroachievements"
        ],
        "release_date": "2000"
    },
    "Blasphemous": {
        "igdb_id": "26820",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2eyn.jpg",
        "world_name": "Blasphemous",
        "igdb_name": "blasphemous",
        "rating": [
            "blood and gore",
            "violence",
            "nudity"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "hack and slash/beat 'em up",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy",
            "horror"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "a foul curse has fallen upon the land of cvstodia and all its inhabitants - it is simply known as the miracle.\n\nplay as the penitent one - a sole survivor of the massacre of the \u2018silent sorrow\u2019. trapped in an endless cycle of death and rebirth, it\u2019s down to you to free the world from this terrible fate and reach the origin of your anguish.",
        "keywords": [
            "retro",
            "bloody",
            "2d",
            "metroidvania",
            "difficult",
            "side-scrolling",
            "crossover",
            "religion",
            "achievements",
            "pixel art",
            "nudity",
            "silent protagonist",
            "2d platformer",
            "great soundtrack",
            "parrying",
            "moving platforms",
            "soulslike",
            "you can pet the dog",
            "interconnected-world"
        ],
        "release_date": "2019"
    },
    "Bomb Rush Cyberfunk": {
        "igdb_id": "135940",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6ya8.jpg",
        "world_name": "Bomb Rush Cyberfunk",
        "igdb_name": "bomb rush cyberfunk",
        "rating": [
            "language",
            "violence",
            "suggestive themes",
            "blood"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "sport",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "start your own cypher and dance, paint, trick, face off with the cops and stake your claim to the extrusions and cavities of a sprawling metropolis in an alternate future set to the musical brainwaves of hideki naganuma.",
        "keywords": [
            "3d platformer",
            "great soundtrack",
            "spiritual successor"
        ],
        "release_date": "2023"
    },
    "Brotato": {
        "igdb_id": "199116",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4pcj.jpg",
        "world_name": "Brotato",
        "igdb_name": "brotato",
        "rating": [
            "fantasy violence",
            "mild blood"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "fighting",
            "shooter",
            "role-playing (rpg)",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "android",
            "pc (microsoft windows)",
            "ios",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "a spaceship from potato world crashes onto an alien planet. the sole survivor: brotato, the only potato capable of handling 6 weapons at the same time. waiting to be rescued by his mates, brotato must survive in this hostile environment.",
        "keywords": [
            "roguelite"
        ],
        "release_date": "2023"
    },
    "Bumper Stickers": {
        "igdb_id": "271950",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co78k5.jpg",
        "world_name": "Bumper Stickers",
        "igdb_name": "bumper stickers archipelago edition",
        "rating": [],
        "player_perspectives": [],
        "genres": [
            "puzzle"
        ],
        "themes": [],
        "platforms": [
            "linux",
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2023"
    },
    "Candy Box 2": {
        "igdb_id": "62779",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3tqk.jpg",
        "world_name": "Candy Box 2",
        "igdb_name": "candy box 2",
        "rating": [],
        "player_perspectives": [
            "text"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)"
        ],
        "themes": [
            "historical",
            "comedy"
        ],
        "platforms": [
            "web browser"
        ],
        "storyline": "",
        "keywords": [
            "medieval",
            "magic",
            "management",
            "merchants"
        ],
        "release_date": "2013"
    },
    "Cat Quest": {
        "igdb_id": "36597",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qlq.jpg",
        "world_name": "Cat Quest",
        "igdb_name": "cat quest",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2017"
    },
    "Celeste": {
        "igdb_id": "26226",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3byy.jpg",
        "world_name": "Celeste",
        "igdb_name": "celeste",
        "rating": [
            "alcohol reference",
            "fantasy violence",
            "mild language"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "google stadia",
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "set on a fictional version of mount celeste, it follows a young woman named madeline who attempts to climb the mountain, and must face her inner demons in her quest to reach the summit.",
        "keywords": [
            "exploration",
            "retro",
            "2d",
            "difficult",
            "female protagonist",
            "cute",
            "atmospheric",
            "pixel art",
            "snow",
            "pixel graphics",
            "story rich",
            "great soundtrack",
            "digital distribution",
            "lgbtq+",
            "conversation"
        ],
        "release_date": "2018"
    },
    "Celeste 64": {
        "igdb_id": "284430",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7oz4.jpg",
        "world_name": "Celeste 64",
        "igdb_name": "celeste 64: fragments of the mountain",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "female protagonist",
            "lgbtq+"
        ],
        "release_date": "2024"
    },
    "Chained Echoes": {
        "igdb_id": "117271",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co544u.jpg",
        "world_name": "Chained Echoes",
        "igdb_name": "chained echoes",
        "rating": [
            "strong language",
            "suggestive themes",
            "sexual themes"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "strategy",
            "turn-based strategy (tbs)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "follow a group of heroes as they explore a land filled to the brim with charming characters, fantastic landscapes and vicious foes. can you bring peace to a continent where war has been waged for generations and betrayal lurks around every corner?",
        "keywords": [
            "jrpg"
        ],
        "release_date": "2022"
    },
    "ChecksFinder": {
        "igdb_id": "",
        "world_name": "ChecksFinder",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "hints",
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Civilization VI": {
        "igdb_id": "293",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1rjp.jpg",
        "world_name": "Civilization VI",
        "igdb_name": "sid meier's civilization iv",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "simulator",
            "strategy",
            "turn-based strategy (tbs)"
        ],
        "themes": [
            "fantasy",
            "historical",
            "educational",
            "4x (explore, expand, exploit, and exterminate)"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "construction",
            "turn-based",
            "spaceship",
            "management",
            "religion",
            "multiple endings",
            "sequel",
            "mining",
            "digital distribution",
            "voice acting",
            "loot gathering",
            "royalty",
            "ambient music"
        ],
        "release_date": "2005"
    },
    "Clique": {
        "igdb_id": "",
        "world_name": "Clique",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld",
            "meme origin"
        ],
        "release_date": ""
    },
    "CrossCode": {
        "igdb_id": "35282",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co28wy.jpg",
        "world_name": "CrossCode",
        "igdb_name": "crosscode",
        "rating": [
            "fantasy violence",
            "language"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "shooter",
            "puzzle",
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "16-bit",
            "action-adventure",
            "pixel art",
            "crowdfunding",
            "digital distribution",
            "a.i. companion",
            "crowd funded"
        ],
        "release_date": "2018"
    },
    "Chrono Trigger Jets of Time": {
        "igdb_id": "20398",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co54iw.jpg",
        "world_name": "Chrono Trigger Jets of Time",
        "igdb_name": "chrono trigger",
        "rating": [
            "animated blood",
            "mild fantasy violence",
            "suggestive themes",
            "use of alcohol"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction"
        ],
        "platforms": [
            "nintendo ds"
        ],
        "storyline": "",
        "keywords": [
            "time travel",
            "magic"
        ],
        "release_date": "2008"
    },
    "Cuphead": {
        "igdb_id": "9061",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co62ao.jpg",
        "world_name": "Cuphead",
        "igdb_name": "cuphead",
        "rating": [
            "use of alcohol and tobacco",
            "mild language",
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "adventure",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "pirates",
            "ghosts",
            "retro",
            "magic",
            "2d",
            "shark",
            "robots",
            "side-scrolling",
            "bird",
            "achievements",
            "multiple endings",
            "dancing",
            "explosion",
            "digital distribution",
            "anthropomorphism",
            "voice acting",
            "cat",
            "shopping",
            "bow and arrow",
            "parrying",
            "violent plants",
            "conveyor belt",
            "auto-scrolling levels",
            "temporary invincibility",
            "boss assistance",
            "the game awards 2017"
        ],
        "release_date": "2017"
    },
    "Castlevania 64": {
        "igdb_id": "1130",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5geb.jpg",
        "world_name": "Castlevania 64",
        "igdb_name": "castlevania",
        "rating": [
            "animated blood",
            "animated violence"
        ],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "platform",
            "puzzle",
            "hack and slash/beat 'em up",
            "adventure"
        ],
        "themes": [
            "action",
            "horror"
        ],
        "platforms": [
            "nintendo 64"
        ],
        "storyline": "castlevania games debut on the n64 this is the first castlevania game in 3d. however, the goal of the game remains the same: defeat dracula and his monsters. the player can choose to be reinhardt schneider with traditional whip or carrie fernandez who uses magic. a new feature is the presence of an in-game clock that switches time from day to night.",
        "keywords": [
            "ghosts",
            "exploration",
            "bloody",
            "magic",
            "summoning support",
            "death",
            "horse",
            "maze",
            "female protagonist",
            "action-adventure",
            "religion",
            "witches",
            "multiple protagonists",
            "backtracking",
            "multiple endings",
            "undead",
            "traps",
            "dog",
            "teleportation",
            "bats",
            "day/night cycle",
            "explosion",
            "anthropomorphism",
            "alternate costumes",
            "voice acting",
            "human",
            "polygonal 3d",
            "shopping",
            "upgradeable weapons",
            "loot gathering",
            "skeletons",
            "descendants of other characters",
            "save point",
            "ice stage",
            "falling damage",
            "unstable platforms",
            "melee",
            "real-time combat",
            "male antagonist",
            "instant kill",
            "difficulty level",
            "moving platforms",
            "plot twist",
            "ambient music",
            "poisoning",
            "time paradox",
            "retroachievements"
        ],
        "release_date": "1999"
    },
    "Castlevania - Circle of the Moon": {
        "igdb_id": "1132",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2zq1.jpg",
        "world_name": "Castlevania - Circle of the Moon",
        "igdb_name": "castlevania: circle of the moon",
        "rating": [
            "mild violence",
            "animated blood"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "horror"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "taking place in 1830, circle of the moon is set in one of the fictional universes of the castlevania series. the premise of the original series is the eternal conflict between the vampire hunters of the belmont clan and the immortal vampire dracula. circle of the moon's protagonist, however, is nathan graves, whose parents died a decade ago to banish dracula. morris baldwin, who helped in dracula's banishment, trained him to defeat dracula and the monsters; morris ultimately chose him as his successor and gave him the \"hunter whip\", to the displeasure of hugh, morris' son who trained alongside him.\n\nat an old castle, camilla, a minion of dracula, revives him, only to be interrupted by the arrival of morris, nathan, and hugh. before they are able to banish him again, dracula destroys the floor under nathan and hugh, causing them to plummet down a long tunnel. surviving the fall and wishing to find his father, hugh leaves nathan behind. nathan proceeds to search the castle for his mentor. along the way, he learns that at the next full moon, morris' soul will be used to return dracula to full power. he also periodically encounters hugh, who becomes more hostile as the game progresses. eventually, nathan encounters camilla, who hints that she and dracula are responsible for the changes in his personality. nathan vanquishes camilla in her true form and meets up with hugh once more. upon seeing him, hugh immediately attacks him with the goal of proving himself to his father through nathan's defeat; nathan, however, realizes that dracula is controlling hugh. nathan defeats him, and dracula's control over hugh breaks. confessing that he doubted his self-worth when nathan was chosen as successor, hugh tasks him with morris' rescue.\n\narriving at the ceremonial room, nathan confronts dracula, who confirms that he had tampered with hugh's soul to cause the changes in his personality. they begin to fight and halfway through, dracula teleports away to gain his full power. hugh then frees his father and tasks nathan with dracula's banishment. nathan continues the battle and defeats dracula; escaping the collapsing castle, he reunites with morris and hugh. nathan is declared a master vampire hunter by morris. hugh vows to retrain under morris due to his failure.",
        "keywords": [
            "gravity",
            "magic",
            "metroidvania",
            "death",
            "horse",
            "action-adventure",
            "backtracking",
            "wolf",
            "wall jump",
            "bats",
            "leveling up",
            "skeletons",
            "save point",
            "unstable platforms",
            "melee",
            "moving platforms",
            "villain"
        ],
        "release_date": "2001"
    },
    "Dark Souls II": {
        "igdb_id": "2368",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2eoo.jpg",
        "world_name": "Dark Souls II",
        "igdb_name": "dark souls ii",
        "rating": [
            "blood and gore",
            "partial nudity",
            "violence",
            "mild language"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 3",
            "pc (microsoft windows)",
            "xbox 360"
        ],
        "storyline": "",
        "keywords": [
            "medieval",
            "magic",
            "3d",
            "metroidvania",
            "death",
            "action-adventure",
            "achievements",
            "undead",
            "traps",
            "sequel",
            "sword & sorcery",
            "spider",
            "customizable characters",
            "leveling up",
            "human",
            "bow and arrow",
            "upgradeable weapons",
            "checkpoints",
            "saving the world",
            "side quests",
            "melee",
            "real-time combat",
            "parrying",
            "rpg elements",
            "mercenary",
            "boss assistance",
            "sliding down ladders",
            "fire manipulation",
            "status effects",
            "hidden room",
            "soulslike",
            "interconnected-world"
        ],
        "release_date": "2014"
    },
    "Dark Souls III": {
        "igdb_id": "11133",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1vcf.jpg",
        "world_name": "Dark Souls III",
        "igdb_name": "dark souls iii",
        "rating": [
            "blood",
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "xbox one"
        ],
        "storyline": "set in the kingdom of lothric, a bell has rung to signal that the first flame, responsible for maintaining the age of fire, is dying out. as has happened many times before, the coming of the age of dark produces the undead: cursed beings that rise after death. the age of fire can be prolonged by linking the fire, a ritual in which great lords and heroes sacrifice their souls to rekindle the first flame. however, prince lothric, the chosen linker for this age, abandoned his duty and decided to watch the flame die from afar. the bell is the last hope for the age of fire, resurrecting previous lords of cinder (heroes who linked the flame in past ages) to attempt to link the fire again; however, all but one lord shirk their duty. meanwhile, sulyvahn, a sorcerer from the painted world of ariandel, wrongfully proclaims himself pontiff and seizes power over irithyll of the boreal valley and the returning anor londo cathedral from dark souls as a tyrant.\n\nthe ashen one, an undead who failed to become a lord of cinder and thus called an unkindled, rises and must link the fire by returning prince lothric and the defiant lords of cinder to their thrones in firelink shrine. the lords include the abyss watchers, a legion of warriors sworn by the old wolf's blood which linked their souls into one to protect the land from the abyss and ultimately locked in an endless battle between each other; yhorm the giant, who sacrificed his life for a nation conquered by his ancestor; and aldrich, who became a lord of cinder despite his ravenous appetite for both men and gods. lothric was raised to link the first flame but neglected his duties and chose to watch the fire fade instead.\n\nonce the ashen one succeeds in returning lothric and the lords of cinder to their thrones, they travel to the ruins of the kiln of the first flame. there, they encounter the soul of cinder, an amalgamation of all the former lords of cinder. upon defeat, the player can attempt to link the fire or access three other optional endings unlocked by the player's in-game decisions. these include summoning the fire keeper to extinguish the flame and begin an age of dark or killing her in a sudden change of heart. a fourth ending consists of the ashen one taking the flame for their own, becoming the lord of hollows.",
        "keywords": [
            "medieval",
            "3d",
            "death",
            "action-adventure",
            "sequel",
            "sword & sorcery",
            "customizable characters",
            "human",
            "pick your gender",
            "parrying",
            "sliding down ladders",
            "entering world in a painting",
            "soulslike",
            "interconnected-world"
        ],
        "release_date": "2016"
    },
    "Diddy Kong Racing": {
        "igdb_id": "2723",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wgj.jpg",
        "world_name": "Diddy Kong Racing",
        "igdb_name": "diddy kong racing",
        "rating": [],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "racing"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "nintendo 64"
        ],
        "storyline": "timber the tiger's parents picked a fine time to go on vacation. when they come back they're going to be faced with an island trashed by the spiteful space bully wizpig - unless the local animals can do something about it! so join diddy kong as he teams up with timber the tiger pipsy the mouse and taj the genie in an epic racing adventure unlike anything you've ever experienced before! this unique game blends adventure and racing like no other game! roam anywhere you want on the island by car plane or hovercraft! an enormous amount of single-player and multi-player modes! feel the action when you use the n64 rumble pak and save your times on the n64 controller pak!",
        "keywords": [
            "flight",
            "crossover",
            "snow",
            "talking animals",
            "anthropomorphism",
            "monkey",
            "secret area",
            "time trials",
            "behind the waterfall",
            "retroachievements"
        ],
        "release_date": "1997"
    },
    "Donkey Kong Country": {
        "igdb_id": "1090",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co70qn.jpg",
        "world_name": "Donkey Kong Country",
        "igdb_name": "donkey kong country",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "on a dark and stormy night in donkey kong island, diddy kong, donkey kong's nephew has taken the weighty responsibility of guarding dk's precious banana hoard for one night, as a part of his \"hero training\". dk entrusts diddy with protecting the hoard until midnight, when he would be relieved, while dk himself goes to sleep as he is tired.\n\neverything seems to go smoothly in the hoard until diddy hears some noises. diddy hears some voices outside and gets scared, asking who's there. king k. rool, who had commanded his kremling minions to steal the bananas. two ropes drop from above and suddenly two kritters appear. diddy cartwheels them both easily, but then a krusha (klump in the instruction booklet) comes in as backup. as diddy is not strong enough to defeat krusha by himself, he is overpowered and defeated by the kremling. the lizars seal diddy inside a barrel and then throw it in the bushes.\ndonkey's grandfather, cranky kong, rushes inside the treehouse to tell donkey kong to wake up so he may tell him what happened. he then tells donkey to check his banana cave. donkey kong is infuriated, exclaiming that the kremlings will pay for stealing his banana hoard and kidnapping his little buddy. donkey goes on to say that he will hunt every corner of the island for his bananas back.",
        "keywords": [
            "gravity",
            "shark",
            "death",
            "2.5d",
            "frog",
            "flight",
            "side-scrolling",
            "multiple protagonists",
            "overworld",
            "snow",
            "giant insects",
            "talking animals",
            "silent protagonist",
            "swimming",
            "darkness",
            "digital distribution",
            "anthropomorphism",
            "bonus stage",
            "monkey",
            "nintendo power",
            "world map",
            "crocodile",
            "breaking the fourth wall",
            "descendants of other characters",
            "save point",
            "ice stage",
            "checkpoints",
            "unstable platforms",
            "real-time combat",
            "underwater gameplay",
            "instant kill",
            "secret area",
            "moving platforms",
            "recurring boss",
            "water level",
            "auto-scrolling levels",
            "western games based on japanese ips",
            "speedrun",
            "boss assistance",
            "villain turned good",
            "over 100% completion",
            "ambient music",
            "resized enemy",
            "on-the-fly character switching",
            "ape",
            "buddy system",
            "retroachievements"
        ],
        "release_date": "1994"
    },
    "Donkey Kong Country 2": {
        "igdb_id": "1092",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co217m.jpg",
        "world_name": "Donkey Kong Country 2",
        "igdb_name": "donkey kong country 2: diddy's kong quest",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "it was a relaxing, sunny day on donkey kong island. funky kong is seen surfing and then falling off his board. he asked for donkey kong to join him, but the hero simply continues lounging. cranky kong goes up to him and complains how he never took breaks, \"whisking off maidens and throwing barrels seven days a week\", but donkey ignores him, confident that he is a hero and that king k. rool is gone for good. cranky soon leaves.\n\nmeanwhile, above, kaptain k. rool, aboard his vessel, the flying krock, commands his minions to invade the island and take donkey captive so that his next attempt at stealing the banana hoard will not be a failure and the hero will never mess with his plans again. donkey, still lounging, did not notice the attack until kutlasses ambushed him and took him prisoner. kaptain k. rool assures donkey kong that he will never see his precious island or his friends again.\n\nlater and back on the island, diddy, dixie and cranky kong find donkey missing, along with a note. it reads:\nhah-arrrrh! we have got the big monkey! if you want him back, you scurvy dogs, you'll have to hand over the banana hoard!\nkaptain k. rool\nat this point, wrinkly, funky and swanky kong come to the scene. cranky suggests to give up the hoard, but diddy insists that donkey kong would be furious if he lost his bananas after all trouble recovering them at the last time. diddy and dixie kong ride to crocodile isle via enguarde the swordfish, and then start their quest.",
        "keywords": [
            "pirates",
            "ghosts",
            "gravity",
            "2.5d",
            "frog",
            "female protagonist",
            "side-scrolling",
            "multiple protagonists",
            "overworld",
            "multiple endings",
            "dancing",
            "sequel",
            "giant insects",
            "talking animals",
            "silent protagonist",
            "climbing",
            "swimming",
            "darkness",
            "explosion",
            "digital distribution",
            "anthropomorphism",
            "bonus stage",
            "monkey",
            "spider",
            "nintendo power",
            "world map",
            "crocodile",
            "cat",
            "breaking the fourth wall",
            "game reference",
            "cameo appearance",
            "descendants of other characters",
            "save point",
            "sprinting mechanics",
            "ice stage",
            "checkpoints",
            "underwater gameplay",
            "instant kill",
            "secret area",
            "self-referential humor",
            "liberation",
            "recurring boss",
            "water level",
            "auto-scrolling levels",
            "temporary invincibility",
            "western games based on japanese ips",
            "boss assistance",
            "over 100% completion",
            "completion percentage",
            "ambient music",
            "resized enemy",
            "fireworks",
            "on-the-fly character switching",
            "ape",
            "buddy system",
            "retroachievements"
        ],
        "release_date": "1995"
    },
    "Donkey Kong Country 3": {
        "igdb_id": "1094",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co217n.jpg",
        "world_name": "Donkey Kong Country 3",
        "igdb_name": "donkey kong country 3: dixie kong's double trouble!",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "months after the kongs' second triumph over the kremling krew, they continue to celebrate. one day, dk and diddy suddenly disappear, and a letter from diddy says they were out exploring the island again.\n\nhowever, several days pass without their return, and dixie knows something is up. she takes matters into her own hands, and made her way to the southern shores of donkey kong island, to the northern kremisphere, a canadian and northern european-inspired landmass. there she meets wrinkly kong, and wrinkly confirmed that the kongs had passed by. dixie then makes her way to funky's rentals. funky suggests her to take her baby cousin kiddy kong along with her in the search. funky lends them a boat and the two venture off to find donkey and diddy kong.",
        "keywords": [
            "gravity",
            "minigames",
            "2.5d",
            "female protagonist",
            "side-scrolling",
            "multiple protagonists",
            "overworld",
            "bird",
            "dancing",
            "snow",
            "giant insects",
            "talking animals",
            "swimming",
            "darkness",
            "snowman",
            "explosion",
            "anthropomorphism",
            "bonus stage",
            "monkey",
            "nintendo power",
            "world map",
            "crocodile",
            "descendants of other characters",
            "save point",
            "ice stage",
            "checkpoints",
            "secret area",
            "shielded enemies",
            "moving platforms",
            "recurring boss",
            "auto-scrolling levels",
            "western games based on japanese ips",
            "over 100% completion",
            "ambient music",
            "on-the-fly character switching",
            "behind the waterfall",
            "ape",
            "buddy system",
            "retroachievements"
        ],
        "release_date": "1996"
    },
    "DLCQuest": {
        "igdb_id": "3004",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2105.jpg",
        "world_name": "DLCQuest",
        "igdb_name": "dlc quest",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac",
            "xbox 360"
        ],
        "storyline": "",
        "keywords": [
            "exploration",
            "steam greenlight",
            "digital distribution",
            "deliberately retro",
            "punctuation mark above head"
        ],
        "release_date": "2011"
    },
    "Don": {
        "igdb_id": "17832",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6la0.jpg",
        "world_name": "Don",
        "igdb_name": "don't starve together",
        "rating": [
            "crude humor",
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "simulator",
            "strategy",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "horror",
            "survival",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac",
            "nintendo switch"
        ],
        "storyline": "discover and explore a massive procedurally generated and biome-rich world with countless resources and threats. whether you stick to the surface world, go spelunking in the caves, dive deeper into the ancient archive, or set sail for the lunar islands, it will be a long time before you run out of things to do.\n\nseasonal bosses, wandering menaces, lurking shadow creatures, and plenty of flora and fauna ready to turn you into a spooky ghost.\n\nplow fields and sow seeds to grow the farm of your dreams. tend to your crops to help your fellow survivors stay fed and ready for the challenges to come.\n\nprotect yourself, your friends, and everything you have managed to gather, because you can be sure, somebody or something is going to want it back.\n\nenter a strange and unexplored world full of odd creatures, hidden dangers, and ancient secrets. gather resources to craft items and build structures that match your survival style. play your way as you unravel the mysteries of \"the constant\".\n\ncooperate with your friends in a private game, or find new friends online. work with other players to survive the harsh environment, or strike out on your own.\n\ndo whatever it takes, but most importantly, don't starve.",
        "keywords": [
            "2d",
            "crafting",
            "difficult",
            "action-adventure",
            "funny",
            "atmospheric",
            "survival horror",
            "sequel",
            "digital distribution",
            "bees"
        ],
        "release_date": "2016"
    },
    "DOOM 1993": {
        "igdb_id": "673",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5rav.jpg",
        "world_name": "DOOM 1993",
        "igdb_name": "doom",
        "rating": [
            "intense violence",
            "blood and gore",
            "violence",
            "animated violence",
            "animated blood and gore"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "shooter"
        ],
        "themes": [
            "action",
            "science fiction",
            "horror"
        ],
        "platforms": [
            "windows mobile",
            "pc-9800 series",
            "linux",
            "dos"
        ],
        "storyline": "the player takes the role of a marine (unnamed to further represent the person playing), \"one of earth's toughest, hardened in combat and trained for action\", who has been incarcerated on mars after assaulting a senior officer when ordered to fire upon civilians. there, he works alongside the union aerospace corporation (uac), a multi-planetary conglomerate and military contractor performing secret experiments on interdimensional travel. recently, the teleportation has shown signs of anomalies and instability, but the research continues nonetheless.\n\nsuddenly, something goes wrong and creatures from hell swarm out of the teleportation gates on deimos and phobos. a defensive response from base security fails to halt the invasion, and the bases are quickly overrun by monsters; all personnel are killed or turned into zombies\n\na military detachment from mars travels to phobos to investigate the incident. the player is tasked with securing the perimeter, as the assault team and their heavy weapons are brought inside. radio contact soon ceases and the player realizes that he is the only survivor. being unable to pilot the shuttle off of phobos by himself, the only way to escape is to go inside and fight through the complexes of the moon base.",
        "keywords": [
            "2.5d",
            "maze",
            "silent protagonist",
            "melee",
            "real-time combat",
            "invisibility"
        ],
        "release_date": "1993"
    },
    "DOOM II": {
        "igdb_id": "312",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6iip.jpg",
        "world_name": "DOOM II",
        "igdb_name": "doom ii: hell on earth",
        "rating": [
            "violence",
            "blood and gore"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "shooter",
            "puzzle"
        ],
        "themes": [
            "action",
            "science fiction",
            "horror"
        ],
        "platforms": [
            "pc-9800 series",
            "tapwave zodiac",
            "pc (microsoft windows)",
            "mac",
            "dos"
        ],
        "storyline": "immediately following the events in doom, the player once again assumes the role of the unnamed space marine. after defeating the demon invasion of the mars moon bases and returning from hell, doomguy finds that earth has also been invaded by the demons, who have killed billions of people.\n\nthe humans who survived the attack have developed a plan to build massive spaceships which will carry the remaining survivors into space. once the ships are ready, the survivors prepare to evacuate earth. unfortunately, earth's only ground spaceport gets taken over by the demons, who place a flame barrier over it, preventing any ships from leaving.",
        "keywords": [
            "bloody",
            "death",
            "2.5d",
            "achievements",
            "multiple endings",
            "traps",
            "artificial intelligence",
            "easter egg",
            "teleportation",
            "sequel",
            "darkness",
            "explosion",
            "digital distribution",
            "voice acting",
            "human",
            "breaking the fourth wall",
            "game reference",
            "unstable platforms",
            "melee",
            "real-time combat",
            "stat tracking",
            "secret area",
            "walking through walls",
            "difficulty level",
            "rock music",
            "sequence breaking",
            "temporary invincibility",
            "dimension travel",
            "boss assistance",
            "over 100% completion",
            "invisibility",
            "hidden room",
            "another world"
        ],
        "release_date": "1994"
    },
    "DORONKO WANKO": {
        "igdb_id": "290647",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7zj5.jpg",
        "world_name": "DORONKO WANKO",
        "igdb_name": "doronko wanko",
        "rating": [],
        "player_perspectives": [],
        "genres": [
            "simulator"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "dog"
        ],
        "release_date": "2024"
    },
    "Dark Souls Remastered": {
        "igdb_id": "81085",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2uro.jpg",
        "world_name": "Dark Souls Remastered",
        "igdb_name": "dark souls: remastered",
        "rating": [
            "blood and gore",
            "partial nudity",
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "magic",
            "3d",
            "undead",
            "soulslike",
            "interconnected-world"
        ],
        "release_date": "2018"
    },
    "Dungeon Clawler": {
        "igdb_id": "290897",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7ygu.jpg",
        "world_name": "Dungeon Clawler",
        "igdb_name": "dungeon clawler",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "simulator",
            "strategy",
            "turn-based strategy (tbs)",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "fantasy",
            "survival"
        ],
        "platforms": [
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "roguelike",
            "roguelite"
        ],
        "release_date": "2024"
    },
    "Digimon World": {
        "igdb_id": "3878",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2dyy.jpg",
        "world_name": "Digimon World",
        "igdb_name": "digimon world 4",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "xbox",
            "nintendo gamecube",
            "playstation 2"
        ],
        "storyline": "the yamato server disappears after the x-virus attacks, and the doom server has taken it's place. it's up to the you and up to 3 of your friends, the digital security guard (d.s.g.) to venture into the doom server, discover the source of the virus and deal with the infection before it can infect the home server.\n\nyou will venture into the dry lands stop the virus from spreading, into the venom jungle to stop the dread note from launching and then the machine pit to destroy the final boss.\n\nafter finishing the game for the first time, you unlock hard mode, where the enemies are stronger, but you keep all of your levels, equipment and digivolutions. do it again, and you unlock the hardest difficulty, very hard.",
        "keywords": [
            "anime",
            "sequel",
            "leveling up",
            "voice acting",
            "polygonal 3d",
            "shopping"
        ],
        "release_date": "2005"
    },
    "EarthBound": {
        "igdb_id": "2899",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6v07.jpg",
        "world_name": "EarthBound",
        "igdb_name": "earthbound",
        "rating": [],
        "player_perspectives": [
            "first person",
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction",
            "drama"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii u",
            "new nintendo 3ds",
            "game boy advance",
            "super famicom"
        ],
        "storyline": "the story begins when ness is awakened by a meteor that has plummeted to the earth near his home, whereupon he proceeds to investigate the crash site. when ness gets to the crash site he discovers a police roadblock and pokey minch, his friend and neighbor, who tells him to go home. later, ness is woken up again by pokey knocking at his door, demanding help to find his brother picky.\n\nthey find him near the meteor sleeping behind a tree and wake him up. then the three encounter an insect from the meteor named buzz buzz who informs ness that he is from the future where the \"universal cosmic destroyer\", giygas, dominates the planet. buzz buzz senses great potential in ness and instructs him to embark on a journey to seek out and record the melodies of eight \"sanctuaries,\" unite his own powers with the earth's and gain the strength required to confront giygas.",
        "keywords": [
            "aliens",
            "ghosts",
            "dinosaurs",
            "time travel",
            "2d",
            "16-bit",
            "turn-based",
            "robots",
            "female protagonist",
            "religion",
            "multiple protagonists",
            "teleportation",
            "darkness",
            "nintendo power",
            "leveling up",
            "damsel in distress",
            "party system",
            "descendants of other characters",
            "save point",
            "saving the world",
            "royalty",
            "male antagonist",
            "self-referential humor",
            "kidnapping",
            "fire manipulation",
            "censored version",
            "status effects",
            "retroachievements"
        ],
        "release_date": "1994"
    },
    "Ender Lilies": {
        "igdb_id": "138858",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9s9e.jpg",
        "world_name": "Ender Lilies",
        "igdb_name": "ender lilies: quietus of the knights",
        "rating": [
            "violence",
            "blood"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "once upon a time, in the end's kingdom, the dying rain suddenly started to fall, transforming all living things it touched into bloodthirsty corpses. following this tragedy, the kingdom quickly fell into chaos and soon, no one remained. the rain, as if cursed, would never stop falling on the land. in the depths of a forsaken church, lily opens her eyes...",
        "keywords": [
            "metroidvania",
            "female protagonist",
            "witches",
            "soulslike",
            "conversation"
        ],
        "release_date": "2021"
    },
    "Factorio": {
        "igdb_id": "7046",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1tfy.jpg",
        "world_name": "Factorio",
        "igdb_name": "factorio",
        "rating": [
            "blood",
            "violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "simulator",
            "strategy",
            "indie"
        ],
        "themes": [
            "science fiction",
            "survival",
            "sandbox"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac",
            "nintendo switch"
        ],
        "storyline": "you crash land on an alien planet and must research a way to get yourself a rocket out of the planet. defend yourself from the natives who dislike the pollution your production generates.",
        "keywords": [
            "aliens",
            "crafting",
            "digital distribution"
        ],
        "release_date": "2020"
    },
    "Factorio - Space Age Without Space": {
        "igdb_id": "263344",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co91k3.jpg",
        "world_name": "Factorio - Space Age Without Space",
        "igdb_name": "factorio: space age",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "simulator",
            "strategy",
            "indie"
        ],
        "themes": [
            "science fiction",
            "survival",
            "sandbox"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "crafting"
        ],
        "release_date": "2024"
    },
    "Faxanadu": {
        "igdb_id": "1974",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5jif.jpg",
        "world_name": "Faxanadu",
        "igdb_name": "faxanadu",
        "rating": [
            "mild fantasy violence",
            "use of tobacco"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox"
        ],
        "platforms": [
            "wii",
            "family computer",
            "nintendo entertainment system"
        ],
        "storyline": "the player-controlled protagonist of is an unidentified wanderer. he has no name, though the japanese version allows the player to choose one. the game begins when he approaches eolis, his hometown, after an absence to find it in disrepair and virtually abandoned. worse still, the town is under attack by dwarves.the elven king explains that the elf fountain water, their life source, has stopped and provides the protagonist with 1500 golds, the games currency, to prepare for his journey to uncover the cause.as the story unfolds, it is revealed that elves and dwarfs lived in harmony among the world tree until the evil one emerged from a fallen meteorite. the evil one then transformed the dwarves into monsters against their will and set them against the elves. the dwarf king, grieve, swallowed his magical sword before he was transformed, hiding it in his own body to prevent the evil one from acquiring it. it is only with this sword that the evil one can be destroyed.his journey takes him to four overworld areas: the tree's buttress, the inside of the trunk, the tree's branches and finally the dwarves' mountain stronghold.",
        "keywords": [
            "magic",
            "metroidvania",
            "backtracking",
            "save point",
            "temporary invincibility",
            "merchants"
        ],
        "release_date": "1987"
    },
    "Final Fantasy": {
        "igdb_id": "385",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2xv8.jpg",
        "world_name": "Final Fantasy",
        "igdb_name": "final fantasy",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "kids"
        ],
        "platforms": [
            "nintendo 3ds",
            "wii",
            "family computer",
            "wii u",
            "nintendo entertainment system"
        ],
        "storyline": "the story follows four youths called the light warriors, who each carry one of their world's four elemental orbs which have been darkened by the four elemental fiends. together, they quest to defeat these evil forces, restore light to the orbs, and save their world.",
        "keywords": [
            "jrpg"
        ],
        "release_date": "1987"
    },
    "Final Fantasy IV Free Enterprise": {
        "igdb_id": "387",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2y6s.jpg",
        "world_name": "Final Fantasy IV Free Enterprise",
        "igdb_name": "final fantasy ii",
        "rating": [
            "mild fantasy violence",
            "mild suggestive themes"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii"
        ],
        "storyline": "",
        "keywords": [
            "jrpg",
            "retroachievements"
        ],
        "release_date": "1991"
    },
    "Final Fantasy Mystic Quest": {
        "igdb_id": "415",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2y0b.jpg",
        "world_name": "Final Fantasy Mystic Quest",
        "igdb_name": "final fantasy: mystic quest",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "super famicom"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "casual",
            "ninja",
            "turn-based",
            "jrpg",
            "overworld",
            "undead",
            "sword & sorcery",
            "explosion",
            "party system",
            "rock music",
            "retroachievements"
        ],
        "release_date": "1992"
    },
    "Final Fantasy Tactics Advance": {
        "igdb_id": "414",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wyp.jpg",
        "world_name": "Final Fantasy Tactics Advance",
        "igdb_name": "final fantasy tactics advance",
        "rating": [
            "mild violence",
            "alcohol reference"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "strategy",
            "turn-based strategy (tbs)",
            "tactical"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "ninja",
            "magic",
            "grinding",
            "turn-based",
            "summoning support",
            "jrpg",
            "death",
            "management",
            "overworld",
            "backtracking",
            "snow",
            "sequel",
            "explosion",
            "bow and arrow",
            "breaking the fourth wall",
            "party system",
            "melee",
            "stat tracking",
            "rock music",
            "coming of age",
            "been here before",
            "androgyny",
            "random encounter",
            "damage over time"
        ],
        "release_date": "2003"
    },
    "Yu-Gi-Oh! Forbidden Memories": {
        "igdb_id": "4108",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ui5.jpg",
        "world_name": "Yu-Gi-Oh! Forbidden Memories",
        "igdb_name": "yu-gi-oh! forbidden memories",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "strategy",
            "turn-based strategy (tbs)",
            "card & board game"
        ],
        "themes": [
            "fantasy",
            "historical"
        ],
        "platforms": [
            "playstation"
        ],
        "storyline": "the game begins in ancient egypt, with prince atem sneaking out of the palace to see his friends, jono and teana, at the dueling grounds. while there, they witness a ceremony performed by the mages, which is darker than the ceremonies that they normally perform. after the ceremony, atem duels one of the priests, named seto, and defeats him.\n\nwhen atem returns to the palace, he is quickly sent to bed by simon muran, his tutor and advisor. as simon walks away, he is informed by a guard that the high priest heishin has invaded the palace, using a strange magic. muran searches for heishin. when muran finds him, heishin tells muran that he has found the dark power, then uses the millennium rod to blast muran. when heishin finds atem, he threatens to kill the egyptian king and queen if he does not hand over the millennium puzzle. muran appears behind heishin and tells atem to smash the puzzle. atem obeys, and muran seals himself and atem inside the puzzle, to wait for someone to reassemble it.\n\nfive thousand years later, yugi mutou reassembles the puzzle. he speaks to atem in the puzzle, and atem gives yugi six blank cards. not sure what they are for, he carries them into a dueling tournament. after he defeats one of the duelists, one of the cards is filled with a millennium item. realizing what the cards are for, yugi completes the tournament and fills all six cards with millennium items. this allows atem to return to his time.\n\nonce in his own time, muran tells atem of what has happened since he was sealed away. heishin and the mages have taken control of the kingdom with the millennium items, and that the only way to free the kingdom is to recover the items from the mages guarding them. after passing this on, muran dies.\n\nafter he catches up with jono and teana, he goes to the destroyed palace and searches it. he finds seto, who gives him a map with the locations of the mages and the millennium items, and asks him to defeat the mages.\n\nafter atem recovers all of the millennium items but one, seto leads him to heishin, who holds the millennium rod. atem defeats heishin, but discovers that seto has the millennium rod, and merely wanted to use atem to gather the items in one place. atem duels seto for the items and defeats him, but after the duel, heishin grabs the items and uses them to summon the darknite. hoping to use the darknite to destroy his enemies, he doesn't have the item to prove his authority and as a result, the darknite instead turns heishin into a card. heishin now turned into a playing card, darknite now mocks heishin before incinerating the card. after atem shows that he had the millennium items, darknite challenges him to a duel. atem defeats him, and he transforms into nitemare, who challenges atem again. atem defeats him again, and nitemare begrudgingly returns from where he came. atem then is able to take the throne and lead his people in peace.",
        "keywords": [
            "anime",
            "turn-based",
            "summoning support"
        ],
        "release_date": "1999"
    },
    "Getting Over It": {
        "igdb_id": "72373",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3wl5.jpg",
        "world_name": "Getting Over It",
        "igdb_name": "getting over it with bennett foddy",
        "rating": [],
        "player_perspectives": [
            "third person",
            "side view"
        ],
        "genres": [
            "platform",
            "simulator",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "horror",
            "comedy"
        ],
        "platforms": [
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "climb up an enormous mountain with nothing but a hammer and a pot.",
        "keywords": [
            "casual",
            "psychological horror",
            "difficult",
            "space",
            "funny",
            "story rich",
            "great soundtrack",
            "digital distribution",
            "humble bundle"
        ],
        "release_date": "2017"
    },
    "Golden Sun The Lost Age": {
        "igdb_id": "1173",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co25rt.jpg",
        "world_name": "Golden Sun The Lost Age",
        "igdb_name": "golden sun: the lost age",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "open world"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "\"it is the dawn of a new age...and the heroes of golden sun have been abandoned. now, the world is falling into darkness. a new band of adventurers is the world's final hope...but they may also be its doom. pursued by the heroes of the original golden sun, they must race to complete their quest before the world becomes lost to the ages.\"",
        "keywords": [
            "anime",
            "magic",
            "minigames",
            "turn-based",
            "summoning support",
            "death",
            "overworld",
            "snow",
            "sequel",
            "silent protagonist",
            "leveling up",
            "human",
            "party system",
            "save point",
            "potion",
            "melee",
            "rock music",
            "been here before",
            "sleeping",
            "villain turned good",
            "androgyny",
            "ancient advanced civilization technology",
            "random encounter",
            "fire manipulation",
            "battle screen",
            "behind the waterfall"
        ],
        "release_date": "2002"
    },
    "gzDoom": {
        "igdb_id": "307741",
        "cover_url": "",
        "world_name": "gzDoom",
        "igdb_name": "gzdoom sm64",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": ""
    },
    "Hades": {
        "igdb_id": "113112",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co39vc.jpg",
        "world_name": "Hades",
        "igdb_name": "hades",
        "rating": [
            "mild language",
            "alcohol reference",
            "violence",
            "suggestive themes",
            "blood"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "hack and slash/beat 'em up",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy",
            "drama"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "ios",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "zagreus, the son of hades, has discovered that his mother, which he was led to believe was nyx, night incarnate, is actually someone else, and is outside hell. he is now attempting to escape his father's domain, with the help of the other gods of olympus, in an attempt to find his real mother.",
        "keywords": [
            "roguelike",
            "difficult",
            "stylized",
            "story rich",
            "roguelite",
            "you can pet the dog"
        ],
        "release_date": "2020"
    },
    "Heretic": {
        "igdb_id": "6362",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mwz.jpg",
        "world_name": "Heretic",
        "igdb_name": "heretic",
        "rating": [],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "shooter"
        ],
        "themes": [
            "fantasy",
            "historical"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac",
            "dos"
        ],
        "storyline": "",
        "keywords": [
            "bloody",
            "medieval",
            "magic",
            "death",
            "2.5d",
            "undead",
            "sword & sorcery",
            "digital distribution",
            "skeletons",
            "melee",
            "secret area",
            "hidden room"
        ],
        "release_date": "1994"
    },
    "Hollow Knight": {
        "igdb_id": "14593",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co93cr.jpg",
        "world_name": "Hollow Knight",
        "igdb_name": "hollow knight",
        "rating": [
            "fantasy violence",
            "mild blood"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "wii u",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "2d",
            "metroidvania",
            "action-adventure",
            "atmospheric",
            "giant insects",
            "silent protagonist",
            "crowdfunding",
            "2d platformer",
            "crowd funded",
            "shielded enemies",
            "parrying",
            "merchants",
            "creature compendium",
            "the game awards 2017",
            "interconnected-world",
            "popular"
        ],
        "release_date": "2017"
    },
    "Hunie Pop": {
        "igdb_id": "9655",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2sor.jpg",
        "world_name": "Hunie Pop",
        "igdb_name": "huniepop",
        "rating": [],
        "player_perspectives": [
            "first person",
            "text"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "simulator",
            "strategy",
            "indie",
            "visual novel"
        ],
        "themes": [
            "fantasy",
            "comedy",
            "erotic",
            "romance"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "anime",
            "nudity"
        ],
        "release_date": "2015"
    },
    "Hunie Pop 2": {
        "igdb_id": "72472",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5x87.jpg",
        "world_name": "Hunie Pop 2",
        "igdb_name": "huniepop 2: double date",
        "rating": [],
        "player_perspectives": [
            "first person",
            "text"
        ],
        "genres": [
            "puzzle",
            "simulator",
            "strategy",
            "indie",
            "visual novel"
        ],
        "themes": [
            "erotic",
            "romance"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "an era of darkness and destruction draws near as an ancient evil of limitless lechery, the nymphojinn, will soon be awoken by a cosmic super-period of unspeakable pms. reunite with kyu, your old love fairy sidekick, and travel to the island of inna de poona to develop your double dating prowess and overcome the insatiable lust of the demonic pair.",
        "keywords": [
            "anime",
            "fairy",
            "achievements",
            "funny",
            "nudity",
            "digital distribution",
            "voice acting"
        ],
        "release_date": "2021"
    },
    "Hylics 2": {
        "igdb_id": "98469",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co290q.jpg",
        "world_name": "Hylics 2",
        "igdb_name": "hylics 2",
        "rating": [],
        "player_perspectives": [
            "first person",
            "third person",
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure",
            "indie"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "the tyrant gibby\u2019s minions seek to reconstitute their long-presumed-annihilated master. it\u2019s up to our crescent headed protagonist wayne to assemble a crew and put a stop to that sort of thing.",
        "keywords": [
            "exploration",
            "retro",
            "3d",
            "jrpg",
            "flight",
            "side-scrolling",
            "stylized",
            "atmospheric",
            "sequel",
            "story rich",
            "2d platformer",
            "great soundtrack"
        ],
        "release_date": "2020"
    },
    "Inscryption": {
        "igdb_id": "139090",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co401c.jpg",
        "world_name": "Inscryption",
        "igdb_name": "inscryption",
        "rating": [
            "blood",
            "strong language",
            "violence"
        ],
        "player_perspectives": [
            "first person",
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "strategy",
            "adventure",
            "indie",
            "card & board game"
        ],
        "themes": [
            "horror",
            "mystery"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "from the creator of pony island and the hex comes the latest mind melting, self-destructing love letter to video games. inscryption is an inky black card-based odyssey that blends the deckbuilding roguelike, escape-room style puzzles, and psychological horror into a blood-laced smoothie. darker still are the secrets inscrybed upon the cards...\nin inscryption you will...\n\nacquire a deck of woodland creature cards by draft, surgery, and self mutilation\nunlock the secrets lurking behind the walls of leshy's cabin\nembark on an unexpected and deeply disturbing odyssey",
        "keywords": [],
        "release_date": "2021"
    },
    "Jak and Daxter: The Precursor Legacy": {
        "igdb_id": "1528",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1w7q.jpg",
        "world_name": "Jak and Daxter: The Precursor Legacy",
        "igdb_name": "jak and daxter: the precursor legacy",
        "rating": [
            "fantasy violence",
            "mild suggestive themes"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "racing",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "comedy",
            "open world"
        ],
        "platforms": [
            "playstation 4",
            "playstation 2"
        ],
        "storyline": "the opening sequence of the game features jak and daxter in a speedboat headed for misty island, an area prohibited by their watch over samos. upon arriving to the island, daxter had second thoughts about straying from the village. the two perch on a large skeleton to observe a legion of lurkers crowded around two dark figures, gol and maia, who were commanding the lurkers to \"deal harshly with anyone who strays from the village,\" and to search for any precursor artifacts and eco near sandover village.[4] after the secret observation, jak and daxter continue searching the island. daxter trips on a dark eco canister which he tosses to jak after expressing his dislike for the item, and as jak caught the object it lit up. shortly afterwards a bone armor lurker suddenly confronted the two, where jak threw the dark eco canister at the lurker, killing it, but inadvertently knocked daxter into a dark eco silo behind him. when daxter reemerged, he was in the form of an ottsel, and upon realizing the transformation he began to panic.",
        "keywords": [
            "exploration",
            "mascot",
            "shark",
            "frog",
            "backtracking",
            "artificial intelligence",
            "snow",
            "teleportation",
            "silent protagonist",
            "climbing",
            "swimming",
            "day/night cycle",
            "anthropomorphism",
            "world map",
            "voice acting",
            "polygonal 3d",
            "breaking the fourth wall",
            "cameo appearance",
            "descendants of other characters",
            "save point",
            "ice stage",
            "checkpoints",
            "auto-saving",
            "coming of age",
            "moving platforms",
            "temporary invincibility",
            "spiky-haired protagonist",
            "ancient advanced civilization technology",
            "time paradox",
            "damage over time"
        ],
        "release_date": "2001"
    },
    "Jigsaw": {
        "igdb_id": "",
        "world_name": "Jigsaw",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer",
            "puzzle"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Kirby 64 - The Crystal Shards": {
        "igdb_id": "2713",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wcz.jpg",
        "world_name": "Kirby 64 - The Crystal Shards",
        "igdb_name": "kirby 64: the crystal shards",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "on the planet of ripple star, lives a group of kind and peaceful fairies. the planet itself is protected from danger by the power of the great crystal, which watches over ripple star. this power, however, draws the attention of dark matter, who wishes to use the great crystal for its own evil agenda. its gigantic mass attacks and searches for the crystal, blackening the sky and sending the fairies into panic. in response to the threat dark matter presents, the queen of ripple star orders a fairy named ribbon to take the crystal to a safe place. ribbon tries to fly away with the crystal in tow, but is stopped by three orbs sent by dark matter. the crystal shatters into 74 shards, scattered throughout several planets, and ribbon crashes onto planet popstar. kirby finds one shard and gives it to ribbon, whereupon the two set out to find the others. once kirby and his friends collect every crystal shard and defeat miracle matter, dark matter flees ripple star and explodes. the victory is cut short, however, as the crystal detects a powerful presence of dark matter energy within the fairy queen and expels it from her, manifesting over the planet to create dark star. kirby and his friends infiltrate dark star, and king dedede launches them up to challenge 02. kirby and ribbon, armed with their shard gun, destroyed 02 and the dark star.",
        "keywords": [
            "minigames",
            "mascot",
            "2.5d",
            "side-scrolling",
            "fairy",
            "multiple endings",
            "kid friendly",
            "silent protagonist",
            "anthropomorphism",
            "polygonal 3d",
            "melee",
            "moving platforms",
            "shape-shifting",
            "auto-scrolling levels",
            "sliding down ladders",
            "whale",
            "fireworks",
            "collection marathon",
            "retroachievements"
        ],
        "release_date": "2000"
    },
    "Kirby's Dream Land 3": {
        "igdb_id": "3720",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co25su.jpg",
        "world_name": "Kirby's Dream Land 3",
        "igdb_name": "kirby's dream land 3",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "super famicom"
        ],
        "storyline": "",
        "keywords": [
            "mascot",
            "side-scrolling",
            "melee",
            "shape-shifting",
            "whale",
            "retroachievements"
        ],
        "release_date": "1997"
    },
    "Kingdom Hearts": {
        "igdb_id": "1219",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co30zf.jpg",
        "world_name": "Kingdom Hearts",
        "igdb_name": "kingdom hearts",
        "rating": [
            "violence",
            "cartoon violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "playstation 2"
        ],
        "storyline": "when his world is destroyed and his friends mysteriously disappear, a young boy named sora is thrust into a quest to find his missing friends and prevent the armies of darkness from destroying many other worlds. during his quest, he meets many characters from classic disney films and a handful from the final fantasy video game series.",
        "keywords": [
            "pirates",
            "grinding",
            "minigames",
            "summoning support",
            "death",
            "action-adventure",
            "crossover",
            "backtracking",
            "multiple endings",
            "princess",
            "swimming",
            "sword & sorcery",
            "anthropomorphism",
            "alternate costumes",
            "leveling up",
            "voice acting",
            "cat",
            "polygonal 3d",
            "damsel in distress",
            "party system",
            "save point",
            "potion",
            "melee",
            "real-time combat",
            "underwater gameplay",
            "a.i. companion",
            "stat tracking",
            "villain",
            "recurring boss",
            "water level",
            "invisible wall",
            "plot twist",
            "villain turned good",
            "spiky-haired protagonist",
            "gliding",
            "random encounter",
            "whale"
        ],
        "release_date": "2002"
    },
    "Kingdom Hearts 2": {
        "igdb_id": "1221",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co30t1.jpg",
        "world_name": "Kingdom Hearts 2",
        "igdb_name": "kingdom hearts ii",
        "rating": [
            "mild blood",
            "violence",
            "use of alcohol"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 3",
            "playstation 4",
            "playstation 2"
        ],
        "storyline": "one year after the events of kingdom hearts: chain of memories, sora, donald and goofy awaken in twilight town. bent on the quest to find riku and king mickey mouse, the three begin their journey. however, they soon discover that while they have been asleep, the heartless are back. not only that, but new enemies also showed up during their absence. sora, donald and goofy set off on a quest to rid the world of the heartless once more, uncovering the many secrets that linger about ansem and the mysterious organization xiii.",
        "keywords": [],
        "release_date": "2005"
    },
    "Link's Awakening DX": {
        "igdb_id": "1027",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4o47.jpg",
        "world_name": "Link's Awakening DX",
        "igdb_name": "the legend of zelda: link's awakening dx",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "game boy color",
            "nintendo 3ds"
        ],
        "storyline": "after the events of a link to the past, the hero link travels by ship to other countries to train for further threats. after being attacked at sea, link's ship sinks and he finds himself stranded on koholint island. he awakens to see a beautiful woman looking down at him and soon learns the island has a giant egg on top of a mountain that the wind fish inhabits deep inside. link is told to awaken the wind fish and all will be answered, so he sets out on another quest.",
        "keywords": [
            "magic",
            "mascot",
            "fishing",
            "death",
            "maze",
            "action-adventure",
            "fairy",
            "backtracking",
            "undead",
            "campaign",
            "princess",
            "pixel art",
            "easter egg",
            "silent protagonist",
            "sword & sorcery",
            "darkness",
            "digital distribution",
            "monkey",
            "world map",
            "human",
            "bow and arrow",
            "breaking the fourth wall",
            "disorientation zone",
            "side quests",
            "potion",
            "real-time combat",
            "walking through walls",
            "moving platforms",
            "tentacles",
            "fetch quests",
            "animal cruelty",
            "status effects",
            "another world"
        ],
        "release_date": "1998"
    },
    "Landstalker - The Treasures of King Nole": {
        "igdb_id": "15072",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kb9.jpg",
        "world_name": "Landstalker - The Treasures of King Nole",
        "igdb_name": "landstalker",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox"
        ],
        "platforms": [
            "linux",
            "wii",
            "sega mega drive/genesis",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "action-adventure",
            "fairy",
            "leveling up",
            "real-time combat"
        ],
        "release_date": "1992"
    },
    "Lethal Company": {
        "igdb_id": "212089",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5ive.jpg",
        "world_name": "Lethal Company",
        "igdb_name": "lethal company",
        "rating": [],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "indie"
        ],
        "themes": [
            "action",
            "science fiction",
            "horror",
            "comedy"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "you are a contracted worker for the company. your job is to collect scrap from abandoned, industrialized moons to meet the company's profit quota. you can use the cash you earn to travel to new moons with higher risks and rewards--or you can buy fancy suits and decorations for your ship. experience nature, scanning any creature you find to add them to your bestiary. explore the wondrous outdoors and rummage through their derelict, steel and concrete underbellies. just never miss the quota.",
        "keywords": [
            "aliens",
            "exploration",
            "monsters",
            "psychological horror",
            "survival horror"
        ],
        "release_date": "2023"
    },
    "Lingo": {
        "igdb_id": "189169",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5iy5.jpg",
        "world_name": "Lingo",
        "igdb_name": "lingo",
        "rating": [],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "puzzle",
            "adventure"
        ],
        "themes": [
            "open world"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "exploration",
            "3d"
        ],
        "release_date": "2021"
    },
    "Lufia II Ancient Cave": {
        "igdb_id": "1178",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9mg3.jpg",
        "world_name": "Lufia II Ancient Cave",
        "igdb_name": "lufia ii: rise of the sinistrals",
        "rating": [
            "mild animated violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "super famicom"
        ],
        "storyline": "",
        "keywords": [
            "retroachievements"
        ],
        "release_date": "1995"
    },
    "Luigi's Mansion": {
        "igdb_id": "2485",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wr1.jpg",
        "world_name": "Luigi's Mansion",
        "igdb_name": "luigi's mansion",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "adventure"
        ],
        "themes": [
            "action",
            "horror",
            "comedy"
        ],
        "platforms": [
            "nintendo gamecube"
        ],
        "storyline": "one day, luigi received an unexpected message: you've won a huge mansion! naturally, he[sic] got very excited and called his brother, mario. \"mario? it's me, luigi. i won myself a big mansion! meet me there and we'll celebrate, what do you say?\"\n\nluigi tried to follow the map to his new mansion, but the night was dark, and he became hopelessly lost in an eerie forest along the way. finally, he came upon a gloomy mansion on the edge of the woods. according to the map, this mansion seemed to be the one luigi was looking for. as soon as luigi set foot in the mansion, he started to feel nervous. mario, who should have arrived first, was nowhere to be seen. not only that, but there were ghosts in the mansion!\n\nsuddenly, a ghost lunged at luigi! \"mario! help meee!\" that's when a strange old man with a vacuum cleaner on his back appeared out of nowhere! this strange fellow managed to rescue luigi from the ghosts, then the two of them escaped...\n\nit just so happened that the old man, professor elvin gadd, who lived near the house, was researching his favorite subject, ghosts. luigi told professor e. gadd that his brother mario was missing, so the professor decided to give luigi two inventions that would help him search for his brother.\n\nluigi's not exactly known for his bravery. can he get rid of all the prank-loving ghosts and find mario?",
        "keywords": [
            "ghosts",
            "3d",
            "death",
            "action-adventure",
            "darkness",
            "polygonal 3d",
            "descendants of other characters",
            "save point",
            "stereoscopic 3d",
            "italian accent",
            "interconnected-world"
        ],
        "release_date": "2001"
    },
    "Super Mario Land 2": {
        "igdb_id": "1071",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7gxg.jpg",
        "world_name": "Super Mario Land 2",
        "igdb_name": "super mario land 2: 6 golden coins",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "nintendo 3ds",
            "game boy"
        ],
        "storyline": "danger! danger!\n\nwhile i was away crusading against the mystery alien tatanga in sarasa land, an evil creep took over my castle and put the people of mario land under his control with a magic spell. this intruder goes by the name of wario. he mimics my appearance, and has tried to steal my castle many times. it seems he has succeeded this time.\n\nwario has scattered the 6 golden coins from my castle all over mario land. these golden coins are guarded by those under wario's spell. without these coins, we can't get into the castle to deal with wario. we must collect the 6 coins, attack wario in the castle, and save everybody!\n\nit\u2019s time to set out on our mission!!",
        "keywords": [
            "space",
            "mario",
            "turtle",
            "whale"
        ],
        "release_date": "1992"
    },
    "Hatsune Miku Project Diva Mega Mix+": {
        "igdb_id": "120278",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co991n.jpg",
        "world_name": "Hatsune Miku Project Diva Mega Mix+",
        "igdb_name": "hatsune miku: project diva mega mix",
        "rating": [
            "blood",
            "sexual themes",
            "violence"
        ],
        "player_perspectives": [
            "third person",
            "side view"
        ],
        "genres": [
            "music",
            "arcade"
        ],
        "themes": [],
        "platforms": [
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2020"
    },
    "The Messenger": {
        "igdb_id": "71628",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2hr9.jpg",
        "world_name": "The Messenger",
        "igdb_name": "the messenger",
        "rating": [
            "fantasy violence",
            "language",
            "crude humor"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "retro",
            "ninja",
            "2d",
            "metroidvania",
            "difficult",
            "pixel graphics"
        ],
        "release_date": "2018"
    },
    "Metroid Prime": {
        "igdb_id": "1105",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3w4w.jpg",
        "world_name": "Metroid Prime",
        "igdb_name": "metroid prime",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "shooter",
            "platform",
            "puzzle",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "open world"
        ],
        "platforms": [
            "nintendo gamecube"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "pirates",
            "ghosts",
            "exploration",
            "bloody",
            "gravity",
            "metroidvania",
            "death",
            "spaceship",
            "female protagonist",
            "action-adventure",
            "backtracking",
            "time limit",
            "multiple endings",
            "artificial intelligence",
            "snow",
            "explosion",
            "countdown timer",
            "world map",
            "polygonal 3d",
            "damsel in distress",
            "upgradeable weapons",
            "save point",
            "ice stage",
            "falling damage",
            "unstable platforms",
            "auto-aim",
            "real-time combat",
            "underwater gameplay",
            "difficulty level",
            "multiple gameplay perspectives",
            "mercenary",
            "violent plants",
            "moving platforms",
            "sequence breaking",
            "shape-shifting",
            "tentacles",
            "western games based on japanese ips",
            "speedrun",
            "boss assistance",
            "fetch quests",
            "completion percentage",
            "linear gameplay",
            "meme origin",
            "ancient advanced civilization technology",
            "ambient music",
            "creature compendium",
            "isolation"
        ],
        "release_date": "2002"
    },
    "Minecraft": {
        "igdb_id": "121",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8fu6.jpg",
        "world_name": "Minecraft",
        "igdb_name": "minecraft: java edition",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "first person",
            "third person",
            "virtual reality"
        ],
        "genres": [
            "simulator",
            "adventure"
        ],
        "themes": [
            "fantasy",
            "survival",
            "sandbox",
            "kids",
            "open world"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "minecraft: java edition (previously known as minecraft) is the original version of minecraft, developed by mojang studios for windows, macos, and linux. notch began development on may 10, 2009, publicly releasing minecraft on may 17, 2009. the full release of the game was on november 18, 2011, at minecon 2011.",
        "keywords": [
            "monsters",
            "construction",
            "fishing",
            "crafting",
            "death",
            "procedural generation",
            "horse",
            "action-adventure",
            "achievements",
            "traps",
            "snow",
            "wolf",
            "mining",
            "swimming",
            "day/night cycle",
            "darkness",
            "explosion",
            "digital distribution",
            "spider",
            "cat",
            "polygonal 3d",
            "bow and arrow",
            "deliberately retro",
            "humble bundle",
            "falling damage",
            "stereoscopic 3d",
            "potion",
            "auto-saving",
            "real-time combat",
            "difficulty level",
            "multiple gameplay perspectives",
            "rpg elements",
            "sleeping",
            "meme origin",
            "fire manipulation",
            "bees"
        ],
        "release_date": "2011"
    },
    "Mario Kart 64": {
        "igdb_id": "2342",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co67hm.jpg",
        "world_name": "Mario Kart 64",
        "igdb_name": "mario kart 64",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "racing",
            "arcade"
        ],
        "themes": [
            "action",
            "kids",
            "party"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "",
        "keywords": [
            "crossover",
            "princess",
            "artificial intelligence",
            "snow",
            "sequel",
            "bats",
            "turtle",
            "explosion",
            "anthropomorphism",
            "monkey",
            "polygonal 3d",
            "ice stage",
            "difficulty level",
            "invisible wall",
            "temporary invincibility",
            "time trials",
            "italian accent",
            "ape",
            "retroachievements"
        ],
        "release_date": "1996"
    },
    "Mario & Luigi Superstar Saga": {
        "igdb_id": "3351",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co21rg.jpg",
        "world_name": "Mario & Luigi Superstar Saga",
        "igdb_name": "mario & luigi: superstar saga",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "turn-based",
            "multiple protagonists",
            "undead",
            "princess",
            "giant insects",
            "silent protagonist",
            "mario",
            "turtle",
            "spiritual successor",
            "digital distribution",
            "anthropomorphism",
            "super-ness",
            "shopping",
            "breaking the fourth wall",
            "party system",
            "save point",
            "royalty",
            "self-referential humor",
            "rpg elements",
            "tentacles",
            "fireworks",
            "italian accent",
            "battle screen",
            "wiggler",
            "princess peach"
        ],
        "release_date": "2003"
    },
    "Mega Man 2": {
        "igdb_id": "1734",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5572.jpg",
        "world_name": "Mega Man 2",
        "igdb_name": "mega man ii",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "nintendo 3ds",
            "game boy"
        ],
        "storyline": "even after his crushing defeat at the hands of mega man during the events of mega man: dr. wily's revenge, dr. wily was already planning his next scheme. if he could get his hands on the time machine (named time skimmer in the american manual) that was being developed at the time-space research laboratory (named chronos institute in the american manual), he thought he just might be able to change the past.\n\nafter stealing the time machine, wily had wanted to set out immediately on a trip across time, but had to put an emergency brake down on his plans when he discovered that the time machine had a serious flaw.\n\nmeanwhile, dr. light had been dispatched to the time-space laboratory to investigate. with the help of rush\u2019s super-sense of smell, he was able to deduce that it was none other than dr. wily behind the theft. having a bad feeling about the incident, dr. light quickly called upon mega man and rush to search out dr. wily\u2019s whereabouts.",
        "keywords": [
            "mascot",
            "death",
            "robots",
            "flight",
            "side-scrolling",
            "pixel art",
            "sequel",
            "explosion",
            "psone classics",
            "upgradeable weapons",
            "checkpoints",
            "underwater gameplay",
            "male antagonist",
            "instant kill",
            "difficulty level",
            "moving platforms",
            "conveyor belt",
            "villain",
            "water level",
            "monomyth"
        ],
        "release_date": "1991"
    },
    "MegaMan Battle Network 3": {
        "igdb_id": "1758",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co203k.jpg",
        "world_name": "MegaMan Battle Network 3",
        "igdb_name": "mega man battle network 3 blue",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2002"
    },
    "Majora's Mask Recompiled": {
        "igdb_id": "1030",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3pah.jpg",
        "world_name": "Majora's Mask Recompiled",
        "igdb_name": "the legend of zelda: majora's mask",
        "rating": [
            "animated violence",
            "cartoon violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "horror",
            "open world"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "64dd",
            "wii u"
        ],
        "storyline": "after the events of the legend of zelda: ocarina of time, link departs on his horse epona in the lost woods and is assaulted by an imp named skull kid who dons a mysterious mask, accompanied by the fairies tael and tatl. skull kid turns link into a small plant-like creature known as deku scrub and takes away his horse and his magical ocarina. shortly afterward, tatl joins link and agrees to help him revert to his native form. a meeting with a wandering mask salesman reveals that the skull kid is wearing majora's mask, an ancient item used in hexing rituals, which calls forth a menacing moon hovering over the land of termina. link has exactly three days to find a way to prevent this from happening.",
        "keywords": [
            "psychological horror",
            "time travel",
            "archery",
            "action-adventure",
            "fairy",
            "sequel",
            "day/night cycle",
            "sword & sorcery",
            "descendants of other characters",
            "sprinting mechanics",
            "auto-aim",
            "shape-shifting",
            "dimension travel",
            "boss assistance",
            "meme origin",
            "living inventory",
            "another world",
            "retroachievements"
        ],
        "release_date": "2000"
    },
    "Momodora Moonlit Farewell": {
        "igdb_id": "188088",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7mxs.jpg",
        "world_name": "Momodora Moonlit Farewell",
        "igdb_name": "momodora: moonlit farewell",
        "rating": [
            "fantasy violence",
            "blood",
            "suggestive themes"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5",
            "nintendo switch"
        ],
        "storyline": "momodora: moonlit farewell presents the account of the greatest calamity to befall the village of koho, five years after the events of momodora iii. once the toll of an ominous bell is heard, the village is soon threatened by a demon invasion.\n\nthe village's matriarch sends momo reinol, their most capable priestess, to investigate the bell and find the bellringer responsible for summoning demons. it is their hope that by finding the culprit, they will also be able to secure the village's safety, and most importantly, the sacred lun tree's, a source of life and healing for koho...",
        "keywords": [
            "metroidvania",
            "pixel graphics"
        ],
        "release_date": "2024"
    },
    "Monster Sanctuary": {
        "igdb_id": "89594",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1q3q.jpg",
        "world_name": "Monster Sanctuary",
        "igdb_name": "monster sanctuary",
        "rating": [
            "fantasy violence",
            "mild blood",
            "tobacco reference"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "strategy",
            "turn-based strategy (tbs)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "metroidvania"
        ],
        "release_date": "2020"
    },
    "Muse Dash": {
        "igdb_id": "86316",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6h43.jpg",
        "world_name": "Muse Dash",
        "igdb_name": "muse dash",
        "rating": [
            "sexual themes",
            "mild blood",
            "mild lyrics",
            "fantasy violence",
            "suggestive themes"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "music",
            "indie"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "anime",
            "casual",
            "2d",
            "side-scrolling",
            "achievements",
            "cute",
            "nudity",
            "digital distribution",
            "difficulty level"
        ],
        "release_date": "2018"
    },
    "Metroid Zero Mission": {
        "igdb_id": "1107",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1vci.jpg",
        "world_name": "Metroid Zero Mission",
        "igdb_name": "metroid: zero mission",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "open world"
        ],
        "platforms": [
            "wii u",
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "pirates",
            "gravity",
            "collecting",
            "metroidvania",
            "death",
            "maze",
            "spaceship",
            "female protagonist",
            "side-scrolling",
            "backtracking",
            "multiple endings",
            "pixel art",
            "wall jump",
            "explosion",
            "countdown timer",
            "upgradeable weapons",
            "save point",
            "difficulty level",
            "rpg elements",
            "sequence breaking",
            "completion percentage",
            "ambient music",
            "isolation",
            "interconnected-world"
        ],
        "release_date": "2004"
    },
    "Noita": {
        "igdb_id": "52006",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qp1.jpg",
        "world_name": "Noita",
        "igdb_name": "noita",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "shooter",
            "role-playing (rpg)",
            "simulator",
            "adventure",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "magic",
            "pixel graphics",
            "roguelite"
        ],
        "release_date": "2020"
    },
    "Ocarina of Time": {
        "igdb_id": "1029",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3nnx.jpg",
        "world_name": "Ocarina of Time",
        "igdb_name": "the legend of zelda: ocarina of time",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "64dd",
            "wii u"
        ],
        "storyline": "a young boy named link was raised in the village of the elf-like kokiri people. one day a fairy named navi introduces him to the village's guardian, the great deku tree. it appears that a mysterious man has cursed the tree, and link is sent to the hyrule castle to find out more. princess zelda tells link that ganondorf, the leader of the gerudo tribe, seeks to obtain the triforce, a holy relic that grants immense power to the one who possesses it. link must do everything in his power to obtain the triforce before ganondorf does, and save hyrule.",
        "keywords": [
            "gravity",
            "time travel",
            "minigames",
            "death",
            "horse",
            "archery",
            "time manipulation",
            "action-adventure",
            "religion",
            "fairy",
            "backtracking",
            "undead",
            "campaign",
            "princess",
            "dog",
            "sequel",
            "silent protagonist",
            "swimming",
            "day/night cycle",
            "sword & sorcery",
            "block puzzle",
            "countdown timer",
            "world map",
            "polygonal 3d",
            "bow and arrow",
            "damsel in distress",
            "game reference",
            "cameo appearance",
            "disorientation zone",
            "descendants of other characters",
            "sprinting mechanics",
            "ice stage",
            "falling damage",
            "side quests",
            "auto-aim",
            "real-time combat",
            "underwater gameplay",
            "walking through walls",
            "mercenary",
            "coming of age",
            "sequence breaking",
            "villain",
            "been here before",
            "water level",
            "invisible wall",
            "plot twist",
            "boss assistance",
            "androgyny",
            "animal cruelty",
            "resized enemy",
            "time paradox",
            "fast traveling",
            "censored version",
            "context sensitive",
            "living inventory",
            "damage over time",
            "color cartridges",
            "retroachievements",
            "popular"
        ],
        "release_date": "1998"
    },
    "OpenRCT2": {
        "igdb_id": "80720",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ngq.jpg",
        "world_name": "OpenRCT2",
        "igdb_name": "openrct2",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "real time strategy (rts)",
            "simulator",
            "strategy"
        ],
        "themes": [
            "business",
            "4x (explore, expand, exploit, and exterminate)"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "death",
            "maze",
            "kid friendly",
            "easter egg",
            "explosion",
            "kidnapping"
        ],
        "release_date": "2014"
    },
    "Ori and the Blind Forest": {
        "igdb_id": "7344",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1y41.jpg",
        "world_name": "Ori and the Blind Forest",
        "igdb_name": "ori and the blind forest",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "thriller"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "ori, the protagonist of the game, falls from the spirit tree and is adopted by naru, who raises ori as her own. when a disastrous event occurs causing the forest to wither and naru to die, ori is left to explore the forest. ori eventually encounters sein, who begins to guide ori on an adventure to restore the forest through the recovery of the light of three main elements supporting the balance of the forest: waters, winds and warmth.",
        "keywords": [
            "metroidvania",
            "achievements",
            "wall jump",
            "digital distribution",
            "spider",
            "unstable platforms",
            "rpg elements",
            "coming of age"
        ],
        "release_date": "2015"
    },
    "Old School Runescape": {
        "igdb_id": "79824",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mo1.jpg",
        "world_name": "Old School Runescape",
        "igdb_name": "old school runescape",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "text"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "fantasy",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "grinding"
        ],
        "release_date": "2013"
    },
    "osu!": {
        "igdb_id": "3012",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8a4m.jpg",
        "world_name": "osu!",
        "igdb_name": "osu!",
        "rating": [],
        "player_perspectives": [
            "auditory"
        ],
        "genres": [
            "music",
            "indie",
            "arcade"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "anime",
            "stat tracking",
            "difficulty level"
        ],
        "release_date": "2007"
    },
    "Outer Wilds": {
        "igdb_id": "11737",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co65ac.jpg",
        "world_name": "Outer Wilds",
        "igdb_name": "outer wilds",
        "rating": [
            "fantasy violence",
            "alcohol reference"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "puzzle",
            "simulator",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "science fiction",
            "open world",
            "mystery"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "welcome to the space program! you're the newest recruit of outer wilds ventures, a fledgling space program searching for answers in a strange, constantly evolving solar system. what lurks in the heart of the ominous dark bramble? who built the alien ruins on the moon? can the endless time loop be stopped? answers await you in the most dangerous reaches of space.\n\nthe planets of outer wilds are packed with hidden locations that change with the passage of time. visit an underground city of before it's swallowed by sand, or explore the surface of a planet as it crumbles beneath your feet. every secret is guarded by hazardous environments and natural catastrophes.\n\nstrap on your hiking boots, check your oxygen levels, and get ready to venture into space. use a variety of unique gadgets to probe your surroundings, track down mysterious signals, decipher ancient alien writing, and roast the perfect marshmallow.",
        "keywords": [
            "exploration",
            "time travel"
        ],
        "release_date": "2019"
    },
    "Overcooked! 2": {
        "igdb_id": "103341",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1usu.jpg",
        "world_name": "Overcooked! 2",
        "igdb_name": "overcooked! 2",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "simulator",
            "strategy",
            "tactical",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "comedy",
            "kids",
            "party"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "you can pet the dog"
        ],
        "release_date": "2018"
    },
    "Paint": {
        "igdb_id": "",
        "world_name": "Paint",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer",
            "puzzle"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Paper Mario": {
        "igdb_id": "3340",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qda.jpg",
        "world_name": "Paper Mario",
        "igdb_name": "paper mario",
        "rating": [
            "comic mischief"
        ],
        "player_perspectives": [
            "third person",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "gravity",
            "mascot",
            "turn-based",
            "death",
            "maze",
            "gambling",
            "undead",
            "princess",
            "easter egg",
            "silent protagonist",
            "turtle",
            "snowman",
            "spiritual successor",
            "anthropomorphism",
            "leveling up",
            "human",
            "damsel in distress",
            "breaking the fourth wall",
            "party system",
            "save point",
            "melee",
            "self-referential humor",
            "moving platforms",
            "villain",
            "recurring boss",
            "sleeping",
            "tentacles",
            "temporary invincibility",
            "boss assistance",
            "poisoning",
            "invisibility",
            "fire manipulation",
            "battle screen",
            "retroachievements"
        ],
        "release_date": "2000"
    },
    "Peaks of Yore": {
        "igdb_id": "238690",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8zzc.jpg",
        "world_name": "Peaks of Yore",
        "igdb_name": "peaks of yore",
        "rating": [],
        "player_perspectives": [],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2023"
    },
    "Pokemon Mystery Dungeon Explorers of Sky": {
        "igdb_id": "2323",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7ovf.jpg",
        "world_name": "Pokemon Mystery Dungeon Explorers of Sky",
        "igdb_name": "pok\u00e9mon mystery dungeon: explorers of sky",
        "rating": [
            "mild cartoon violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)"
        ],
        "themes": [
            "fantasy",
            "kids"
        ],
        "platforms": [
            "wii u",
            "nintendo ds"
        ],
        "storyline": "",
        "keywords": [
            "time travel",
            "roguelike",
            "jrpg"
        ],
        "release_date": "2009"
    },
    "Pokemon Crystal": {
        "igdb_id": "1514",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pil.jpg",
        "world_name": "Pokemon Crystal",
        "igdb_name": "pok\u00e9mon crystal version",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "kids"
        ],
        "platforms": [
            "game boy color",
            "nintendo 3ds"
        ],
        "storyline": "",
        "keywords": [
            "exploration",
            "anime",
            "collecting",
            "minigames",
            "turn-based",
            "gambling",
            "kid friendly",
            "teleportation",
            "bats",
            "day/night cycle",
            "leveling up",
            "world map",
            "shopping",
            "party system",
            "sprinting mechanics",
            "side quests",
            "pick your gender",
            "potion",
            "melee",
            "coming of age",
            "punctuation mark above head",
            "been here before",
            "sleeping",
            "tentacles",
            "animal cruelty",
            "poisoning",
            "random encounter",
            "fire manipulation",
            "battle screen",
            "status effects",
            "damage over time",
            "color cartridges"
        ],
        "release_date": "2000"
    },
    "Pokemon Emerald": {
        "igdb_id": "1517",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1zhr.jpg",
        "world_name": "Pokemon Emerald",
        "igdb_name": "pok\u00e9mon emerald version",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "kids"
        ],
        "platforms": [
            "game boy advance"
        ],
        "storyline": "both team magma and team aqua are featured as the villainous teams, each stirring trouble at different stages in the game. the objective of each team, to awaken groudon and kyogre, respectively, is eventually fulfilled.\nrayquaza is prominent plot-wise, awakened in order to stop the destructive battle between groudon and kyogre. it is now the one out of the three ancient pok\u00e9mon that can be caught prior to the elite four challenge, while still at the same place and at the same high level as in ruby and sapphire.",
        "keywords": [
            "exploration",
            "anime",
            "collecting",
            "minigames",
            "turn-based",
            "gambling",
            "bird",
            "kid friendly",
            "teleportation",
            "giant insects",
            "silent protagonist",
            "leveling up",
            "shopping",
            "party system",
            "sprinting mechanics",
            "side quests",
            "pick your gender",
            "potion",
            "melee",
            "coming of age",
            "punctuation mark above head",
            "recurring boss",
            "tentacles",
            "animal cruelty",
            "poisoning",
            "random encounter",
            "fire manipulation",
            "fast traveling",
            "battle screen",
            "creature compendium",
            "status effects",
            "damage over time",
            "color cartridges"
        ],
        "release_date": "2004"
    },
    "Pokemon FireRed and LeafGreen": {
        "igdb_id": "1516",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1zip.jpg",
        "world_name": "Pokemon FireRed and LeafGreen",
        "igdb_name": "pok\u00e9mon leafgreen version",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction",
            "kids"
        ],
        "platforms": [
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "monsters",
            "collecting",
            "popular"
        ],
        "release_date": "2004"
    },
    "Pokemon Red and Blue": {
        "igdb_id": "1561",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pi4.jpg",
        "world_name": "Pokemon Red and Blue",
        "igdb_name": "pok\u00e9mon red version",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "kids",
            "open world"
        ],
        "platforms": [
            "nintendo 3ds",
            "game boy"
        ],
        "storyline": "the player character starts out in pallet town. when the player character tries to leave the town without a pok\u00e9mon of their own, they are stopped in the nick of time by professor oak, who invites them to his lab. there, he gives them a pok\u00e9mon of their own and a pok\u00e9dex, telling them about his dream to make a complete guide on every pok\u00e9mon in the world. after the player character battles their rival and leaves the lab, they are entitled to win every gym badge, compete in the pok\u00e9mon league, and fulfill oak's dream by catching every pok\u00e9mon.",
        "keywords": [
            "collecting"
        ],
        "release_date": "1996"
    },
    "Pseudoregalia": {
        "igdb_id": "259465",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6vcy.jpg",
        "world_name": "Pseudoregalia",
        "igdb_name": "pseudoregalia: jam ver.",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "metroidvania"
        ],
        "release_date": "2023"
    },
    "Ratchet & Clank 2": {
        "igdb_id": "1770",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co230n.jpg",
        "world_name": "Ratchet & Clank 2",
        "igdb_name": "ratchet & clank: going commando",
        "rating": [
            "animated blood",
            "comic mischief",
            "fantasy violence",
            "mild language"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "shooter",
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "comedy"
        ],
        "platforms": [
            "playstation 2"
        ],
        "storyline": "having defeated chairman drek in their last intergalactic adventure, ratchet and clank find themselves returning to a more sedate lifestyle. that is, until they are approached by abercrombie fizzwidget, the cro of megacorp, who needs the duo to track down the company\u2019s most promising experimental project, which has been stolen by a mysterious masked figure. initially, the mission seemed like a sunday stroll in the park, but we soon find our heroes entangled in a colossal struggle for control of the galaxy. along the way, the duo unleashes some of the coolest weapons and gadgets ever invented upon the most dangerous foes they have ever faced. ratchet and clanks set out to destroy anything and anyone who stands in their way of discovering the secrets that lie behind \u201cthe experiment.\u201d",
        "keywords": [],
        "release_date": "2003"
    },
    "Raft": {
        "igdb_id": "27082",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1xdc.jpg",
        "world_name": "Raft",
        "igdb_name": "raft",
        "rating": [
            "violence",
            "blood"
        ],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "simulator",
            "adventure",
            "indie"
        ],
        "themes": [
            "survival"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5"
        ],
        "storyline": "trapped on a small raft with nothing but a hook made of old plastic, players awake on a vast, blue ocean totally alone and with no land in sight! with a dry throat and an empty stomach, survival will not be easy!\n\nresources are tough to come by at sea: players will have to make sure to catch whatever debris floats by using their trusty hook and when possible, scavenge the reefs beneath the waves and the islands above. however, thirst and hunger is not the only danger in the ocean\u2026 watch out for the man-eating shark determined to end your voyage!",
        "keywords": [
            "shark",
            "crafting",
            "bees"
        ],
        "release_date": "2022"
    },
    "Resident Evil 2 Remake": {
        "igdb_id": "19686",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ir3.jpg",
        "world_name": "Resident Evil 2 Remake",
        "igdb_name": "resident evil 2",
        "rating": [
            "strong language",
            "intense violence",
            "blood and gore"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "shooter",
            "adventure"
        ],
        "themes": [
            "action",
            "horror",
            "survival"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "ios",
            "playstation 5",
            "mac",
            "xbox one"
        ],
        "storyline": "players join rookie police officer leon kennedy and college student claire redfield, who are thrust together by a disastrous outbreak in raccoon city that transformed its population into deadly zombies. both leon and claire have their own separate playable campaigns, allowing players to see the story from both characters\u2019 perspectives. the fate of these two fan favorite characters is in the player's hands as they work together to survive and get to the bottom of what is behind the terrifying attack on the city.",
        "keywords": [
            "bloody",
            "survival horror",
            "censored version"
        ],
        "release_date": "2019"
    },
    "Resident Evil 3 Remake": {
        "igdb_id": "115115",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co22l7.jpg",
        "world_name": "Resident Evil 3 Remake",
        "igdb_name": "resident evil 3",
        "rating": [
            "intense violence",
            "strong language",
            "blood and gore"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "shooter",
            "adventure"
        ],
        "themes": [
            "action",
            "horror",
            "survival"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "ios",
            "playstation 5",
            "mac",
            "xbox one"
        ],
        "storyline": "a series of strange disappearances have been occurring in the american midwest within a place called racoon city. a specialist squad of the police force known as s.t.a.r.s. has been investigating the case, and have determined that the pharmaceutical company umbrella and their biological weapon, the t-virus, are behind the incidents. jill valentine and the other surviving s.t.a.r.s. members try to make this truth known, but find that the police department itself is under umbrella's sway and their reports are rejected out of hand. with the viral plague spreading through the town and to her very doorstep, jill is determined to survive. however, an extremely powerful pursuer has already been dispatched to eliminate her.",
        "keywords": [
            "survival horror"
        ],
        "release_date": "2020"
    },
    "Rogue Legacy": {
        "igdb_id": "3221",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co27fi.jpg",
        "world_name": "Rogue Legacy",
        "igdb_name": "rogue legacy",
        "rating": [
            "fantasy violence",
            "crude humor"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle",
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "playstation 3",
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "playstation vita",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "exploration",
            "medieval",
            "ninja",
            "magic",
            "minigames",
            "16-bit",
            "roguelike",
            "metroidvania",
            "death",
            "procedural generation",
            "horse",
            "gambling",
            "time manipulation",
            "female protagonist",
            "flight",
            "action-adventure",
            "side-scrolling",
            "multiple protagonists",
            "bird",
            "time limit",
            "traps",
            "pixel art",
            "wolf",
            "pixel graphics",
            "easter egg",
            "teleportation",
            "darkness",
            "explosion",
            "digital distribution",
            "countdown timer",
            "bow and arrow",
            "breaking the fourth wall",
            "game reference",
            "descendants of other characters",
            "royalty",
            "potion",
            "stat tracking",
            "secret area",
            "shielded enemies",
            "violent plants",
            "punctuation mark above head",
            "temporary invincibility",
            "boss assistance",
            "fire manipulation",
            "resized enemy",
            "lgbtq+"
        ],
        "release_date": "2013"
    },
    "Risk of Rain": {
        "igdb_id": "3173",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2k2z.jpg",
        "world_name": "Risk of Rain",
        "igdb_name": "risk of rain",
        "rating": [
            "alcohol reference",
            "fantasy violence",
            "mild blood",
            "mild language"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "role-playing (rpg)",
            "hack and slash/beat 'em up",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction",
            "survival"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "playstation vita",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "roguelike",
            "difficult",
            "time limit",
            "pixel art",
            "steam greenlight",
            "crowdfunding",
            "bow and arrow",
            "crowd funded",
            "roguelite"
        ],
        "release_date": "2013"
    },
    "Risk of Rain 2": {
        "igdb_id": "28512",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2eu7.jpg",
        "world_name": "Risk of Rain 2",
        "igdb_name": "risk of rain 2",
        "rating": [
            "blood",
            "drug reference",
            "fantasy violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "shooter",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "science fiction",
            "survival"
        ],
        "platforms": [
            "google stadia",
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "risk of rain 2 follows the crew of ues: safe travels as they try to find ues: contact light and any survivors along their path. they have to try and survive the hostile wildlife and environment as difficulty increases over time, navigating petrichor v via the teleporters strewn across the entire planet. the crew loop endlessly through many distinct environments, but end upon the moon to defeat the final boss.\n\nwith each run, you\u2019ll learn the patterns of your foes, and even the longest odds can be overcome with enough skill. a unique scaling system means both you and your foes limitlessly increase in power over the course of a game\u2013what once was a bossfight will in time become a common enemy.\n\nmyriad survivors, items, enemies, and bosses return to risk 2, and many new ones are joining the fight. brand new survivors like the artificer and mul-t debut alongside classic survivors such as the engineer, huntress, and\u2013of course\u2013the commando. with over 75 items to unlock and exploit, each run will keep you cleverly strategizing your way out of sticky situations.",
        "keywords": [
            "roguelite"
        ],
        "release_date": "2019"
    },
    "Sonic Adventure 2 Battle": {
        "igdb_id": "192194",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5p3o.jpg",
        "world_name": "Sonic Adventure 2 Battle",
        "igdb_name": "sonic adventure 2: battle",
        "rating": [
            "mild lyrics",
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "playstation 3",
            "pc (microsoft windows)",
            "xbox 360"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2012"
    },
    "Sonic Adventure DX": {
        "igdb_id": "192114",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4iln.jpg",
        "world_name": "Sonic Adventure DX",
        "igdb_name": "sonic adventure: sonic adventure dx upgrade",
        "rating": [
            "animated violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "playstation 3",
            "pc (microsoft windows)",
            "xbox 360"
        ],
        "storyline": "doctor robotnik seeks a new way to defeat his longtime nemesis sonic and conquer the world. during his research, he learns about an entity called chaos\u2014a creature that, thousands of years ago, helped to protect the chao and the all-powerful master emerald, which balances the power of the seven chaos emeralds. when a tribe of echidnas sought to steal the power of the emeralds, breaking the harmony they had with the chao, chaos retaliated by using the emeralds' power to transform into a monstrous beast, perfect chaos, and wipe them out. before it could destroy the world, tikal, a young echidna who befriended chaos, imprisoned it in the master emerald along with herself. eggman releases chaos and sonic and his friends must act against eggman's plans and prevent the monster from becoming more powerful.",
        "keywords": [],
        "release_date": "2010"
    },
    "Starcraft 2": {
        "igdb_id": "239",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1tnn.jpg",
        "world_name": "Starcraft 2",
        "igdb_name": "starcraft ii: wings of liberty",
        "rating": [
            "blood and gore",
            "language",
            "suggestive themes",
            "use of alcohol and tobacco",
            "violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "real time strategy (rts)",
            "strategy"
        ],
        "themes": [
            "action",
            "science fiction",
            "warfare"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "space",
            "human",
            "side quests",
            "mercenary"
        ],
        "release_date": "2010"
    },
    "Sea of Thieves": {
        "igdb_id": "11137",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2558.jpg",
        "world_name": "Sea of Thieves",
        "igdb_name": "sea of thieves",
        "rating": [
            "crude humor",
            "use of alcohol",
            "violence"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "simulator",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "open world"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one"
        ],
        "storyline": "",
        "keywords": [
            "pirates",
            "exploration",
            "grinding",
            "crafting",
            "action-adventure",
            "digital distribution",
            "skeletons",
            "the game awards 2017",
            "you can pet the dog"
        ],
        "release_date": "2018"
    },
    "Not an idle game": {
        "igdb_id": "134826",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4tfx.jpg",
        "world_name": "Not an idle game",
        "igdb_name": "shapez",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "simulator",
            "strategy",
            "indie"
        ],
        "themes": [
            "sandbox"
        ],
        "platforms": [
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2020"
    },
    "Shivers": {
        "igdb_id": "12477",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7a5z.jpg",
        "world_name": "Shivers",
        "igdb_name": "shivers",
        "rating": [
            "realistic blood and gore",
            "realistic blood"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "point-and-click",
            "puzzle",
            "adventure",
            "indie"
        ],
        "themes": [
            "horror"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "1995"
    },
    "A Short Hike": {
        "igdb_id": "116753",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6e83.jpg",
        "world_name": "A Short Hike",
        "igdb_name": "a short hike",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "adventure",
            "indie"
        ],
        "themes": [
            "fantasy",
            "open world"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "the main character is claire, a young anthropomorphic bird who travels to hawk peak provincial park, where her aunt may works as a ranger, to spend days off. however, claire cannot get cellphone reception unless she reaches the top of the peak, and is expecting an important call. for this reason, she decides to reach the highest point in the park.",
        "keywords": [
            "exploration",
            "casual",
            "fishing",
            "female protagonist",
            "flight",
            "bird",
            "cute",
            "funny",
            "pixel graphics",
            "relaxing",
            "3d platformer",
            "great soundtrack"
        ],
        "release_date": "2019"
    },
    "The Sims 4": {
        "igdb_id": "3212",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3h3l.jpg",
        "world_name": "The Sims 4",
        "igdb_name": "the sims 4",
        "rating": [
            "sexual themes",
            "crude humor",
            "violence"
        ],
        "player_perspectives": [
            "first person",
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "simulator"
        ],
        "themes": [
            "action",
            "fantasy",
            "comedy",
            "sandbox",
            "romance"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "mac",
            "xbox one"
        ],
        "storyline": "choose how sims look, act, and dress. determine how they\u2019ll live out each day. design and build incredible homes for every family, then decorate with your favorite furnishings and d\u00e9cor. travel to different neighborhoods where you can meet other sims and learn about their lives. discover beautiful locations with distinctive environments, and go on spontaneous adventures. manage the ups and downs of sims\u2019 everyday lives and see what happens when you play out realistic or fantastical scenarios. tell your stories your way while developing relationships, pursuing careers and life aspirations, and immersing yourself in an extraordinary game where the possibilities are endless.",
        "keywords": [
            "casual",
            "management",
            "cute",
            "funny",
            "relaxing",
            "lgbtq+",
            "you can pet the dog"
        ],
        "release_date": "2014"
    },
    "Sly Cooper and the Thievius Raccoonus": {
        "igdb_id": "1798",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1p0r.jpg",
        "world_name": "Sly Cooper and the Thievius Raccoonus",
        "igdb_name": "sly cooper and the thievius raccoonus",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "stealth",
            "comedy"
        ],
        "platforms": [
            "playstation 2"
        ],
        "storyline": "sly cooper comes from a long line of master thieves (the cooper clan) who only steal from other criminals, thus making them vigilantes. the cooper family's heirloom, an ancient book by the name the thievius raccoonus, records all the secret moves and techniques from every member in the clan. on his 8th birthday, sly was supposed to inherit the book and learn all of his family's ancient secrets which was supposed to help him become a master thief, however, a group of thugs by the name \"the fiendish five\" (led by clockwerk, who is the arch-nemesis of the family clan) attack the cooper household and kills sly's parents and stole all of the pages from the thievius raccoonus. after that, the ruthless gang go their separate ways to commit dastardly crimes around the world. sly is sent to an orphanage where he meets and teams up and forms a gang with two guys who become his lifelong best friends, bentley, a technician, inventor and a talented mathematical hacker with encyclopedic knowledge who plays the role as the brains of the gang, and murray, a huge husky cowardly guy with a ginormous appetite who plays the role as the brawns and the getaway driver of the gang. the three leave the orphanage together at age 16 to start their lives becoming international vigilante criminals together, naming themselves \"the cooper gang\". sly swears one day to avenge his family and track down the fiendish five and steal back the thievius raccoonus. two years later, the cooper gang head to paris, france, to infiltrate itnerpol (a police headquarters) in order to find the secret police file which stores details and information about the fiendish five but during the heist they are ambushed by inspector carmelita fox (towards whom sly develops a romantic attraction), a police officer who is affiliated with interpol and is after the cooper gang. the gang manage to steal the police file and successfully escapes from her and the rest of the cops. with the secret police file finally in their hands, the cooper gang manage to track down the fiendish five.",
        "keywords": [
            "ghosts",
            "mascot",
            "death",
            "artificial intelligence",
            "dog",
            "talking animals",
            "climbing",
            "turtle",
            "anthropomorphism",
            "spider",
            "voice acting",
            "crocodile",
            "polygonal 3d",
            "skeletons",
            "descendants of other characters",
            "checkpoints",
            "unstable platforms",
            "stereoscopic 3d",
            "melee",
            "moving platforms",
            "gliding",
            "invisibility",
            "time trials",
            "fireworks"
        ],
        "release_date": "2002"
    },
    "Super Metroid": {
        "igdb_id": "1103",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5osy.jpg",
        "world_name": "Super Metroid",
        "igdb_name": "super metroid",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "thriller"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "after samus completed her mission and eradicated the entire metroid population on sr388 as commanded by the galactic federation (sans the metroid hatchling, which she nicknamed \"baby\"), she brought the hatchling to the ceres space colony for research. however, shortly after she left, she received a distress signal from the station and returned to investigate.\n\nwhen samus arrives at the space science academy where the baby was being studied, she finds all the scientists slaughtered and the containment unit that held the baby missing. upon further exploration of the station, she finds the baby in a small capsule. as she approaches, ridley appears and grabs the capsule. after a brief battle, samus repels ridley, and he activates a self-destruct sequence to destroy ceres.\n\nafter escaping the explosion, ridley flees to zebes, and samus goes after him.",
        "keywords": [
            "aliens",
            "exploration",
            "2d",
            "16-bit",
            "metroidvania",
            "time manipulation",
            "female protagonist",
            "action-adventure",
            "side-scrolling",
            "time limit",
            "pixel art",
            "wall jump",
            "darkness",
            "explosion",
            "countdown timer",
            "nintendo power",
            "damsel in distress",
            "save point",
            "unstable platforms",
            "real-time combat",
            "secret area",
            "liberation",
            "mercenary",
            "sequence breaking",
            "isolation",
            "interconnected-world"
        ],
        "release_date": "1994"
    },
    "Super Metroid Map Rando": {
        "igdb_id": "1103",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5osy.jpg",
        "world_name": "Super Metroid Map Rando",
        "igdb_name": "super metroid",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "thriller"
        ],
        "platforms": [
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "after samus completed her mission and eradicated the entire metroid population on sr388 as commanded by the galactic federation (sans the metroid hatchling, which she nicknamed \"baby\"), she brought the hatchling to the ceres space colony for research. however, shortly after she left, she received a distress signal from the station and returned to investigate.\n\nwhen samus arrives at the space science academy where the baby was being studied, she finds all the scientists slaughtered and the containment unit that held the baby missing. upon further exploration of the station, she finds the baby in a small capsule. as she approaches, ridley appears and grabs the capsule. after a brief battle, samus repels ridley, and he activates a self-destruct sequence to destroy ceres.\n\nafter escaping the explosion, ridley flees to zebes, and samus goes after him.",
        "keywords": [
            "aliens",
            "exploration",
            "2d",
            "16-bit",
            "metroidvania",
            "time manipulation",
            "female protagonist",
            "action-adventure",
            "side-scrolling",
            "time limit",
            "pixel art",
            "wall jump",
            "darkness",
            "explosion",
            "countdown timer",
            "nintendo power",
            "damsel in distress",
            "save point",
            "unstable platforms",
            "real-time combat",
            "secret area",
            "liberation",
            "mercenary",
            "sequence breaking",
            "isolation",
            "interconnected-world"
        ],
        "release_date": "1994"
    },
    "Super Mario 64": {
        "igdb_id": "1074",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co721v.jpg",
        "world_name": "Super Mario 64",
        "igdb_name": "super mario 64",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "open world"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "\u201cmario, please come to the castle. i've baked a cake for you. yours truly, princess toadstool.\u201d\n\n\u201cwow, an invitation from peach! i'll head out right away. i hope she can wait for me!\u201d\n\nmario is so excited to receive the invitation from the princess, who lives in the mushroom castle that he quickly dresses in his best and leaves right away.\n\n\u201chmmm, something's not quite right here... it's so quiet...\u201d\n\nshaking off his uneasy premonition, mario steps into the silent castle, where he is greeted by the gruff words, \u201cno one's home! now scram! bwa, ha, ha.\u201d\n\nthe sound seems to come from everywhere.\n\n\u201cwho's there?! i've heard that voice somewhere before...\u201d\n\nmario begins searching all over the castle. most of the doors are locked, but finding one open, he peeks inside. hanging on the wall is the largest painting he has ever seen, and from behind the painting comes the strangest sound that he has ever heard...\n\n\u201ci think i hear someone calling. what secrets does this painting hold?\u201d\n\nwithout a second thought, mario jumps at the painting. as he is drawn into it, another world opens before his very eyes.\n\nonce inside the painting, mario finds himself in the midst of battling bob-ombs. according to the bob-omb buddies, someone...or something...has suddenly attacked the castle and stolen the \u201cpower stars.\u201d these stars protect the castle. with the stars in his control, the beast plans to take over the mushroom castle.\n\nto help him accomplish this, he plans to convert the residents of the painting world into monsters as well. if nothing is done, all those monsters will soon begin to overflow from inside the painting.\n\n\u201ca plan this maniacal, this cunning...this must be the work of bowser!\u201d\n\nprincess toadstool and toad are missing, too. bowser must have taken them and sealed them inside the painting. unless mario recovers the power stars immediately, the inhabitants of this world will become bowser's army.\n\n\u201cwell, bowser's not going to get away with it, not as long as i'm around!\u201d\n\nstolen power stars are hidden throughout the painting world. use your wisdom and strength to recover the power stars and restore peace to the mushroom castle.\n\n\u201cmario! you are the only one we can count on.\u201d",
        "keywords": [
            "rabbit",
            "3d platformer",
            "swimming",
            "snowman",
            "super-ness",
            "sprinting mechanics",
            "real-time combat",
            "underwater gameplay",
            "speedrun",
            "linear gameplay",
            "wiggler",
            "entering world in a painting",
            "retroachievements",
            "princess peach",
            "popular"
        ],
        "release_date": "1996"
    },
    "SM64 Romhack": {
        "igdb_id": "1074",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co721v.jpg",
        "world_name": "SM64 Romhack",
        "igdb_name": "super mario 64",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "open world"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "\u201cmario, please come to the castle. i've baked a cake for you. yours truly, princess toadstool.\u201d\n\n\u201cwow, an invitation from peach! i'll head out right away. i hope she can wait for me!\u201d\n\nmario is so excited to receive the invitation from the princess, who lives in the mushroom castle that he quickly dresses in his best and leaves right away.\n\n\u201chmmm, something's not quite right here... it's so quiet...\u201d\n\nshaking off his uneasy premonition, mario steps into the silent castle, where he is greeted by the gruff words, \u201cno one's home! now scram! bwa, ha, ha.\u201d\n\nthe sound seems to come from everywhere.\n\n\u201cwho's there?! i've heard that voice somewhere before...\u201d\n\nmario begins searching all over the castle. most of the doors are locked, but finding one open, he peeks inside. hanging on the wall is the largest painting he has ever seen, and from behind the painting comes the strangest sound that he has ever heard...\n\n\u201ci think i hear someone calling. what secrets does this painting hold?\u201d\n\nwithout a second thought, mario jumps at the painting. as he is drawn into it, another world opens before his very eyes.\n\nonce inside the painting, mario finds himself in the midst of battling bob-ombs. according to the bob-omb buddies, someone...or something...has suddenly attacked the castle and stolen the \u201cpower stars.\u201d these stars protect the castle. with the stars in his control, the beast plans to take over the mushroom castle.\n\nto help him accomplish this, he plans to convert the residents of the painting world into monsters as well. if nothing is done, all those monsters will soon begin to overflow from inside the painting.\n\n\u201ca plan this maniacal, this cunning...this must be the work of bowser!\u201d\n\nprincess toadstool and toad are missing, too. bowser must have taken them and sealed them inside the painting. unless mario recovers the power stars immediately, the inhabitants of this world will become bowser's army.\n\n\u201cwell, bowser's not going to get away with it, not as long as i'm around!\u201d\n\nstolen power stars are hidden throughout the painting world. use your wisdom and strength to recover the power stars and restore peace to the mushroom castle.\n\n\u201cmario! you are the only one we can count on.\u201d",
        "keywords": [
            "rabbit",
            "3d platformer",
            "swimming",
            "snowman",
            "super-ness",
            "sprinting mechanics",
            "real-time combat",
            "underwater gameplay",
            "speedrun",
            "linear gameplay",
            "wiggler",
            "entering world in a painting",
            "retroachievements",
            "princess peach"
        ],
        "release_date": "1996"
    },
    "Super Mario Odyssey": {
        "igdb_id": "26758",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mxf.jpg",
        "world_name": "Super Mario Odyssey",
        "igdb_name": "super mario odyssey",
        "rating": [
            "cartoon violence",
            "comic mischief"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "nintendo switch 2",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "dinosaurs",
            "3d",
            "rabbit",
            "dog",
            "sequel",
            "wall jump",
            "3d platformer",
            "swimming",
            "2d platformer",
            "alternate costumes",
            "deliberately retro",
            "checkpoints",
            "underwater gameplay",
            "wiggler",
            "behind the waterfall",
            "entering world in a painting",
            "the game awards 2017"
        ],
        "release_date": "2017"
    },
    "Super Mario Sunshine": {
        "igdb_id": "1075",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co21rh.jpg",
        "world_name": "Super Mario Sunshine",
        "igdb_name": "super mario sunshine",
        "rating": [
            "comic mischief"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "sandbox"
        ],
        "platforms": [
            "nintendo gamecube"
        ],
        "storyline": "close your eyes and imagine\u2026soothing sunshine accompanied by the sound of waves gently breaking on the shore. high above, seagulls turn lazy circles in a clear blue sky. this is isle delfino.\n\nfar from the hustle and bustle of the mushroom kingdom, this island resort glitters like a gem in the waters of a southern sea.\n\nmario, peach, and an entourage of toads have come to isle delfino to relax and unwind. at least, that\u2019s their plan\u2026but when they arrive, they find things have gone horribly wrong...\n\naccording to the island inhabitants, the person responsible for the mess has a round nose, a thick mustache, and a cap\u2026\n\nwhat? but\u2026that sounds like mario!!\n\nthe islanders are saying that mario's mess has polluted the island and caused their energy source, the shine sprites, to vanish.\n\nnow the falsely accused mario has promised to clean up the island, but...how?\n\nnever fear! fludd, the latest invention from gadd science, inc., can help mario tidy up the island, take on baddies, and lend a nozzle in all kinds of sticky situations.\n\ncan mario clean the island, capture the villain, and clear his good name? it\u2019s time for another mario adventure to get started!",
        "keywords": [
            "ghosts",
            "dinosaurs",
            "death",
            "robots",
            "action-adventure",
            "time limit",
            "sequel",
            "giant insects",
            "wall jump",
            "3d platformer",
            "climbing",
            "swimming",
            "mario",
            "turtle",
            "explosion",
            "anthropomorphism",
            "super-ness",
            "alternate costumes",
            "voice acting",
            "human",
            "polygonal 3d",
            "damsel in distress",
            "descendants of other characters",
            "sprinting mechanics",
            "unstable platforms",
            "real-time combat",
            "underwater gameplay",
            "male antagonist",
            "violent plants",
            "moving platforms",
            "been here before",
            "water level",
            "sleeping",
            "tentacles",
            "boss assistance",
            "linear gameplay",
            "gliding",
            "kidnapping",
            "italian accent",
            "wiggler",
            "collection marathon",
            "princess peach"
        ],
        "release_date": "2002"
    },
    "Super Mario World": {
        "igdb_id": "1070",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8lo8.jpg",
        "world_name": "Super Mario World",
        "igdb_name": "super mario world",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "arcade",
            "super nintendo entertainment system",
            "wii",
            "wii u",
            "new nintendo 3ds",
            "super famicom"
        ],
        "storyline": "mario is having a vacation in dinosaur land when he learns that princess peach toadstool has been kidnapped by the evil king koopa bowser. when mario starts searching for her he finds a giant egg with a dinosaur named yoshi hatching out of it. yoshi tells mario that his fellow dinosaurs have been imprisoned in eggs by bowser's underlings. the intrepid plumber has to travel to their castles, rescue the dinosaurs, and eventually face king koopa himself, forcing him to release the princess.",
        "keywords": [
            "dinosaurs",
            "princess",
            "mario",
            "digital distribution",
            "bonus stage",
            "damsel in distress",
            "retroachievements",
            "popular"
        ],
        "release_date": "1990"
    },
    "SMZ3": {
        "igdb_id": "210231",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5zep.jpg",
        "world_name": "SMZ3",
        "igdb_name": "super metroid and a link to the past crossover randomizer",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action",
            "open world"
        ],
        "platforms": [
            "super nintendo entertainment system"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2018"
    },
    "Secret of Evermore": {
        "igdb_id": "1359",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8kz6.jpg",
        "world_name": "Secret of Evermore",
        "igdb_name": "secret of evermore",
        "rating": [
            "mild animated violence"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [
            "action",
            "science fiction",
            "historical"
        ],
        "platforms": [
            "super nintendo entertainment system"
        ],
        "storyline": "in dr. sidney ruffleberg's old, decaying mansion, a boy and his dog stumble upon a mysterious machine. by sheer accident they are propelled into evermore, a one-time utopia that now has become a confounding and deadly world. a world of prehistoric jungles, ancient civilizations, medieval kingdoms and futuristic cities. during his odyssey, the boy must master a variety of weapons, learn to harness the forces of alchemy, and make powerful allies to battle evermore's diabolical monsters. what's more, his dog masters shape-changing to aid the quest. but even if they can muster enough skill and courage, even if they can uncover the mysterious clues, they can only find their way home by discovering the secret of evermore.",
        "keywords": [
            "medieval",
            "dog",
            "giant insects",
            "sprinting mechanics",
            "ambient music"
        ],
        "release_date": "1995"
    },
    "Sonic Heroes": {
        "igdb_id": "4156",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9olx.jpg",
        "world_name": "Sonic Heroes",
        "igdb_name": "sonic heroes",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "platform",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "xbox",
            "nintendo gamecube",
            "pc (microsoft windows)",
            "playstation 2"
        ],
        "storyline": "dr. eggman has come back to challenge sonic and crew again to defeat his new scheme. sonic the hedgehog, miles \"tails\" prower, and knuckles the echidna gladly accept and race off to tackle the doctor's latest plan. meanwhile, rouge the bat swings in on one of eggman's old fortresses and discovers shadow the hedgehog encapsuled. after an odd encounter, rouge, shadow, and e-123 omega join up to find out what happened to shadow and to get revenge on eggman.\nat a resort, amy rose looks at an ad that shows sonic in it with chocola and froggy, cheese's and big's best friends respectively. after getting over boredom, amy, cream the rabbit, and big the cat decide to find sonic and get what they want back. elsewhere, in a run down building, the chaotix detective agency receive a package that contains a walkie-talkie. tempting them, vector the crocodile, espio the chameleon and charmy bee decide to work for this mysterious person, so they can earn some money.",
        "keywords": [
            "3d",
            "robots",
            "rabbit",
            "multiple protagonists",
            "achievements",
            "amnesia",
            "3d platformer",
            "explosion",
            "anthropomorphism",
            "bonus stage",
            "voice acting",
            "checkpoints",
            "rock music",
            "moving platforms",
            "temporary invincibility",
            "spiky-haired protagonist",
            "on-the-fly character switching",
            "retroachievements"
        ],
        "release_date": "2003"
    },
    "Symphony of the Night": {
        "igdb_id": "1128",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co53m8.jpg",
        "world_name": "Symphony of the Night",
        "igdb_name": "castlevania: symphony of the night",
        "rating": [
            "animated blood and gore",
            "animated violence",
            "violence",
            "blood and gore",
            "cartoon violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "horror",
            "open world"
        ],
        "platforms": [
            "playstation 3",
            "playstation",
            "playstation portable",
            "xbox 360"
        ],
        "storyline": "the game's story takes place during the year 1797, 5 years after the events of rondo of blood and begins with richter belmont's defeat of count dracula, mirroring the end of the former game. however, despite dracula being defeated, richter vanishes without a trace. castlevania rises again five years later, and while there are no belmonts to storm the castle, alucard, the son of dracula, awakens from his self-induced sleep, and decides to investigate what transpired during his slumber.\n\nmeanwhile, maria renard, richter's sister-in-law, enters castlevania herself to search for the missing richter. she assists alucard multiple times throughout the game.",
        "keywords": [
            "ghosts",
            "bloody",
            "gravity",
            "magic",
            "2d",
            "metroidvania",
            "death",
            "horse",
            "action-adventure",
            "side-scrolling",
            "multiple protagonists",
            "backtracking",
            "achievements",
            "multiple endings",
            "undead",
            "pixel art",
            "wolf",
            "nudity",
            "bats",
            "day/night cycle",
            "explosion",
            "digital distribution",
            "leveling up",
            "human",
            "polygonal 3d",
            "psone classics",
            "shopping",
            "skeletons",
            "descendants of other characters",
            "save point",
            "playstation plus",
            "melee",
            "real-time combat",
            "a.i. companion",
            "secret area",
            "rock music",
            "rpg elements",
            "moving platforms",
            "sequence breaking",
            "villain",
            "shape-shifting",
            "speedrun",
            "villain turned good",
            "over 100% completion",
            "completion percentage",
            "meme origin",
            "androgyny",
            "creature compendium",
            "behind the waterfall",
            "isolation",
            "interconnected-world"
        ],
        "release_date": "1997"
    },
    "Slay the Spire": {
        "igdb_id": "296831",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co82c5.jpg",
        "world_name": "Slay the Spire",
        "igdb_name": "slay the spire ii",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "strategy",
            "indie",
            "card & board game"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "roguelike"
        ],
        "release_date": ""
    },
    "Spyro 3": {
        "igdb_id": "1578",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7t4m.jpg",
        "world_name": "Spyro 3",
        "igdb_name": "spyro: year of the dragon",
        "rating": [
            "comic mischief"
        ],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "playstation 3",
            "playstation",
            "playstation portable"
        ],
        "storyline": "the game follows the titular purple dragon spyro as he travels to the forgotten worlds after 150 magical dragon eggs are stolen from the land of the dragons by an evil sorceress.",
        "keywords": [
            "minigames",
            "mascot",
            "flight",
            "multiple protagonists",
            "swimming",
            "sword & sorcery",
            "anthropomorphism",
            "bonus stage",
            "polygonal 3d",
            "psone classics",
            "game reference",
            "cameo appearance",
            "playstation plus",
            "auto-saving",
            "real-time combat",
            "moving platforms",
            "gliding",
            "time trials"
        ],
        "release_date": "2000"
    },
    "Skyward Sword": {
        "igdb_id": "534",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5wrj.jpg",
        "world_name": "Skyward Sword",
        "igdb_name": "the legend of zelda: skyward sword",
        "rating": [
            "fantasy violence",
            "animated blood",
            "comic mischief"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "puzzle",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "historical",
            "open world"
        ],
        "platforms": [
            "wii",
            "wii u"
        ],
        "storyline": "born on an island suspended in the sky, a young man called link accepts his destiny to venture to the world below to save his childhood friend zelda after being kidnapped and brought to an abandoned land.",
        "keywords": [
            "medieval",
            "archery",
            "action-adventure",
            "campaign",
            "princess",
            "silent protagonist",
            "day/night cycle",
            "sword & sorcery",
            "human",
            "polygonal 3d",
            "bow and arrow",
            "damsel in distress",
            "potion",
            "auto-aim",
            "real-time combat",
            "mercenary",
            "violent plants",
            "androgyny",
            "ancient advanced civilization technology",
            "context sensitive",
            "living inventory",
            "behind the waterfall",
            "monomyth"
        ],
        "release_date": "2011"
    },
    "Stardew Valley": {
        "igdb_id": "17000",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/xrpmydnu9rpxvxfjkiu7.jpg",
        "world_name": "Stardew Valley",
        "igdb_name": "stardew valley",
        "rating": [
            "fantasy violence",
            "mild blood",
            "mild language",
            "simulated gambling",
            "use of tobacco",
            "use of alcohol",
            "use of alcohol and tobacco"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "simulator",
            "strategy",
            "adventure",
            "indie"
        ],
        "themes": [
            "fantasy",
            "business",
            "sandbox",
            "romance"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "wii u",
            "playstation vita",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "you\u2019ve inherited your grandfather\u2019s old farm plot in stardew valley. armed with hand-me-down tools and a few coins, you set out to begin your new life. can you learn to live off the land and turn these overgrown fields into a thriving home? it won\u2019t be easy. ever since joja corporation came to town, the old ways of life have all but disappeared. the community center, once the town\u2019s most vibrant hub of activity, now lies in shambles. but the valley seems full of opportunity. with a little dedication, you might just be the one to restore stardew valley to greatness!",
        "keywords": [
            "2d",
            "fishing",
            "crafting",
            "fairy",
            "pixel art",
            "relaxing",
            "mining",
            "day/night cycle",
            "customizable characters",
            "deliberately retro"
        ],
        "release_date": "2016"
    },
    "Star Fox 64": {
        "igdb_id": "2591",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2e4k.jpg",
        "world_name": "Star Fox 64",
        "igdb_name": "star fox 64",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "shooter"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "wii",
            "nintendo 64",
            "wii u"
        ],
        "storyline": "mad scientist andross arises as the emperor of venom and declares war on the entire lylat system, starting with corneria. general pepper sends in the star fox team to protect the key planets of the lylat system and stop dr. andross.",
        "keywords": [
            "gravity",
            "death",
            "robots",
            "frog",
            "spaceship",
            "flight",
            "multiple endings",
            "artificial intelligence",
            "wolf",
            "dog",
            "talking animals",
            "anthropomorphism",
            "voice acting",
            "polygonal 3d",
            "descendants of other characters",
            "a.i. companion",
            "secret area",
            "difficulty level",
            "villain",
            "auto-scrolling levels",
            "meme origin",
            "retroachievements"
        ],
        "release_date": "1997"
    },
    "Subnautica": {
        "igdb_id": "9254",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1iqw.jpg",
        "world_name": "Subnautica",
        "igdb_name": "subnautica",
        "rating": [
            "mild language",
            "fantasy violence"
        ],
        "player_perspectives": [
            "first person",
            "virtual reality"
        ],
        "genres": [
            "adventure",
            "indie"
        ],
        "themes": [
            "science fiction",
            "survival",
            "open world"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "steamvr",
            "playstation 5",
            "mac",
            "oculus rift",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "you have crash-landed on an alien ocean world, and the only way to go is down. subnautica's oceans range from sun drenched shallow coral reefs to treacherous deep-sea trenches, lava fields, and bio-luminescent underwater rivers. manage your oxygen supply as you explore kelp forests, plateaus, reefs, and winding cave systems. the water teems with life: some of it helpful, much of it harmful.\n\nafter crash landing in your life pod, the clock is ticking to find water, food, and to develop the equipment you need to explore. collect resources from the ocean around you. craft diving gear, lights, habitat modules, and submersibles. venture deeper and further form to find rarer resources, allowing you to craft more advanced items.",
        "keywords": [
            "exploration",
            "swimming",
            "underwater gameplay"
        ],
        "release_date": "2018"
    },
    "Star Wars Episode I Racer": {
        "igdb_id": "154",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3wj7.jpg",
        "world_name": "Star Wars Episode I Racer",
        "igdb_name": "star wars: episode i - racer",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "racing"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "playstation 4",
            "nintendo 64",
            "pc (microsoft windows)",
            "mac",
            "xbox one",
            "nintendo switch",
            "dreamcast"
        ],
        "storyline": "",
        "keywords": [
            "robots"
        ],
        "release_date": "1999"
    },
    "The Binding of Isaac Repentance": {
        "igdb_id": "310643",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8kxf.jpg",
        "world_name": "The Binding of Isaac Repentance",
        "igdb_name": "the binding of isaac: repentance",
        "rating": [
            "blood and gore",
            "crude humor",
            "violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "shooter",
            "indie"
        ],
        "themes": [],
        "platforms": [
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2021"
    },
    "Terraria": {
        "igdb_id": "1879",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1rbo.jpg",
        "world_name": "Terraria",
        "igdb_name": "terraria",
        "rating": [
            "mild suggestive themes",
            "blood and gore",
            "use of alcohol",
            "cartoon violence",
            "suggestive themes",
            "violence",
            "blood",
            "alcohol reference"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "simulator",
            "strategy",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction",
            "horror",
            "survival",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "google stadia",
            "playstation 3",
            "playstation 4",
            "linux",
            "nintendo 3ds",
            "windows phone",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "wii u",
            "playstation vita",
            "xbox 360",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "exploration",
            "magic",
            "2d",
            "construction",
            "fishing",
            "crafting",
            "death",
            "procedural generation",
            "rabbit",
            "flight",
            "action-adventure",
            "fairy",
            "undead",
            "pixel art",
            "snow",
            "teleportation",
            "mining",
            "climbing",
            "swimming",
            "bats",
            "day/night cycle",
            "sword & sorcery",
            "darkness",
            "explosion",
            "digital distribution",
            "customizable characters",
            "human",
            "bow and arrow",
            "loot gathering",
            "skeletons",
            "deliberately retro",
            "playstation plus",
            "ice stage",
            "falling damage",
            "pick your gender",
            "melee",
            "underwater gameplay",
            "violent plants",
            "merchants",
            "you can pet the dog",
            "bees"
        ],
        "release_date": "2011"
    },
    "Tetris Attack": {
        "igdb_id": "2739",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2w6k.jpg",
        "world_name": "Tetris Attack",
        "igdb_name": "tetris attack",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "puzzle"
        ],
        "themes": [
            "action",
            "kids"
        ],
        "platforms": [
            "super nintendo entertainment system"
        ],
        "storyline": "the story mode takes place in the world of yoshi's island, where bowser and his minions have cursed all of yoshi's friends. playing as yoshi, the player must defeat each of his friends in order to remove the curse. once all friends have been freed, the game proceeds to a series of bowser's minions, and then to bowser himself. during these final matches, the player can select yoshi or any of his friends to play out the stage.",
        "keywords": [
            "retroachievements"
        ],
        "release_date": "1996"
    },
    "Timespinner": {
        "igdb_id": "28952",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co24ag.jpg",
        "world_name": "Timespinner",
        "igdb_name": "timespinner",
        "rating": [
            "fantasy violence",
            "sexual themes",
            "mild language"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "playstation vita",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "with her family murdered in front of her and the ancient timespinner device destroyed, lunais is suddenly transported into a unknown world, stranded with seemingly no hope of return. using her power to control time, lunais vows to take her revenge on the evil lachiem empire, but sometimes the course of history isn\u2019t quite as black and white as it seems...",
        "keywords": [
            "time travel",
            "metroidvania",
            "time manipulation",
            "female protagonist",
            "action-adventure",
            "pixel art",
            "steam greenlight",
            "crowdfunding",
            "digital distribution",
            "deliberately retro",
            "crowd funded",
            "merchants",
            "lgbtq+"
        ],
        "release_date": "2018"
    },
    "The Legend of Zelda": {
        "igdb_id": "1022",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1uii.jpg",
        "world_name": "The Legend of Zelda",
        "igdb_name": "the legend of zelda",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "open world"
        ],
        "platforms": [
            "family computer disk system",
            "nintendo 3ds",
            "wii",
            "family computer",
            "wii u",
            "nintendo entertainment system"
        ],
        "storyline": "in one of the darkest times in the kingdom of hyrule, a young boy named link takes on an epic quest to restore the fragmented triforce of wisdom and save the princess zelda from the clutches of the evil ganon.",
        "keywords": [
            "fairy",
            "overworld",
            "meme origin"
        ],
        "release_date": "1986"
    },
    "The Legend of Zelda - Oracle of Ages": {
        "igdb_id": "1041",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2tw1.jpg",
        "world_name": "The Legend of Zelda - Oracle of Ages",
        "igdb_name": "the legend of zelda: oracle of ages",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "game boy color",
            "nintendo 3ds"
        ],
        "storyline": "a pall of darkness has fallen over the land of labrynna. the sorceress of shadows has captured the oracle of ages and is using her power to do evil. link has been summoned to help and must travel back and forth in time to stop the sorceress of shadows and return labrynna to its former glory.",
        "keywords": [
            "pirates",
            "ghosts",
            "time travel",
            "minigames",
            "death",
            "rabbit",
            "action-adventure",
            "witches",
            "fairy",
            "undead",
            "campaign",
            "princess",
            "dancing",
            "silent protagonist",
            "climbing",
            "swimming",
            "sword & sorcery",
            "explosion",
            "block puzzle",
            "anthropomorphism",
            "shopping",
            "damsel in distress",
            "disorientation zone",
            "descendants of other characters",
            "side quests",
            "real-time combat",
            "shielded enemies",
            "walking through walls",
            "multiple gameplay perspectives",
            "conveyor belt",
            "punctuation mark above head",
            "sequence breaking",
            "villain",
            "time paradox",
            "context sensitive",
            "status effects",
            "behind the waterfall"
        ],
        "release_date": "2001"
    },
    "The Legend of Zelda - Oracle of Seasons": {
        "igdb_id": "1032",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2tw0.jpg",
        "world_name": "The Legend of Zelda - Oracle of Seasons",
        "igdb_name": "the legend of zelda: oracle of seasons",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "game boy color",
            "nintendo 3ds"
        ],
        "storyline": "the land of holodrum is slowly withering. onox, the general of darkness, has imprisoned the oracle of seasons and is draining the very life out of the land. with the seasons in tumult and the forces of evil running rampant, the world looks for a hero... and finds link. his quest won't be easy - he'll have to master the seasons themselves if he's to turn back the evil tide.",
        "keywords": [
            "pirates",
            "time travel",
            "magic",
            "grinding",
            "mascot",
            "death",
            "action-adventure",
            "witches",
            "fairy",
            "backtracking",
            "multiple endings",
            "undead",
            "campaign",
            "princess",
            "pixel art",
            "dog",
            "teleportation",
            "silent protagonist",
            "climbing",
            "sword & sorcery",
            "block puzzle",
            "digital distribution",
            "anthropomorphism",
            "world map",
            "cat",
            "shopping",
            "bow and arrow",
            "damsel in distress",
            "disorientation zone",
            "side quests",
            "potion",
            "real-time combat",
            "secret area",
            "walking through walls",
            "multiple gameplay perspectives",
            "villain",
            "fetch quests",
            "poisoning",
            "context sensitive",
            "status effects",
            "damage over time"
        ],
        "release_date": "2001"
    },
    "Toontown": {
        "igdb_id": "25326",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co28yv.jpg",
        "world_name": "Toontown",
        "igdb_name": "toontown online",
        "rating": [
            "cartoon violence",
            "comic mischief"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [
            "comedy",
            "open world"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "toontown online's story centers on an ongoing battle between a population of cartoon animals known as the toons and a collection of business-minded robots known as the cogs who are trying to take over the town. players would choose and customize their own toon and go on to complete toontasks, play mini-games, and fight the cogs.",
        "keywords": [
            "minigames"
        ],
        "release_date": "2003"
    },
    "Twilight Princess": {
        "igdb_id": "134014",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3w1h.jpg",
        "world_name": "Twilight Princess",
        "igdb_name": "the legend of zelda: twilight princess",
        "rating": [
            "fantasy violence",
            "animated blood"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "wii"
        ],
        "storyline": "link, a young farm boy whose tasks consist of herding goats to watching children in ordon village, is asked by the mayor to run an errand in castle town. but things went strange that day: the land becomes dark and strange creatures appear from another world called the twilight realm which turns most people into ghosts. unlike the others, link transforms into a wolf but is captured. a mysterious figure named midna helps him break free, and with the aid of her magic, they set off to free the land from the shadows. link must explore the vast land of hyrule and uncover the mystery behind its plunge into darkness.",
        "keywords": [],
        "release_date": "2006"
    },
    "Trackmania": {
        "igdb_id": "133807",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2fe9.jpg",
        "world_name": "Trackmania",
        "igdb_name": "trackmania",
        "rating": [],
        "player_perspectives": [
            "first person",
            "third person"
        ],
        "genres": [
            "racing",
            "sport",
            "arcade"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2020"
    },
    "Paper Mario The Thousand Year Door": {
        "igdb_id": "328663",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9p1w.jpg",
        "world_name": "Paper Mario The Thousand Year Door",
        "igdb_name": "paper mario: the thousand-year door",
        "rating": [],
        "player_perspectives": [],
        "genres": [
            "puzzle"
        ],
        "themes": [],
        "platforms": [
            "web browser"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2004"
    },
    "TUNIC": {
        "igdb_id": "23733",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/td1t8kb33gyo8mvhl2pc.jpg",
        "world_name": "TUNIC",
        "igdb_name": "tunic",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "mac",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "tunic is an action adventure game about a small fox in a big world, who must explore the countryside, fight monsters, and discover secrets. crafted to evoke feelings of classic action adventure games, tunic will challenge the player with unique items, skillful combat techniques, and arcane mysteries as our hero forges their way through an intriguing new world.",
        "keywords": [
            "exploration",
            "3d",
            "difficult",
            "stylized",
            "cute",
            "atmospheric",
            "great soundtrack",
            "digital distribution",
            "anthropomorphism",
            "soulslike"
        ],
        "release_date": "2022"
    },
    "The Wind Waker": {
        "igdb_id": "1033",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3ohz.jpg",
        "world_name": "The Wind Waker",
        "igdb_name": "the legend of zelda: the wind waker",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy"
        ],
        "platforms": [
            "nintendo gamecube"
        ],
        "storyline": "set hundreds of years after the events of ocarina of time, the wind waker finds the hero link living with his grandmother on the outset island, one of the many small islands lost amidst the waters of the great sea. on his tenth birthday, link encounters a giant bird carrying a girl. he rescues the girl, but as a result his own sister is taken away by the bird. the girl is a pirate captain named tetra, who agrees to help link find and rescue his sister. during the course of their journey, the two of them realize that a powerful, legendary evil is active again, and must find a way to stop him.",
        "keywords": [
            "archery",
            "action-adventure",
            "fairy",
            "day/night cycle",
            "sword & sorcery",
            "auto-aim",
            "living inventory"
        ],
        "release_date": "2002"
    },
    "Tyrian": {
        "igdb_id": "14432",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2zg1.jpg",
        "world_name": "Tyrian",
        "igdb_name": "tyrian 2000",
        "rating": [
            "animated violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "shooter",
            "arcade"
        ],
        "themes": [
            "action",
            "science fiction"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac",
            "dos"
        ],
        "storyline": "",
        "keywords": [
            "pixel art"
        ],
        "release_date": "1999"
    },
    "UFO 50": {
        "igdb_id": "54555",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co24v0.jpg",
        "world_name": "UFO 50",
        "igdb_name": "ufo 50",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "shooter",
            "platform",
            "puzzle",
            "role-playing (rpg)",
            "strategy",
            "adventure",
            "indie",
            "arcade"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [
            "digital distribution",
            "deliberately retro"
        ],
        "release_date": "2024"
    },
    "ULTRAKILL": {
        "igdb_id": "124333",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co46s3.jpg",
        "world_name": "ULTRAKILL",
        "igdb_name": "ultrakill",
        "rating": [
            "violence",
            "blood and gore"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "shooter",
            "platform",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction"
        ],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "mankind has gone extinct and the only beings left on earth are machines fueled by blood.\nbut now that blood is starting to run out on the surface...\n\nmachines are racing to the depths of hell in search of more.",
        "keywords": [
            "bloody",
            "robots",
            "stylized",
            "silent protagonist",
            "great soundtrack",
            "rock music"
        ],
        "release_date": "2020"
    },
    "Undertale": {
        "igdb_id": "12517",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2855.jpg",
        "world_name": "Undertale",
        "igdb_name": "undertale",
        "rating": [
            "mild blood",
            "mild language",
            "use of tobacco",
            "simulated gambling",
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "role-playing (rpg)",
            "turn-based strategy (tbs)",
            "adventure",
            "indie"
        ],
        "themes": [
            "fantasy",
            "horror",
            "comedy",
            "drama"
        ],
        "platforms": [
            "playstation 4",
            "linux",
            "pc (microsoft windows)",
            "mac",
            "playstation vita",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "\"a long time ago, two races ruled peacefully over the earth: humans and monsters. one day, a terrible war broke out between the two races. after a long battle, the humans were victorious. they sealed the monsters underground with a magical spell.\n\nin the year 201x, a small child scales mt. ebott. it is said that those who climb the mountain never return.\n\nseeking refuge from the rainy weather, the child enters a cave and discovers an enormous hole.\n\nmoving closer to get a better look... the child falls in.\n\nnow, our story begins.\"",
        "keywords": [
            "retro",
            "psychological horror",
            "2d",
            "turn-based",
            "female protagonist",
            "backtracking",
            "multiple endings",
            "cute",
            "funny",
            "pixel art",
            "pixel graphics",
            "story rich",
            "great soundtrack",
            "anthropomorphism",
            "leveling up",
            "breaking the fourth wall",
            "skeletons",
            "plot twist",
            "fast traveling",
            "conversation",
            "you can pet the dog"
        ],
        "release_date": "2015"
    },
    "VVVVVV": {
        "igdb_id": "1990",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4ieg.jpg",
        "world_name": "VVVVVV",
        "igdb_name": "vvvvvv",
        "rating": [
            "mild fantasy violence",
            "mild language"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure",
            "indie",
            "arcade"
        ],
        "themes": [
            "action",
            "fantasy",
            "science fiction"
        ],
        "platforms": [
            "playstation 4",
            "ouya",
            "linux",
            "nintendo 3ds",
            "android",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "playstation vita",
            "nintendo switch"
        ],
        "storyline": "a spaceship with six crew members - viridian, victoria, vitellary, vermillion, verdigris, and violet - suddenly encountered mysterious trouble while underway.\nthe group escapes by means of a teleportation device, but for some reason all the crew members are sent to different places.\nviridian, the protagonist, must find the other crew members and escape from this mysterious labyrinth...",
        "keywords": [
            "ghosts",
            "exploration",
            "retro",
            "gravity",
            "2d",
            "metroidvania",
            "death",
            "spaceship",
            "space",
            "achievements",
            "pixel art",
            "pixel graphics",
            "teleportation",
            "2d platformer",
            "digital distribution",
            "world map",
            "deliberately retro",
            "humble bundle",
            "save point",
            "playstation plus",
            "checkpoints",
            "unstable platforms",
            "stereoscopic 3d",
            "instant kill",
            "moving platforms",
            "auto-scrolling levels",
            "time trials",
            "conversation"
        ],
        "release_date": "2010"
    },
    "Wargroove": {
        "igdb_id": "27441",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4hgb.jpg",
        "world_name": "Wargroove",
        "igdb_name": "wargroove",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "strategy",
            "turn-based strategy (tbs)",
            "tactical",
            "indie"
        ],
        "themes": [
            "fantasy",
            "warfare"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "wargroove is a modern take on the simple yet deep turn-based tactical gameplay popularised in the 2000s by handheld games such as advance wars. as big fans of those games we were disappointed to find that nothing in this genre was available on current generation platforms and set out to fill the gap ourselves. wargroove aims to recreate the charm and accessibility of the titles that inspired it whilst bringing modern technology into the formula. this modern focus allows for higher resolution pixel art, robust online play and deep modding capability, ultimately creating the most complete experience for advance wars and tbs fans.",
        "keywords": [
            "pixel art"
        ],
        "release_date": "2019"
    },
    "Wargroove 2": {
        "igdb_id": "241149",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co731u.jpg",
        "world_name": "Wargroove 2",
        "igdb_name": "wargroove 2",
        "rating": [
            "fantasy violence"
        ],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
        ],
        "genres": [
            "role-playing (rpg)",
            "strategy",
            "turn-based strategy (tbs)",
            "indie"
        ],
        "themes": [
            "fantasy",
            "warfare"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "three years have passed since queen mercia and her allies defeated the ancient adversaries and restored peace to aurania. now, an ambitious foreign faction is unearthing forbidden technologies that could have catastrophic consequences for the land and its people. battle your way through 3 campaigns following 1 interweaving story. only bold decisions, smart resourcing, and tactical know-how can repair a fractured realm\u2026",
        "keywords": [
            "pirates"
        ],
        "release_date": "2023"
    },
    "The Witness": {
        "igdb_id": "5601",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3hih.jpg",
        "world_name": "The Witness",
        "igdb_name": "the witness",
        "rating": [
            "alcohol reference"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "puzzle",
            "adventure",
            "indie"
        ],
        "themes": [
            "science fiction",
            "open world",
            "mystery"
        ],
        "platforms": [
            "playstation 4",
            "pc (microsoft windows)",
            "ios",
            "mac",
            "xbox one"
        ],
        "storyline": "you wake up, alone, on a strange island full of puzzles that will challenge and surprise you.\n\nyou don't remember who you are, and you don't remember how you got here, but there's one thing you can do: explore the island in hope of discovering clues, regaining your memory, and somehow finding your way home.",
        "keywords": [
            "exploration",
            "procedural generation",
            "maze",
            "backtracking",
            "time limit",
            "multiple endings",
            "amnesia",
            "darkness",
            "digital distribution",
            "voice acting",
            "polygonal 3d",
            "game reference",
            "auto-saving",
            "stat tracking",
            "secret area"
        ],
        "release_date": "2016"
    },
    "Wario Land": {
        "igdb_id": "1072",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co216h.jpg",
        "world_name": "Wario Land",
        "igdb_name": "wario land: super mario land 3",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "nintendo 3ds",
            "game boy"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "1994"
    },
    "Wario Land 4": {
        "igdb_id": "1699",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wpx.jpg",
        "world_name": "Wario Land 4",
        "igdb_name": "wario land 4",
        "rating": [
            "comic mischief"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure"
        ],
        "themes": [
            "action"
        ],
        "platforms": [
            "nintendo 3ds",
            "wii u",
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "ghosts",
            "anime",
            "minigames",
            "flight",
            "time limit",
            "multiple endings",
            "pixel art",
            "sequel",
            "swimming",
            "digital distribution",
            "countdown timer",
            "cat",
            "sprinting mechanics",
            "ice stage",
            "melee",
            "moving platforms",
            "sequence breaking",
            "sliding down ladders"
        ],
        "release_date": "2001"
    },
    "Wordipelago": {
        "igdb_id": "",
        "world_name": "Wordipelago",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Xenoblade X": {
        "igdb_id": "2366",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1nwh.jpg",
        "world_name": "Xenoblade X",
        "igdb_name": "xenoblade chronicles x",
        "rating": [
            "suggestive themes",
            "use of alcohol",
            "language",
            "violence",
            "animated blood"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "science fiction",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "wii u"
        ],
        "storyline": "xenoblade chronicles x opens as humanity, warned of its impending destruction in the crossfire between two warring alien races, constructs interstellar arks to escape earth. however, only a few arks escape the destruction, including the white whale ark. two years after launching, the white whale is attacked and transported to mira. during the crash-landing, the lifehold\u2014a device containing the majority of the human colonists\u2014is separated from the white whale, with lifepods containing colonists being scattered across mira. the avatar is awoken from a lifepod by elma and brought back to new los angeles. while suffering from amnesia, the avatar joins blade, working with elma and lin to recover more lifepods and search for the lifehold. during their missions across mira, blade encounters multiple alien races, learning that those attacking them are part of the ganglion coalition, an alliance of races led by the ganglion race, who are intent on destroying humanity.",
        "keywords": [
            "aliens",
            "construction",
            "robots",
            "flight",
            "action-adventure",
            "amnesia",
            "day/night cycle",
            "spiritual successor",
            "customizable characters",
            "voice acting",
            "polygonal 3d",
            "loot gathering",
            "party system",
            "side quests",
            "real-time combat",
            "censored version"
        ],
        "release_date": "2015"
    },
    "Yacht Dice": {
        "igdb_id": "",
        "world_name": "Yacht Dice",
        "igdb_name": "",
        "rating": "",
        "player_perspectives": [],
        "genres": [
            "multiplayer",
            "card & board game"
        ],
        "themes": [],
        "platforms": [
            "archipelago"
        ],
        "storyline": "",
        "keywords": [
            "archipelago",
            "multiworld"
        ],
        "release_date": ""
    },
    "Yoshi's Island": {
        "igdb_id": "1073",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kn9.jpg",
        "world_name": "Yoshi's Island",
        "igdb_name": "super mario world 2: yoshi's island",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform"
        ],
        "themes": [
            "action",
            "fantasy",
            "kids"
        ],
        "platforms": [
            "satellaview",
            "super nintendo entertainment system",
            "super famicom"
        ],
        "storyline": "a stork carrying the infant mario brothers is attacked by kamek the magikoopa, who steals baby luigi and knocks baby mario out of the sky. baby mario lands on yoshi's island on the back of yoshi himself. with the help of his seven other yoshi friends, yoshi must traverse the island to safely reunite baby mario with his brother and get the babies to their parents.",
        "keywords": [
            "dinosaurs",
            "side-scrolling",
            "digital distribution",
            "kidnapping"
        ],
        "release_date": "1995"
    },
    "Yu-Gi-Oh! 2006": {
        "igdb_id": "49377",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7yau.jpg",
        "world_name": "Yu-Gi-Oh! 2006",
        "igdb_name": "yu-gi-oh! ultimate masters: world championship tournament 2006",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "text"
        ],
        "genres": [
            "strategy",
            "turn-based strategy (tbs)",
            "card & board game"
        ],
        "themes": [
            "fantasy",
            "survival"
        ],
        "platforms": [
            "game boy advance"
        ],
        "storyline": "",
        "keywords": [
            "monsters"
        ],
        "release_date": "2006"
    },
    "Yu-Gi-Oh! Dungeon Dice Monsters": {
        "igdb_id": "49211",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5ztw.jpg",
        "world_name": "Yu-Gi-Oh! Dungeon Dice Monsters",
        "igdb_name": "yu-gi-oh! dungeon dice monsters",
        "rating": [
            "mild violence"
        ],
        "player_perspectives": [
            "first person",
            "bird view / isometric"
        ],
        "genres": [
            "puzzle",
            "strategy",
            "turn-based strategy (tbs)",
            "card & board game"
        ],
        "themes": [
            "fantasy"
        ],
        "platforms": [
            "game boy advance"
        ],
        "storyline": "dungeon dice monsters is the newest addition to the yu-gi-oh! universe. as featured in the dungeon dice monsters story arc in the animated television series, players collect and fight with dice inscribed with mystical powers and magic in order to defeat their opponents. enter a dozen different tournaments and ultimately faceoff against the scheming creator of dungeon dice monsters, duke devlin.",
        "keywords": [
            "anime",
            "shopping",
            "merchants"
        ],
        "release_date": "2001"
    },
    "Zelda II: The Adventure of Link": {
        "igdb_id": "1025",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1uje.jpg",
        "world_name": "Zelda II: The Adventure of Link",
        "igdb_name": "zelda ii: the adventure of link",
        "rating": [
            "mild fantasy violence"
        ],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "role-playing (rpg)",
            "adventure"
        ],
        "themes": [
            "action",
            "fantasy",
            "sandbox"
        ],
        "platforms": [
            "family computer disk system",
            "nintendo 3ds",
            "wii",
            "wii u",
            "nintendo entertainment system"
        ],
        "storyline": "several years after the events of the legend of zelda, link has just turned sixteen and discovers a strange birthmark on his hand. with the help of impa, zelda's nursemaid, link learns that this mark is the key to unlock a secret room where princess zelda lies sleeping. when young, princess zelda was given knowledge of the triforce of power which was used to rule the kingdom of hyrule, but when a magician unsuccessfully tried to find out about the triforce from zelda, he put her into an eternal sleep. in his grief, the prince placed zelda in this room hoping she may wake some day. he ordered all female children in the royal household to be named zelda from this point on, so the tragedy would not be forgotten. now, to bring princess zelda back, link must locate all the pieces of the triforce which have been hidden throughout the land.",
        "keywords": [
            "magic",
            "collecting",
            "2d",
            "metroidvania",
            "death",
            "difficult",
            "action-adventure",
            "side-scrolling",
            "fairy",
            "overworld",
            "campaign",
            "pixel art",
            "sequel",
            "silent protagonist",
            "bats",
            "darkness",
            "explosion",
            "spider",
            "leveling up",
            "human",
            "damsel in distress",
            "unstable platforms",
            "saving the world",
            "potion",
            "real-time combat",
            "secret area",
            "rpg elements",
            "villain",
            "fetch quests",
            "meme origin",
            "status effects",
            "monomyth",
            "color cartridges"
        ],
        "release_date": "1987"
    },
    "Zillion": {
        "igdb_id": "18141",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7xxj.jpg",
        "world_name": "Zillion",
        "igdb_name": "zillion",
        "rating": [],
        "player_perspectives": [
            "side view"
        ],
        "genres": [
            "platform",
            "puzzle"
        ],
        "themes": [
            "science fiction"
        ],
        "platforms": [
            "sega master system/mark iii"
        ],
        "storyline": "are you ready for the ultimate danger? you're alone, outnumbered and there's no guarantee you'll make it alive. you're j.j. your objective: secretly infiltrate the underground labyrinth of the norsa empire and steal their plans for domination. armed with the ultra speed and power of the zillion laser, your mission is complex. and sheer strength will not win this one alone. you'll need more brains than brawn in this sophisticated operation. so, how will you think your way to victory? with cunning strategy and memory to guide you successfully through the maze which awaits. where once inside, you'll find the information needed to destroy the norsas and restore peace forever.",
        "keywords": [
            "anime",
            "metroidvania",
            "action-adventure"
        ],
        "release_date": "1987"
    },
    "Zork Grand Inquisitor": {
        "igdb_id": "1955",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kql.jpg",
        "world_name": "Zork Grand Inquisitor",
        "igdb_name": "zork: grand inquisitor",
        "rating": [
            "comic mischief",
            "suggestive themes",
            "use of alcohol and tobacco"
        ],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "point-and-click",
            "puzzle",
            "adventure"
        ],
        "themes": [
            "fantasy",
            "comedy"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "",
        "keywords": [
            "magic"
        ],
        "release_date": "1997"
    }
}

SEARCH_INDEX = {
    "adventure": [
        "Celeste",
        "Skyward Sword",
        "VVVVVV",
        "TUNIC",
        "Shivers",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Super Mario 64",
        "Digimon World",
        "Getting Over It",
        "Twilight Princess",
        "Sonic Adventure 2 Battle",
        "Mega Man 2",
        "Noita",
        "Blasphemous",
        "Super Mario World",
        "Final Fantasy Mystic Quest",
        "SM64 Romhack",
        "Minecraft",
        "Subnautica",
        "Banjo-Tooie",
        "Aquaria",
        "Luigi's Mansion",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "SMZ3",
        "Dark Souls Remastered",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Raft",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "Zork Grand Inquisitor",
        "CrossCode",
        "ANIMAL WELL",
        "Hades",
        "Risk of Rain 2",
        "Castlevania 64",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Sonic Heroes",
        "Sea of Thieves",
        "The Legend of Zelda",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Xenoblade X",
        "Final Fantasy",
        "Super Mario Odyssey",
        "EarthBound",
        "Resident Evil 2 Remake",
        "Terraria",
        "Kingdom Hearts 2",
        "Inscryption",
        "Pokemon Crystal",
        "Celeste 64",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Old School Runescape",
        "A Short Hike",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Kirby's Dream Land 3",
        "Ori and the Blind Forest",
        "Timespinner",
        "Risk of Rain",
        "Peaks of Yore",
        "Super Metroid",
        "An Untitled Story",
        "Chained Echoes",
        "Dark Souls III",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 3",
        "Ratchet & Clank 2",
        "Lingo",
        "Don",
        "The Legend of Zelda - Oracle of Ages",
        "Cat Quest",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Outer Wilds",
        "Super Metroid Map Rando",
        "DLCQuest",
        "Metroid Prime",
        "The Wind Waker",
        "Undertale",
        "The Witness",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Pseudoregalia",
        "Dark Souls II",
        "UFO 50",
        "Jak and Daxter: The Precursor Legacy",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Adventure",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "bird view / isometric": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "TUNIC",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "SMZ3",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Inscryption",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Not an idle game",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "The Binding of Isaac Repentance",
        "Hylics 2",
        "Old School Runescape",
        "A Short Hike",
        "MegaMan Battle Network 3",
        "Pokemon Red and Blue",
        "Hades",
        "Super Mario Sunshine",
        "Overcooked! 2",
        "OpenRCT2",
        "Civilization VI",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "The Sims 4",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Diddy Kong Racing",
        "Chained Echoes",
        "Starcraft 2",
        "UFO 50",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Sonic Heroes",
        "Wargroove",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Adventure",
        "Don",
        "Brotato",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "bird": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "Banjo-Tooie",
        "TUNIC",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "SMZ3",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Inscryption",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Not an idle game",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "The Binding of Isaac Repentance",
        "Hylics 2",
        "Old School Runescape",
        "A Short Hike",
        "MegaMan Battle Network 3",
        "Pokemon Red and Blue",
        "Hades",
        "Super Mario Sunshine",
        "Overcooked! 2",
        "OpenRCT2",
        "Civilization VI",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "The Sims 4",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "An Untitled Story",
        "Diddy Kong Racing",
        "Chained Echoes",
        "Starcraft 2",
        "UFO 50",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Sonic Heroes",
        "Wargroove",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Adventure",
        "Don",
        "Brotato",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "view": [
        "Celeste",
        "VVVVVV",
        "TUNIC",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Digimon World",
        "Getting Over It",
        "Chrono Trigger Jets of Time",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "The Binding of Isaac Repentance",
        "Mega Man 2",
        "Noita",
        "Blasphemous",
        "The Sims 4",
        "Super Mario World",
        "Tyrian",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Wario Land",
        "Brotato",
        "Aquaria",
        "Wario Land 4",
        "Donkey Kong Country",
        "SMZ3",
        "A Link Between Worlds",
        "Cuphead",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "ANIMAL WELL",
        "Hades",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Diddy Kong Racing",
        "Starcraft 2",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Sonic Heroes",
        "The Legend of Zelda",
        "Tetris Attack",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Final Fantasy",
        "EarthBound",
        "Terraria",
        "Inscryption",
        "Hatsune Miku Project Diva Mega Mix+",
        "Pokemon Crystal",
        "Castlevania - Circle of the Moon",
        "Not an idle game",
        "Old School Runescape",
        "A Short Hike",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Kirby's Dream Land 3",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Wargroove 2",
        "Risk of Rain",
        "Super Metroid",
        "Yoshi's Island",
        "An Untitled Story",
        "Chained Echoes",
        "Factorio",
        "Donkey Kong Country 3",
        "Don",
        "The Legend of Zelda - Oracle of Ages",
        "Slay the Spire",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Super Metroid Map Rando",
        "DLCQuest",
        "Final Fantasy Tactics Advance",
        "Against the Storm",
        "Undertale",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Muse Dash",
        "Overcooked! 2",
        "OpenRCT2",
        "Civilization VI",
        "Factorio - Space Age Without Space",
        "Zillion",
        "Super Mario Land 2",
        "UFO 50",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Landstalker - The Treasures of King Nole",
        "Adventure",
        "Mario & Luigi Superstar Saga",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "/": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "TUNIC",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "SMZ3",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Inscryption",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Not an idle game",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "The Binding of Isaac Repentance",
        "Hylics 2",
        "Old School Runescape",
        "A Short Hike",
        "MegaMan Battle Network 3",
        "Pokemon Red and Blue",
        "Hades",
        "Super Mario Sunshine",
        "Overcooked! 2",
        "OpenRCT2",
        "Civilization VI",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "The Sims 4",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Diddy Kong Racing",
        "Chained Echoes",
        "Starcraft 2",
        "UFO 50",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Sonic Heroes",
        "Wargroove",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Adventure",
        "Don",
        "Brotato",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "isometric": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "TUNIC",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "SMZ3",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Inscryption",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Not an idle game",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "The Binding of Isaac Repentance",
        "Hylics 2",
        "Old School Runescape",
        "A Short Hike",
        "MegaMan Battle Network 3",
        "Pokemon Red and Blue",
        "Hades",
        "Super Mario Sunshine",
        "Overcooked! 2",
        "OpenRCT2",
        "Civilization VI",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "The Sims 4",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Diddy Kong Racing",
        "Chained Echoes",
        "Starcraft 2",
        "UFO 50",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Sonic Heroes",
        "Wargroove",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Adventure",
        "Don",
        "Brotato",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "fantasy": [
        "Celeste",
        "Skyward Sword",
        "VVVVVV",
        "TUNIC",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Super Mario 64",
        "Digimon World",
        "Twilight Princess",
        "Chrono Trigger Jets of Time",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Noita",
        "Blasphemous",
        "The Sims 4",
        "Super Mario World",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Wario Land",
        "Brotato",
        "SM64 Romhack",
        "Minecraft",
        "Subnautica",
        "Banjo-Tooie",
        "Aquaria",
        "Majora's Mask Recompiled",
        "Dark Souls Remastered",
        "ULTRAKILL",
        "Heretic",
        "A Link Between Worlds",
        "Cuphead",
        "Zork Grand Inquisitor",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "ANIMAL WELL",
        "Hades",
        "Risk of Rain 2",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Sonic Heroes",
        "Sea of Thieves",
        "The Legend of Zelda",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Final Fantasy",
        "Super Mario Odyssey",
        "EarthBound",
        "Terraria",
        "Kingdom Hearts 2",
        "Pokemon Crystal",
        "A Hat in Time",
        "Old School Runescape",
        "A Short Hike",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Wargroove 2",
        "Risk of Rain",
        "Hunie Pop",
        "Yoshi's Island",
        "Chained Echoes",
        "Dark Souls III",
        "Ratchet & Clank 2",
        "Don",
        "Slay the Spire",
        "Cat Quest",
        "A Link to the Past",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Outer Wilds",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Against the Storm",
        "Undertale",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Muse Dash",
        "Pseudoregalia",
        "Civilization VI",
        "Dark Souls II",
        "Jak and Daxter: The Precursor Legacy",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Star Wars Episode I Racer",
        "Yu-Gi-Oh! Forbidden Memories",
        "Landstalker - The Treasures of King Nole",
        "Adventure",
        "Mario & Luigi Superstar Saga"
    ],
    "1983": [
        "Adventure"
    ],
    "against the storm": [
        "Against the Storm"
    ],
    "mild blood": [
        "Kingdom Hearts 2",
        "Muse Dash",
        "Monster Sanctuary",
        "Hollow Knight",
        "Stardew Valley",
        "Brotato",
        "Risk of Rain",
        "Against the Storm",
        "Undertale"
    ],
    "mild": [
        "The Legend of Zelda - Oracle of Ages",
        "Celeste",
        "Subnautica",
        "The Legend of Zelda",
        "VVVVVV",
        "Monster Sanctuary",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "Hollow Knight",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "Faxanadu",
        "Super Metroid Map Rando",
        "Terraria",
        "Kingdom Hearts 2",
        "Cuphead",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Sonic Adventure 2 Battle",
        "ANIMAL WELL",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "MegaMan Battle Network 3",
        "Muse Dash",
        "Hades",
        "Donkey Kong Country 2",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Risk of Rain",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Super Metroid",
        "Ape Escape",
        "Final Fantasy Mystic Quest",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Star Wars Episode I Racer",
        "Landstalker - The Treasures of King Nole",
        "Wario Land",
        "Ratchet & Clank 2",
        "Sonic Heroes",
        "Brotato",
        "Secret of Evermore"
    ],
    "blood": [
        "Skyward Sword",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Xenoblade X",
        "Shivers",
        "Dark Souls Remastered",
        "Resident Evil 2 Remake",
        "ULTRAKILL",
        "Terraria",
        "Kingdom Hearts 2",
        "Inscryption",
        "Hatsune Miku Project Diva Mega Mix+",
        "Resident Evil 3 Remake",
        "Raft",
        "Twilight Princess",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Undertale",
        "The Binding of Isaac Repentance",
        "Ender Lilies",
        "DOOM II",
        "Muse Dash",
        "Hades",
        "Risk of Rain 2",
        "Castlevania 64",
        "Risk of Rain",
        "Blasphemous",
        "Dark Souls II",
        "Dark Souls III",
        "Starcraft 2",
        "DOOM 1993",
        "Factorio",
        "Ratchet & Clank 2",
        "Brotato"
    ],
    "alcohol reference": [
        "The Witness",
        "Outer Wilds",
        "Celeste",
        "Terraria",
        "Hades",
        "Final Fantasy Tactics Advance",
        "Risk of Rain",
        "Against the Storm"
    ],
    "alcohol": [
        "The Witness",
        "Outer Wilds",
        "Celeste",
        "Starcraft 2",
        "Terraria",
        "Kingdom Hearts 2",
        "Hades",
        "Cuphead",
        "Final Fantasy Tactics Advance",
        "Xenoblade X",
        "Stardew Valley",
        "Zork Grand Inquisitor",
        "Chrono Trigger Jets of Time",
        "Risk of Rain",
        "Against the Storm",
        "Sea of Thieves"
    ],
    "reference": [
        "The Witness",
        "Outer Wilds",
        "Celeste",
        "Terraria",
        "DOOM II",
        "Rogue Legacy",
        "Hades",
        "Monster Sanctuary",
        "Donkey Kong Country 2",
        "Ocarina of Time",
        "Risk of Rain 2",
        "Spyro 3",
        "Final Fantasy Tactics Advance",
        "Risk of Rain",
        "Against the Storm"
    ],
    "use of tobacco": [
        "Stardew Valley",
        "Faxanadu",
        "Against the Storm",
        "Undertale"
    ],
    "use": [
        "Faxanadu",
        "Starcraft 2",
        "Terraria",
        "Kingdom Hearts 2",
        "Cuphead",
        "Xenoblade X",
        "Zork Grand Inquisitor",
        "Stardew Valley",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Sea of Thieves",
        "Undertale"
    ],
    "of": [
        "The Legend of Zelda - Oracle of Ages",
        "Star Fox 64",
        "Symphony of the Night",
        "A Link to the Past",
        "Luigi's Mansion",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Donkey Kong Country",
        "Faxanadu",
        "EarthBound",
        "Terraria",
        "Kingdom Hearts 2",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Zork Grand Inquisitor",
        "Stardew Valley",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Undertale",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Ori and the Blind Forest",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Ocarina of Time",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Sea of Thieves"
    ],
    "tobacco": [
        "Faxanadu",
        "Starcraft 2",
        "Monster Sanctuary",
        "Cuphead",
        "Zork Grand Inquisitor",
        "Stardew Valley",
        "Against the Storm",
        "Undertale"
    ],
    "language": [
        "Celeste",
        "Subnautica",
        "VVVVVV",
        "Xenoblade X",
        "The Messenger",
        "Resident Evil 2 Remake",
        "Inscryption",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "CrossCode",
        "Undertale",
        "Against the Storm",
        "Hades",
        "Timespinner",
        "Risk of Rain",
        "Dark Souls II",
        "Chained Echoes",
        "Starcraft 2",
        "Ratchet & Clank 2"
    ],
    "fantasy violence": [
        "Celeste",
        "Minecraft",
        "Subnautica",
        "Cat Quest",
        "Skyward Sword",
        "Monster Sanctuary",
        "TUNIC",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "The Messenger",
        "Outer Wilds",
        "Digimon World",
        "A Link Between Worlds",
        "Cuphead",
        "Twilight Princess",
        "Stardew Valley",
        "CrossCode",
        "A Hat in Time",
        "Against the Storm",
        "Undertale",
        "Metroid Zero Mission",
        "Muse Dash",
        "Risk of Rain 2",
        "Timespinner",
        "Wargroove 2",
        "Risk of Rain",
        "Jak and Daxter: The Precursor Legacy",
        "Wargroove",
        "Rogue Legacy",
        "Ratchet & Clank 2",
        "Don",
        "Brotato"
    ],
    "violence": [
        "Celeste",
        "Star Fox 64",
        "Skyward Sword",
        "VVVVVV",
        "TUNIC",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Digimon World",
        "Twilight Princess",
        "Chrono Trigger Jets of Time",
        "Sonic Adventure 2 Battle",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "The Binding of Isaac Repentance",
        "Blasphemous",
        "The Sims 4",
        "Tyrian",
        "Ape Escape",
        "Final Fantasy Mystic Quest",
        "Wario Land",
        "Brotato",
        "Minecraft",
        "Subnautica",
        "Banjo-Tooie",
        "Majora's Mask Recompiled",
        "Dark Souls Remastered",
        "ULTRAKILL",
        "Sonic Adventure DX",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Raft",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "CrossCode",
        "ANIMAL WELL",
        "Hades",
        "Risk of Rain 2",
        "Castlevania 64",
        "Zelda II: The Adventure of Link",
        "Starcraft 2",
        "DOOM 1993",
        "Ocarina of Time",
        "Toontown",
        "Sonic Heroes",
        "Sea of Thieves",
        "The Legend of Zelda",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Xenoblade X",
        "Final Fantasy",
        "Super Mario Odyssey",
        "Resident Evil 2 Remake",
        "Terraria",
        "Kingdom Hearts 2",
        "Inscryption",
        "Hatsune Miku Project Diva Mega Mix+",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Wargroove 2",
        "Risk of Rain",
        "Super Metroid",
        "Dark Souls III",
        "Factorio",
        "Sly Cooper and the Thievius Raccoonus",
        "Ratchet & Clank 2",
        "Don",
        "The Legend of Zelda - Oracle of Ages",
        "Cat Quest",
        "A Link to the Past",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Outer Wilds",
        "Super Metroid Map Rando",
        "Metroid Prime",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Against the Storm",
        "Undertale",
        "DOOM II",
        "Muse Dash",
        "Civilization VI",
        "Dark Souls II",
        "Jak and Daxter: The Precursor Legacy",
        "Wargroove",
        "Star Wars Episode I Racer",
        "Rogue Legacy",
        "Yu-Gi-Oh! Forbidden Memories",
        "Landstalker - The Treasures of King Nole",
        "Secret of Evermore"
    ],
    "real time strategy (rts)": [
        "Starcraft 2",
        "OpenRCT2",
        "Against the Storm"
    ],
    "real": [
        "Starcraft 2",
        "OpenRCT2",
        "Against the Storm"
    ],
    "time": [
        "The Legend of Zelda - Oracle of Ages",
        "VVVVVV",
        "A Link to the Past",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "The Legend of Zelda - Oracle of Seasons",
        "Outer Wilds",
        "EarthBound",
        "Super Metroid Map Rando",
        "Pokemon Crystal",
        "Metroid Prime",
        "Final Fantasy Tactics Advance",
        "A Hat in Time",
        "Chrono Trigger Jets of Time",
        "Against the Storm",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "The Witness",
        "Mario Kart 64",
        "Super Mario Sunshine",
        "Castlevania 64",
        "OpenRCT2",
        "Timespinner",
        "Risk of Rain",
        "Super Metroid",
        "Ape Escape",
        "Diddy Kong Racing",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Ocarina of Time",
        "Pokemon Emerald",
        "Spyro 3"
    ],
    "strategy": [
        "Slay the Spire",
        "Monster Sanctuary",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "EarthBound",
        "Terraria",
        "Inscryption",
        "Final Fantasy Tactics Advance",
        "Stardew Valley",
        "Dungeon Clawler",
        "Against the Storm",
        "Not an idle game",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Undertale",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Overcooked! 2",
        "OpenRCT2",
        "Paper Mario",
        "Civilization VI",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Yu-Gi-Oh! 2006",
        "Hunie Pop",
        "Balatro",
        "Chained Echoes",
        "Hunie Pop 2",
        "Starcraft 2",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "UFO 50",
        "Wargroove",
        "Pokemon Emerald",
        "Yu-Gi-Oh! Forbidden Memories",
        "Don"
    ],
    "(rts)": [
        "Starcraft 2",
        "OpenRCT2",
        "Against the Storm"
    ],
    "simulator": [
        "Minecraft",
        "Outer Wilds",
        "Terraria",
        "Getting Over It",
        "Raft",
        "Stardew Valley",
        "Dungeon Clawler",
        "Not an idle game",
        "Against the Storm",
        "Overcooked! 2",
        "OpenRCT2",
        "DORONKO WANKO",
        "Civilization VI",
        "Noita",
        "Factorio - Space Age Without Space",
        "The Sims 4",
        "Hunie Pop",
        "Hunie Pop 2",
        "Factorio",
        "Don",
        "Sea of Thieves"
    ],
    "indie": [
        "Slay the Spire",
        "Celeste",
        "Subnautica",
        "Aquaria",
        "Cat Quest",
        "VVVVVV",
        "Monster Sanctuary",
        "TUNIC",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "The Messenger",
        "Shivers",
        "Outer Wilds",
        "ULTRAKILL",
        "osu!",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Inscryption",
        "Cuphead",
        "Raft",
        "Celeste 64",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "A Hat in Time",
        "Against the Storm",
        "Not an idle game",
        "ANIMAL WELL",
        "Undertale",
        "The Binding of Isaac Repentance",
        "The Witness",
        "Hylics 2",
        "A Short Hike",
        "Lethal Company",
        "Ender Lilies",
        "Muse Dash",
        "Hades",
        "Risk of Rain 2",
        "Overcooked! 2",
        "Pseudoregalia",
        "Timespinner",
        "Wargroove 2",
        "Factorio - Space Age Without Space",
        "Blasphemous",
        "Noita",
        "Peaks of Yore",
        "Risk of Rain",
        "Hunie Pop",
        "Balatro",
        "An Untitled Story",
        "Chained Echoes",
        "Hunie Pop 2",
        "UFO 50",
        "Factorio",
        "Wargroove",
        "Rogue Legacy",
        "Don",
        "Brotato"
    ],
    "roguelite": [
        "Hades",
        "Risk of Rain 2",
        "Risk of Rain",
        "Dungeon Clawler",
        "Brotato",
        "Noita",
        "Against the Storm"
    ],
    "2023": [
        "Lethal Company",
        "Peaks of Yore",
        "Pseudoregalia",
        "Bumper Stickers",
        "Bomb Rush Cyberfunk",
        "Wargroove 2",
        "Brotato",
        "Against the Storm"
    ],
    "a hat in time": [
        "A Hat in Time"
    ],
    "first person": [
        "Minecraft",
        "Subnautica",
        "Star Fox 64",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Shivers",
        "Outer Wilds",
        "EarthBound",
        "ULTRAKILL",
        "Trackmania",
        "Heretic",
        "Inscryption",
        "Raft",
        "Metroid Prime",
        "Zork Grand Inquisitor",
        "A Hat in Time",
        "The Witness",
        "Hylics 2",
        "Lethal Company",
        "DOOM II",
        "Castlevania 64",
        "The Sims 4",
        "Hunie Pop",
        "Hunie Pop 2",
        "DOOM 1993",
        "Star Wars Episode I Racer",
        "Yu-Gi-Oh! Forbidden Memories",
        "Lingo",
        "Sea of Thieves"
    ],
    "first": [
        "Minecraft",
        "Subnautica",
        "Star Fox 64",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Shivers",
        "Outer Wilds",
        "EarthBound",
        "ULTRAKILL",
        "Trackmania",
        "Heretic",
        "Inscryption",
        "Raft",
        "Metroid Prime",
        "Zork Grand Inquisitor",
        "A Hat in Time",
        "The Witness",
        "Hylics 2",
        "Lethal Company",
        "DOOM II",
        "Castlevania 64",
        "The Sims 4",
        "Hunie Pop",
        "Hunie Pop 2",
        "DOOM 1993",
        "Star Wars Episode I Racer",
        "Yu-Gi-Oh! Forbidden Memories",
        "Lingo",
        "Sea of Thieves"
    ],
    "person": [
        "Minecraft",
        "Subnautica",
        "Banjo-Tooie",
        "Star Fox 64",
        "Cat Quest",
        "Skyward Sword",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Shivers",
        "Dark Souls Remastered",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Outer Wilds",
        "Resident Evil 2 Remake",
        "Super Mario 64",
        "Super Mario Odyssey",
        "ULTRAKILL",
        "Digimon World",
        "Getting Over It",
        "Kingdom Hearts 2",
        "Heretic",
        "Inscryption",
        "A Link Between Worlds",
        "Hatsune Miku Project Diva Mega Mix+",
        "Resident Evil 3 Remake",
        "Raft",
        "Metroid Prime",
        "Sonic Adventure DX",
        "Twilight Princess",
        "Celeste 64",
        "Bomb Rush Cyberfunk",
        "The Wind Waker",
        "Zork Grand Inquisitor",
        "A Hat in Time",
        "Sonic Adventure 2 Battle",
        "The Witness",
        "Hylics 2",
        "Lethal Company",
        "Mario Kart 64",
        "Trackmania",
        "DOOM II",
        "Risk of Rain 2",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Pseudoregalia",
        "Paper Mario",
        "The Sims 4",
        "Dark Souls II",
        "Hunie Pop",
        "Ape Escape",
        "Diddy Kong Racing",
        "Hunie Pop 2",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "gzDoom",
        "Sly Cooper and the Thievius Raccoonus",
        "Star Wars Episode I Racer",
        "Ocarina of Time",
        "Toontown",
        "Yu-Gi-Oh! Forbidden Memories",
        "Ratchet & Clank 2",
        "Lingo",
        "Sonic Heroes",
        "SM64 Romhack",
        "Spyro 3",
        "Sea of Thieves",
        "Secret of Evermore"
    ],
    "third person": [
        "Minecraft",
        "Banjo-Tooie",
        "Star Fox 64",
        "Cat Quest",
        "Skyward Sword",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Dark Souls Remastered",
        "Golden Sun The Lost Age",
        "Resident Evil 2 Remake",
        "Super Mario 64",
        "Super Mario Odyssey",
        "Digimon World",
        "Getting Over It",
        "Kingdom Hearts 2",
        "Sonic Adventure DX",
        "Hatsune Miku Project Diva Mega Mix+",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Trackmania",
        "Raft",
        "Twilight Princess",
        "The Wind Waker",
        "Celeste 64",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "Sonic Adventure 2 Battle",
        "Hylics 2",
        "Mario Kart 64",
        "Risk of Rain 2",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Pseudoregalia",
        "Paper Mario",
        "The Sims 4",
        "Dark Souls II",
        "Ape Escape",
        "Diddy Kong Racing",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "gzDoom",
        "Sly Cooper and the Thievius Raccoonus",
        "Star Wars Episode I Racer",
        "Ocarina of Time",
        "Toontown",
        "Ratchet & Clank 2",
        "Sonic Heroes",
        "SM64 Romhack",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "third": [
        "Minecraft",
        "Banjo-Tooie",
        "Star Fox 64",
        "Cat Quest",
        "Skyward Sword",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Dark Souls Remastered",
        "Golden Sun The Lost Age",
        "Resident Evil 2 Remake",
        "Super Mario 64",
        "Super Mario Odyssey",
        "Digimon World",
        "Getting Over It",
        "Kingdom Hearts 2",
        "Sonic Adventure DX",
        "Hatsune Miku Project Diva Mega Mix+",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Trackmania",
        "Raft",
        "Twilight Princess",
        "The Wind Waker",
        "Celeste 64",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "Sonic Adventure 2 Battle",
        "Hylics 2",
        "Mario Kart 64",
        "Risk of Rain 2",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Pseudoregalia",
        "Paper Mario",
        "The Sims 4",
        "Dark Souls II",
        "Ape Escape",
        "Diddy Kong Racing",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "gzDoom",
        "Sly Cooper and the Thievius Raccoonus",
        "Star Wars Episode I Racer",
        "Ocarina of Time",
        "Toontown",
        "Ratchet & Clank 2",
        "Sonic Heroes",
        "SM64 Romhack",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "platform": [
        "Celeste",
        "Banjo-Tooie",
        "Aquaria",
        "Skyward Sword",
        "VVVVVV",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Momodora Moonlit Farewell",
        "Kirby 64 - The Crystal Shards",
        "Wario Land 4",
        "Hollow Knight",
        "Donkey Kong Country",
        "The Messenger",
        "SMZ3",
        "Faxanadu",
        "Super Mario Odyssey",
        "Super Metroid Map Rando",
        "Super Mario 64",
        "ULTRAKILL",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Sonic Adventure DX",
        "Cuphead",
        "Metroid Prime",
        "Celeste 64",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Sonic Adventure 2 Battle",
        "ANIMAL WELL",
        "Hylics 2",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Pseudoregalia",
        "Kirby's Dream Land 3",
        "Ori and the Blind Forest",
        "Timespinner",
        "Mega Man 2",
        "Risk of Rain",
        "Blasphemous",
        "Peaks of Yore",
        "Super Mario World",
        "Super Mario Land 2",
        "Super Metroid",
        "Ape Escape",
        "Yoshi's Island",
        "Zelda II: The Adventure of Link",
        "An Untitled Story",
        "Zillion",
        "UFO 50",
        "Jak and Daxter: The Precursor Legacy",
        "gzDoom",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Donkey Kong Country 3",
        "Wario Land",
        "Ratchet & Clank 2",
        "Sonic Heroes",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "action": [
        "Celeste",
        "Star Fox 64",
        "Skyward Sword",
        "VVVVVV",
        "TUNIC",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Super Mario 64",
        "Digimon World",
        "Getting Over It",
        "Trackmania",
        "Twilight Princess",
        "Chrono Trigger Jets of Time",
        "Sonic Adventure 2 Battle",
        "DORONKO WANKO",
        "Mega Man 2",
        "Noita",
        "Blasphemous",
        "The Sims 4",
        "Super Mario World",
        "Tyrian",
        "Ape Escape",
        "Final Fantasy Mystic Quest",
        "Wario Land",
        "Brotato",
        "SM64 Romhack",
        "Banjo-Tooie",
        "Luigi's Mansion",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "Donkey Kong Country",
        "SMZ3",
        "Dark Souls Remastered",
        "ULTRAKILL",
        "Sonic Adventure DX",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Bomb Rush Cyberfunk",
        "Dungeon Clawler",
        "CrossCode",
        "ANIMAL WELL",
        "Hades",
        "Risk of Rain 2",
        "Castlevania 64",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Diddy Kong Racing",
        "Starcraft 2",
        "DOOM 1993",
        "gzDoom",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Sonic Heroes",
        "Sea of Thieves",
        "The Legend of Zelda",
        "Tetris Attack",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "Xenoblade X",
        "Final Fantasy",
        "Super Mario Odyssey",
        "EarthBound",
        "Resident Evil 2 Remake",
        "Terraria",
        "Kingdom Hearts 2",
        "Pokemon Crystal",
        "Celeste 64",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Lethal Company",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Kirby's Dream Land 3",
        "Ori and the Blind Forest",
        "Timespinner",
        "Risk of Rain",
        "Peaks of Yore",
        "Super Metroid",
        "Yoshi's Island",
        "An Untitled Story",
        "Chained Echoes",
        "Dark Souls III",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 3",
        "Ratchet & Clank 2",
        "Don",
        "The Legend of Zelda - Oracle of Ages",
        "Cat Quest",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Outer Wilds",
        "Super Metroid Map Rando",
        "osu!",
        "DLCQuest",
        "Metroid Prime",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Mario Kart 64",
        "Pokemon Red and Blue",
        "DOOM II",
        "Muse Dash",
        "Overcooked! 2",
        "Pseudoregalia",
        "Dark Souls II",
        "Super Mario Land 2",
        "UFO 50",
        "Jak and Daxter: The Precursor Legacy",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Star Wars Episode I Racer",
        "Landstalker - The Treasures of King Nole",
        "Mario & Luigi Superstar Saga",
        "Spyro 3",
        "Secret of Evermore"
    ],
    "time travel": [
        "The Legend of Zelda - Oracle of Ages",
        "Ape Escape",
        "EarthBound",
        "Outer Wilds",
        "Ocarina of Time",
        "Majora's Mask Recompiled",
        "Timespinner",
        "A Hat in Time",
        "Chrono Trigger Jets of Time",
        "The Legend of Zelda - Oracle of Seasons",
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "travel": [
        "The Legend of Zelda - Oracle of Ages",
        "Ape Escape",
        "EarthBound",
        "Outer Wilds",
        "DOOM II",
        "A Link Between Worlds",
        "A Link to the Past",
        "Ocarina of Time",
        "Majora's Mask Recompiled",
        "Timespinner",
        "A Hat in Time",
        "Chrono Trigger Jets of Time",
        "The Legend of Zelda - Oracle of Seasons",
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "spaceship": [
        "Star Fox 64",
        "Metroid Zero Mission",
        "VVVVVV",
        "Metroid Prime",
        "Civilization VI",
        "A Hat in Time"
    ],
    "female protagonist": [
        "Super Metroid",
        "Celeste",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Short Hike",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Celeste 64",
        "Timespinner",
        "A Hat in Time",
        "Undertale"
    ],
    "female": [
        "Super Metroid",
        "Celeste",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Short Hike",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Celeste 64",
        "Timespinner",
        "A Hat in Time",
        "Undertale"
    ],
    "protagonist": [
        "The Legend of Zelda - Oracle of Ages",
        "Celeste",
        "Skyward Sword",
        "Kingdom Hearts",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "Hollow Knight",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Super Metroid Map Rando",
        "ULTRAKILL",
        "Metroid Prime",
        "Celeste 64",
        "A Hat in Time",
        "Undertale",
        "A Short Hike",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Paper Mario",
        "Timespinner",
        "Blasphemous",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Mario & Luigi Superstar Saga"
    ],
    "action-adventure": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Banjo-Tooie",
        "Aquaria",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Luigi's Mansion",
        "Hollow Knight",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Terraria",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Wind Waker",
        "CrossCode",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Timespinner",
        "Zelda II: The Adventure of Link",
        "Zillion",
        "Dark Souls II",
        "Super Metroid",
        "An Untitled Story",
        "Dark Souls III",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Don",
        "Sea of Thieves"
    ],
    "cute": [
        "Celeste",
        "A Short Hike",
        "Muse Dash",
        "TUNIC",
        "A Hat in Time",
        "Undertale",
        "The Sims 4",
        "ANIMAL WELL"
    ],
    "snow": [
        "Golden Sun The Lost Age",
        "Celeste",
        "Minecraft",
        "Diddy Kong Racing",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "A Hat in Time",
        "A Link Between Worlds",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country"
    ],
    "wall jump": [
        "Super Metroid",
        "Super Mario Odyssey",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Ori and the Blind Forest",
        "A Hat in Time",
        "Castlevania - Circle of the Moon"
    ],
    "wall": [
        "Banjo-Tooie",
        "Kingdom Hearts",
        "Donkey Kong Country",
        "Super Mario Odyssey",
        "Super Metroid Map Rando",
        "Final Fantasy Tactics Advance",
        "A Hat in Time",
        "Castlevania - Circle of the Moon",
        "Undertale",
        "Mario Kart 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Ori and the Blind Forest",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Mario & Luigi Superstar Saga"
    ],
    "jump": [
        "Super Metroid",
        "Super Mario Odyssey",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Super Mario Sunshine",
        "Ori and the Blind Forest",
        "A Hat in Time",
        "Castlevania - Circle of the Moon"
    ],
    "3d platformer": [
        "Super Mario Odyssey",
        "Super Mario 64",
        "A Short Hike",
        "Sonic Heroes",
        "Super Mario Sunshine",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "SM64 Romhack"
    ],
    "3d": [
        "Minecraft",
        "Star Fox 64",
        "Skyward Sword",
        "VVVVVV",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Kirby 64 - The Crystal Shards",
        "TUNIC",
        "Xenoblade X",
        "Dark Souls Remastered",
        "Super Mario Odyssey",
        "Super Mario 64",
        "Digimon World",
        "A Link Between Worlds",
        "Metroid Prime",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "The Witness",
        "Hylics 2",
        "A Short Hike",
        "Mario Kart 64",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Dark Souls II",
        "Ape Escape",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Ocarina of Time",
        "Lingo",
        "Sonic Heroes",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "platformer": [
        "Super Mario Odyssey",
        "Super Mario 64",
        "Hylics 2",
        "A Short Hike",
        "Sonic Heroes",
        "VVVVVV",
        "Super Mario Sunshine",
        "Hollow Knight",
        "Bomb Rush Cyberfunk",
        "A Hat in Time",
        "SM64 Romhack",
        "Blasphemous"
    ],
    "swimming": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Subnautica",
        "Banjo-Tooie",
        "Aquaria",
        "Kingdom Hearts",
        "A Link to the Past",
        "Wario Land 4",
        "Donkey Kong Country",
        "Super Mario Odyssey",
        "Super Mario 64",
        "Terraria",
        "A Link Between Worlds",
        "A Hat in Time",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 3",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "steam greenlight": [
        "A Hat in Time",
        "DLCQuest",
        "Timespinner",
        "Risk of Rain"
    ],
    "steam": [
        "A Hat in Time",
        "DLCQuest",
        "Timespinner",
        "Risk of Rain"
    ],
    "greenlight": [
        "A Hat in Time",
        "DLCQuest",
        "Timespinner",
        "Risk of Rain"
    ],
    "crowdfunding": [
        "A Hat in Time",
        "Hollow Knight",
        "Timespinner",
        "CrossCode",
        "Risk of Rain"
    ],
    "crowd funded": [
        "A Hat in Time",
        "Hollow Knight",
        "Timespinner",
        "CrossCode",
        "Risk of Rain"
    ],
    "crowd": [
        "A Hat in Time",
        "Hollow Knight",
        "Timespinner",
        "CrossCode",
        "Risk of Rain"
    ],
    "funded": [
        "A Hat in Time",
        "Hollow Knight",
        "Timespinner",
        "CrossCode",
        "Risk of Rain"
    ],
    "collection marathon": [
        "Kirby 64 - The Crystal Shards",
        "A Hat in Time",
        "Banjo-Tooie",
        "Super Mario Sunshine"
    ],
    "collection": [
        "Kirby 64 - The Crystal Shards",
        "A Hat in Time",
        "Banjo-Tooie",
        "Super Mario Sunshine"
    ],
    "marathon": [
        "Kirby 64 - The Crystal Shards",
        "A Hat in Time",
        "Banjo-Tooie",
        "Super Mario Sunshine"
    ],
    "2017": [
        "Super Mario Odyssey",
        "Cat Quest",
        "Getting Over It",
        "Cuphead",
        "Hollow Knight",
        "A Hat in Time",
        "Sea of Thieves"
    ],
    "a link between worlds": [
        "A Link Between Worlds"
    ],
    "puzzle": [
        "The Legend of Zelda - Oracle of Ages",
        "Tetris Attack",
        "Skyward Sword",
        "VVVVVV",
        "Sudoku",
        "TUNIC",
        "A Link to the Past",
        "Wario Land 4",
        "Jigsaw",
        "The Legend of Zelda - Oracle of Seasons",
        "Paint",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Shivers",
        "Outer Wilds",
        "Inscryption",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Wind Waker",
        "Zork Grand Inquisitor",
        "CrossCode",
        "Not an idle game",
        "Undertale",
        "ANIMAL WELL",
        "The Witness",
        "DOOM II",
        "Castlevania 64",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Zillion",
        "Hunie Pop",
        "Candy Box 2",
        "Hunie Pop 2",
        "UFO 50",
        "Rogue Legacy",
        "Ocarina of Time",
        "Bumper Stickers",
        "Lingo",
        "Spyro 3",
        "Paper Mario The Thousand Year Door"
    ],
    "role-playing (rpg)": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "Cat Quest",
        "Skyward Sword",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "TUNIC",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Final Fantasy",
        "Dark Souls Remastered",
        "Faxanadu",
        "EarthBound",
        "Golden Sun The Lost Age",
        "Digimon World",
        "Terraria",
        "Kingdom Hearts 2",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Twilight Princess",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Old School Runescape",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Pokemon Red and Blue",
        "Hades",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Timespinner",
        "Wargroove 2",
        "Noita",
        "Blasphemous",
        "Risk of Rain",
        "Dark Souls II",
        "The Sims 4",
        "Hunie Pop",
        "Final Fantasy Mystic Quest",
        "Zelda II: The Adventure of Link",
        "Candy Box 2",
        "Chained Echoes",
        "Dark Souls III",
        "UFO 50",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Toontown",
        "Brotato",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "role-playing": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "Cat Quest",
        "Skyward Sword",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "TUNIC",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Final Fantasy",
        "Dark Souls Remastered",
        "Faxanadu",
        "EarthBound",
        "Golden Sun The Lost Age",
        "Digimon World",
        "Terraria",
        "Kingdom Hearts 2",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Twilight Princess",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Old School Runescape",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Pokemon Red and Blue",
        "Hades",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Timespinner",
        "Wargroove 2",
        "Noita",
        "Blasphemous",
        "Risk of Rain",
        "Dark Souls II",
        "The Sims 4",
        "Hunie Pop",
        "Final Fantasy Mystic Quest",
        "Zelda II: The Adventure of Link",
        "Candy Box 2",
        "Chained Echoes",
        "Dark Souls III",
        "UFO 50",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Toontown",
        "Brotato",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "(rpg)": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "Cat Quest",
        "Skyward Sword",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Kingdom Hearts",
        "Final Fantasy IV Free Enterprise",
        "TUNIC",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Final Fantasy",
        "Dark Souls Remastered",
        "Faxanadu",
        "EarthBound",
        "Golden Sun The Lost Age",
        "Digimon World",
        "Terraria",
        "Kingdom Hearts 2",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Twilight Princess",
        "The Wind Waker",
        "Final Fantasy Tactics Advance",
        "Bomb Rush Cyberfunk",
        "Stardew Valley",
        "Dungeon Clawler",
        "CrossCode",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Old School Runescape",
        "MegaMan Battle Network 3",
        "Ender Lilies",
        "Pokemon Red and Blue",
        "Hades",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Timespinner",
        "Wargroove 2",
        "Noita",
        "Blasphemous",
        "Risk of Rain",
        "Dark Souls II",
        "The Sims 4",
        "Hunie Pop",
        "Final Fantasy Mystic Quest",
        "Zelda II: The Adventure of Link",
        "Candy Box 2",
        "Chained Echoes",
        "Dark Souls III",
        "UFO 50",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Emerald",
        "Toontown",
        "Brotato",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "historical": [
        "Candy Box 2",
        "Skyward Sword",
        "Heretic",
        "A Link Between Worlds",
        "Yu-Gi-Oh! Forbidden Memories",
        "Civilization VI",
        "Secret of Evermore"
    ],
    "sandbox": [
        "Faxanadu",
        "Super Mario Odyssey",
        "Minecraft",
        "Old School Runescape",
        "Terraria",
        "Factorio",
        "Super Mario Sunshine",
        "A Link Between Worlds",
        "Noita",
        "Landstalker - The Treasures of King Nole",
        "Ocarina of Time",
        "Zelda II: The Adventure of Link",
        "Xenoblade X",
        "Stardew Valley",
        "Don",
        "Factorio - Space Age Without Space",
        "Not an idle game",
        "The Sims 4"
    ],
    "open world": [
        "Minecraft",
        "Subnautica",
        "The Legend of Zelda",
        "Skyward Sword",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "SMZ3",
        "Golden Sun The Lost Age",
        "Outer Wilds",
        "Super Mario 64",
        "Super Mario Odyssey",
        "Terraria",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Witness",
        "Old School Runescape",
        "A Short Hike",
        "Metroid Zero Mission",
        "Pokemon Red and Blue",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Toontown",
        "Lingo",
        "Don",
        "SM64 Romhack",
        "Sea of Thieves"
    ],
    "open": [
        "Minecraft",
        "Subnautica",
        "The Legend of Zelda",
        "Skyward Sword",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "SMZ3",
        "Golden Sun The Lost Age",
        "Outer Wilds",
        "Super Mario 64",
        "Super Mario Odyssey",
        "Terraria",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Witness",
        "Old School Runescape",
        "A Short Hike",
        "Metroid Zero Mission",
        "Pokemon Red and Blue",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Toontown",
        "Lingo",
        "Don",
        "SM64 Romhack",
        "Sea of Thieves"
    ],
    "world": [
        "Minecraft",
        "Subnautica",
        "The Legend of Zelda",
        "Aquaria",
        "Skyward Sword",
        "VVVVVV",
        "Symphony of the Night",
        "A Link to the Past",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "SMZ3",
        "Golden Sun The Lost Age",
        "Outer Wilds",
        "EarthBound",
        "Super Mario 64",
        "Super Mario Odyssey",
        "Terraria",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Metroid Prime",
        "The Witness",
        "Old School Runescape",
        "A Short Hike",
        "Metroid Zero Mission",
        "DOOM II",
        "Pokemon Red and Blue",
        "Donkey Kong Country 2",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Toontown",
        "Donkey Kong Country 3",
        "Lingo",
        "Don",
        "SM64 Romhack",
        "Sea of Thieves"
    ],
    "medieval": [
        "Candy Box 2",
        "Dark Souls III",
        "Secret of Evermore",
        "Skyward Sword",
        "Heretic",
        "Rogue Legacy",
        "A Link Between Worlds",
        "Dark Souls II"
    ],
    "magic": [
        "Aquaria",
        "Symphony of the Night",
        "A Link to the Past",
        "The Legend of Zelda - Oracle of Seasons",
        "Dark Souls Remastered",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "Terraria",
        "Heretic",
        "A Link Between Worlds",
        "Cuphead",
        "Final Fantasy Tactics Advance",
        "Zork Grand Inquisitor",
        "Castlevania - Circle of the Moon",
        "Chrono Trigger Jets of Time",
        "Castlevania 64",
        "Noita",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Candy Box 2",
        "Rogue Legacy",
        "Link's Awakening DX"
    ],
    "minigames": [
        "The Legend of Zelda - Oracle of Ages",
        "Golden Sun The Lost Age",
        "Ape Escape",
        "Rogue Legacy",
        "A Link Between Worlds",
        "Kingdom Hearts",
        "Kirby 64 - The Crystal Shards",
        "Ocarina of Time",
        "Donkey Kong Country 3",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Toontown",
        "Wario Land 4",
        "Spyro 3"
    ],
    "2.5d": [
        "DOOM 1993",
        "DOOM II",
        "Heretic",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "archery": [
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Wind Waker",
        "Majora's Mask Recompiled"
    ],
    "fairy": [
        "The Legend of Zelda - Oracle of Ages",
        "The Legend of Zelda",
        "Hunie Pop 2",
        "Terraria",
        "A Link Between Worlds",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "Ocarina of Time",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "Stardew Valley",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "princess": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Mario 64",
        "Mario Kart 64",
        "The Legend of Zelda - Oracle of Seasons",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "Ocarina of Time",
        "Paper Mario",
        "SM64 Romhack",
        "Mario & Luigi Superstar Saga",
        "Super Mario World"
    ],
    "sequel": [
        "Banjo-Tooie",
        "A Link to the Past",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "Golden Sun The Lost Age",
        "Super Mario Odyssey",
        "Digimon World",
        "A Link Between Worlds",
        "Final Fantasy Tactics Advance",
        "Hylics 2",
        "Mario Kart 64",
        "DOOM II",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Civilization VI",
        "Mega Man 2",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Dark Souls III",
        "Ocarina of Time",
        "Don"
    ],
    "sword & sorcery": [
        "The Legend of Zelda - Oracle of Ages",
        "Final Fantasy Mystic Quest",
        "Dark Souls III",
        "Terraria",
        "Skyward Sword",
        "Heretic",
        "A Link Between Worlds",
        "A Link to the Past",
        "Kingdom Hearts",
        "Link's Awakening DX",
        "Ocarina of Time",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "The Legend of Zelda - Oracle of Seasons",
        "Spyro 3",
        "Dark Souls II"
    ],
    "sword": [
        "The Legend of Zelda - Oracle of Ages",
        "Final Fantasy Mystic Quest",
        "Dark Souls III",
        "Terraria",
        "Skyward Sword",
        "Heretic",
        "A Link Between Worlds",
        "A Link to the Past",
        "Kingdom Hearts",
        "Link's Awakening DX",
        "Ocarina of Time",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "The Legend of Zelda - Oracle of Seasons",
        "Spyro 3",
        "Dark Souls II"
    ],
    "&": [
        "The Legend of Zelda - Oracle of Ages",
        "Slay the Spire",
        "Skyward Sword",
        "Kingdom Hearts",
        "A Link to the Past",
        "Yacht Dice",
        "Majora's Mask Recompiled",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Terraria",
        "Heretic",
        "Inscryption",
        "A Link Between Worlds",
        "The Wind Waker",
        "Dark Souls II",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Dark Souls III",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Yu-Gi-Oh! Forbidden Memories",
        "Spyro 3"
    ],
    "sorcery": [
        "The Legend of Zelda - Oracle of Ages",
        "Final Fantasy Mystic Quest",
        "Dark Souls III",
        "Terraria",
        "Skyward Sword",
        "Heretic",
        "A Link Between Worlds",
        "A Link to the Past",
        "Kingdom Hearts",
        "Link's Awakening DX",
        "Ocarina of Time",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "The Legend of Zelda - Oracle of Seasons",
        "Spyro 3",
        "Dark Souls II"
    ],
    "darkness": [
        "The Witness",
        "Super Metroid",
        "EarthBound",
        "Minecraft",
        "Super Metroid Map Rando",
        "Aquaria",
        "Terraria",
        "DOOM II",
        "Rogue Legacy",
        "A Link Between Worlds",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Luigi's Mansion",
        "Donkey Kong Country",
        "Zelda II: The Adventure of Link"
    ],
    "digital distribution": [
        "Celeste",
        "Minecraft",
        "Banjo-Tooie",
        "VVVVVV",
        "Symphony of the Night",
        "TUNIC",
        "Wario Land 4",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Heretic",
        "A Link Between Worlds",
        "Cuphead",
        "CrossCode",
        "The Witness",
        "DOOM II",
        "Muse Dash",
        "Donkey Kong Country 2",
        "Civilization VI",
        "Ori and the Blind Forest",
        "Timespinner",
        "Super Mario World",
        "Ape Escape",
        "Yoshi's Island",
        "Hunie Pop 2",
        "UFO 50",
        "Factorio",
        "Rogue Legacy",
        "Link's Awakening DX",
        "Don",
        "Mario & Luigi Superstar Saga",
        "Sea of Thieves"
    ],
    "digital": [
        "Celeste",
        "Minecraft",
        "Banjo-Tooie",
        "VVVVVV",
        "Symphony of the Night",
        "TUNIC",
        "Wario Land 4",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Heretic",
        "A Link Between Worlds",
        "Cuphead",
        "CrossCode",
        "The Witness",
        "DOOM II",
        "Muse Dash",
        "Donkey Kong Country 2",
        "Civilization VI",
        "Ori and the Blind Forest",
        "Timespinner",
        "Super Mario World",
        "Ape Escape",
        "Yoshi's Island",
        "Hunie Pop 2",
        "UFO 50",
        "Factorio",
        "Rogue Legacy",
        "Link's Awakening DX",
        "Don",
        "Mario & Luigi Superstar Saga",
        "Sea of Thieves"
    ],
    "distribution": [
        "Celeste",
        "Minecraft",
        "Banjo-Tooie",
        "VVVVVV",
        "Symphony of the Night",
        "TUNIC",
        "Wario Land 4",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Heretic",
        "A Link Between Worlds",
        "Cuphead",
        "CrossCode",
        "The Witness",
        "DOOM II",
        "Muse Dash",
        "Donkey Kong Country 2",
        "Civilization VI",
        "Ori and the Blind Forest",
        "Timespinner",
        "Super Mario World",
        "Ape Escape",
        "Yoshi's Island",
        "Hunie Pop 2",
        "UFO 50",
        "Factorio",
        "Rogue Legacy",
        "Link's Awakening DX",
        "Don",
        "Mario & Luigi Superstar Saga",
        "Sea of Thieves"
    ],
    "anthropomorphism": [
        "The Legend of Zelda - Oracle of Ages",
        "Banjo-Tooie",
        "Star Fox 64",
        "Kingdom Hearts",
        "TUNIC",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "A Link Between Worlds",
        "Cuphead",
        "Undertale",
        "Mario Kart 64",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Paper Mario",
        "Ape Escape",
        "Diddy Kong Racing",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "polygonal 3d": [
        "Minecraft",
        "Star Fox 64",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Kirby 64 - The Crystal Shards",
        "Xenoblade X",
        "Digimon World",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Witness",
        "Mario Kart 64",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Ocarina of Time",
        "Spyro 3"
    ],
    "polygonal": [
        "Minecraft",
        "Star Fox 64",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Kirby 64 - The Crystal Shards",
        "Xenoblade X",
        "Digimon World",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Witness",
        "Mario Kart 64",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Ocarina of Time",
        "Spyro 3"
    ],
    "bow and arrow": [
        "Minecraft",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "A Link Between Worlds",
        "A Link to the Past",
        "Link's Awakening DX",
        "Cuphead",
        "Ocarina of Time",
        "Final Fantasy Tactics Advance",
        "Risk of Rain",
        "Dark Souls II"
    ],
    "bow": [
        "Minecraft",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "A Link Between Worlds",
        "A Link to the Past",
        "Link's Awakening DX",
        "Cuphead",
        "Ocarina of Time",
        "Final Fantasy Tactics Advance",
        "Risk of Rain",
        "Dark Souls II"
    ],
    "and": [
        "Minecraft",
        "Skyward Sword",
        "Symphony of the Night",
        "A Link to the Past",
        "The Legend of Zelda - Oracle of Seasons",
        "Shivers",
        "Dark Souls Remastered",
        "Resident Evil 2 Remake",
        "ULTRAKILL",
        "Terraria",
        "A Link Between Worlds",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Final Fantasy Tactics Advance",
        "Zork Grand Inquisitor",
        "Stardew Valley",
        "The Binding of Isaac Repentance",
        "DOOM II",
        "Hades",
        "Castlevania 64",
        "OpenRCT2",
        "Civilization VI",
        "Risk of Rain",
        "Blasphemous",
        "Dark Souls II",
        "Starcraft 2",
        "DOOM 1993",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX"
    ],
    "arrow": [
        "Minecraft",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "A Link Between Worlds",
        "A Link to the Past",
        "Link's Awakening DX",
        "Cuphead",
        "Ocarina of Time",
        "Final Fantasy Tactics Advance",
        "Risk of Rain",
        "Dark Souls II"
    ],
    "damsel in distress": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "A Link to the Past",
        "A Link Between Worlds",
        "Ocarina of Time",
        "Metroid Prime",
        "Paper Mario",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Super Mario World"
    ],
    "damsel": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "A Link to the Past",
        "A Link Between Worlds",
        "Ocarina of Time",
        "Metroid Prime",
        "Paper Mario",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Super Mario World"
    ],
    "in": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "Kingdom Hearts",
        "A Link to the Past",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Mario Odyssey",
        "EarthBound",
        "Super Metroid Map Rando",
        "Super Mario 64",
        "A Link Between Worlds",
        "Metroid Prime",
        "Super Mario Sunshine",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Super Mario World",
        "Super Metroid",
        "Dark Souls III",
        "Ocarina of Time",
        "SM64 Romhack"
    ],
    "distress": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "A Link to the Past",
        "A Link Between Worlds",
        "Ocarina of Time",
        "Metroid Prime",
        "Paper Mario",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Super Mario World"
    ],
    "upgradeable weapons": [
        "Metroid Zero Mission",
        "A Link Between Worlds",
        "Castlevania 64",
        "Metroid Prime",
        "Mega Man 2",
        "Dark Souls II"
    ],
    "upgradeable": [
        "Metroid Zero Mission",
        "A Link Between Worlds",
        "Castlevania 64",
        "Metroid Prime",
        "Mega Man 2",
        "Dark Souls II"
    ],
    "weapons": [
        "Metroid Zero Mission",
        "A Link Between Worlds",
        "Castlevania 64",
        "Metroid Prime",
        "Mega Man 2",
        "Dark Souls II"
    ],
    "disorientation zone": [
        "The Legend of Zelda - Oracle of Ages",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "disorientation": [
        "The Legend of Zelda - Oracle of Ages",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "zone": [
        "The Legend of Zelda - Oracle of Ages",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "descendants of other characters": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "Star Fox 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Luigi's Mansion",
        "Donkey Kong Country 3",
        "Ocarina of Time",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Donkey Kong Country"
    ],
    "descendants": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "Star Fox 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Luigi's Mansion",
        "Donkey Kong Country 3",
        "Ocarina of Time",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Donkey Kong Country"
    ],
    "other": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "Star Fox 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Luigi's Mansion",
        "Donkey Kong Country 3",
        "Ocarina of Time",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Donkey Kong Country"
    ],
    "characters": [
        "The Legend of Zelda - Oracle of Ages",
        "Star Fox 64",
        "Symphony of the Night",
        "Luigi's Mansion",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Donkey Kong Country",
        "EarthBound",
        "Terraria",
        "A Link Between Worlds",
        "Stardew Valley",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Dark Souls II",
        "Dark Souls III",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 3"
    ],
    "save point": [
        "Aquaria",
        "VVVVVV",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Donkey Kong Country",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link Between Worlds",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Paper Mario",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Donkey Kong Country 3",
        "Mario & Luigi Superstar Saga"
    ],
    "save": [
        "Aquaria",
        "VVVVVV",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Donkey Kong Country",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link Between Worlds",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Paper Mario",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Donkey Kong Country 3",
        "Mario & Luigi Superstar Saga"
    ],
    "point": [
        "Aquaria",
        "VVVVVV",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "Donkey Kong Country",
        "Faxanadu",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link Between Worlds",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Paper Mario",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Donkey Kong Country 3",
        "Mario & Luigi Superstar Saga"
    ],
    "stereoscopic 3d": [
        "Minecraft",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "A Link Between Worlds",
        "Luigi's Mansion"
    ],
    "stereoscopic": [
        "Minecraft",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "A Link Between Worlds",
        "Luigi's Mansion"
    ],
    "side quests": [
        "The Legend of Zelda - Oracle of Ages",
        "Starcraft 2",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Dark Souls II"
    ],
    "side": [
        "The Legend of Zelda - Oracle of Ages",
        "Slay the Spire",
        "Celeste",
        "Aquaria",
        "Tetris Attack",
        "VVVVVV",
        "Symphony of the Night",
        "Monster Sanctuary",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "Kirby 64 - The Crystal Shards",
        "Momodora Moonlit Farewell",
        "Wario Land 4",
        "Hollow Knight",
        "Xenoblade X",
        "Donkey Kong Country",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Final Fantasy",
        "SMZ3",
        "Faxanadu",
        "Super Metroid Map Rando",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Hatsune Miku Project Diva Mega Mix+",
        "A Link Between Worlds",
        "Cuphead",
        "Pokemon Crystal",
        "Dungeon Clawler",
        "Castlevania - Circle of the Moon",
        "ANIMAL WELL",
        "Zillion",
        "Hylics 2",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Muse Dash",
        "Pokemon Red and Blue",
        "Donkey Kong Country 2",
        "Kirby's Dream Land 3",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Mega Man 2",
        "Wargroove 2",
        "Noita",
        "Blasphemous",
        "Risk of Rain",
        "Dark Souls II",
        "Super Mario Land 2",
        "Super Metroid",
        "Final Fantasy Mystic Quest",
        "Super Mario World",
        "Yoshi's Island",
        "An Untitled Story",
        "Zelda II: The Adventure of Link",
        "Starcraft 2",
        "UFO 50",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Wario Land",
        "Mario & Luigi Superstar Saga"
    ],
    "quests": [
        "The Legend of Zelda - Oracle of Ages",
        "Starcraft 2",
        "A Link Between Worlds",
        "A Link to the Past",
        "Link's Awakening DX",
        "Ocarina of Time",
        "Metroid Prime",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Xenoblade X",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "potion": [
        "Golden Sun The Lost Age",
        "Minecraft",
        "Skyward Sword",
        "Rogue Legacy",
        "Kingdom Hearts",
        "A Link to the Past",
        "Link's Awakening DX",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "real-time combat": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Xenoblade X",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Super Mario 64",
        "A Link Between Worlds",
        "Metroid Prime",
        "DOOM II",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Super Metroid",
        "DOOM 1993",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "real-time": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Xenoblade X",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Super Mario 64",
        "A Link Between Worlds",
        "Metroid Prime",
        "DOOM II",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Super Metroid",
        "DOOM 1993",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "combat": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Skyward Sword",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Xenoblade X",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Super Mario 64",
        "A Link Between Worlds",
        "Metroid Prime",
        "DOOM II",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Super Metroid",
        "DOOM 1993",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Landstalker - The Treasures of King Nole",
        "SM64 Romhack",
        "Spyro 3"
    ],
    "self-referential humor": [
        "EarthBound",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "self-referential": [
        "EarthBound",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "humor": [
        "The Binding of Isaac Repentance",
        "EarthBound",
        "Banjo-Tooie",
        "The Sims 4",
        "Rogue Legacy",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Don",
        "The Messenger",
        "Mario & Luigi Superstar Saga",
        "Sea of Thieves"
    ],
    "multiple gameplay perspectives": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "multiple": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Star Fox 64",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Wario Land 4",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "EarthBound",
        "A Link Between Worlds",
        "Cuphead",
        "Metroid Prime",
        "Undertale",
        "The Witness",
        "Metroid Zero Mission",
        "DOOM II",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Civilization VI",
        "Ape Escape",
        "Rogue Legacy",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "gameplay": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Mario Odyssey",
        "Minecraft",
        "Super Mario 64",
        "Banjo-Tooie",
        "Subnautica",
        "Aquaria",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Super Mario Sunshine",
        "A Link Between Worlds",
        "Donkey Kong Country 2",
        "Kingdom Hearts",
        "Ocarina of Time",
        "Metroid Prime",
        "Mega Man 2",
        "Donkey Kong Country",
        "SM64 Romhack"
    ],
    "perspectives": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "A Link Between Worlds",
        "Metroid Prime",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "rpg elements": [
        "Minecraft",
        "Banjo-Tooie",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "A Link Between Worlds",
        "Ori and the Blind Forest",
        "Mario & Luigi Superstar Saga",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "rpg": [
        "Minecraft",
        "Banjo-Tooie",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "A Link Between Worlds",
        "Ori and the Blind Forest",
        "Mario & Luigi Superstar Saga",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "elements": [
        "Minecraft",
        "Banjo-Tooie",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "A Link Between Worlds",
        "Ori and the Blind Forest",
        "Mario & Luigi Superstar Saga",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "mercenary": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Starcraft 2",
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "Metroid Prime",
        "Dark Souls II"
    ],
    "coming of age": [
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "Ori and the Blind Forest"
    ],
    "coming": [
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "Ori and the Blind Forest"
    ],
    "age": [
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "Ori and the Blind Forest"
    ],
    "dimension travel": [
        "A Link to the Past",
        "DOOM II",
        "Majora's Mask Recompiled",
        "A Link Between Worlds"
    ],
    "dimension": [
        "A Link to the Past",
        "DOOM II",
        "Majora's Mask Recompiled",
        "A Link Between Worlds"
    ],
    "androgyny": [
        "Golden Sun The Lost Age",
        "Skyward Sword",
        "Symphony of the Night",
        "Ocarina of Time",
        "A Link Between Worlds",
        "Final Fantasy Tactics Advance"
    ],
    "fast traveling": [
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Emerald",
        "A Link Between Worlds",
        "Undertale"
    ],
    "fast": [
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Emerald",
        "A Link Between Worlds",
        "Undertale"
    ],
    "traveling": [
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Emerald",
        "A Link Between Worlds",
        "Undertale"
    ],
    "context sensitive": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "context": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "sensitive": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "living inventory": [
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Wind Waker",
        "Majora's Mask Recompiled"
    ],
    "living": [
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Wind Waker",
        "Majora's Mask Recompiled"
    ],
    "inventory": [
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "A Link Between Worlds",
        "The Wind Waker",
        "Majora's Mask Recompiled"
    ],
    "bees": [
        "Minecraft",
        "Terraria",
        "A Link Between Worlds",
        "A Link to the Past",
        "Raft",
        "Don"
    ],
    "2013": [
        "Candy Box 2",
        "Old School Runescape",
        "Rogue Legacy",
        "A Link Between Worlds",
        "Risk of Rain"
    ],
    "a link to the past": [
        "A Link to the Past"
    ],
    "mild violence": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "Super Metroid Map Rando",
        "MegaMan Battle Network 3",
        "Sly Cooper and the Thievius Raccoonus",
        "A Link to the Past",
        "Final Fantasy Tactics Advance",
        "Castlevania - Circle of the Moon",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "mild animated violence": [
        "A Link to the Past",
        "Ape Escape",
        "Lufia II Ancient Cave",
        "Secret of Evermore"
    ],
    "animated": [
        "Ape Escape",
        "Banjo-Tooie",
        "DOOM 1993",
        "Sonic Adventure DX",
        "Symphony of the Night",
        "Skyward Sword",
        "A Link to the Past",
        "Castlevania 64",
        "Castlevania - Circle of the Moon",
        "Twilight Princess",
        "Lufia II Ancient Cave",
        "Majora's Mask Recompiled",
        "Ratchet & Clank 2",
        "Xenoblade X",
        "Chrono Trigger Jets of Time",
        "Tyrian",
        "Secret of Evermore"
    ],
    "ghosts": [
        "The Legend of Zelda - Oracle of Ages",
        "Final Fantasy Mystic Quest",
        "EarthBound",
        "An Untitled Story",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Symphony of the Night",
        "A Link to the Past",
        "Castlevania 64",
        "Cuphead",
        "Donkey Kong Country 2",
        "Luigi's Mansion",
        "Metroid Prime",
        "Paper Mario",
        "Wario Land 4",
        "Mario & Luigi Superstar Saga"
    ],
    "mascot": [
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "Link's Awakening DX",
        "Kirby's Dream Land 3",
        "Paper Mario",
        "Mega Man 2",
        "The Legend of Zelda - Oracle of Seasons",
        "Spyro 3"
    ],
    "death": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Star Fox 64",
        "VVVVVV",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Luigi's Mansion",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Golden Sun The Lost Age",
        "Terraria",
        "Heretic",
        "Metroid Prime",
        "Final Fantasy Tactics Advance",
        "Castlevania - Circle of the Moon",
        "Metroid Zero Mission",
        "DOOM II",
        "Super Mario Sunshine",
        "Castlevania 64",
        "OpenRCT2",
        "Paper Mario",
        "Mega Man 2",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Dark Souls III",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX"
    ],
    "maze": [
        "The Witness",
        "Metroid Zero Mission",
        "DOOM 1993",
        "A Link to the Past",
        "Castlevania 64",
        "Link's Awakening DX",
        "OpenRCT2",
        "Paper Mario"
    ],
    "backtracking": [
        "The Witness",
        "Faxanadu",
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Castlevania 64",
        "Link's Awakening DX",
        "Metroid Prime",
        "Ocarina of Time",
        "Final Fantasy Tactics Advance",
        "Castlevania - Circle of the Moon",
        "The Legend of Zelda - Oracle of Seasons",
        "Undertale"
    ],
    "undead": [
        "The Legend of Zelda - Oracle of Ages",
        "Dark Souls Remastered",
        "Final Fantasy Mystic Quest",
        "The Legend of Zelda - Oracle of Seasons",
        "Terraria",
        "Heretic",
        "Symphony of the Night",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64",
        "Link's Awakening DX",
        "Paper Mario",
        "Mario & Luigi Superstar Saga",
        "Dark Souls II"
    ],
    "campaign": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "pixel art": [
        "Celeste",
        "VVVVVV",
        "Symphony of the Night",
        "A Link to the Past",
        "Wario Land 4",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Terraria",
        "Stardew Valley",
        "CrossCode",
        "Undertale",
        "ANIMAL WELL",
        "Metroid Zero Mission",
        "Timespinner",
        "Mega Man 2",
        "Risk of Rain",
        "Tyrian",
        "Blasphemous",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Wargroove",
        "Rogue Legacy",
        "Link's Awakening DX"
    ],
    "pixel": [
        "Celeste",
        "VVVVVV",
        "Symphony of the Night",
        "A Link to the Past",
        "Momodora Moonlit Farewell",
        "Wario Land 4",
        "The Messenger",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Terraria",
        "Stardew Valley",
        "CrossCode",
        "Undertale",
        "ANIMAL WELL",
        "A Short Hike",
        "Metroid Zero Mission",
        "Timespinner",
        "Mega Man 2",
        "Risk of Rain",
        "Noita",
        "Blasphemous",
        "Tyrian",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Wargroove",
        "Rogue Legacy",
        "Link's Awakening DX"
    ],
    "art": [
        "Celeste",
        "VVVVVV",
        "Symphony of the Night",
        "A Link to the Past",
        "Wario Land 4",
        "The Legend of Zelda - Oracle of Seasons",
        "Super Metroid Map Rando",
        "Terraria",
        "Stardew Valley",
        "CrossCode",
        "Undertale",
        "ANIMAL WELL",
        "Metroid Zero Mission",
        "Timespinner",
        "Mega Man 2",
        "Risk of Rain",
        "Tyrian",
        "Blasphemous",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Wargroove",
        "Rogue Legacy",
        "Link's Awakening DX"
    ],
    "easter egg": [
        "Ape Escape",
        "Banjo-Tooie",
        "DOOM II",
        "Rogue Legacy",
        "A Link to the Past",
        "Link's Awakening DX",
        "OpenRCT2",
        "Paper Mario"
    ],
    "easter": [
        "Ape Escape",
        "Banjo-Tooie",
        "DOOM II",
        "Rogue Legacy",
        "A Link to the Past",
        "Link's Awakening DX",
        "OpenRCT2",
        "Paper Mario"
    ],
    "egg": [
        "Ape Escape",
        "Banjo-Tooie",
        "DOOM II",
        "Rogue Legacy",
        "A Link to the Past",
        "Link's Awakening DX",
        "OpenRCT2",
        "Paper Mario"
    ],
    "teleportation": [
        "EarthBound",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "DOOM II",
        "Rogue Legacy",
        "VVVVVV",
        "A Link to the Past",
        "Castlevania 64",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "giant insects": [
        "Super Mario Sunshine",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Hollow Knight",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "giant": [
        "Super Mario Sunshine",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Hollow Knight",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "insects": [
        "Super Mario Sunshine",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Hollow Knight",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Secret of Evermore"
    ],
    "silent protagonist": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "Hollow Knight",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Golden Sun The Lost Age",
        "ULTRAKILL",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Blasphemous",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Mario & Luigi Superstar Saga"
    ],
    "silent": [
        "The Legend of Zelda - Oracle of Ages",
        "Skyward Sword",
        "A Link to the Past",
        "Kirby 64 - The Crystal Shards",
        "Hollow Knight",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Golden Sun The Lost Age",
        "ULTRAKILL",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Blasphemous",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Mario & Luigi Superstar Saga"
    ],
    "explosion": [
        "The Legend of Zelda - Oracle of Ages",
        "Minecraft",
        "Symphony of the Night",
        "A Link to the Past",
        "Super Metroid Map Rando",
        "Terraria",
        "Cuphead",
        "Metroid Prime",
        "Final Fantasy Tactics Advance",
        "Mario Kart 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "OpenRCT2",
        "Mega Man 2",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Final Fantasy Mystic Quest",
        "Rogue Legacy",
        "Donkey Kong Country 3",
        "Sonic Heroes"
    ],
    "block puzzle": [
        "A Link to the Past",
        "The Legend of Zelda - Oracle of Seasons",
        "The Legend of Zelda - Oracle of Ages",
        "Ocarina of Time"
    ],
    "block": [
        "A Link to the Past",
        "The Legend of Zelda - Oracle of Seasons",
        "The Legend of Zelda - Oracle of Ages",
        "Ocarina of Time"
    ],
    "monkey": [
        "Ape Escape",
        "Diddy Kong Racing",
        "Mario Kart 64",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "nintendo power": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "nintendo": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "power": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "world map": [
        "Aquaria",
        "Jak and Daxter: The Precursor Legacy",
        "VVVVVV",
        "Ocarina of Time",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Pokemon Crystal",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "map": [
        "Aquaria",
        "Jak and Daxter: The Precursor Legacy",
        "VVVVVV",
        "Ocarina of Time",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Pokemon Crystal",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "human": [
        "Golden Sun The Lost Age",
        "Ape Escape",
        "Dark Souls III",
        "Starcraft 2",
        "Skyward Sword",
        "DOOM II",
        "Symphony of the Night",
        "Super Mario Sunshine",
        "Terraria",
        "A Link to the Past",
        "Castlevania 64",
        "Link's Awakening DX",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "shopping": [
        "The Legend of Zelda - Oracle of Ages",
        "Digimon World",
        "The Legend of Zelda - Oracle of Seasons",
        "Symphony of the Night",
        "A Link to the Past",
        "Castlevania 64",
        "Cuphead",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Mario & Luigi Superstar Saga",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "ice stage": [
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Wario Land 4",
        "Donkey Kong Country"
    ],
    "ice": [
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Wario Land 4",
        "Donkey Kong Country"
    ],
    "stage": [
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Wario Land 4",
        "Sonic Heroes",
        "Donkey Kong Country",
        "Spyro 3",
        "Super Mario World"
    ],
    "saving the world": [
        "A Link to the Past",
        "EarthBound",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "saving": [
        "A Link to the Past",
        "EarthBound",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "the": [
        "The Legend of Zelda - Oracle of Ages",
        "Banjo-Tooie",
        "Skyward Sword",
        "Symphony of the Night",
        "A Link to the Past",
        "Hollow Knight",
        "Donkey Kong Country",
        "Golden Sun The Lost Age",
        "Super Mario Odyssey",
        "EarthBound",
        "Terraria",
        "Cuphead",
        "Final Fantasy Tactics Advance",
        "Undertale",
        "DOOM II",
        "Hades",
        "Donkey Kong Country 2",
        "Overcooked! 2",
        "Paper Mario",
        "Blasphemous",
        "The Sims 4",
        "Dark Souls II",
        "Zelda II: The Adventure of Link",
        "Diddy Kong Racing",
        "Jak and Daxter: The Precursor Legacy",
        "Rogue Legacy",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Mario & Luigi Superstar Saga",
        "Sea of Thieves"
    ],
    "secret area": [
        "The Witness",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Diddy Kong Racing",
        "Star Fox 64",
        "DOOM II",
        "Heretic",
        "Rogue Legacy",
        "Symphony of the Night",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "secret": [
        "The Witness",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Diddy Kong Racing",
        "Star Fox 64",
        "DOOM II",
        "Heretic",
        "Rogue Legacy",
        "Symphony of the Night",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "area": [
        "The Witness",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Diddy Kong Racing",
        "Star Fox 64",
        "DOOM II",
        "Heretic",
        "Rogue Legacy",
        "Symphony of the Night",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "shielded enemies": [
        "The Legend of Zelda - Oracle of Ages",
        "Rogue Legacy",
        "A Link to the Past",
        "Donkey Kong Country 3",
        "Hollow Knight"
    ],
    "shielded": [
        "The Legend of Zelda - Oracle of Ages",
        "Rogue Legacy",
        "A Link to the Past",
        "Donkey Kong Country 3",
        "Hollow Knight"
    ],
    "enemies": [
        "The Legend of Zelda - Oracle of Ages",
        "Rogue Legacy",
        "A Link to the Past",
        "Donkey Kong Country 3",
        "Hollow Knight"
    ],
    "walking through walls": [
        "The Legend of Zelda - Oracle of Ages",
        "DOOM II",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "walking": [
        "The Legend of Zelda - Oracle of Ages",
        "DOOM II",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "through": [
        "The Legend of Zelda - Oracle of Ages",
        "DOOM II",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "walls": [
        "The Legend of Zelda - Oracle of Ages",
        "DOOM II",
        "Ocarina of Time",
        "A Link to the Past",
        "Link's Awakening DX",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "liberation": [
        "A Link to the Past",
        "Super Metroid",
        "Donkey Kong Country 2",
        "Super Metroid Map Rando"
    ],
    "conveyor belt": [
        "A Link to the Past",
        "Mega Man 2",
        "Cuphead",
        "The Legend of Zelda - Oracle of Ages"
    ],
    "conveyor": [
        "A Link to the Past",
        "Mega Man 2",
        "Cuphead",
        "The Legend of Zelda - Oracle of Ages"
    ],
    "belt": [
        "A Link to the Past",
        "Mega Man 2",
        "Cuphead",
        "The Legend of Zelda - Oracle of Ages"
    ],
    "villain": [
        "The Legend of Zelda - Oracle of Ages",
        "Golden Sun The Lost Age",
        "Banjo-Tooie",
        "Star Fox 64",
        "Symphony of the Night",
        "Kingdom Hearts",
        "A Link to the Past",
        "Ocarina of Time",
        "Paper Mario",
        "Mega Man 2",
        "Donkey Kong Country",
        "Castlevania - Circle of the Moon",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "recurring boss": [
        "Banjo-Tooie",
        "Kingdom Hearts",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Paper Mario",
        "Donkey Kong Country"
    ],
    "recurring": [
        "Banjo-Tooie",
        "Kingdom Hearts",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Paper Mario",
        "Donkey Kong Country"
    ],
    "boss": [
        "Banjo-Tooie",
        "DOOM II",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Cuphead",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Ocarina of Time",
        "Majora's Mask Recompiled",
        "Paper Mario",
        "Pokemon Emerald",
        "Donkey Kong Country",
        "Dark Souls II"
    ],
    "been here before": [
        "Golden Sun The Lost Age",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "been": [
        "Golden Sun The Lost Age",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "here": [
        "Golden Sun The Lost Age",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "before": [
        "Golden Sun The Lost Age",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "sleeping": [
        "Golden Sun The Lost Age",
        "Minecraft",
        "Super Mario Sunshine",
        "A Link to the Past",
        "Pokemon Crystal",
        "Paper Mario"
    ],
    "merchants": [
        "Faxanadu",
        "Candy Box 2",
        "Terraria",
        "A Link to the Past",
        "Hollow Knight",
        "Timespinner",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "fetch quests": [
        "A Link to the Past",
        "Link's Awakening DX",
        "Metroid Prime",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "fetch": [
        "A Link to the Past",
        "Link's Awakening DX",
        "Metroid Prime",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link"
    ],
    "kidnapping": [
        "EarthBound",
        "Yoshi's Island",
        "Super Mario Sunshine",
        "A Link to the Past",
        "OpenRCT2"
    ],
    "poisoning": [
        "A Link to the Past",
        "Castlevania 64",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Paper Mario",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "time paradox": [
        "The Legend of Zelda - Oracle of Ages",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64"
    ],
    "paradox": [
        "The Legend of Zelda - Oracle of Ages",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64"
    ],
    "status effects": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "A Link to the Past",
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "status": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "A Link to the Past",
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "effects": [
        "The Legend of Zelda - Oracle of Ages",
        "EarthBound",
        "A Link to the Past",
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "The Legend of Zelda - Oracle of Seasons",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "hidden room": [
        "A Link to the Past",
        "DOOM II",
        "Heretic",
        "Dark Souls II"
    ],
    "hidden": [
        "A Link to the Past",
        "DOOM II",
        "Heretic",
        "Dark Souls II"
    ],
    "room": [
        "A Link to the Past",
        "DOOM II",
        "Heretic",
        "Dark Souls II"
    ],
    "another world": [
        "A Link to the Past",
        "DOOM II",
        "Majora's Mask Recompiled",
        "Link's Awakening DX"
    ],
    "another": [
        "A Link to the Past",
        "DOOM II",
        "Majora's Mask Recompiled",
        "Link's Awakening DX"
    ],
    "damage over time": [
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "A Link to the Past",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "damage": [
        "Minecraft",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Ocarina of Time",
        "A Link to the Past",
        "Castlevania 64",
        "Pokemon Crystal",
        "Metroid Prime",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "over": [
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Symphony of the Night",
        "Ocarina of Time",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Crystal",
        "Donkey Kong Country 3",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "monomyth": [
        "A Link to the Past",
        "Mega Man 2",
        "Skyward Sword",
        "Zelda II: The Adventure of Link"
    ],
    "buddy system": [
        "A Link to the Past",
        "Donkey Kong Country",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3"
    ],
    "buddy": [
        "A Link to the Past",
        "Donkey Kong Country",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3"
    ],
    "system": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "EarthBound",
        "Kingdom Hearts",
        "A Link to the Past",
        "Donkey Kong Country 2",
        "Pokemon Crystal",
        "Donkey Kong Country 3",
        "Paper Mario",
        "Pokemon Emerald",
        "Final Fantasy Tactics Advance",
        "Xenoblade X",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga"
    ],
    "retroachievements": [
        "Banjo-Tooie",
        "Star Fox 64",
        "Tetris Attack",
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "Kirby 64 - The Crystal Shards",
        "Majora's Mask Recompiled",
        "Donkey Kong Country",
        "EarthBound",
        "Super Mario 64",
        "Mario Kart 64",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Kirby's Dream Land 3",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Super Mario World",
        "Final Fantasy Mystic Quest",
        "Diddy Kong Racing",
        "Ocarina of Time",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "SM64 Romhack"
    ],
    "popular": [
        "Super Mario 64",
        "Pokemon FireRed and LeafGreen",
        "Ocarina of Time",
        "A Link to the Past",
        "Hollow Knight",
        "Super Mario World"
    ],
    "1991": [
        "A Link to the Past",
        "Final Fantasy IV Free Enterprise",
        "Mega Man 2"
    ],
    "animal well": [
        "ANIMAL WELL"
    ],
    "mild fantasy violence": [
        "Faxanadu",
        "ANIMAL WELL",
        "Final Fantasy Mystic Quest",
        "The Legend of Zelda",
        "Sonic Heroes",
        "Star Wars Episode I Racer",
        "VVVVVV",
        "Donkey Kong Country 2",
        "Final Fantasy IV Free Enterprise",
        "Landstalker - The Treasures of King Nole",
        "Wario Land",
        "Ori and the Blind Forest",
        "Chrono Trigger Jets of Time",
        "Zelda II: The Adventure of Link",
        "Final Fantasy"
    ],
    "side view": [
        "Slay the Spire",
        "Celeste",
        "Aquaria",
        "Tetris Attack",
        "VVVVVV",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Final Fantasy IV Free Enterprise",
        "Kirby 64 - The Crystal Shards",
        "Momodora Moonlit Farewell",
        "Wario Land 4",
        "Hollow Knight",
        "Donkey Kong Country",
        "The Messenger",
        "Final Fantasy",
        "SMZ3",
        "Faxanadu",
        "Super Metroid Map Rando",
        "Terraria",
        "Getting Over It",
        "DLCQuest",
        "Hatsune Miku Project Diva Mega Mix+",
        "Cuphead",
        "Pokemon Crystal",
        "Dungeon Clawler",
        "Castlevania - Circle of the Moon",
        "ANIMAL WELL",
        "Hylics 2",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Muse Dash",
        "Pokemon Red and Blue",
        "Donkey Kong Country 2",
        "Kirby's Dream Land 3",
        "Paper Mario",
        "Lufia II Ancient Cave",
        "Ori and the Blind Forest",
        "Timespinner",
        "Mega Man 2",
        "Wargroove 2",
        "Noita",
        "Blasphemous",
        "Risk of Rain",
        "Super Mario World",
        "Super Mario Land 2",
        "Super Metroid",
        "Final Fantasy Mystic Quest",
        "Yoshi's Island",
        "Zelda II: The Adventure of Link",
        "An Untitled Story",
        "Zillion",
        "UFO 50",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Rogue Legacy",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Donkey Kong Country 3",
        "Wario Land",
        "Mario & Luigi Superstar Saga"
    ],
    "horror": [
        "Shivers",
        "Resident Evil 2 Remake",
        "Lethal Company",
        "Terraria",
        "DOOM 1993",
        "DOOM II",
        "Getting Over It",
        "Inscryption",
        "Resident Evil 3 Remake",
        "Luigi's Mansion",
        "Castlevania 64",
        "Symphony of the Night",
        "Majora's Mask Recompiled",
        "Undertale",
        "Don",
        "Castlevania - Circle of the Moon",
        "Blasphemous",
        "ANIMAL WELL"
    ],
    "survival": [
        "Yu-Gi-Oh! 2006",
        "Dungeon Clawler",
        "Minecraft",
        "Resident Evil 2 Remake",
        "Subnautica",
        "Lethal Company",
        "Terraria",
        "Factorio",
        "Risk of Rain 2",
        "Resident Evil 3 Remake",
        "Raft",
        "Risk of Rain",
        "Don",
        "Factorio - Space Age Without Space",
        "ANIMAL WELL"
    ],
    "mystery": [
        "The Witness",
        "Outer Wilds",
        "Inscryption",
        "ANIMAL WELL"
    ],
    "exploration": [
        "Celeste",
        "Subnautica",
        "Aquaria",
        "VVVVVV",
        "TUNIC",
        "Outer Wilds",
        "Super Metroid Map Rando",
        "Terraria",
        "DLCQuest",
        "Pokemon Crystal",
        "Metroid Prime",
        "ANIMAL WELL",
        "The Witness",
        "Hylics 2",
        "A Short Hike",
        "Lethal Company",
        "Castlevania 64",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Lingo",
        "Sea of Thieves"
    ],
    "retro": [
        "Super Mario Odyssey",
        "Celeste",
        "Minecraft",
        "Undertale",
        "Hylics 2",
        "UFO 50",
        "Terraria",
        "VVVVVV",
        "DLCQuest",
        "Cuphead",
        "Timespinner",
        "Stardew Valley",
        "The Messenger",
        "Blasphemous",
        "ANIMAL WELL"
    ],
    "2d": [
        "Celeste",
        "VVVVVV",
        "Symphony of the Night",
        "Hollow Knight",
        "The Messenger",
        "Super Mario Odyssey",
        "EarthBound",
        "Super Metroid Map Rando",
        "Terraria",
        "Cuphead",
        "Stardew Valley",
        "Undertale",
        "ANIMAL WELL",
        "Hylics 2",
        "Muse Dash",
        "Zelda II: The Adventure of Link",
        "Blasphemous",
        "Super Metroid",
        "Don"
    ],
    "metroidvania": [
        "Aquaria",
        "VVVVVV",
        "Symphony of the Night",
        "Monster Sanctuary",
        "Momodora Moonlit Farewell",
        "Hollow Knight",
        "The Messenger",
        "Faxanadu",
        "Super Metroid Map Rando",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "ANIMAL WELL",
        "Ender Lilies",
        "Metroid Zero Mission",
        "Pseudoregalia",
        "Ori and the Blind Forest",
        "Timespinner",
        "Blasphemous",
        "Zelda II: The Adventure of Link",
        "Dark Souls II",
        "Zillion",
        "Super Metroid",
        "An Untitled Story",
        "Rogue Legacy"
    ],
    "atmospheric": [
        "Celeste",
        "Hylics 2",
        "TUNIC",
        "Hollow Knight",
        "Don",
        "ANIMAL WELL"
    ],
    "pixel graphics": [
        "Celeste",
        "A Short Hike",
        "VVVVVV",
        "Rogue Legacy",
        "Momodora Moonlit Farewell",
        "The Messenger",
        "Noita",
        "Undertale",
        "ANIMAL WELL"
    ],
    "graphics": [
        "Celeste",
        "A Short Hike",
        "VVVVVV",
        "Rogue Legacy",
        "Momodora Moonlit Farewell",
        "The Messenger",
        "Noita",
        "Undertale",
        "ANIMAL WELL"
    ],
    "relaxing": [
        "Stardew Valley",
        "The Sims 4",
        "A Short Hike",
        "ANIMAL WELL"
    ],
    "2024": [
        "Balatro",
        "UFO 50",
        "Momodora Moonlit Farewell",
        "DORONKO WANKO",
        "Celeste 64",
        "Dungeon Clawler",
        "Factorio - Space Age Without Space",
        "ANIMAL WELL"
    ],
    "ape escape": [
        "Ape Escape"
    ],
    "anime": [
        "Hunie Pop",
        "Ape Escape",
        "Golden Sun The Lost Age",
        "osu!",
        "Hunie Pop 2",
        "Digimon World",
        "Muse Dash",
        "Pokemon Emerald",
        "Yu-Gi-Oh! Forbidden Memories",
        "Pokemon Crystal",
        "Wario Land 4",
        "Zillion",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "dinosaurs": [
        "Ape Escape",
        "EarthBound",
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Yoshi's Island",
        "Super Mario Sunshine",
        "Super Mario World"
    ],
    "collecting": [
        "Ape Escape",
        "Banjo-Tooie",
        "Metroid Zero Mission",
        "Pokemon FireRed and LeafGreen",
        "Pokemon Red and Blue",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Zelda II: The Adventure of Link"
    ],
    "multiple endings": [
        "The Witness",
        "Ape Escape",
        "Star Fox 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Cuphead",
        "Kirby 64 - The Crystal Shards",
        "Metroid Prime",
        "Wario Land 4",
        "Civilization VI",
        "The Legend of Zelda - Oracle of Seasons",
        "Undertale"
    ],
    "endings": [
        "The Witness",
        "Ape Escape",
        "Star Fox 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Cuphead",
        "Kirby 64 - The Crystal Shards",
        "Metroid Prime",
        "Wario Land 4",
        "Civilization VI",
        "The Legend of Zelda - Oracle of Seasons",
        "Undertale"
    ],
    "amnesia": [
        "The Witness",
        "Ape Escape",
        "Aquaria",
        "Xenoblade X",
        "Sonic Heroes"
    ],
    "voice acting": [
        "The Witness",
        "Ape Escape",
        "Star Fox 64",
        "Hunie Pop 2",
        "Digimon World",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64",
        "Cuphead",
        "Civilization VI",
        "Sonic Heroes",
        "Xenoblade X"
    ],
    "voice": [
        "The Witness",
        "Ape Escape",
        "Star Fox 64",
        "Hunie Pop 2",
        "Digimon World",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64",
        "Cuphead",
        "Civilization VI",
        "Sonic Heroes",
        "Xenoblade X"
    ],
    "acting": [
        "The Witness",
        "Ape Escape",
        "Star Fox 64",
        "Hunie Pop 2",
        "Digimon World",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64",
        "Cuphead",
        "Civilization VI",
        "Sonic Heroes",
        "Xenoblade X"
    ],
    "psone classics": [
        "Mega Man 2",
        "Ape Escape",
        "Symphony of the Night",
        "Spyro 3"
    ],
    "psone": [
        "Mega Man 2",
        "Ape Escape",
        "Symphony of the Night",
        "Spyro 3"
    ],
    "classics": [
        "Mega Man 2",
        "Ape Escape",
        "Symphony of the Night",
        "Spyro 3"
    ],
    "moving platforms": [
        "VVVVVV",
        "Symphony of the Night",
        "Wario Land 4",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Paper Mario",
        "Mega Man 2",
        "Blasphemous",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Spyro 3"
    ],
    "moving": [
        "VVVVVV",
        "Symphony of the Night",
        "Wario Land 4",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Paper Mario",
        "Mega Man 2",
        "Blasphemous",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Spyro 3"
    ],
    "platforms": [
        "VVVVVV",
        "Symphony of the Night",
        "Wario Land 4",
        "Kirby 64 - The Crystal Shards",
        "Donkey Kong Country",
        "Super Metroid Map Rando",
        "Metroid Prime",
        "Castlevania - Circle of the Moon",
        "DOOM II",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Paper Mario",
        "Ori and the Blind Forest",
        "Mega Man 2",
        "Blasphemous",
        "Zelda II: The Adventure of Link",
        "Super Metroid",
        "Ape Escape",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Link's Awakening DX",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Spyro 3"
    ],
    "spiky-haired protagonist": [
        "Ape Escape",
        "Sonic Heroes",
        "Jak and Daxter: The Precursor Legacy",
        "Kingdom Hearts"
    ],
    "spiky-haired": [
        "Ape Escape",
        "Sonic Heroes",
        "Jak and Daxter: The Precursor Legacy",
        "Kingdom Hearts"
    ],
    "time trials": [
        "Ape Escape",
        "Diddy Kong Racing",
        "Mario Kart 64",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "Spyro 3"
    ],
    "trials": [
        "Ape Escape",
        "Diddy Kong Racing",
        "Mario Kart 64",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "Spyro 3"
    ],
    "1999": [
        "Ape Escape",
        "Star Wars Episode I Racer",
        "Castlevania 64",
        "Yu-Gi-Oh! Forbidden Memories",
        "Tyrian"
    ],
    "sudoku": [
        "Sudoku"
    ],
    "multiplayer": [
        "ArchipIDLE",
        "Clique",
        "Sudoku",
        "Wordipelago",
        "Jigsaw",
        "Yacht Dice",
        "ChecksFinder",
        "Paint"
    ],
    "hints": [
        "ChecksFinder",
        "Sudoku"
    ],
    "archipelago": [
        "ArchipIDLE",
        "Clique",
        "Sudoku",
        "Wordipelago",
        "Jigsaw",
        "Yacht Dice",
        "ChecksFinder",
        "Paint"
    ],
    "multiworld": [
        "ArchipIDLE",
        "Clique",
        "Sudoku",
        "Wordipelago",
        "Jigsaw",
        "Yacht Dice",
        "ChecksFinder",
        "Paint"
    ],
    "aquaria": [
        "Aquaria"
    ],
    "drama": [
        "Aquaria",
        "EarthBound",
        "Undertale",
        "Hades"
    ],
    "alternate costumes": [
        "Super Mario Odyssey",
        "Aquaria",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64"
    ],
    "alternate": [
        "Super Mario Odyssey",
        "Aquaria",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64"
    ],
    "costumes": [
        "Super Mario Odyssey",
        "Aquaria",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Castlevania 64"
    ],
    "humble bundle": [
        "Aquaria",
        "Getting Over It",
        "Minecraft",
        "VVVVVV"
    ],
    "humble": [
        "Aquaria",
        "Getting Over It",
        "Minecraft",
        "VVVVVV"
    ],
    "bundle": [
        "Aquaria",
        "Getting Over It",
        "Minecraft",
        "VVVVVV"
    ],
    "underwater gameplay": [
        "Super Mario Odyssey",
        "Super Mario 64",
        "Subnautica",
        "Banjo-Tooie",
        "Aquaria",
        "Terraria",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Ocarina of Time",
        "Metroid Prime",
        "Mega Man 2",
        "Donkey Kong Country",
        "SM64 Romhack"
    ],
    "underwater": [
        "Super Mario Odyssey",
        "Super Mario 64",
        "Subnautica",
        "Banjo-Tooie",
        "Aquaria",
        "Terraria",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Ocarina of Time",
        "Metroid Prime",
        "Mega Man 2",
        "Donkey Kong Country",
        "SM64 Romhack"
    ],
    "shape-shifting": [
        "Banjo-Tooie",
        "Aquaria",
        "Symphony of the Night",
        "Kirby 64 - The Crystal Shards",
        "Kirby's Dream Land 3",
        "Metroid Prime",
        "Majora's Mask Recompiled"
    ],
    "plot twist": [
        "Aquaria",
        "Ocarina of Time",
        "Kingdom Hearts",
        "Castlevania 64",
        "Undertale"
    ],
    "plot": [
        "Aquaria",
        "Ocarina of Time",
        "Kingdom Hearts",
        "Castlevania 64",
        "Undertale"
    ],
    "twist": [
        "Aquaria",
        "Ocarina of Time",
        "Kingdom Hearts",
        "Castlevania 64",
        "Undertale"
    ],
    "2007": [
        "Aquaria",
        "An Untitled Story",
        "osu!"
    ],
    "archipidle": [
        "ArchipIDLE"
    ],
    "an untitled story": [
        "An Untitled Story"
    ],
    "balatro": [
        "Balatro"
    ],
    "simulated gambling": [
        "Stardew Valley",
        "Balatro",
        "Undertale"
    ],
    "simulated": [
        "Stardew Valley",
        "Balatro",
        "Undertale"
    ],
    "gambling": [
        "Balatro",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Stardew Valley",
        "Undertale"
    ],
    "turn-based strategy (tbs)": [
        "Monster Sanctuary",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "EarthBound",
        "Final Fantasy Tactics Advance",
        "Dungeon Clawler",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Paper Mario",
        "Civilization VI",
        "Wargroove 2",
        "Yu-Gi-Oh! 2006",
        "Balatro",
        "Chained Echoes",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Pokemon Emerald",
        "Yu-Gi-Oh! Forbidden Memories"
    ],
    "turn-based": [
        "Monster Sanctuary",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "Golden Sun The Lost Age",
        "EarthBound",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Dungeon Clawler",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Paper Mario",
        "Civilization VI",
        "Wargroove 2",
        "Yu-Gi-Oh! 2006",
        "Final Fantasy Mystic Quest",
        "Balatro",
        "Chained Echoes",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Pokemon Emerald",
        "Yu-Gi-Oh! Forbidden Memories",
        "Mario & Luigi Superstar Saga"
    ],
    "(tbs)": [
        "Monster Sanctuary",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "Final Fantasy",
        "EarthBound",
        "Final Fantasy Tactics Advance",
        "Dungeon Clawler",
        "Undertale",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Hylics 2",
        "Pokemon Red and Blue",
        "Paper Mario",
        "Civilization VI",
        "Wargroove 2",
        "Yu-Gi-Oh! 2006",
        "Balatro",
        "Chained Echoes",
        "Wargroove",
        "Pokemon FireRed and LeafGreen",
        "Pokemon Emerald",
        "Yu-Gi-Oh! Forbidden Memories"
    ],
    "card & board game": [
        "Yu-Gi-Oh! 2006",
        "Slay the Spire",
        "Balatro",
        "Inscryption",
        "Yu-Gi-Oh! Forbidden Memories",
        "Yacht Dice",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "card": [
        "Yu-Gi-Oh! 2006",
        "Slay the Spire",
        "Balatro",
        "Inscryption",
        "Yu-Gi-Oh! Forbidden Memories",
        "Yacht Dice",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "board": [
        "Yu-Gi-Oh! 2006",
        "Slay the Spire",
        "Balatro",
        "Inscryption",
        "Yu-Gi-Oh! Forbidden Memories",
        "Yacht Dice",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "game": [
        "The Witness",
        "Yu-Gi-Oh! 2006",
        "Super Mario Odyssey",
        "Balatro",
        "Slay the Spire",
        "Yu-Gi-Oh! Dungeon Dice Monsters",
        "DOOM II",
        "Rogue Legacy",
        "Inscryption",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Yu-Gi-Oh! Forbidden Memories",
        "Cuphead",
        "Yacht Dice",
        "Hollow Knight",
        "Spyro 3",
        "Sea of Thieves"
    ],
    "roguelike": [
        "Slay the Spire",
        "Balatro",
        "Rogue Legacy",
        "Hades",
        "Dungeon Clawler",
        "Risk of Rain",
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "banjo-tooie": [
        "Banjo-Tooie"
    ],
    "crude humor": [
        "The Binding of Isaac Repentance",
        "Banjo-Tooie",
        "The Sims 4",
        "Rogue Legacy",
        "Don",
        "The Messenger",
        "Sea of Thieves"
    ],
    "crude": [
        "The Binding of Isaac Repentance",
        "Banjo-Tooie",
        "The Sims 4",
        "Rogue Legacy",
        "Don",
        "The Messenger",
        "Sea of Thieves"
    ],
    "animated violence": [
        "Banjo-Tooie",
        "DOOM 1993",
        "Sonic Adventure DX",
        "Symphony of the Night",
        "Castlevania 64",
        "Majora's Mask Recompiled",
        "Tyrian"
    ],
    "comic mischief": [
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Toontown",
        "Wario Land 4",
        "Paper Mario",
        "Ratchet & Clank 2",
        "Zork Grand Inquisitor",
        "Spyro 3"
    ],
    "comic": [
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Toontown",
        "Wario Land 4",
        "Paper Mario",
        "Ratchet & Clank 2",
        "Zork Grand Inquisitor",
        "Spyro 3"
    ],
    "mischief": [
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Skyward Sword",
        "Super Mario Sunshine",
        "Toontown",
        "Wario Land 4",
        "Paper Mario",
        "Ratchet & Clank 2",
        "Zork Grand Inquisitor",
        "Spyro 3"
    ],
    "cartoon violence": [
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Terraria",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Toontown",
        "Majora's Mask Recompiled"
    ],
    "cartoon": [
        "Super Mario Odyssey",
        "Banjo-Tooie",
        "Terraria",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Toontown",
        "Majora's Mask Recompiled",
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "quiz/trivia": [
        "Banjo-Tooie"
    ],
    "comedy": [
        "Banjo-Tooie",
        "Kingdom Hearts",
        "Luigi's Mansion",
        "The Messenger",
        "Digimon World",
        "Getting Over It",
        "DLCQuest",
        "Cuphead",
        "Zork Grand Inquisitor",
        "Undertale",
        "Lethal Company",
        "Muse Dash",
        "Donkey Kong Country 2",
        "Overcooked! 2",
        "Paper Mario",
        "DORONKO WANKO",
        "The Sims 4",
        "Hunie Pop",
        "Diddy Kong Racing",
        "Candy Box 2",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Rogue Legacy",
        "Toontown",
        "Ratchet & Clank 2",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "aliens": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "Banjo-Tooie",
        "Lethal Company",
        "Starcraft 2",
        "Factorio",
        "Metroid Zero Mission",
        "Metroid Prime",
        "Xenoblade X",
        "Factorio - Space Age Without Space"
    ],
    "flight": [
        "Banjo-Tooie",
        "Hylics 2",
        "Diddy Kong Racing",
        "A Short Hike",
        "Star Fox 64",
        "Terraria",
        "Rogue Legacy",
        "Wario Land 4",
        "Xenoblade X",
        "Mega Man 2",
        "Donkey Kong Country",
        "Spyro 3"
    ],
    "witches": [
        "The Legend of Zelda - Oracle of Ages",
        "Banjo-Tooie",
        "Ender Lilies",
        "Castlevania 64",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "achievements": [
        "Minecraft",
        "Banjo-Tooie",
        "Hunie Pop 2",
        "Sonic Heroes",
        "DOOM II",
        "Muse Dash",
        "Symphony of the Night",
        "VVVVVV",
        "Cuphead",
        "Ori and the Blind Forest",
        "Blasphemous",
        "Dark Souls II"
    ],
    "talking animals": [
        "Banjo-Tooie",
        "Diddy Kong Racing",
        "Star Fox 64",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "talking": [
        "Banjo-Tooie",
        "Diddy Kong Racing",
        "Star Fox 64",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "animals": [
        "Banjo-Tooie",
        "Diddy Kong Racing",
        "Star Fox 64",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "breaking the fourth wall": [
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Paper Mario",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Undertale"
    ],
    "breaking": [
        "The Legend of Zelda - Oracle of Ages",
        "Banjo-Tooie",
        "Symphony of the Night",
        "Wario Land 4",
        "Donkey Kong Country",
        "Super Metroid Map Rando",
        "Metroid Prime",
        "Final Fantasy Tactics Advance",
        "Undertale",
        "Metroid Zero Mission",
        "DOOM II",
        "Donkey Kong Country 2",
        "Paper Mario",
        "Super Metroid",
        "Jak and Daxter: The Precursor Legacy",
        "Rogue Legacy",
        "Ocarina of Time",
        "Link's Awakening DX",
        "Mario & Luigi Superstar Saga"
    ],
    "fourth": [
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Link's Awakening DX",
        "Paper Mario",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Undertale"
    ],
    "cameo appearance": [
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Spyro 3"
    ],
    "cameo": [
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Spyro 3"
    ],
    "appearance": [
        "Banjo-Tooie",
        "Jak and Daxter: The Precursor Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Spyro 3"
    ],
    "invisible wall": [
        "Mario Kart 64",
        "Ocarina of Time",
        "Banjo-Tooie",
        "Kingdom Hearts"
    ],
    "invisible": [
        "Mario Kart 64",
        "Ocarina of Time",
        "Banjo-Tooie",
        "Kingdom Hearts"
    ],
    "temporary invincibility": [
        "Faxanadu",
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Cuphead",
        "Paper Mario",
        "Sonic Heroes"
    ],
    "temporary": [
        "Faxanadu",
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Cuphead",
        "Paper Mario",
        "Sonic Heroes"
    ],
    "invincibility": [
        "Faxanadu",
        "Banjo-Tooie",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM II",
        "Rogue Legacy",
        "Donkey Kong Country 2",
        "Cuphead",
        "Paper Mario",
        "Sonic Heroes"
    ],
    "gliding": [
        "Banjo-Tooie",
        "Sly Cooper and the Thievius Raccoonus",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Spyro 3"
    ],
    "lgbtq+": [
        "Celeste",
        "Banjo-Tooie",
        "Rogue Legacy",
        "Celeste 64",
        "Timespinner",
        "The Sims 4"
    ],
    "2000": [
        "Banjo-Tooie",
        "Kirby 64 - The Crystal Shards",
        "Pokemon Crystal",
        "Paper Mario",
        "Majora's Mask Recompiled",
        "Spyro 3"
    ],
    "blasphemous": [
        "Blasphemous"
    ],
    "blood and gore": [
        "Dark Souls Remastered",
        "The Binding of Isaac Repentance",
        "Resident Evil 2 Remake",
        "ULTRAKILL",
        "Starcraft 2",
        "Terraria",
        "DOOM 1993",
        "DOOM II",
        "Symphony of the Night",
        "Resident Evil 3 Remake",
        "Blasphemous",
        "Dark Souls II"
    ],
    "gore": [
        "Shivers",
        "Dark Souls Remastered",
        "The Binding of Isaac Repentance",
        "Resident Evil 2 Remake",
        "ULTRAKILL",
        "Starcraft 2",
        "Terraria",
        "DOOM 1993",
        "DOOM II",
        "Symphony of the Night",
        "Resident Evil 3 Remake",
        "Blasphemous",
        "Dark Souls II"
    ],
    "nudity": [
        "Dark Souls Remastered",
        "Hunie Pop",
        "Hunie Pop 2",
        "Muse Dash",
        "Symphony of the Night",
        "Blasphemous",
        "Dark Souls II"
    ],
    "hack and slash/beat 'em up": [
        "Castlevania 64",
        "Risk of Rain",
        "Blasphemous",
        "Hades"
    ],
    "hack": [
        "Castlevania 64",
        "Risk of Rain",
        "Blasphemous",
        "Hades"
    ],
    "slash/beat": [
        "Castlevania 64",
        "Risk of Rain",
        "Blasphemous",
        "Hades"
    ],
    "'em": [
        "Castlevania 64",
        "Risk of Rain",
        "Blasphemous",
        "Hades"
    ],
    "up": [
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Symphony of the Night",
        "Hades",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Castlevania 64",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Crystal",
        "Paper Mario",
        "Undertale",
        "Zelda II: The Adventure of Link",
        "Castlevania - Circle of the Moon",
        "Risk of Rain",
        "Blasphemous",
        "Dark Souls II"
    ],
    "bloody": [
        "Resident Evil 2 Remake",
        "ULTRAKILL",
        "DOOM II",
        "Heretic",
        "Symphony of the Night",
        "Castlevania 64",
        "Metroid Prime",
        "Blasphemous"
    ],
    "difficult": [
        "Celeste",
        "Getting Over It",
        "Hades",
        "TUNIC",
        "Zelda II: The Adventure of Link",
        "Don",
        "The Messenger",
        "Risk of Rain",
        "Blasphemous"
    ],
    "side-scrolling": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Yoshi's Island",
        "Hylics 2",
        "Metroid Zero Mission",
        "Muse Dash",
        "Rogue Legacy",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Cuphead",
        "Donkey Kong Country 3",
        "Kirby's Dream Land 3",
        "Zelda II: The Adventure of Link",
        "Mega Man 2",
        "Donkey Kong Country",
        "Blasphemous"
    ],
    "crossover": [
        "Mario Kart 64",
        "Blasphemous",
        "Diddy Kong Racing",
        "Kingdom Hearts"
    ],
    "religion": [
        "EarthBound",
        "Ocarina of Time",
        "Castlevania 64",
        "Civilization VI",
        "Blasphemous"
    ],
    "2d platformer": [
        "Super Mario Odyssey",
        "Hylics 2",
        "VVVVVV",
        "Hollow Knight",
        "Blasphemous"
    ],
    "great soundtrack": [
        "Celeste",
        "ULTRAKILL",
        "Hylics 2",
        "A Short Hike",
        "Getting Over It",
        "TUNIC",
        "Bomb Rush Cyberfunk",
        "Blasphemous",
        "Undertale"
    ],
    "great": [
        "Celeste",
        "ULTRAKILL",
        "Hylics 2",
        "A Short Hike",
        "Getting Over It",
        "TUNIC",
        "Bomb Rush Cyberfunk",
        "Blasphemous",
        "Undertale"
    ],
    "soundtrack": [
        "Celeste",
        "ULTRAKILL",
        "Hylics 2",
        "A Short Hike",
        "Getting Over It",
        "TUNIC",
        "Bomb Rush Cyberfunk",
        "Blasphemous",
        "Undertale"
    ],
    "parrying": [
        "Dark Souls III",
        "Cuphead",
        "Hollow Knight",
        "Blasphemous",
        "Dark Souls II"
    ],
    "soulslike": [
        "Dark Souls Remastered",
        "Dark Souls III",
        "Ender Lilies",
        "TUNIC",
        "Blasphemous",
        "Dark Souls II"
    ],
    "you can pet the dog": [
        "Terraria",
        "Hades",
        "Overcooked! 2",
        "The Sims 4",
        "Blasphemous",
        "Sea of Thieves",
        "Undertale"
    ],
    "you": [
        "Terraria",
        "Hades",
        "Overcooked! 2",
        "The Sims 4",
        "Blasphemous",
        "Sea of Thieves",
        "Undertale"
    ],
    "can": [
        "Terraria",
        "Hades",
        "Overcooked! 2",
        "The Sims 4",
        "Blasphemous",
        "Sea of Thieves",
        "Undertale"
    ],
    "pet": [
        "Terraria",
        "Hades",
        "Overcooked! 2",
        "The Sims 4",
        "Blasphemous",
        "Sea of Thieves",
        "Undertale"
    ],
    "dog": [
        "Super Mario Odyssey",
        "Star Fox 64",
        "Terraria",
        "Sly Cooper and the Thievius Raccoonus",
        "Hades",
        "Ocarina of Time",
        "Castlevania 64",
        "Overcooked! 2",
        "DORONKO WANKO",
        "Undertale",
        "The Sims 4",
        "The Legend of Zelda - Oracle of Seasons",
        "Blasphemous",
        "Sea of Thieves",
        "Secret of Evermore"
    ],
    "interconnected-world": [
        "Dark Souls Remastered",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Dark Souls III",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "Luigi's Mansion",
        "Hollow Knight",
        "Blasphemous",
        "Dark Souls II"
    ],
    "2019": [
        "Outer Wilds",
        "Resident Evil 2 Remake",
        "A Short Hike",
        "Wargroove",
        "Risk of Rain 2",
        "Blasphemous"
    ],
    "bomb rush cyberfunk": [
        "Bomb Rush Cyberfunk"
    ],
    "suggestive themes": [
        "Chained Echoes",
        "Starcraft 2",
        "Terraria",
        "Muse Dash",
        "Hades",
        "Momodora Moonlit Farewell",
        "Xenoblade X",
        "Bomb Rush Cyberfunk",
        "Zork Grand Inquisitor",
        "Chrono Trigger Jets of Time"
    ],
    "suggestive": [
        "Chained Echoes",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Muse Dash",
        "Hades",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Xenoblade X",
        "Bomb Rush Cyberfunk",
        "Zork Grand Inquisitor",
        "Chrono Trigger Jets of Time"
    ],
    "themes": [
        "Timespinner",
        "Chained Echoes",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria",
        "Muse Dash",
        "Hades",
        "Hatsune Miku Project Diva Mega Mix+",
        "Final Fantasy IV Free Enterprise",
        "Momodora Moonlit Farewell",
        "Xenoblade X",
        "Bomb Rush Cyberfunk",
        "Zork Grand Inquisitor",
        "Chrono Trigger Jets of Time",
        "The Sims 4"
    ],
    "sport": [
        "Trackmania",
        "Bomb Rush Cyberfunk"
    ],
    "science fiction": [
        "Subnautica",
        "Star Fox 64",
        "VVVVVV",
        "Xenoblade X",
        "Outer Wilds",
        "EarthBound",
        "Super Metroid Map Rando",
        "ULTRAKILL",
        "Terraria",
        "Metroid Prime",
        "Bomb Rush Cyberfunk",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "The Witness",
        "Lethal Company",
        "MegaMan Battle Network 3",
        "Metroid Zero Mission",
        "DOOM II",
        "Risk of Rain 2",
        "Mega Man 2",
        "Risk of Rain",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "Zillion",
        "Super Metroid",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Star Wars Episode I Racer",
        "Ratchet & Clank 2",
        "Brotato",
        "Secret of Evermore"
    ],
    "science": [
        "Subnautica",
        "Star Fox 64",
        "VVVVVV",
        "Xenoblade X",
        "Outer Wilds",
        "EarthBound",
        "Super Metroid Map Rando",
        "ULTRAKILL",
        "Terraria",
        "Metroid Prime",
        "Bomb Rush Cyberfunk",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "The Witness",
        "Lethal Company",
        "MegaMan Battle Network 3",
        "Metroid Zero Mission",
        "DOOM II",
        "Risk of Rain 2",
        "Mega Man 2",
        "Risk of Rain",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "Zillion",
        "Super Metroid",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Star Wars Episode I Racer",
        "Ratchet & Clank 2",
        "Brotato",
        "Secret of Evermore"
    ],
    "fiction": [
        "Subnautica",
        "Star Fox 64",
        "VVVVVV",
        "Xenoblade X",
        "Outer Wilds",
        "EarthBound",
        "Super Metroid Map Rando",
        "ULTRAKILL",
        "Terraria",
        "Metroid Prime",
        "Bomb Rush Cyberfunk",
        "CrossCode",
        "Chrono Trigger Jets of Time",
        "The Witness",
        "Lethal Company",
        "MegaMan Battle Network 3",
        "Metroid Zero Mission",
        "DOOM II",
        "Risk of Rain 2",
        "Mega Man 2",
        "Risk of Rain",
        "Factorio - Space Age Without Space",
        "Tyrian",
        "Zillion",
        "Super Metroid",
        "Starcraft 2",
        "Jak and Daxter: The Precursor Legacy",
        "DOOM 1993",
        "Factorio",
        "Pokemon FireRed and LeafGreen",
        "Star Wars Episode I Racer",
        "Ratchet & Clank 2",
        "Brotato",
        "Secret of Evermore"
    ],
    "spiritual successor": [
        "Paper Mario",
        "Mario & Luigi Superstar Saga",
        "Xenoblade X",
        "Bomb Rush Cyberfunk"
    ],
    "spiritual": [
        "Paper Mario",
        "Mario & Luigi Superstar Saga",
        "Xenoblade X",
        "Bomb Rush Cyberfunk"
    ],
    "successor": [
        "Paper Mario",
        "Mario & Luigi Superstar Saga",
        "Xenoblade X",
        "Bomb Rush Cyberfunk"
    ],
    "brotato": [
        "Brotato"
    ],
    "fighting": [
        "Brotato"
    ],
    "shooter": [
        "Star Fox 64",
        "Resident Evil 2 Remake",
        "Super Metroid Map Rando",
        "ULTRAKILL",
        "Heretic",
        "Resident Evil 3 Remake",
        "Cuphead",
        "Metroid Prime",
        "CrossCode",
        "The Binding of Isaac Repentance",
        "Metroid Zero Mission",
        "DOOM II",
        "Risk of Rain 2",
        "Risk of Rain",
        "Noita",
        "Tyrian",
        "Super Metroid",
        "UFO 50",
        "DOOM 1993",
        "Ratchet & Clank 2",
        "Brotato"
    ],
    "arcade": [
        "ULTRAKILL",
        "osu!",
        "Mario Kart 64",
        "UFO 50",
        "Trackmania",
        "VVVVVV",
        "Hatsune Miku Project Diva Mega Mix+",
        "Overcooked! 2",
        "Cuphead",
        "Dungeon Clawler",
        "The Messenger",
        "Brotato",
        "Noita",
        "Tyrian"
    ],
    "bumper stickers": [
        "Bumper Stickers"
    ],
    "candy box 2": [
        "Candy Box 2"
    ],
    "text": [
        "Yu-Gi-Oh! 2006",
        "Hunie Pop",
        "Old School Runescape",
        "Hunie Pop 2",
        "Candy Box 2"
    ],
    "management": [
        "The Sims 4",
        "Final Fantasy Tactics Advance",
        "Civilization VI",
        "Candy Box 2"
    ],
    "cat quest": [
        "Cat Quest"
    ],
    "celeste": [
        "Celeste"
    ],
    "mild language": [
        "Celeste",
        "Subnautica",
        "VVVVVV",
        "Hades",
        "Cuphead",
        "Ratchet & Clank 2",
        "Timespinner",
        "Stardew Valley",
        "Risk of Rain",
        "Undertale",
        "Dark Souls II"
    ],
    "story rich": [
        "Celeste",
        "Hylics 2",
        "Getting Over It",
        "Hades",
        "Undertale"
    ],
    "story": [
        "Celeste",
        "Hylics 2",
        "Getting Over It",
        "Hades",
        "Undertale"
    ],
    "rich": [
        "Celeste",
        "Hylics 2",
        "Getting Over It",
        "Hades",
        "Undertale"
    ],
    "conversation": [
        "VVVVVV",
        "Ender Lilies",
        "Celeste",
        "Undertale"
    ],
    "2018": [
        "Dark Souls Remastered",
        "Celeste",
        "Subnautica",
        "Muse Dash",
        "The Messenger",
        "Overcooked! 2",
        "Timespinner",
        "CrossCode",
        "Sea of Thieves",
        "SMZ3"
    ],
    "celeste 64": [
        "Celeste 64"
    ],
    "chained echoes": [
        "Chained Echoes"
    ],
    "strong language": [
        "Chained Echoes",
        "Resident Evil 2 Remake",
        "Inscryption",
        "Resident Evil 3 Remake"
    ],
    "strong": [
        "Chained Echoes",
        "Resident Evil 2 Remake",
        "Inscryption",
        "Resident Evil 3 Remake"
    ],
    "sexual themes": [
        "Chained Echoes",
        "Muse Dash",
        "Hatsune Miku Project Diva Mega Mix+",
        "Timespinner",
        "The Sims 4"
    ],
    "sexual": [
        "Chained Echoes",
        "Muse Dash",
        "Hatsune Miku Project Diva Mega Mix+",
        "Timespinner",
        "The Sims 4"
    ],
    "jrpg": [
        "Final Fantasy Mystic Quest",
        "Hylics 2",
        "Chained Echoes",
        "Final Fantasy IV Free Enterprise",
        "Final Fantasy Tactics Advance",
        "Pokemon Mystery Dungeon Explorers of Sky",
        "Final Fantasy"
    ],
    "2022": [
        "Chained Echoes",
        "Raft",
        "TUNIC"
    ],
    "checksfinder": [
        "ChecksFinder"
    ],
    "civilization vi": [
        "Civilization VI"
    ],
    "educational": [
        "Civilization VI"
    ],
    "4x (explore, expand, exploit, and exterminate)": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "4x": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "(explore,": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "expand,": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "exploit,": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "exterminate)": [
        "OpenRCT2",
        "Civilization VI"
    ],
    "construction": [
        "Terraria",
        "Minecraft",
        "Civilization VI",
        "Xenoblade X"
    ],
    "mining": [
        "Stardew Valley",
        "Terraria",
        "Minecraft",
        "Civilization VI"
    ],
    "loot gathering": [
        "Castlevania 64",
        "Terraria",
        "Civilization VI",
        "Xenoblade X"
    ],
    "loot": [
        "Castlevania 64",
        "Terraria",
        "Civilization VI",
        "Xenoblade X"
    ],
    "gathering": [
        "Castlevania 64",
        "Terraria",
        "Civilization VI",
        "Xenoblade X"
    ],
    "royalty": [
        "EarthBound",
        "Mario & Luigi Superstar Saga",
        "Rogue Legacy",
        "Civilization VI"
    ],
    "ambient music": [
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Civilization VI",
        "Donkey Kong Country",
        "Secret of Evermore"
    ],
    "ambient": [
        "Metroid Zero Mission",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Civilization VI",
        "Donkey Kong Country",
        "Secret of Evermore"
    ],
    "music": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "ULTRAKILL",
        "osu!",
        "Metroid Zero Mission",
        "DOOM II",
        "Muse Dash",
        "Hatsune Miku Project Diva Mega Mix+",
        "Sonic Heroes",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Symphony of the Night",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Civilization VI",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country",
        "Secret of Evermore"
    ],
    "2005": [
        "Digimon World",
        "Kingdom Hearts 2",
        "Civilization VI"
    ],
    "clique": [
        "Clique"
    ],
    "meme origin": [
        "Minecraft",
        "The Legend of Zelda",
        "Star Fox 64",
        "Symphony of the Night",
        "Metroid Prime",
        "Majora's Mask Recompiled",
        "Clique",
        "Zelda II: The Adventure of Link"
    ],
    "meme": [
        "Minecraft",
        "The Legend of Zelda",
        "Star Fox 64",
        "Symphony of the Night",
        "Metroid Prime",
        "Majora's Mask Recompiled",
        "Clique",
        "Zelda II: The Adventure of Link"
    ],
    "origin": [
        "Minecraft",
        "The Legend of Zelda",
        "Star Fox 64",
        "Symphony of the Night",
        "Metroid Prime",
        "Majora's Mask Recompiled",
        "Clique",
        "Zelda II: The Adventure of Link"
    ],
    "crosscode": [
        "CrossCode"
    ],
    "16-bit": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "Rogue Legacy",
        "CrossCode"
    ],
    "a.i. companion": [
        "CrossCode",
        "Star Fox 64",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "a.i.": [
        "CrossCode",
        "Star Fox 64",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "companion": [
        "CrossCode",
        "Star Fox 64",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "chrono trigger jets of time": [
        "Chrono Trigger Jets of Time"
    ],
    "animated blood": [
        "Skyward Sword",
        "Castlevania 64",
        "Twilight Princess",
        "Ratchet & Clank 2",
        "Xenoblade X",
        "Chrono Trigger Jets of Time",
        "Castlevania - Circle of the Moon"
    ],
    "use of alcohol": [
        "Terraria",
        "Kingdom Hearts 2",
        "Xenoblade X",
        "Stardew Valley",
        "Chrono Trigger Jets of Time",
        "Sea of Thieves"
    ],
    "2008": [
        "Chrono Trigger Jets of Time"
    ],
    "cuphead": [
        "Cuphead"
    ],
    "use of alcohol and tobacco": [
        "Stardew Valley",
        "Starcraft 2",
        "Cuphead",
        "Zork Grand Inquisitor"
    ],
    "pirates": [
        "The Legend of Zelda - Oracle of Ages",
        "Metroid Zero Mission",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Cuphead",
        "Metroid Prime",
        "Wargroove 2",
        "The Legend of Zelda - Oracle of Seasons",
        "Sea of Thieves"
    ],
    "shark": [
        "Raft",
        "Cuphead",
        "Jak and Daxter: The Precursor Legacy",
        "Donkey Kong Country"
    ],
    "robots": [
        "EarthBound",
        "ULTRAKILL",
        "Star Fox 64",
        "Star Wars Episode I Racer",
        "Super Mario Sunshine",
        "Cuphead",
        "Xenoblade X",
        "Sonic Heroes",
        "Mega Man 2"
    ],
    "dancing": [
        "Donkey Kong Country 2",
        "Cuphead",
        "Donkey Kong Country 3",
        "The Legend of Zelda - Oracle of Ages"
    ],
    "cat": [
        "Minecraft",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Wario Land 4",
        "Cuphead",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "violent plants": [
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Cuphead",
        "Metroid Prime"
    ],
    "violent": [
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Cuphead",
        "Metroid Prime"
    ],
    "plants": [
        "Terraria",
        "Skyward Sword",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Cuphead",
        "Metroid Prime"
    ],
    "auto-scrolling levels": [
        "Star Fox 64",
        "VVVVVV",
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Cuphead",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "auto-scrolling": [
        "Star Fox 64",
        "VVVVVV",
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Cuphead",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "levels": [
        "Star Fox 64",
        "VVVVVV",
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Cuphead",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "boss assistance": [
        "DOOM II",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Cuphead",
        "Metroid Prime",
        "Paper Mario",
        "Majora's Mask Recompiled",
        "Donkey Kong Country",
        "Dark Souls II"
    ],
    "assistance": [
        "DOOM II",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Cuphead",
        "Metroid Prime",
        "Paper Mario",
        "Majora's Mask Recompiled",
        "Donkey Kong Country",
        "Dark Souls II"
    ],
    "the game awards 2017": [
        "Cuphead",
        "Super Mario Odyssey",
        "Hollow Knight",
        "Sea of Thieves"
    ],
    "awards": [
        "Cuphead",
        "Super Mario Odyssey",
        "Hollow Knight",
        "Sea of Thieves"
    ],
    "castlevania 64": [
        "Castlevania 64"
    ],
    "summoning support": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Castlevania 64",
        "Yu-Gi-Oh! Forbidden Memories",
        "Final Fantasy Tactics Advance"
    ],
    "summoning": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Castlevania 64",
        "Yu-Gi-Oh! Forbidden Memories",
        "Final Fantasy Tactics Advance"
    ],
    "support": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Castlevania 64",
        "Yu-Gi-Oh! Forbidden Memories",
        "Final Fantasy Tactics Advance"
    ],
    "horse": [
        "Minecraft",
        "Rogue Legacy",
        "Symphony of the Night",
        "Ocarina of Time",
        "Castlevania 64",
        "Castlevania - Circle of the Moon"
    ],
    "multiple protagonists": [
        "EarthBound",
        "Rogue Legacy",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "protagonists": [
        "EarthBound",
        "Rogue Legacy",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Donkey Kong Country",
        "Mario & Luigi Superstar Saga",
        "Spyro 3"
    ],
    "traps": [
        "Minecraft",
        "DOOM II",
        "Rogue Legacy",
        "Castlevania 64",
        "Dark Souls II"
    ],
    "bats": [
        "Mario Kart 64",
        "Terraria",
        "Symphony of the Night",
        "Castlevania 64",
        "Pokemon Crystal",
        "Castlevania - Circle of the Moon",
        "Zelda II: The Adventure of Link"
    ],
    "day/night cycle": [
        "Minecraft",
        "Jak and Daxter: The Precursor Legacy",
        "Skyward Sword",
        "Terraria",
        "Symphony of the Night",
        "Ocarina of Time",
        "Castlevania 64",
        "Pokemon Crystal",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Stardew Valley"
    ],
    "day/night": [
        "Minecraft",
        "Jak and Daxter: The Precursor Legacy",
        "Skyward Sword",
        "Terraria",
        "Symphony of the Night",
        "Ocarina of Time",
        "Castlevania 64",
        "Pokemon Crystal",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Stardew Valley"
    ],
    "cycle": [
        "Minecraft",
        "Jak and Daxter: The Precursor Legacy",
        "Skyward Sword",
        "Terraria",
        "Symphony of the Night",
        "Ocarina of Time",
        "Castlevania 64",
        "Pokemon Crystal",
        "The Wind Waker",
        "Majora's Mask Recompiled",
        "Xenoblade X",
        "Stardew Valley"
    ],
    "skeletons": [
        "Terraria",
        "Sly Cooper and the Thievius Raccoonus",
        "Heretic",
        "Symphony of the Night",
        "Castlevania 64",
        "Castlevania - Circle of the Moon",
        "Undertale",
        "Sea of Thieves"
    ],
    "falling damage": [
        "Minecraft",
        "Terraria",
        "Ocarina of Time",
        "Castlevania 64",
        "Metroid Prime"
    ],
    "falling": [
        "Minecraft",
        "Terraria",
        "Ocarina of Time",
        "Castlevania 64",
        "Metroid Prime"
    ],
    "unstable platforms": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "VVVVVV",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Metroid Prime",
        "Ori and the Blind Forest",
        "Donkey Kong Country",
        "Castlevania - Circle of the Moon",
        "Zelda II: The Adventure of Link"
    ],
    "unstable": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "VVVVVV",
        "Super Mario Sunshine",
        "Castlevania 64",
        "Metroid Prime",
        "Ori and the Blind Forest",
        "Donkey Kong Country",
        "Castlevania - Circle of the Moon",
        "Zelda II: The Adventure of Link"
    ],
    "melee": [
        "Golden Sun The Lost Age",
        "Terraria",
        "Symphony of the Night",
        "DOOM 1993",
        "DOOM II",
        "Heretic",
        "Sly Cooper and the Thievius Raccoonus",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Castlevania 64",
        "Kirby 64 - The Crystal Shards",
        "Kirby's Dream Land 3",
        "Paper Mario",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance",
        "Wario Land 4",
        "Castlevania - Circle of the Moon",
        "Dark Souls II"
    ],
    "male antagonist": [
        "Mega Man 2",
        "Castlevania 64",
        "EarthBound",
        "Super Mario Sunshine"
    ],
    "male": [
        "Mega Man 2",
        "Castlevania 64",
        "EarthBound",
        "Super Mario Sunshine"
    ],
    "antagonist": [
        "Mega Man 2",
        "Castlevania 64",
        "EarthBound",
        "Super Mario Sunshine"
    ],
    "instant kill": [
        "VVVVVV",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "instant": [
        "VVVVVV",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "kill": [
        "VVVVVV",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "difficulty level": [
        "Minecraft",
        "osu!",
        "Star Fox 64",
        "Mario Kart 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Muse Dash",
        "Castlevania 64",
        "Metroid Prime",
        "Mega Man 2"
    ],
    "difficulty": [
        "Minecraft",
        "osu!",
        "Star Fox 64",
        "Mario Kart 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Muse Dash",
        "Castlevania 64",
        "Metroid Prime",
        "Mega Man 2"
    ],
    "level": [
        "Minecraft",
        "osu!",
        "Star Fox 64",
        "Mario Kart 64",
        "Metroid Zero Mission",
        "DOOM II",
        "Muse Dash",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Donkey Kong Country 2",
        "Castlevania 64",
        "Ocarina of Time",
        "Metroid Prime",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "castlevania - circle of the moon": [
        "Castlevania - Circle of the Moon"
    ],
    "gravity": [
        "Star Fox 64",
        "Metroid Zero Mission",
        "VVVVVV",
        "Symphony of the Night",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Paper Mario",
        "Donkey Kong Country",
        "Castlevania - Circle of the Moon"
    ],
    "wolf": [
        "Minecraft",
        "Star Fox 64",
        "Symphony of the Night",
        "Rogue Legacy",
        "Castlevania - Circle of the Moon"
    ],
    "leveling up": [
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Crystal",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Castlevania - Circle of the Moon",
        "Undertale",
        "Dark Souls II"
    ],
    "leveling": [
        "Golden Sun The Lost Age",
        "EarthBound",
        "Digimon World",
        "Symphony of the Night",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Landstalker - The Treasures of King Nole",
        "Pokemon Crystal",
        "Paper Mario",
        "Zelda II: The Adventure of Link",
        "Castlevania - Circle of the Moon",
        "Undertale",
        "Dark Souls II"
    ],
    "2001": [
        "The Legend of Zelda - Oracle of Ages",
        "Jak and Daxter: The Precursor Legacy",
        "Luigi's Mansion",
        "Wario Land 4",
        "Castlevania - Circle of the Moon",
        "The Legend of Zelda - Oracle of Seasons",
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "dark souls ii": [
        "Dark Souls II"
    ],
    "partial nudity": [
        "Dark Souls Remastered",
        "Dark Souls II"
    ],
    "partial": [
        "Dark Souls Remastered",
        "Dark Souls II"
    ],
    "spider": [
        "Minecraft",
        "Sly Cooper and the Thievius Raccoonus",
        "Donkey Kong Country 2",
        "Ori and the Blind Forest",
        "Zelda II: The Adventure of Link",
        "Dark Souls II"
    ],
    "customizable characters": [
        "Dark Souls III",
        "Terraria",
        "Xenoblade X",
        "Stardew Valley",
        "Dark Souls II"
    ],
    "customizable": [
        "Dark Souls III",
        "Terraria",
        "Xenoblade X",
        "Stardew Valley",
        "Dark Souls II"
    ],
    "checkpoints": [
        "Super Mario Odyssey",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "VVVVVV",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Mega Man 2",
        "Donkey Kong Country",
        "Dark Souls II"
    ],
    "sliding down ladders": [
        "Wario Land 4",
        "Dark Souls III",
        "Kirby 64 - The Crystal Shards",
        "Dark Souls II"
    ],
    "sliding": [
        "Wario Land 4",
        "Dark Souls III",
        "Kirby 64 - The Crystal Shards",
        "Dark Souls II"
    ],
    "down": [
        "Wario Land 4",
        "Dark Souls III",
        "Kirby 64 - The Crystal Shards",
        "Dark Souls II"
    ],
    "ladders": [
        "Wario Land 4",
        "Dark Souls III",
        "Kirby 64 - The Crystal Shards",
        "Dark Souls II"
    ],
    "fire manipulation": [
        "Golden Sun The Lost Age",
        "EarthBound",
        "Minecraft",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Dark Souls II"
    ],
    "fire": [
        "Golden Sun The Lost Age",
        "EarthBound",
        "Minecraft",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Dark Souls II"
    ],
    "manipulation": [
        "Golden Sun The Lost Age",
        "Super Metroid",
        "EarthBound",
        "Minecraft",
        "Super Metroid Map Rando",
        "Rogue Legacy",
        "Ocarina of Time",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Timespinner",
        "Dark Souls II"
    ],
    "2014": [
        "OpenRCT2",
        "The Sims 4",
        "Dark Souls II"
    ],
    "dark souls iii": [
        "Dark Souls III"
    ],
    "pick your gender": [
        "Pokemon Emerald",
        "Dark Souls III",
        "Pokemon Crystal",
        "Terraria"
    ],
    "pick": [
        "Pokemon Emerald",
        "Dark Souls III",
        "Pokemon Crystal",
        "Terraria"
    ],
    "your": [
        "Pokemon Emerald",
        "Dark Souls III",
        "Pokemon Crystal",
        "Terraria"
    ],
    "gender": [
        "Pokemon Emerald",
        "Dark Souls III",
        "Pokemon Crystal",
        "Terraria"
    ],
    "entering world in a painting": [
        "Dark Souls III",
        "Super Mario Odyssey",
        "Super Mario 64",
        "SM64 Romhack"
    ],
    "entering": [
        "Dark Souls III",
        "Super Mario Odyssey",
        "Super Mario 64",
        "SM64 Romhack"
    ],
    "a": [
        "Dark Souls III",
        "Super Mario Odyssey",
        "Super Mario 64",
        "SM64 Romhack"
    ],
    "painting": [
        "Dark Souls III",
        "Super Mario Odyssey",
        "Super Mario 64",
        "SM64 Romhack"
    ],
    "2016": [
        "Stardew Valley",
        "Dark Souls III",
        "Don",
        "The Witness"
    ],
    "diddy kong racing": [
        "Diddy Kong Racing"
    ],
    "racing": [
        "Diddy Kong Racing",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Trackmania",
        "Star Wars Episode I Racer"
    ],
    "behind the waterfall": [
        "The Legend of Zelda - Oracle of Ages",
        "Golden Sun The Lost Age",
        "Super Mario Odyssey",
        "Diddy Kong Racing",
        "Skyward Sword",
        "Symphony of the Night",
        "Donkey Kong Country 3"
    ],
    "behind": [
        "The Legend of Zelda - Oracle of Ages",
        "Golden Sun The Lost Age",
        "Super Mario Odyssey",
        "Diddy Kong Racing",
        "Skyward Sword",
        "Symphony of the Night",
        "Donkey Kong Country 3"
    ],
    "waterfall": [
        "The Legend of Zelda - Oracle of Ages",
        "Golden Sun The Lost Age",
        "Super Mario Odyssey",
        "Diddy Kong Racing",
        "Skyward Sword",
        "Symphony of the Night",
        "Donkey Kong Country 3"
    ],
    "1997": [
        "Diddy Kong Racing",
        "Star Fox 64",
        "Symphony of the Night",
        "Kirby's Dream Land 3",
        "Zork Grand Inquisitor"
    ],
    "donkey kong country": [
        "Donkey Kong Country"
    ],
    "frog": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Jak and Daxter: The Precursor Legacy",
        "Star Fox 64"
    ],
    "overworld": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "The Legend of Zelda",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Final Fantasy Tactics Advance",
        "Donkey Kong Country",
        "Zelda II: The Adventure of Link"
    ],
    "bonus stage": [
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Donkey Kong Country",
        "Spyro 3",
        "Super Mario World"
    ],
    "bonus": [
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Sonic Heroes",
        "Donkey Kong Country",
        "Spyro 3",
        "Super Mario World"
    ],
    "crocodile": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Sly Cooper and the Thievius Raccoonus"
    ],
    "water level": [
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Kingdom Hearts",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "water": [
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Kingdom Hearts",
        "Mega Man 2",
        "Donkey Kong Country"
    ],
    "western games based on japanese ips": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "western": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "games": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "based": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "on": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "japanese": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "ips": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Metroid Prime"
    ],
    "speedrun": [
        "Super Mario 64",
        "Symphony of the Night",
        "Metroid Prime",
        "Donkey Kong Country",
        "SM64 Romhack"
    ],
    "villain turned good": [
        "Golden Sun The Lost Age",
        "Donkey Kong Country",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "turned": [
        "Golden Sun The Lost Age",
        "Donkey Kong Country",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "good": [
        "Golden Sun The Lost Age",
        "Donkey Kong Country",
        "Symphony of the Night",
        "Kingdom Hearts"
    ],
    "over 100% completion": [
        "DOOM II",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "100%": [
        "DOOM II",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Donkey Kong Country"
    ],
    "completion": [
        "Metroid Zero Mission",
        "DOOM II",
        "Symphony of the Night",
        "Donkey Kong Country 2",
        "Donkey Kong Country 3",
        "Metroid Prime",
        "Donkey Kong Country"
    ],
    "resized enemy": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Rogue Legacy",
        "Ocarina of Time"
    ],
    "resized": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Rogue Legacy",
        "Ocarina of Time"
    ],
    "enemy": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Rogue Legacy",
        "Ocarina of Time"
    ],
    "on-the-fly character switching": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Sonic Heroes"
    ],
    "on-the-fly": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Sonic Heroes"
    ],
    "character": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Sonic Heroes"
    ],
    "switching": [
        "Donkey Kong Country 2",
        "Donkey Kong Country",
        "Donkey Kong Country 3",
        "Sonic Heroes"
    ],
    "ape": [
        "Donkey Kong Country 2",
        "Mario Kart 64",
        "Donkey Kong Country",
        "Donkey Kong Country 3"
    ],
    "1994": [
        "Super Metroid",
        "EarthBound",
        "Super Metroid Map Rando",
        "DOOM II",
        "Heretic",
        "Wario Land",
        "Donkey Kong Country"
    ],
    "donkey kong country 2": [
        "Donkey Kong Country 2"
    ],
    "climbing": [
        "The Legend of Zelda - Oracle of Ages",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "Terraria",
        "Super Mario Sunshine",
        "Donkey Kong Country 2",
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "game reference": [
        "The Witness",
        "DOOM II",
        "Rogue Legacy",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Spyro 3"
    ],
    "sprinting mechanics": [
        "Super Mario 64",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "SM64 Romhack",
        "Secret of Evermore"
    ],
    "sprinting": [
        "Super Mario 64",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "SM64 Romhack",
        "Secret of Evermore"
    ],
    "mechanics": [
        "Super Mario 64",
        "Super Mario Sunshine",
        "Ocarina of Time",
        "Donkey Kong Country 2",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Wario Land 4",
        "Majora's Mask Recompiled",
        "SM64 Romhack",
        "Secret of Evermore"
    ],
    "completion percentage": [
        "Donkey Kong Country 2",
        "Metroid Zero Mission",
        "Metroid Prime",
        "Symphony of the Night"
    ],
    "percentage": [
        "Donkey Kong Country 2",
        "Metroid Zero Mission",
        "Metroid Prime",
        "Symphony of the Night"
    ],
    "fireworks": [
        "Donkey Kong Country 2",
        "Kirby 64 - The Crystal Shards",
        "Sly Cooper and the Thievius Raccoonus",
        "Mario & Luigi Superstar Saga"
    ],
    "1995": [
        "Shivers",
        "Yoshi's Island",
        "Donkey Kong Country 2",
        "Lufia II Ancient Cave",
        "Secret of Evermore"
    ],
    "donkey kong country 3": [
        "Donkey Kong Country 3"
    ],
    "snowman": [
        "SM64 Romhack",
        "Super Mario 64",
        "Donkey Kong Country 3",
        "Paper Mario"
    ],
    "1996": [
        "Super Mario 64",
        "Mario Kart 64",
        "Tetris Attack",
        "Pokemon Red and Blue",
        "Donkey Kong Country 3",
        "SM64 Romhack"
    ],
    "dlcquest": [
        "DLCQuest"
    ],
    "deliberately retro": [
        "Super Mario Odyssey",
        "Minecraft",
        "UFO 50",
        "Terraria",
        "VVVVVV",
        "DLCQuest",
        "Timespinner",
        "Stardew Valley"
    ],
    "deliberately": [
        "Super Mario Odyssey",
        "Minecraft",
        "UFO 50",
        "Terraria",
        "VVVVVV",
        "DLCQuest",
        "Timespinner",
        "Stardew Valley"
    ],
    "punctuation mark above head": [
        "The Legend of Zelda - Oracle of Ages",
        "DLCQuest",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal"
    ],
    "punctuation": [
        "The Legend of Zelda - Oracle of Ages",
        "DLCQuest",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal"
    ],
    "mark": [
        "The Legend of Zelda - Oracle of Ages",
        "DLCQuest",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal"
    ],
    "above": [
        "The Legend of Zelda - Oracle of Ages",
        "DLCQuest",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal"
    ],
    "head": [
        "The Legend of Zelda - Oracle of Ages",
        "DLCQuest",
        "Rogue Legacy",
        "Pokemon Emerald",
        "Pokemon Crystal"
    ],
    "2011": [
        "Skyward Sword",
        "Terraria",
        "Minecraft",
        "DLCQuest"
    ],
    "don": [
        "Don"
    ],
    "crafting": [
        "Minecraft",
        "Terraria",
        "Factorio",
        "Raft",
        "Stardew Valley",
        "Don",
        "Factorio - Space Age Without Space",
        "Sea of Thieves"
    ],
    "funny": [
        "A Short Hike",
        "Hunie Pop 2",
        "Getting Over It",
        "Don",
        "Undertale",
        "The Sims 4"
    ],
    "survival horror": [
        "Lethal Company",
        "Don",
        "Resident Evil 2 Remake",
        "Resident Evil 3 Remake"
    ],
    "doom 1993": [
        "DOOM 1993"
    ],
    "intense violence": [
        "Resident Evil 2 Remake",
        "DOOM 1993",
        "Resident Evil 3 Remake"
    ],
    "intense": [
        "Resident Evil 2 Remake",
        "DOOM 1993",
        "Resident Evil 3 Remake"
    ],
    "animated blood and gore": [
        "DOOM 1993",
        "Symphony of the Night"
    ],
    "invisibility": [
        "Paper Mario",
        "DOOM 1993",
        "DOOM II",
        "Sly Cooper and the Thievius Raccoonus"
    ],
    "1993": [
        "DOOM 1993"
    ],
    "doom ii": [
        "DOOM II"
    ],
    "artificial intelligence": [
        "Star Fox 64",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Metroid Prime"
    ],
    "artificial": [
        "Star Fox 64",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Metroid Prime"
    ],
    "intelligence": [
        "Star Fox 64",
        "Mario Kart 64",
        "Jak and Daxter: The Precursor Legacy",
        "Sly Cooper and the Thievius Raccoonus",
        "DOOM II",
        "Metroid Prime"
    ],
    "stat tracking": [
        "The Witness",
        "osu!",
        "DOOM II",
        "Rogue Legacy",
        "Kingdom Hearts",
        "Final Fantasy Tactics Advance"
    ],
    "stat": [
        "The Witness",
        "osu!",
        "DOOM II",
        "Rogue Legacy",
        "Kingdom Hearts",
        "Final Fantasy Tactics Advance"
    ],
    "tracking": [
        "The Witness",
        "osu!",
        "DOOM II",
        "Rogue Legacy",
        "Kingdom Hearts",
        "Final Fantasy Tactics Advance"
    ],
    "rock music": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "ULTRAKILL",
        "DOOM II",
        "Symphony of the Night",
        "Final Fantasy Tactics Advance",
        "Sonic Heroes"
    ],
    "rock": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "ULTRAKILL",
        "DOOM II",
        "Symphony of the Night",
        "Final Fantasy Tactics Advance",
        "Sonic Heroes"
    ],
    "sequence breaking": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "DOOM II",
        "Symphony of the Night",
        "Ocarina of Time",
        "Wario Land 4",
        "Metroid Prime"
    ],
    "sequence": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "DOOM II",
        "Symphony of the Night",
        "Ocarina of Time",
        "Wario Land 4",
        "Metroid Prime"
    ],
    "doronko wanko": [
        "DORONKO WANKO"
    ],
    "dark souls remastered": [
        "Dark Souls Remastered"
    ],
    "dungeon clawler": [
        "Dungeon Clawler"
    ],
    "digimon world": [
        "Digimon World"
    ],
    "earthbound": [
        "EarthBound"
    ],
    "party system": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "EarthBound",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Final Fantasy Tactics Advance",
        "Xenoblade X",
        "Mario & Luigi Superstar Saga"
    ],
    "party": [
        "Golden Sun The Lost Age",
        "Final Fantasy Mystic Quest",
        "EarthBound",
        "Mario Kart 64",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Overcooked! 2",
        "Pokemon Crystal",
        "Paper Mario",
        "Final Fantasy Tactics Advance",
        "Xenoblade X",
        "Mario & Luigi Superstar Saga"
    ],
    "censored version": [
        "Resident Evil 2 Remake",
        "EarthBound",
        "Xenoblade X",
        "Ocarina of Time"
    ],
    "censored": [
        "Resident Evil 2 Remake",
        "EarthBound",
        "Xenoblade X",
        "Ocarina of Time"
    ],
    "version": [
        "Resident Evil 2 Remake",
        "EarthBound",
        "Xenoblade X",
        "Ocarina of Time"
    ],
    "ender lilies": [
        "Ender Lilies"
    ],
    "2021": [
        "The Binding of Isaac Repentance",
        "Hunie Pop 2",
        "Ender Lilies",
        "Inscryption",
        "Lingo"
    ],
    "factorio": [
        "Factorio"
    ],
    "2020": [
        "ULTRAKILL",
        "Hylics 2",
        "Factorio",
        "Trackmania",
        "Hatsune Miku Project Diva Mega Mix+",
        "Hades",
        "Monster Sanctuary",
        "Resident Evil 3 Remake",
        "Noita",
        "Not an idle game"
    ],
    "factorio - space age without space": [
        "Factorio - Space Age Without Space"
    ],
    "faxanadu": [
        "Faxanadu"
    ],
    "1987": [
        "Zillion",
        "Faxanadu",
        "Zelda II: The Adventure of Link",
        "Final Fantasy"
    ],
    "final fantasy": [
        "Final Fantasy"
    ],
    "kids": [
        "Minecraft",
        "Yoshi's Island",
        "Mario Kart 64",
        "Tetris Attack",
        "Pokemon Red and Blue",
        "Pokemon FireRed and LeafGreen",
        "Pokemon Emerald",
        "Overcooked! 2",
        "Pokemon Crystal",
        "Final Fantasy",
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "final fantasy iv free enterprise": [
        "Final Fantasy IV Free Enterprise"
    ],
    "mild suggestive themes": [
        "Final Fantasy IV Free Enterprise",
        "Jak and Daxter: The Precursor Legacy",
        "Terraria"
    ],
    "final fantasy mystic quest": [
        "Final Fantasy Mystic Quest"
    ],
    "casual": [
        "Final Fantasy Mystic Quest",
        "A Short Hike",
        "Getting Over It",
        "Muse Dash",
        "The Sims 4"
    ],
    "ninja": [
        "Final Fantasy Mystic Quest",
        "Rogue Legacy",
        "Final Fantasy Tactics Advance",
        "The Messenger"
    ],
    "1992": [
        "Super Mario Land 2",
        "Landstalker - The Treasures of King Nole",
        "Final Fantasy Mystic Quest"
    ],
    "final fantasy tactics advance": [
        "Final Fantasy Tactics Advance"
    ],
    "tactical": [
        "Overcooked! 2",
        "Wargroove",
        "Final Fantasy Tactics Advance"
    ],
    "grinding": [
        "Old School Runescape",
        "Kingdom Hearts",
        "Final Fantasy Tactics Advance",
        "The Legend of Zelda - Oracle of Seasons",
        "Sea of Thieves"
    ],
    "random encounter": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "random": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "encounter": [
        "Golden Sun The Lost Age",
        "Kingdom Hearts",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Final Fantasy Tactics Advance"
    ],
    "2003": [
        "Toontown",
        "Ratchet & Clank 2",
        "Final Fantasy Tactics Advance",
        "Sonic Heroes",
        "Mario & Luigi Superstar Saga"
    ],
    "yu-gi-oh! forbidden memories": [
        "Yu-Gi-Oh! Forbidden Memories"
    ],
    "getting over it": [
        "Getting Over It"
    ],
    "psychological horror": [
        "Lethal Company",
        "Getting Over It",
        "Undertale",
        "Majora's Mask Recompiled"
    ],
    "psychological": [
        "Lethal Company",
        "Getting Over It",
        "Undertale",
        "Majora's Mask Recompiled"
    ],
    "space": [
        "Super Mario Land 2",
        "Starcraft 2",
        "Getting Over It",
        "VVVVVV"
    ],
    "golden sun the lost age": [
        "Golden Sun The Lost Age"
    ],
    "ancient advanced civilization technology": [
        "Skyward Sword",
        "Golden Sun The Lost Age",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Prime"
    ],
    "ancient": [
        "Skyward Sword",
        "Golden Sun The Lost Age",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Prime"
    ],
    "advanced": [
        "Skyward Sword",
        "Golden Sun The Lost Age",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Prime"
    ],
    "civilization": [
        "Skyward Sword",
        "Golden Sun The Lost Age",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Prime"
    ],
    "technology": [
        "Skyward Sword",
        "Golden Sun The Lost Age",
        "Jak and Daxter: The Precursor Legacy",
        "Metroid Prime"
    ],
    "battle screen": [
        "Golden Sun The Lost Age",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "battle": [
        "Golden Sun The Lost Age",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "screen": [
        "Golden Sun The Lost Age",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "2002": [
        "Golden Sun The Lost Age",
        "MegaMan Battle Network 3",
        "Sly Cooper and the Thievius Raccoonus",
        "Super Mario Sunshine",
        "Kingdom Hearts",
        "Metroid Prime",
        "The Wind Waker"
    ],
    "gzdoom": [
        "gzDoom"
    ],
    "hades": [
        "Hades"
    ],
    "stylized": [
        "ULTRAKILL",
        "Hylics 2",
        "Hades",
        "TUNIC"
    ],
    "heretic": [
        "Heretic"
    ],
    "hollow knight": [
        "Hollow Knight"
    ],
    "creature compendium": [
        "Pokemon Emerald",
        "Symphony of the Night",
        "Metroid Prime",
        "Hollow Knight"
    ],
    "creature": [
        "Pokemon Emerald",
        "Symphony of the Night",
        "Metroid Prime",
        "Hollow Knight"
    ],
    "compendium": [
        "Pokemon Emerald",
        "Symphony of the Night",
        "Metroid Prime",
        "Hollow Knight"
    ],
    "hunie pop": [
        "Hunie Pop"
    ],
    "visual novel": [
        "Hunie Pop 2",
        "Hunie Pop"
    ],
    "visual": [
        "Hunie Pop 2",
        "Hunie Pop"
    ],
    "novel": [
        "Hunie Pop 2",
        "Hunie Pop"
    ],
    "erotic": [
        "Hunie Pop 2",
        "Hunie Pop"
    ],
    "romance": [
        "Hunie Pop 2",
        "Hunie Pop",
        "The Sims 4",
        "Stardew Valley"
    ],
    "2015": [
        "Hunie Pop",
        "Undertale",
        "Xenoblade X",
        "Ori and the Blind Forest"
    ],
    "hunie pop 2": [
        "Hunie Pop 2"
    ],
    "hylics 2": [
        "Hylics 2"
    ],
    "inscryption": [
        "Inscryption"
    ],
    "jak and daxter: the precursor legacy": [
        "Jak and Daxter: The Precursor Legacy"
    ],
    "auto-saving": [
        "The Witness",
        "Jak and Daxter: The Precursor Legacy",
        "Minecraft",
        "Spyro 3"
    ],
    "jigsaw": [
        "Jigsaw"
    ],
    "kirby 64 - the crystal shards": [
        "Kirby 64 - The Crystal Shards"
    ],
    "kid friendly": [
        "Pokemon Emerald",
        "Kirby 64 - The Crystal Shards",
        "Pokemon Crystal",
        "OpenRCT2"
    ],
    "kid": [
        "Pokemon Emerald",
        "Kirby 64 - The Crystal Shards",
        "Pokemon Crystal",
        "OpenRCT2"
    ],
    "friendly": [
        "Pokemon Emerald",
        "Kirby 64 - The Crystal Shards",
        "Pokemon Crystal",
        "OpenRCT2"
    ],
    "whale": [
        "Super Mario Land 2",
        "Kirby 64 - The Crystal Shards",
        "Kirby's Dream Land 3",
        "Kingdom Hearts"
    ],
    "kirby's dream land 3": [
        "Kirby's Dream Land 3"
    ],
    "kingdom hearts": [
        "Kingdom Hearts"
    ],
    "kingdom hearts 2": [
        "Kingdom Hearts 2"
    ],
    "link's awakening dx": [
        "Link's Awakening DX"
    ],
    "fishing": [
        "Minecraft",
        "A Short Hike",
        "Terraria",
        "Link's Awakening DX",
        "Stardew Valley"
    ],
    "tentacles": [
        "Super Mario Sunshine",
        "Link's Awakening DX",
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Metroid Prime",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "animal cruelty": [
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Ocarina of Time"
    ],
    "animal": [
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Ocarina of Time"
    ],
    "cruelty": [
        "Link's Awakening DX",
        "Pokemon Crystal",
        "Pokemon Emerald",
        "Ocarina of Time"
    ],
    "1998": [
        "Link's Awakening DX",
        "Ocarina of Time"
    ],
    "landstalker - the treasures of king nole": [
        "Landstalker - The Treasures of King Nole"
    ],
    "lethal company": [
        "Lethal Company"
    ],
    "monsters": [
        "Lethal Company",
        "Yu-Gi-Oh! 2006",
        "Minecraft",
        "Pokemon FireRed and LeafGreen"
    ],
    "lingo": [
        "Lingo"
    ],
    "lufia ii ancient cave": [
        "Lufia II Ancient Cave"
    ],
    "luigi's mansion": [
        "Luigi's Mansion"
    ],
    "italian accent": [
        "Luigi's Mansion",
        "Mario Kart 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "italian": [
        "Luigi's Mansion",
        "Mario Kart 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "accent": [
        "Luigi's Mansion",
        "Mario Kart 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "super mario land 2": [
        "Super Mario Land 2"
    ],
    "mario": [
        "Super Mario Land 2",
        "Super Mario World",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "turtle": [
        "Super Mario Land 2",
        "Mario Kart 64",
        "Sly Cooper and the Thievius Raccoonus",
        "Super Mario Sunshine",
        "Paper Mario",
        "Mario & Luigi Superstar Saga"
    ],
    "hatsune miku project diva mega mix+": [
        "Hatsune Miku Project Diva Mega Mix+"
    ],
    "the messenger": [
        "The Messenger"
    ],
    "metroid prime": [
        "Metroid Prime"
    ],
    "time limit": [
        "The Witness",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Wario Land 4",
        "Metroid Prime",
        "Risk of Rain"
    ],
    "limit": [
        "The Witness",
        "Super Metroid",
        "Super Metroid Map Rando",
        "Rogue Legacy",
        "Super Mario Sunshine",
        "Wario Land 4",
        "Metroid Prime",
        "Risk of Rain"
    ],
    "countdown timer": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Rogue Legacy",
        "Ocarina of Time",
        "Wario Land 4",
        "Metroid Prime"
    ],
    "countdown": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Rogue Legacy",
        "Ocarina of Time",
        "Wario Land 4",
        "Metroid Prime"
    ],
    "timer": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Rogue Legacy",
        "Ocarina of Time",
        "Wario Land 4",
        "Metroid Prime"
    ],
    "auto-aim": [
        "Skyward Sword",
        "Ocarina of Time",
        "Metroid Prime",
        "The Wind Waker",
        "Majora's Mask Recompiled"
    ],
    "linear gameplay": [
        "Super Mario 64",
        "Metroid Prime",
        "SM64 Romhack",
        "Super Mario Sunshine"
    ],
    "linear": [
        "Super Mario 64",
        "Metroid Prime",
        "SM64 Romhack",
        "Super Mario Sunshine"
    ],
    "isolation": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Metroid Zero Mission",
        "Symphony of the Night",
        "Metroid Prime"
    ],
    "minecraft": [
        "Minecraft"
    ],
    "virtual reality": [
        "Minecraft",
        "Subnautica"
    ],
    "virtual": [
        "Minecraft",
        "Subnautica"
    ],
    "reality": [
        "Minecraft",
        "Subnautica"
    ],
    "procedural generation": [
        "The Witness",
        "Terraria",
        "Minecraft",
        "Rogue Legacy"
    ],
    "procedural": [
        "The Witness",
        "Terraria",
        "Minecraft",
        "Rogue Legacy"
    ],
    "generation": [
        "The Witness",
        "Terraria",
        "Minecraft",
        "Rogue Legacy"
    ],
    "mario kart 64": [
        "Mario Kart 64"
    ],
    "mario & luigi superstar saga": [
        "Mario & Luigi Superstar Saga"
    ],
    "super-ness": [
        "SM64 Romhack",
        "Super Mario 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "wiggler": [
        "Super Mario Odyssey",
        "Super Mario 64",
        "Super Mario Sunshine",
        "Mario & Luigi Superstar Saga",
        "SM64 Romhack"
    ],
    "princess peach": [
        "SM64 Romhack",
        "Super Mario 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "peach": [
        "SM64 Romhack",
        "Super Mario 64",
        "Mario & Luigi Superstar Saga",
        "Super Mario Sunshine"
    ],
    "mega man 2": [
        "Mega Man 2"
    ],
    "megaman battle network 3": [
        "MegaMan Battle Network 3"
    ],
    "majora's mask recompiled": [
        "Majora's Mask Recompiled"
    ],
    "momodora moonlit farewell": [
        "Momodora Moonlit Farewell"
    ],
    "monster sanctuary": [
        "Monster Sanctuary"
    ],
    "tobacco reference": [
        "Monster Sanctuary"
    ],
    "muse dash": [
        "Muse Dash"
    ],
    "mild lyrics": [
        "Muse Dash",
        "Sonic Adventure 2 Battle"
    ],
    "lyrics": [
        "Muse Dash",
        "Sonic Adventure 2 Battle"
    ],
    "metroid zero mission": [
        "Metroid Zero Mission"
    ],
    "2004": [
        "Pokemon Emerald",
        "Metroid Zero Mission",
        "Pokemon FireRed and LeafGreen",
        "Paper Mario The Thousand Year Door"
    ],
    "noita": [
        "Noita"
    ],
    "ocarina of time": [
        "Ocarina of Time"
    ],
    "time manipulation": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Rogue Legacy",
        "Ocarina of Time",
        "Timespinner"
    ],
    "color cartridges": [
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Zelda II: The Adventure of Link",
        "Ocarina of Time"
    ],
    "color": [
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Zelda II: The Adventure of Link",
        "Ocarina of Time"
    ],
    "cartridges": [
        "Pokemon Emerald",
        "Pokemon Crystal",
        "Zelda II: The Adventure of Link",
        "Ocarina of Time"
    ],
    "openrct2": [
        "OpenRCT2"
    ],
    "business": [
        "Stardew Valley",
        "OpenRCT2"
    ],
    "ori and the blind forest": [
        "Ori and the Blind Forest"
    ],
    "thriller": [
        "Super Metroid",
        "Super Metroid Map Rando",
        "Ori and the Blind Forest"
    ],
    "old school runescape": [
        "Old School Runescape"
    ],
    "osu!": [
        "osu!"
    ],
    "auditory": [
        "osu!"
    ],
    "outer wilds": [
        "Outer Wilds"
    ],
    "overcooked! 2": [
        "Overcooked! 2"
    ],
    "paint": [
        "Paint"
    ],
    "paper mario": [
        "Paper Mario"
    ],
    "peaks of yore": [
        "Peaks of Yore"
    ],
    "pokemon mystery dungeon explorers of sky": [
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "mild cartoon violence": [
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "2009": [
        "Pokemon Mystery Dungeon Explorers of Sky"
    ],
    "pokemon crystal": [
        "Pokemon Crystal"
    ],
    "pokemon emerald": [
        "Pokemon Emerald"
    ],
    "pokemon firered and leafgreen": [
        "Pokemon FireRed and LeafGreen"
    ],
    "pokemon red and blue": [
        "Pokemon Red and Blue"
    ],
    "pseudoregalia": [
        "Pseudoregalia"
    ],
    "ratchet & clank 2": [
        "Ratchet & Clank 2"
    ],
    "raft": [
        "Raft"
    ],
    "resident evil 2 remake": [
        "Resident Evil 2 Remake"
    ],
    "resident evil 3 remake": [
        "Resident Evil 3 Remake"
    ],
    "rogue legacy": [
        "Rogue Legacy"
    ],
    "risk of rain": [
        "Risk of Rain"
    ],
    "risk of rain 2": [
        "Risk of Rain 2"
    ],
    "drug reference": [
        "Risk of Rain 2"
    ],
    "drug": [
        "Risk of Rain 2"
    ],
    "sonic adventure 2 battle": [
        "Sonic Adventure 2 Battle"
    ],
    "2012": [
        "Sonic Adventure 2 Battle"
    ],
    "sonic adventure dx": [
        "Sonic Adventure DX"
    ],
    "2010": [
        "Starcraft 2",
        "VVVVVV",
        "Sonic Adventure DX"
    ],
    "starcraft 2": [
        "Starcraft 2"
    ],
    "warfare": [
        "Wargroove 2",
        "Starcraft 2",
        "Wargroove"
    ],
    "sea of thieves": [
        "Sea of Thieves"
    ],
    "not an idle game": [
        "Not an idle game"
    ],
    "shivers": [
        "Shivers"
    ],
    "realistic blood and gore": [
        "Shivers"
    ],
    "realistic": [
        "Shivers"
    ],
    "realistic blood": [
        "Shivers"
    ],
    "point-and-click": [
        "Shivers",
        "Zork Grand Inquisitor"
    ],
    "a short hike": [
        "A Short Hike"
    ],
    "the sims 4": [
        "The Sims 4"
    ],
    "sly cooper and the thievius raccoonus": [
        "Sly Cooper and the Thievius Raccoonus"
    ],
    "stealth": [
        "Sly Cooper and the Thievius Raccoonus"
    ],
    "super metroid": [
        "Super Metroid"
    ],
    "super metroid map rando": [
        "Super Metroid Map Rando"
    ],
    "super mario 64": [
        "Super Mario 64"
    ],
    "rabbit": [
        "The Legend of Zelda - Oracle of Ages",
        "Super Mario Odyssey",
        "Super Mario 64",
        "Terraria",
        "Sonic Heroes",
        "SM64 Romhack"
    ],
    "sm64 romhack": [
        "SM64 Romhack"
    ],
    "super mario odyssey": [
        "Super Mario Odyssey"
    ],
    "super mario sunshine": [
        "Super Mario Sunshine"
    ],
    "super mario world": [
        "Super Mario World"
    ],
    "1990": [
        "Super Mario World"
    ],
    "smz3": [
        "SMZ3"
    ],
    "secret of evermore": [
        "Secret of Evermore"
    ],
    "sonic heroes": [
        "Sonic Heroes"
    ],
    "symphony of the night": [
        "Symphony of the Night"
    ],
    "playstation plus": [
        "Spyro 3",
        "Terraria",
        "VVVVVV",
        "Symphony of the Night"
    ],
    "playstation": [
        "Spyro 3",
        "Terraria",
        "VVVVVV",
        "Symphony of the Night"
    ],
    "plus": [
        "Spyro 3",
        "Terraria",
        "VVVVVV",
        "Symphony of the Night"
    ],
    "slay the spire": [
        "Slay the Spire"
    ],
    "spyro 3": [
        "Spyro 3"
    ],
    "skyward sword": [
        "Skyward Sword"
    ],
    "stardew valley": [
        "Stardew Valley"
    ],
    "star fox 64": [
        "Star Fox 64"
    ],
    "subnautica": [
        "Subnautica"
    ],
    "star wars episode i racer": [
        "Star Wars Episode I Racer"
    ],
    "the binding of isaac repentance": [
        "The Binding of Isaac Repentance"
    ],
    "terraria": [
        "Terraria"
    ],
    "tetris attack": [
        "Tetris Attack"
    ],
    "timespinner": [
        "Timespinner"
    ],
    "the legend of zelda": [
        "The Legend of Zelda"
    ],
    "1986": [
        "The Legend of Zelda"
    ],
    "the legend of zelda - oracle of ages": [
        "The Legend of Zelda - Oracle of Ages"
    ],
    "the legend of zelda - oracle of seasons": [
        "The Legend of Zelda - Oracle of Seasons"
    ],
    "toontown": [
        "Toontown"
    ],
    "twilight princess": [
        "Twilight Princess"
    ],
    "2006": [
        "Yu-Gi-Oh! 2006",
        "Twilight Princess"
    ],
    "trackmania": [
        "Trackmania"
    ],
    "paper mario the thousand year door": [
        "Paper Mario The Thousand Year Door"
    ],
    "tunic": [
        "TUNIC"
    ],
    "the wind waker": [
        "The Wind Waker"
    ],
    "tyrian": [
        "Tyrian"
    ],
    "ufo 50": [
        "UFO 50"
    ],
    "ultrakill": [
        "ULTRAKILL"
    ],
    "undertale": [
        "Undertale"
    ],
    "vvvvvv": [
        "VVVVVV"
    ],
    "wargroove": [
        "Wargroove"
    ],
    "wargroove 2": [
        "Wargroove 2"
    ],
    "the witness": [
        "The Witness"
    ],
    "wario land": [
        "Wario Land"
    ],
    "wario land 4": [
        "Wario Land 4"
    ],
    "wordipelago": [
        "Wordipelago"
    ],
    "xenoblade x": [
        "Xenoblade X"
    ],
    "yacht dice": [
        "Yacht Dice"
    ],
    "yoshi's island": [
        "Yoshi's Island"
    ],
    "yu-gi-oh! 2006": [
        "Yu-Gi-Oh! 2006"
    ],
    "yu-gi-oh! dungeon dice monsters": [
        "Yu-Gi-Oh! Dungeon Dice Monsters"
    ],
    "zelda ii: the adventure of link": [
        "Zelda II: The Adventure of Link"
    ],
    "zillion": [
        "Zillion"
    ],
    "zork grand inquisitor": [
        "Zork Grand Inquisitor"
    ]
}