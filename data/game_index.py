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
    "adventure": {
        "igdb_id": "12239",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/qzcqrjruhpuge5egkzgj.jpg",
        "game_name": "adventure",
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
    "against_the_storm": {
        "igdb_id": "147519",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7j13.jpg",
        "game_name": "against the storm",
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
            "base building",
            "roguelite"
        ],
        "release_date": "2023"
    },
    "ahit": {
        "igdb_id": "6705",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pl5.jpg",
        "game_name": "a hat in time",
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
    "albw": {
        "igdb_id": "2909",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3p0j.jpg",
        "game_name": "a link between worlds",
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
            "bees",
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "2013"
    },
    "alttp": {
        "igdb_id": "1026",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3vzn.jpg",
        "game_name": "a link to the past",
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
            "popular",
            "zelda",
            "link"
        ],
        "release_date": "1991"
    },
    "animal_well": {
        "igdb_id": "191435",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4hdh.jpg",
        "game_name": "animal well",
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
            "dark",
            "2d",
            "metroidvania",
            "cute",
            "atmospheric",
            "pixel art",
            "relaxing",
            "controller support"
        ],
        "release_date": "2024"
    },
    "apeescape": {
        "igdb_id": "3762",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2gzc.jpg",
        "game_name": "ape escape",
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
    "apsudoku": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "sudoku",
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
    "aquaria": {
        "igdb_id": "7406",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1r7r.jpg",
        "game_name": "aquaria",
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
            "save point",
            "underwater gameplay",
            "shape-shifting",
            "plot twist"
        ],
        "release_date": "2007"
    },
    "archipidle": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "archipidle",
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
    "aus": {
        "igdb_id": "72926",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2nok.jpg",
        "game_name": "an untitled story",
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
    "balatro": {
        "igdb_id": "251833",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9f4g.jpg",
        "game_name": "balatro",
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
    "banjo_tooie": {
        "igdb_id": "3418",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6c1w.jpg",
        "game_name": "banjo-tooie",
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
            "animals",
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
            "character growth",
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
    "blasphemous": {
        "igdb_id": "26820",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9yoj.jpg",
        "game_name": "blasphemous",
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
    "bomb_rush_cyberfunk": {
        "igdb_id": "135940",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6ya8.jpg",
        "game_name": "bomb rush cyberfunk",
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
    "brotato": {
        "igdb_id": "199116",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4pcj.jpg",
        "game_name": "brotato",
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
    "bumpstik": {
        "igdb_id": "271950",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co78k5.jpg",
        "game_name": "bumper stickers",
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
    "candybox2": {
        "igdb_id": "62779",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3tqk.jpg",
        "game_name": "candy box 2",
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
    "cat_quest": {
        "igdb_id": "36597",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qlq.jpg",
        "game_name": "cat quest",
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
    "celeste": {
        "igdb_id": "26226",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3byy.jpg",
        "game_name": "celeste",
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
            "story rich",
            "great soundtrack",
            "digital distribution",
            "lgbtq+",
            "conversation"
        ],
        "release_date": "2018"
    },
    "celeste64": {
        "igdb_id": "284430",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7oz4.jpg",
        "game_name": "celeste 64",
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
    "chainedechoes": {
        "igdb_id": "117271",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co544u.jpg",
        "game_name": "chained echoes",
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
    "chatipelago": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "chat plays multiworldgg!",
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
    "checksfinder": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "checksfinder",
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
    "civ_6": {
        "igdb_id": "293",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1rjp.jpg",
        "game_name": "civilization vi",
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
    "clique": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "clique",
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
    "crosscode": {
        "igdb_id": "35282",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co28wy.jpg",
        "game_name": "crosscode",
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
    "ctjot": {
        "igdb_id": "20398",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co54iw.jpg",
        "game_name": "chrono trigger jets of time",
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
    "cuphead": {
        "igdb_id": "9061",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co62ao.jpg",
        "game_name": "log options that are overridden from incompatible combinations to console.",
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
            "boss assistance"
        ],
        "release_date": "2017"
    },
    "cv64": {
        "igdb_id": "1130",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5geb.jpg",
        "game_name": "castlevania 64",
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
    "cvcotm": {
        "igdb_id": "1132",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2zq1.jpg",
        "game_name": "castlevania - circle of the moon",
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
    "dark_souls_2": {
        "igdb_id": "2368",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2eoo.jpg",
        "game_name": "dark souls ii",
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
            "dark",
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
    "dark_souls_3": {
        "igdb_id": "11133",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1vcf.jpg",
        "game_name": "dark souls iii",
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
            "interconnected-world",
            "popular"
        ],
        "release_date": "2016"
    },
    "diddy_kong_racing": {
        "igdb_id": "2723",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wgj.jpg",
        "game_name": "diddy kong racing",
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
            "go-kart",
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
    "dk64": {
        "igdb_id": "1096",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co289i.jpg",
        "game_name": "donkey kong 64",
        "igdb_name": "donkey kong 64",
        "rating": [
            "mild animated violence"
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
            "comedy"
        ],
        "platforms": [
            "nintendo 64",
            "wii u"
        ],
        "storyline": "",
        "keywords": [
            "gravity",
            "minigames",
            "death",
            "fairy",
            "multiple protagonists",
            "multiple endings",
            "artificial intelligence",
            "giant insects",
            "day/night cycle",
            "death match",
            "digital distribution",
            "anthropomorphism",
            "monkey",
            "gorilla",
            "polygonal 3d",
            "upgradeable weapons",
            "loot gathering",
            "descendants of other characters",
            "character growth",
            "real-time combat",
            "moving platforms",
            "recurring boss",
            "invisible wall",
            "franchise reboot",
            "western games based on japanese ips",
            "over 100% completion",
            "completion percentage",
            "mine cart sequence",
            "invisibility",
            "foreshadowing",
            "ape",
            "collection marathon",
            "retroachievements"
        ],
        "release_date": "1999"
    },
    "dkc": {
        "igdb_id": "1090",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co70qn.jpg",
        "game_name": "donkey kong country",
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
            "gorilla",
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
            "franchise reboot",
            "auto-scrolling levels",
            "western games based on japanese ips",
            "speedrun",
            "boss assistance",
            "villain turned good",
            "over 100% completion",
            "mine cart sequence",
            "ambient music",
            "resized enemy",
            "on-the-fly character switching",
            "ape",
            "buddy system",
            "retroachievements"
        ],
        "release_date": "1994"
    },
    "dkc2": {
        "igdb_id": "1092",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co217m.jpg",
        "game_name": "donkey kong country 2",
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
            "gorilla",
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
            "completion percentage",
            "mine cart sequence",
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
    "dkc3": {
        "igdb_id": "1094",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co217n.jpg",
        "game_name": "donkey kong country 3 is an action platforming game.",
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
            "gorilla",
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
    "dlcquest": {
        "igdb_id": "3004",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2105.jpg",
        "game_name": "dlcquest",
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
    "dontstarvetogether": {
        "igdb_id": "17832",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6la0.jpg",
        "game_name": "dont starve together",
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
    "doom_1993": {
        "igdb_id": "673",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5rav.jpg",
        "game_name": "doom 1993",
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
    "doom_ii": {
        "igdb_id": "312",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6iip.jpg",
        "game_name": "doom ii",
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
            "death match",
            "digital distribution",
            "voice acting",
            "human",
            "breaking the fourth wall",
            "pop culture reference",
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
    "doronko_wanko": {
        "igdb_id": "290647",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7zj5.jpg",
        "game_name": "doronko wanko",
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
    "dsr": {
        "igdb_id": "81085",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2uro.jpg",
        "game_name": "dark souls is a game where you die.",
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
    "dungeon_clawler": {
        "igdb_id": "290897",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7ygu.jpg",
        "game_name": "dungeon clawler",
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
    "dw1": {
        "igdb_id": "3878",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2dyy.jpg",
        "game_name": "digimon world is a game about raising digital monsters and recruiting allies to save the digital world.",
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
    "earthbound": {
        "igdb_id": "2899",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6v07.jpg",
        "game_name": "earthbound",
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
    "enderlilies": {
        "igdb_id": "138858",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9s9e.jpg",
        "game_name": "ender lilies",
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
            "forest",
            "witches",
            "soulslike",
            "conversation"
        ],
        "release_date": "2021"
    },
    "factorio": {
        "igdb_id": "7046",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1tfy.jpg",
        "game_name": "factorio",
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
    "factorio_saws": {
        "igdb_id": "263344",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co91k3.jpg",
        "game_name": "factorio space age without space",
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
    "faxanadu": {
        "igdb_id": "1974",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5jif.jpg",
        "game_name": "faxanadu",
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
    "ff1": {
        "igdb_id": "385",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2xv8.jpg",
        "game_name": "final fantasy",
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
    "ff4fe": {
        "igdb_id": "387",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2y6s.jpg",
        "game_name": "final fantasy iv free enterprise",
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
            "turn-based strategy (tbs)",
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
    "ffmq": {
        "igdb_id": "415",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2y0b.jpg",
        "game_name": "final fantasy mystic quest",
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
            "franchise reboot",
            "retroachievements"
        ],
        "release_date": "1992"
    },
    "ffta": {
        "igdb_id": "414",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wyp.jpg",
        "game_name": "final fantasy tactics advance",
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
            "franchise reboot",
            "androgyny",
            "random encounter",
            "damage over time"
        ],
        "release_date": "2003"
    },
    "fm": {
        "igdb_id": "4108",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ui5.jpg",
        "game_name": "yu-gi-oh! forbidden memories",
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
    "generic": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "generic",
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
    "getting_over_it": {
        "igdb_id": "72373",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3wl5.jpg",
        "game_name": "getting over it",
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
            "digital distribution"
        ],
        "release_date": "2017"
    },
    "gstla": {
        "igdb_id": "1173",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co25rt.jpg",
        "game_name": "golden sun the lost age",
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
    "gzdoom": {
        "igdb_id": "307741",
        "cover_url": "",
        "game_name": "gzdoom",
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
    "hades": {
        "igdb_id": "113112",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co39vc.jpg",
        "game_name": "hades",
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
    "hcniko": {
        "igdb_id": "142405",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2o6i.jpg",
        "game_name": "here comes niko!",
        "igdb_name": "here comes niko!",
        "rating": [],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "platform",
            "puzzle",
            "adventure",
            "indie"
        ],
        "themes": [
            "action",
            "comedy"
        ],
        "platforms": [
            "pc (microsoft windows)",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "aliens",
            "exploration",
            "animals",
            "3d",
            "minigames",
            "fishing",
            "frog",
            "female protagonist",
            "crossover",
            "forest",
            "stylized",
            "achievements",
            "cute",
            "pixel art",
            "snow",
            "dog",
            "relaxing",
            "talking animals",
            "3d platformer",
            "swimming",
            "anthropomorphism",
            "game reference",
            "secret area",
            "behind the waterfall",
            "controller support"
        ],
        "release_date": "2021"
    },
    "heretic": {
        "igdb_id": "6362",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mwz.jpg",
        "game_name": "heretic",
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
            "death match",
            "digital distribution",
            "skeletons",
            "melee",
            "secret area",
            "hidden room"
        ],
        "release_date": "1994"
    },
    "hk": {
        "igdb_id": "14593",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co93cr.jpg",
        "game_name": "hollow knight",
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
            "dark",
            "2d",
            "metroidvania",
            "action-adventure",
            "achievements",
            "atmospheric",
            "giant insects",
            "silent protagonist",
            "crowdfunding",
            "2d platformer",
            "crowd funded",
            "shielded enemies",
            "parrying",
            "merchants",
            "fast traveling",
            "creature compendium",
            "controller support",
            "interconnected-world",
            "popular"
        ],
        "release_date": "2017"
    },
    "huniepop": {
        "igdb_id": "9655",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2sor.jpg",
        "game_name": "hunie pop",
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
    "huniepop2": {
        "igdb_id": "72472",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5x87.jpg",
        "game_name": "hunie pop 2",
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
    "hylics2": {
        "igdb_id": "98469",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co290q.jpg",
        "game_name": "hylics 2 is a surreal and unusual rpg, with a bizarre yet unique visual style. play as wayne,",
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
    "inscryption": {
        "igdb_id": "139090",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co401c.jpg",
        "game_name": "inscryption",
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
    "jakanddaxter": {
        "igdb_id": "1528",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1w7q.jpg",
        "game_name": "jak and daxter: the precursor legacy",
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
            "language selection",
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
    "jigsaw": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "make a jigsaw puzzle! but first you'll have to find your pieces.",
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
    "k64": {
        "igdb_id": "2713",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wcz.jpg",
        "game_name": "kirby 64 - the crystal shards",
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
    "kdl3": {
        "igdb_id": "3720",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co25su.jpg",
        "game_name": "kirby's dream land 3",
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
    "kh1": {
        "igdb_id": "1219",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co30zf.jpg",
        "game_name": "kingdom hearts",
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
    "kh2": {
        "igdb_id": "1221",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co30t1.jpg",
        "game_name": "kingdom hearts 2",
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
        "keywords": [
            "popular"
        ],
        "release_date": "2005"
    },
    "ladx": {
        "igdb_id": "1027",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4o47.jpg",
        "game_name": "link's awakening dx beta",
        "igdb_name": "the legend of zelda: link's awakening dx",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric",
            "side view"
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
            "chicken",
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
            "another world",
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "1998"
    },
    "landstalker": {
        "igdb_id": "15072",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kb9.jpg",
        "game_name": "landstalker - the treasures of king nole",
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
    "lethal_company": {
        "igdb_id": "212089",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5ive.jpg",
        "game_name": "lethal company",
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
    "lingo": {
        "igdb_id": "189169",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5iy5.jpg",
        "game_name": "lingo",
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
    "lufia2ac": {
        "igdb_id": "1178",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9mg3.jpg",
        "game_name": "lufia ii: ancient cave",
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
    "luigismansion": {
        "igdb_id": "2485",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wr1.jpg",
        "game_name": "luigi's mansion",
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
    "marioland2": {
        "igdb_id": "1071",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7gxg.jpg",
        "game_name": "super mario land 2",
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
    "mario_kart_double_dash": {
        "igdb_id": "2344",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7ndu.jpg",
        "game_name": "mario kart double dash",
        "igdb_name": "mario kart: double dash!!",
        "rating": [
            "mild cartoon violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "racing",
            "arcade"
        ],
        "themes": [
            "action",
            "kids"
        ],
        "platforms": [
            "nintendo gamecube"
        ],
        "storyline": "",
        "keywords": [
            "go-kart",
            "yoshi",
            "mario",
            "princess peach"
        ],
        "release_date": "2003"
    },
    "megamix": {
        "igdb_id": "120278",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co991n.jpg",
        "game_name": "hatsune miku project diva mega mix+",
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
    "meritous": {
        "igdb_id": "78479",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/zkameytcg0na8alfswsp.jpg",
        "game_name": "meritous gaiden is a procedurally generated bullet-hell dungeon crawl game.",
        "igdb_name": "meritous",
        "rating": [],
        "player_perspectives": [
            "bird view / isometric"
        ],
        "genres": [
            "role-playing (rpg)"
        ],
        "themes": [],
        "platforms": [
            "pc (microsoft windows)"
        ],
        "storyline": "",
        "keywords": [],
        "release_date": "2008"
    },
    "messenger": {
        "igdb_id": "71628",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2hr9.jpg",
        "game_name": "the messenger",
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
            "difficult"
        ],
        "release_date": "2018"
    },
    "metroidprime": {
        "igdb_id": "1105",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3w4w.jpg",
        "game_name": "metroid prime",
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
            "foreshadowing",
            "isolation"
        ],
        "release_date": "2002"
    },
    "minecraft": {
        "igdb_id": "121",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8fu6.jpg",
        "game_name": "minecraft",
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
            "animals",
            "construction",
            "fishing",
            "crafting",
            "death",
            "procedural generation",
            "horse",
            "chicken",
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
            "language selection",
            "polygonal 3d",
            "bow and arrow",
            "deliberately retro",
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
    "mk64": {
        "igdb_id": "2342",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co67hm.jpg",
        "game_name": "mario kart 64",
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
            "go-kart",
            "crossover",
            "princess",
            "artificial intelligence",
            "snow",
            "sequel",
            "bats",
            "turtle",
            "explosion",
            "death match",
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
    "mlss": {
        "igdb_id": "3351",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co21rg.jpg",
        "game_name": "mario & luigi superstar saga",
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
    "mm2": {
        "igdb_id": "1734",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5572.jpg",
        "game_name": "mega man 2",
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
    "mmbn3": {
        "igdb_id": "1758",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co203k.jpg",
        "game_name": "megaman battle network 3",
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
    "mm_recomp": {
        "igdb_id": "1030",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3pah.jpg",
        "game_name": "majora's mask recompiled",
        "igdb_name": "the legend of zelda: majora's mask",
        "rating": [
            "animated violence",
            "cartoon violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "puzzle",
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
    "momodoramoonlitfarewell": {
        "igdb_id": "188088",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7mxs.jpg",
        "game_name": "momodora moonlit farewell",
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
            "metroidvania"
        ],
        "release_date": "2024"
    },
    "monster_sanctuary": {
        "igdb_id": "89594",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1q3q.jpg",
        "game_name": "monster sanctuary",
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
    "musedash": {
        "igdb_id": "86316",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6h43.jpg",
        "game_name": "muse dash",
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
    "mzm": {
        "igdb_id": "1107",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1vci.jpg",
        "game_name": "metroid: zero mission is a retelling of the first metroid on nes. relive samus' first adventure on planet zebes with",
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
            "foreshadowing",
            "isolation",
            "interconnected-world"
        ],
        "release_date": "2004"
    },
    "noita": {
        "igdb_id": "52006",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qp1.jpg",
        "game_name": "noita",
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
            "roguelite"
        ],
        "release_date": "2020"
    },
    "oot": {
        "igdb_id": "1029",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3nnx.jpg",
        "game_name": "ocarina of time",
        "igdb_name": "the legend of zelda: ocarina of time",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "third person"
        ],
        "genres": [
            "puzzle",
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
            "chicken",
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
            "digital distribution",
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
            "character growth",
            "side quests",
            "auto-aim",
            "real-time combat",
            "underwater gameplay",
            "a.i. companion",
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
            "retroachievements",
            "popular",
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "1998"
    },
    "openrct2": {
        "igdb_id": "80720",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ngq.jpg",
        "game_name": "openrct2",
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
    "oribf": {
        "igdb_id": "7344",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1y41.jpg",
        "game_name": "ori and the blind forest",
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
            "forest",
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
    "osrs": {
        "igdb_id": "79824",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mo1.jpg",
        "game_name": "old school runescape",
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
    "osu": {
        "igdb_id": "3012",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8a4m.jpg",
        "game_name": "osu! is a free to play rhythm game featuring 4 modes, an online ranking system/statistics,",
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
    "outer_wilds": {
        "igdb_id": "11737",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co65ac.jpg",
        "game_name": "outer wilds",
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
    "overcooked2": {
        "igdb_id": "103341",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1usu.jpg",
        "game_name": "overcooked! 2",
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
    "paint": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "paint",
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
    "papermario": {
        "igdb_id": "3340",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1qda.jpg",
        "game_name": "paper mario",
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
    "peaks_of_yore": {
        "igdb_id": "238690",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8zzc.jpg",
        "game_name": "peaks of yore",
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
    "placidplasticducksim": {
        "igdb_id": "204122",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4yq5.jpg",
        "game_name": "placid plastic duck simulator",
        "igdb_name": "placid plastic duck simulator",
        "rating": [],
        "player_perspectives": [
            "third person",
            "bird view / isometric"
        ],
        "genres": [
            "music",
            "puzzle",
            "simulator"
        ],
        "themes": [
            "comedy",
            "sandbox",
            "kids",
            "party"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "",
        "keywords": [
            "casual",
            "pop culture reference"
        ],
        "release_date": "2022"
    },
    "pmd_eos": {
        "igdb_id": "2323",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7ovf.jpg",
        "game_name": "pokemon mystery dungeon explorers of sky",
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
    "pokemon_crystal": {
        "igdb_id": "1514",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pil.jpg",
        "game_name": "pokemon crystal",
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
            "character growth",
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
            "damage over time"
        ],
        "release_date": "2000"
    },
    "pokemon_emerald": {
        "igdb_id": "1517",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1zhr.jpg",
        "game_name": "pokemon emerald",
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
            "popular"
        ],
        "release_date": "2004"
    },
    "pokemon_frlg": {
        "igdb_id": "1516",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1zip.jpg",
        "game_name": "pokemon firered and leafgreen",
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
            "collecting"
        ],
        "release_date": "2004"
    },
    "pokemon_rb": {
        "igdb_id": "1561",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5pi4.jpg",
        "game_name": "pokemon red and blue",
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
    "powerwashsimulator": {
        "igdb_id": "138590",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7gek.jpg",
        "game_name": "powerwash simulator",
        "igdb_name": "powerwash simulator",
        "rating": [],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "simulator",
            "indie"
        ],
        "themes": [
            "business",
            "sandbox"
        ],
        "platforms": [
            "xbox series x|s",
            "playstation 4",
            "pc (microsoft windows)",
            "playstation 5",
            "xbox one",
            "nintendo switch"
        ],
        "storyline": "you're looking to start a business \u2013 but what? you decide power washing is super satisfying and you'd like to turn it into a full time gig. you put your good friend harper shaw, a bargain hunter and auction lot buyer up to the task of finding you the perfect vehicle for your new enterprise.\n\nthrough completing various jobs, you get to know the citizens of muckingham, the small town in which the game is set, helping wash away their various problems. figuratively... and literally!\n\nthe first client you are introduced to is cal, harper shaw's new disgruntled neighbour. they are a volcanologist, who\u2019s moved back into town to study mount rushless, the local volcano, and to help look after his ageing parents. he's so worked up as he bought a house without even looking at a picture of the back garden. he thinks the previous owners might have even owned rhinos it's that dirty...",
        "keywords": [
            "3d",
            "funny",
            "atmospheric",
            "relaxing",
            "story rich",
            "family friendly"
        ],
        "release_date": "2022"
    },
    "pseudoregalia": {
        "igdb_id": "259465",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6vcy.jpg",
        "game_name": "pseudoregalia",
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
    "rac2": {
        "igdb_id": "1770",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co230n.jpg",
        "game_name": "ratchet & clank 2",
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
    "raft": {
        "igdb_id": "27082",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1xdc.jpg",
        "game_name": "raft",
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
    "residentevil2remake": {
        "igdb_id": "19686",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1ir3.jpg",
        "game_name": "resident evil 2 remake",
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
    "residentevil3remake": {
        "igdb_id": "115115",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co22l7.jpg",
        "game_name": "resident evil 3 remake",
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
    "rimworld": {
        "igdb_id": "9789",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1j6x.jpg",
        "game_name": "rimworld",
        "igdb_name": "rimworld",
        "rating": [],
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
            "science fiction",
            "survival"
        ],
        "platforms": [
            "linux",
            "pc (microsoft windows)",
            "mac"
        ],
        "storyline": "rimworld follows three survivors from a crashed space liner as they build a colony on a frontier world at the rim of known space. inspired by the space western vibe of firefly, the deep simulation of dwarf fortress, and the epic scale of dune and warhammer 40,000.\n\nmanage colonists' moods, needs, thoughts, individual wounds, and illnesses. engage in deeply-simulated small-team gunplay. fashion structures, weapons, and apparel from metal, wood, stone, cloth, or exotic, futuristic materials. fight pirate raiders, hostile tribes, rampaging animals and ancient killing machines. discover a new generated world each time you play. build colonies in biomes ranging from desert to jungle to tundra, each with unique flora and fauna. manage and develop colonists with unique backstories, traits, and skills. learn to play easily with the help of an intelligent and unobtrusive ai tutor.",
        "keywords": [
            "management",
            "base building"
        ],
        "release_date": "2018"
    },
    "rogue_legacy": {
        "igdb_id": "3221",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co27fi.jpg",
        "game_name": "rogue legacy",
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
            "easter egg",
            "teleportation",
            "darkness",
            "explosion",
            "digital distribution",
            "countdown timer",
            "bow and arrow",
            "breaking the fourth wall",
            "pop culture reference",
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
    "ror1": {
        "igdb_id": "3173",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2k2z.jpg",
        "game_name": "risk of rain",
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
    "ror2": {
        "igdb_id": "28512",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2eu7.jpg",
        "game_name": "risk of rain 2",
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
    "sa2b": {
        "igdb_id": "192194",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5p3o.jpg",
        "game_name": "sonic adventure 2 battle",
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
    "sadx": {
        "igdb_id": "192114",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4iln.jpg",
        "game_name": "sonic adventure dx",
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
    "satisfactory": {
        "igdb_id": "90558",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8tfy.jpg",
        "game_name": "satisfactory",
        "igdb_name": "satisfactory",
        "rating": [],
        "player_perspectives": [
            "first person"
        ],
        "genres": [
            "simulator",
            "strategy",
            "adventure",
            "indie"
        ],
        "themes": [
            "science fiction",
            "sandbox",
            "open world"
        ],
        "platforms": [
            "xbox series x|s",
            "pc (microsoft windows)",
            "playstation 5"
        ],
        "storyline": "",
        "keywords": [
            "crafting",
            "base building"
        ],
        "release_date": "2024"
    },
    "saving_princess": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "saving princess",
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
    "sc2": {
        "igdb_id": "239",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1tnn.jpg",
        "game_name": "starcraft 2",
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
            "mercenary",
            "popular"
        ],
        "release_date": "2010"
    },
    "seaofthieves": {
        "igdb_id": "11137",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2558.jpg",
        "game_name": "sea of thieves",
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
            "you can pet the dog"
        ],
        "release_date": "2018"
    },
    "shapez": {
        "igdb_id": "134826",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4tfx.jpg",
        "game_name": "shapez",
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
        "keywords": [
            "base building"
        ],
        "release_date": "2020"
    },
    "shivers": {
        "igdb_id": "12477",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7a5z.jpg",
        "game_name": "shivers",
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
    "shorthike": {
        "igdb_id": "116753",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co6e83.jpg",
        "game_name": "a short hike",
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
            "relaxing",
            "3d platformer",
            "family friendly",
            "great soundtrack"
        ],
        "release_date": "2019"
    },
    "sims4": {
        "igdb_id": "3212",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3h3l.jpg",
        "game_name": "the sims 4",
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
            "family friendly",
            "lgbtq+",
            "you can pet the dog"
        ],
        "release_date": "2014"
    },
    "sly1": {
        "igdb_id": "1798",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1p0r.jpg",
        "game_name": "sly cooper and the thievius raccoonus",
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
            "language selection",
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
    "sm": {
        "igdb_id": "1103",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5osy.jpg",
        "game_name": "super metroid",
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
    "sm64ex": {
        "igdb_id": "1074",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co721v.jpg",
        "game_name": "super mario 64",
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
            "digital distribution",
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
    "sm64hacks": {
        "igdb_id": "1074",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co721v.jpg",
        "game_name": "sm64 romhack",
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
            "digital distribution",
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
    "smo": {
        "igdb_id": "26758",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1mxf.jpg",
        "game_name": "super mario odyssey",
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
            "entering world in a painting"
        ],
        "release_date": "2017"
    },
    "sms": {
        "igdb_id": "1075",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co21rh.jpg",
        "game_name": "super mario sunshine",
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
            "yoshi",
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
            "foreshadowing",
            "collection marathon",
            "princess peach"
        ],
        "release_date": "2002"
    },
    "smw": {
        "igdb_id": "1070",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8lo8.jpg",
        "game_name": "super mario world",
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
            "yoshi",
            "mario",
            "digital distribution",
            "bonus stage",
            "damsel in distress",
            "retroachievements"
        ],
        "release_date": "1990"
    },
    "smz3": {
        "igdb_id": "210231",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5zep.jpg",
        "game_name": "smz3",
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
    "sm_map_rando": {
        "igdb_id": "1103",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5osy.jpg",
        "game_name": "super metroid map rando",
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
    "soe": {
        "igdb_id": "1359",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8kz6.jpg",
        "game_name": "file name of the soe us rom",
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
    "sonic_heroes": {
        "igdb_id": "4156",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9olx.jpg",
        "game_name": "sonic heroes is a 2003 platform game developed by sonic team usa. the player races a team of series characters through levels to amass rings,",
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
    "sotn": {
        "igdb_id": "1128",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co53m8.jpg",
        "game_name": "symphony of the night is a metroidvania developed by konami",
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
    "spire": {
        "igdb_id": "296831",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co82c5.jpg",
        "game_name": "slay the spire",
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
    "spyro3": {
        "igdb_id": "1578",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7t4m.jpg",
        "game_name": "spyro 3 is a game about a purple dragon who likes eggs.",
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
            "auto-saving",
            "real-time combat",
            "moving platforms",
            "gliding",
            "time trials"
        ],
        "release_date": "2000"
    },
    "ss": {
        "igdb_id": "534",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5wrj.jpg",
        "game_name": "skyward sword",
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
            "puzzle",
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
            "mine cart sequence",
            "androgyny",
            "ancient advanced civilization technology",
            "context sensitive",
            "living inventory",
            "behind the waterfall",
            "monomyth",
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "2011"
    },
    "stardew_valley": {
        "igdb_id": "17000",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/xrpmydnu9rpxvxfjkiu7.jpg",
        "game_name": "stardew valley",
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
            "monsters",
            "animals",
            "minigames",
            "2d",
            "fishing",
            "crafting",
            "chicken",
            "fairy",
            "achievements",
            "pixel art",
            "snow",
            "relaxing",
            "mining",
            "day/night cycle",
            "customizable characters",
            "deliberately retro",
            "controller support",
            "popular"
        ],
        "release_date": "2016"
    },
    "star_fox_64": {
        "igdb_id": "2591",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2e4k.jpg",
        "game_name": "star fox 64",
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
    "subnautica": {
        "igdb_id": "9254",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1iqw.jpg",
        "game_name": "subnautica",
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
            "android",
            "pc (microsoft windows)",
            "ios",
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
    "swr": {
        "igdb_id": "154",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3wj7.jpg",
        "game_name": "star wars episode i racer",
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
    "tboir": {
        "igdb_id": "310643",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co8kxf.jpg",
        "game_name": "the binding of isaac repentance",
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
    "terraria": {
        "igdb_id": "1879",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1rbo.jpg",
        "game_name": "terraria",
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
    "tetrisattack": {
        "igdb_id": "2739",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2w6k.jpg",
        "game_name": "tetris attack",
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
    "timespinner": {
        "igdb_id": "28952",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co24ag.jpg",
        "game_name": "timespinner",
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
    "tloz": {
        "igdb_id": "1022",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1uii.jpg",
        "game_name": "the legend of zelda",
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
    "tloz_ooa": {
        "igdb_id": "1041",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2tw1.jpg",
        "game_name": "the legend of zelda - oracle of ages",
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
    "tloz_oos": {
        "igdb_id": "1032",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2tw0.jpg",
        "game_name": "the legend of zelda - oracle of seasons",
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
            "damage over time",
            "zelda",
            "legend of zelda",
            "link"
        ],
        "release_date": "2001"
    },
    "toontown": {
        "igdb_id": "25326",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co28yv.jpg",
        "game_name": "toontown",
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
            "minigames",
            "go-kart"
        ],
        "release_date": "2003"
    },
    "tp": {
        "igdb_id": "134014",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3w1h.jpg",
        "game_name": "twilight princess",
        "igdb_name": "the legend of zelda: twilight princess",
        "rating": [
            "fantasy violence",
            "animated blood"
        ],
        "player_perspectives": [
            "third person"
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
            "wii"
        ],
        "storyline": "link, a young farm boy whose tasks consist of herding goats to watching children in ordon village, is asked by the mayor to run an errand in castle town. but things went strange that day: the land becomes dark and strange creatures appear from another world called the twilight realm which turns most people into ghosts. unlike the others, link transforms into a wolf but is captured. a mysterious figure named midna helps him break free, and with the aid of her magic, they set off to free the land from the shadows. link must explore the vast land of hyrule and uncover the mystery behind its plunge into darkness.",
        "keywords": [
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "2006"
    },
    "tracker": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "universal tracker",
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
    "trackmania": {
        "igdb_id": "133807",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2fe9.jpg",
        "game_name": "trackmania",
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
    "ttyd": {
        "igdb_id": "328663",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co9p1w.jpg",
        "game_name": "paper mario the thousand year door",
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
    "tunic": {
        "igdb_id": "23733",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/td1t8kb33gyo8mvhl2pc.jpg",
        "game_name": "tunic",
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
            "forest",
            "stylized",
            "achievements",
            "cute",
            "atmospheric",
            "family friendly",
            "great soundtrack",
            "digital distribution",
            "anthropomorphism",
            "secret area",
            "controller support",
            "soulslike"
        ],
        "release_date": "2022"
    },
    "tww": {
        "igdb_id": "1033",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3ohz.jpg",
        "game_name": "the wind waker",
        "igdb_name": "the legend of zelda: the wind waker",
        "rating": [
            "violence"
        ],
        "player_perspectives": [
            "third person"
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
            "living inventory",
            "link",
            "zelda",
            "legend of zelda"
        ],
        "release_date": "2002"
    },
    "tyrian": {
        "igdb_id": "14432",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2zg1.jpg",
        "game_name": "tyrian",
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
    "ufo50": {
        "igdb_id": "54555",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co24v0.jpg",
        "game_name": "ufo 50",
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
    "ultrakill": {
        "igdb_id": "124333",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co46s3.jpg",
        "game_name": "ultrakill",
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
    "undertale": {
        "igdb_id": "12517",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2855.jpg",
        "game_name": "undertale",
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
            "dark",
            "2d",
            "turn-based",
            "female protagonist",
            "backtracking",
            "multiple endings",
            "cute",
            "funny",
            "pixel art",
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
    "v6": {
        "igdb_id": "1990",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4ieg.jpg",
        "game_name": "vvvvvv",
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
            "teleportation",
            "2d platformer",
            "digital distribution",
            "world map",
            "deliberately retro",
            "save point",
            "checkpoints",
            "unstable platforms",
            "stereoscopic 3d",
            "instant kill",
            "moving platforms",
            "auto-scrolling levels",
            "time trials",
            "controller support",
            "conversation"
        ],
        "release_date": "2010"
    },
    "wargroove": {
        "igdb_id": "27441",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co4hgb.jpg",
        "game_name": "wargroove",
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
    "wargroove2": {
        "igdb_id": "241149",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co731u.jpg",
        "game_name": "wargroove 2",
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
    "witness": {
        "igdb_id": "5601",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co3hih.jpg",
        "game_name": "the witness",
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
            "pop culture reference",
            "game reference",
            "auto-saving",
            "stat tracking",
            "secret area"
        ],
        "release_date": "2016"
    },
    "wl": {
        "igdb_id": "1072",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co216h.jpg",
        "game_name": "wario land",
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
    "wl4": {
        "igdb_id": "1699",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1wpx.jpg",
        "game_name": "wario land 4",
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
    "wordipelago": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "wordipelago",
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
    "xenobladex": {
        "igdb_id": "2366",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1nwh.jpg",
        "game_name": "xenoblade x",
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
    "yachtdice": {
        "igdb_id": "",
        "cover_url": "",
        "game_name": "yacht dice is a straightforward game, custom-made for archipelago,",
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
    "yoshisisland": {
        "igdb_id": "1073",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kn9.jpg",
        "game_name": "yoshi's island",
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
            "yoshi",
            "digital distribution",
            "kidnapping"
        ],
        "release_date": "1995"
    },
    "yugioh06": {
        "igdb_id": "49377",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7yau.jpg",
        "game_name": "yu-gi-oh! 2006",
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
    "yugiohddm": {
        "igdb_id": "49211",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co5ztw.jpg",
        "game_name": "yu-gi-oh! dungeon dice monsters",
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
            "language selection",
            "shopping",
            "merchants"
        ],
        "release_date": "2001"
    },
    "zelda2": {
        "igdb_id": "1025",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co1uje.jpg",
        "game_name": "zelda ii: the adventure of link",
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
            "link",
            "zelda"
        ],
        "release_date": "1987"
    },
    "zillion": {
        "igdb_id": "18141",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co7xxj.jpg",
        "game_name": "zillion",
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
    "zork_grand_inquisitor": {
        "igdb_id": "1955",
        "cover_url": "https://images.igdb.com/igdb/image/upload/t_thumb/co2kql.jpg",
        "game_name": "zork grand inquisitor",
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
} # type: ignore

SEARCH_INDEX = {
    "adventure": [
        "hk",
        "ff1",
        "inscryption",
        "shorthike",
        "hades",
        "gstla",
        "cvcotm",
        "ffmq",
        "momodoramoonlitfarewell",
        "dkc3",
        "dontstarvetogether",
        "mzm",
        "animal_well",
        "ladx",
        "ror1",
        "seaofthieves",
        "kh1",
        "sadx",
        "kh2",
        "lingo",
        "rogue_legacy",
        "oot",
        "papermario",
        "sm64ex",
        "dsr",
        "sms",
        "raft",
        "enderlilies",
        "tunic",
        "noita",
        "pokemon_rb",
        "peaks_of_yore",
        "aus",
        "shivers",
        "messenger",
        "sm",
        "adventure",
        "xenobladex",
        "undertale",
        "sm_map_rando",
        "hylics2",
        "ror2",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sotn",
        "subnautica",
        "ahit",
        "tloz_ooa",
        "spyro3",
        "luigismansion",
        "alttp",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "sm64hacks",
        "celeste",
        "dark_souls_3",
        "banjo_tooie",
        "minecraft",
        "crosscode",
        "residentevil2remake",
        "smo",
        "tloz",
        "sly1",
        "earthbound",
        "kdl3",
        "blasphemous",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "rac2",
        "cat_quest",
        "mlss",
        "smw",
        "aquaria",
        "sonic_heroes",
        "mm_recomp",
        "zelda2",
        "mm2",
        "tloz_oos",
        "osrs",
        "smz3",
        "v6",
        "satisfactory",
        "oribf",
        "pseudoregalia",
        "k64",
        "residentevil3remake",
        "dark_souls_2",
        "sa2b",
        "wl4",
        "ss",
        "stardew_valley",
        "zork_grand_inquisitor",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "faxanadu",
        "albw",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "ufo50",
        "dk64",
        "tp",
        "tww",
        "jakanddaxter",
        "timespinner",
        "monster_sanctuary",
        "celeste64"
    ],
    "bird view / isometric": [
        "ffta",
        "yugioh06",
        "factorio",
        "ff1",
        "pokemon_rb",
        "inscryption",
        "tunic",
        "shorthike",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "wargroove",
        "ctjot",
        "wargroove2",
        "hades",
        "shapez",
        "tloz",
        "earthbound",
        "gstla",
        "balatro",
        "stardew_valley",
        "yugiohddm",
        "pmd_eos",
        "soe",
        "ffmq",
        "adventure",
        "diddy_kong_racing",
        "pokemon_frlg",
        "dw1",
        "dontstarvetogether",
        "undertale",
        "landstalker",
        "hylics2",
        "rimworld",
        "tyrian",
        "ladx",
        "against_the_storm",
        "albw",
        "pokemon_emerald",
        "sc2",
        "ufo50",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sonic_heroes",
        "tloz_ooa",
        "overcooked2",
        "placidplasticducksim",
        "spyro3",
        "sims4",
        "dungeon_clawler",
        "meritous",
        "sms",
        "civ_6",
        "alttp",
        "chainedechoes",
        "tboir",
        "tloz_oos",
        "osrs",
        "smz3",
        "openrct2"
    ],
    "bird": [
        "ffta",
        "banjo_tooie",
        "yugioh06",
        "factorio",
        "ff1",
        "pokemon_rb",
        "inscryption",
        "tunic",
        "shorthike",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "wargroove",
        "ctjot",
        "aus",
        "hades",
        "wargroove2",
        "shapez",
        "tloz",
        "earthbound",
        "gstla",
        "balatro",
        "stardew_valley",
        "yugiohddm",
        "pmd_eos",
        "soe",
        "ffmq",
        "adventure",
        "diddy_kong_racing",
        "pokemon_frlg",
        "dw1",
        "dkc3",
        "dontstarvetogether",
        "undertale",
        "landstalker",
        "hylics2",
        "rimworld",
        "tyrian",
        "ladx",
        "against_the_storm",
        "albw",
        "pokemon_emerald",
        "sc2",
        "ufo50",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sonic_heroes",
        "tloz_ooa",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "spyro3",
        "sims4",
        "dungeon_clawler",
        "meritous",
        "sms",
        "civ_6",
        "alttp",
        "chainedechoes",
        "tboir",
        "tloz_oos",
        "osrs",
        "smz3",
        "openrct2"
    ],
    "view": [
        "hk",
        "ff1",
        "inscryption",
        "shorthike",
        "mmbn3",
        "hades",
        "dkc2",
        "gstla",
        "cvcotm",
        "ffmq",
        "momodoramoonlitfarewell",
        "dkc3",
        "dontstarvetogether",
        "landstalker",
        "mzm",
        "animal_well",
        "rimworld",
        "ladx",
        "ror1",
        "placidplasticducksim",
        "rogue_legacy",
        "papermario",
        "sms",
        "enderlilies",
        "ffta",
        "yugioh06",
        "factorio",
        "noita",
        "pokemon_rb",
        "tunic",
        "wargroove",
        "ctjot",
        "aus",
        "balatro",
        "yugiohddm",
        "messenger",
        "sm",
        "adventure",
        "undertale",
        "sm_map_rando",
        "hylics2",
        "tyrian",
        "against_the_storm",
        "tetrisattack",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sotn",
        "tloz_ooa",
        "spyro3",
        "megamix",
        "dungeon_clawler",
        "meritous",
        "alttp",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "celeste",
        "crosscode",
        "wargroove2",
        "tloz",
        "earthbound",
        "kdl3",
        "pmd_eos",
        "blasphemous",
        "diddy_kong_racing",
        "dkc",
        "yoshisisland",
        "sc2",
        "mlss",
        "smw",
        "aquaria",
        "sonic_heroes",
        "overcooked2",
        "sims4",
        "zelda2",
        "mm2",
        "tboir",
        "tloz_oos",
        "osrs",
        "smz3",
        "v6",
        "oribf",
        "k64",
        "factorio_saws",
        "brotato",
        "marioland2",
        "musedash",
        "wl4",
        "shapez",
        "spire",
        "stardew_valley",
        "soe",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "faxanadu",
        "albw",
        "pokemon_emerald",
        "lufia2ac",
        "zillion",
        "ufo50",
        "civ_6",
        "timespinner",
        "monster_sanctuary",
        "wl",
        "openrct2"
    ],
    "/": [
        "ffta",
        "yugioh06",
        "factorio",
        "ff1",
        "pokemon_rb",
        "inscryption",
        "tunic",
        "shorthike",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "wargroove",
        "ctjot",
        "wargroove2",
        "hades",
        "shapez",
        "tloz",
        "earthbound",
        "gstla",
        "balatro",
        "stardew_valley",
        "yugiohddm",
        "pmd_eos",
        "soe",
        "ffmq",
        "adventure",
        "diddy_kong_racing",
        "pokemon_frlg",
        "dw1",
        "dontstarvetogether",
        "undertale",
        "landstalker",
        "hylics2",
        "rimworld",
        "tyrian",
        "ladx",
        "against_the_storm",
        "albw",
        "pokemon_emerald",
        "sc2",
        "ufo50",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sonic_heroes",
        "tloz_ooa",
        "overcooked2",
        "placidplasticducksim",
        "spyro3",
        "sims4",
        "dungeon_clawler",
        "meritous",
        "sms",
        "civ_6",
        "alttp",
        "chainedechoes",
        "tboir",
        "tloz_oos",
        "osrs",
        "smz3",
        "openrct2"
    ],
    "isometric": [
        "ffta",
        "yugioh06",
        "factorio",
        "ff1",
        "pokemon_rb",
        "inscryption",
        "tunic",
        "shorthike",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "wargroove",
        "ctjot",
        "wargroove2",
        "hades",
        "shapez",
        "tloz",
        "earthbound",
        "gstla",
        "balatro",
        "stardew_valley",
        "yugiohddm",
        "pmd_eos",
        "soe",
        "ffmq",
        "adventure",
        "diddy_kong_racing",
        "pokemon_frlg",
        "dw1",
        "dontstarvetogether",
        "undertale",
        "landstalker",
        "hylics2",
        "rimworld",
        "tyrian",
        "ladx",
        "against_the_storm",
        "albw",
        "pokemon_emerald",
        "sc2",
        "ufo50",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sonic_heroes",
        "tloz_ooa",
        "overcooked2",
        "placidplasticducksim",
        "spyro3",
        "sims4",
        "dungeon_clawler",
        "meritous",
        "sms",
        "civ_6",
        "alttp",
        "chainedechoes",
        "tboir",
        "tloz_oos",
        "osrs",
        "smz3",
        "openrct2"
    ],
    "fantasy": [
        "hk",
        "ff1",
        "shorthike",
        "hades",
        "dkc2",
        "gstla",
        "ffmq",
        "landstalker",
        "ladx",
        "ror1",
        "seaofthieves",
        "kh1",
        "kh2",
        "rogue_legacy",
        "oot",
        "papermario",
        "sm64ex",
        "dsr",
        "enderlilies",
        "ffta",
        "yugioh06",
        "tunic",
        "noita",
        "pokemon_rb",
        "wargroove",
        "ctjot",
        "yugiohddm",
        "adventure",
        "undertale",
        "hylics2",
        "against_the_storm",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "ahit",
        "dungeon_clawler",
        "alttp",
        "chainedechoes",
        "sm64hacks",
        "celeste",
        "dark_souls_3",
        "banjo_tooie",
        "minecraft",
        "wargroove2",
        "smo",
        "heretic",
        "tloz",
        "earthbound",
        "pmd_eos",
        "blasphemous",
        "yoshisisland",
        "cat_quest",
        "mlss",
        "smw",
        "aquaria",
        "mm_recomp",
        "sims4",
        "zelda2",
        "tloz_oos",
        "osrs",
        "ultrakill",
        "v6",
        "oribf",
        "pseudoregalia",
        "dark_souls_2",
        "spire",
        "ss",
        "stardew_valley",
        "zork_grand_inquisitor",
        "pokemon_frlg",
        "terraria",
        "fm",
        "huniepop",
        "faxanadu",
        "albw",
        "pokemon_emerald",
        "lufia2ac",
        "tp",
        "tww",
        "civ_6",
        "timespinner",
        "monster_sanctuary"
    ],
    "bbc microcomputer system": [
        "adventure"
    ],
    "bbc": [
        "adventure"
    ],
    "microcomputer": [
        "adventure"
    ],
    "system": [
        "ffta",
        "ff1",
        "tloz",
        "dkc2",
        "earthbound",
        "gstla",
        "kdl3",
        "soe",
        "ffmq",
        "sm",
        "adventure",
        "dkc3",
        "xenobladex",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "tetrisattack",
        "kh1",
        "yoshisisland",
        "pokemon_emerald",
        "lufia2ac",
        "pokemon_crystal",
        "ff4fe",
        "mlss",
        "smw",
        "papermario",
        "zelda2",
        "alttp",
        "smz3"
    ],
    "acorn electron": [
        "adventure"
    ],
    "acorn": [
        "adventure"
    ],
    "electron": [
        "adventure"
    ],
    "against_the_storm": [
        "against_the_storm"
    ],
    "against the storm": [
        "against_the_storm"
    ],
    "against": [
        "against_the_storm"
    ],
    "the": [
        "ffta",
        "banjo_tooie",
        "oribf",
        "k64",
        "dark_souls_2",
        "hades",
        "smo",
        "tloz",
        "dkc2",
        "sly1",
        "spire",
        "earthbound",
        "gstla",
        "ss",
        "cvcotm",
        "messenger",
        "blasphemous",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "terraria",
        "witness",
        "undertale",
        "doom_ii",
        "ttyd",
        "dkc",
        "smz3",
        "ladx",
        "against_the_storm",
        "seaofthieves",
        "albw",
        "lufia2ac",
        "sotn",
        "mlss",
        "tp",
        "tloz_ooa",
        "overcooked2",
        "rogue_legacy",
        "spyro3",
        "mm_recomp",
        "sims4",
        "oot",
        "papermario",
        "tww",
        "zelda2",
        "jakanddaxter",
        "alttp",
        "tboir",
        "tloz_oos",
        "celeste64",
        "enderlilies"
    ],
    "storm": [
        "against_the_storm"
    ],
    "real time strategy (rts)": [
        "sc2",
        "rimworld",
        "against_the_storm",
        "openrct2"
    ],
    "real": [
        "sc2",
        "rimworld",
        "against_the_storm",
        "openrct2"
    ],
    "time": [
        "ffta",
        "ctjot",
        "mk64",
        "wl4",
        "sly1",
        "earthbound",
        "pmd_eos",
        "sm",
        "diddy_kong_racing",
        "outer_wilds",
        "witness",
        "sm_map_rando",
        "apeescape",
        "rimworld",
        "ror1",
        "against_the_storm",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "sc2",
        "pokemon_crystal",
        "ahit",
        "tloz_ooa",
        "rogue_legacy",
        "spyro3",
        "mm_recomp",
        "oot",
        "sms",
        "jakanddaxter",
        "timespinner",
        "alttp",
        "tloz_oos",
        "v6",
        "openrct2"
    ],
    "strategy": [
        "ffta",
        "yugioh06",
        "factorio",
        "ff1",
        "pokemon_rb",
        "inscryption",
        "factorio_saws",
        "wargroove",
        "wargroove2",
        "shapez",
        "spire",
        "earthbound",
        "balatro",
        "stardew_valley",
        "yugiohddm",
        "pmd_eos",
        "pokemon_frlg",
        "dontstarvetogether",
        "terraria",
        "undertale",
        "fm",
        "huniepop",
        "hylics2",
        "rimworld",
        "against_the_storm",
        "pokemon_emerald",
        "sc2",
        "ufo50",
        "ff4fe",
        "huniepop2",
        "overcooked2",
        "papermario",
        "dungeon_clawler",
        "civ_6",
        "chainedechoes",
        "monster_sanctuary",
        "satisfactory",
        "openrct2"
    ],
    "(rts)": [
        "sc2",
        "rimworld",
        "against_the_storm",
        "openrct2"
    ],
    "simulator": [
        "factorio",
        "minecraft",
        "noita",
        "factorio_saws",
        "powerwashsimulator",
        "shapez",
        "stardew_valley",
        "outer_wilds",
        "dontstarvetogether",
        "terraria",
        "doronko_wanko",
        "huniepop",
        "rimworld",
        "against_the_storm",
        "seaofthieves",
        "huniepop2",
        "overcooked2",
        "placidplasticducksim",
        "sims4",
        "dungeon_clawler",
        "civ_6",
        "getting_over_it",
        "raft",
        "satisfactory",
        "openrct2"
    ],
    "indie": [
        "hk",
        "factorio",
        "noita",
        "pseudoregalia",
        "inscryption",
        "tunic",
        "shorthike",
        "factorio_saws",
        "brotato",
        "crosscode",
        "musedash",
        "peaks_of_yore",
        "powerwashsimulator",
        "aus",
        "hades",
        "wargroove",
        "shapez",
        "wargroove2",
        "spire",
        "shivers",
        "balatro",
        "stardew_valley",
        "messenger",
        "blasphemous",
        "momodoramoonlitfarewell",
        "hcniko",
        "dontstarvetogether",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "terraria",
        "undertale",
        "witness",
        "hylics2",
        "huniepop",
        "animal_well",
        "rimworld",
        "ror1",
        "against_the_storm",
        "ror2",
        "ufo50",
        "cuphead",
        "cat_quest",
        "osu",
        "subnautica",
        "aquaria",
        "ahit",
        "v6",
        "huniepop2",
        "overcooked2",
        "rogue_legacy",
        "dungeon_clawler",
        "lethal_company",
        "timespinner",
        "chainedechoes",
        "dlcquest",
        "tboir",
        "getting_over_it",
        "monster_sanctuary",
        "celeste64",
        "ultrakill",
        "celeste",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "xbox series x|s": [
        "tunic",
        "inscryption",
        "residentevil3remake",
        "brotato",
        "residentevil2remake",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "momodoramoonlitfarewell",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "animal_well",
        "trackmania",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "subnautica",
        "placidplasticducksim",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "xbox": [
        "hk",
        "oribf",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "dark_souls_2",
        "residentevil2remake",
        "sa2b",
        "wargroove",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "momodoramoonlitfarewell",
        "dw1",
        "outer_wilds",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "animal_well",
        "trackmania",
        "ror1",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "swr",
        "sadx",
        "cuphead",
        "sotn",
        "subnautica",
        "ahit",
        "sonic_heroes",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "sims4",
        "dsr",
        "timespinner",
        "chainedechoes",
        "dlcquest",
        "monster_sanctuary",
        "celeste",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "series": [
        "tunic",
        "inscryption",
        "residentevil3remake",
        "brotato",
        "residentevil2remake",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "momodoramoonlitfarewell",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "doom_ii",
        "animal_well",
        "trackmania",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "doom_1993",
        "subnautica",
        "placidplasticducksim",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "x|s": [
        "tunic",
        "inscryption",
        "residentevil3remake",
        "brotato",
        "residentevil2remake",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "momodoramoonlitfarewell",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "animal_well",
        "trackmania",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "subnautica",
        "placidplasticducksim",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "pc (microsoft windows)": [
        "hk",
        "inscryption",
        "shorthike",
        "hades",
        "momodoramoonlitfarewell",
        "dontstarvetogether",
        "landstalker",
        "doronko_wanko",
        "animal_well",
        "rimworld",
        "trackmania",
        "ror1",
        "seaofthieves",
        "toontown",
        "sadx",
        "lingo",
        "placidplasticducksim",
        "rogue_legacy",
        "dsr",
        "raft",
        "enderlilies",
        "factorio",
        "noita",
        "tunic",
        "peaks_of_yore",
        "wargroove",
        "powerwashsimulator",
        "aus",
        "gzdoom",
        "shivers",
        "balatro",
        "messenger",
        "undertale",
        "doom_ii",
        "hylics2",
        "tyrian",
        "against_the_storm",
        "ror2",
        "cuphead",
        "bumpstik",
        "osu",
        "subnautica",
        "ahit",
        "huniepop2",
        "dungeon_clawler",
        "meritous",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "celeste",
        "dark_souls_3",
        "minecraft",
        "crosscode",
        "residentevil2remake",
        "wargroove2",
        "heretic",
        "blasphemous",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "swr",
        "sc2",
        "cat_quest",
        "aquaria",
        "sonic_heroes",
        "overcooked2",
        "sims4",
        "lethal_company",
        "osrs",
        "ultrakill",
        "v6",
        "satisfactory",
        "oribf",
        "pseudoregalia",
        "factorio_saws",
        "brotato",
        "dark_souls_2",
        "sa2b",
        "residentevil3remake",
        "musedash",
        "shapez",
        "spire",
        "stardew_valley",
        "zork_grand_inquisitor",
        "terraria",
        "huniepop",
        "ufo50",
        "civ_6",
        "timespinner",
        "monster_sanctuary",
        "celeste64",
        "openrct2"
    ],
    "pc": [
        "hk",
        "inscryption",
        "shorthike",
        "hades",
        "momodoramoonlitfarewell",
        "dontstarvetogether",
        "landstalker",
        "doronko_wanko",
        "animal_well",
        "rimworld",
        "trackmania",
        "ror1",
        "seaofthieves",
        "toontown",
        "sadx",
        "lingo",
        "placidplasticducksim",
        "rogue_legacy",
        "dsr",
        "raft",
        "enderlilies",
        "factorio",
        "noita",
        "tunic",
        "peaks_of_yore",
        "wargroove",
        "powerwashsimulator",
        "aus",
        "gzdoom",
        "shivers",
        "balatro",
        "messenger",
        "undertale",
        "doom_ii",
        "hylics2",
        "tyrian",
        "against_the_storm",
        "ror2",
        "cuphead",
        "bumpstik",
        "osu",
        "subnautica",
        "ahit",
        "huniepop2",
        "dungeon_clawler",
        "meritous",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "celeste",
        "dark_souls_3",
        "minecraft",
        "crosscode",
        "residentevil2remake",
        "wargroove2",
        "heretic",
        "blasphemous",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "swr",
        "sc2",
        "cat_quest",
        "aquaria",
        "sonic_heroes",
        "overcooked2",
        "sims4",
        "lethal_company",
        "osrs",
        "ultrakill",
        "v6",
        "satisfactory",
        "oribf",
        "pseudoregalia",
        "factorio_saws",
        "brotato",
        "dark_souls_2",
        "sa2b",
        "residentevil3remake",
        "musedash",
        "shapez",
        "spire",
        "stardew_valley",
        "zork_grand_inquisitor",
        "terraria",
        "huniepop",
        "ufo50",
        "civ_6",
        "timespinner",
        "monster_sanctuary",
        "celeste64",
        "openrct2"
    ],
    "(microsoft": [
        "hk",
        "inscryption",
        "shorthike",
        "hades",
        "momodoramoonlitfarewell",
        "dontstarvetogether",
        "landstalker",
        "doronko_wanko",
        "animal_well",
        "rimworld",
        "trackmania",
        "ror1",
        "seaofthieves",
        "toontown",
        "sadx",
        "lingo",
        "placidplasticducksim",
        "rogue_legacy",
        "dsr",
        "raft",
        "enderlilies",
        "factorio",
        "noita",
        "tunic",
        "peaks_of_yore",
        "wargroove",
        "powerwashsimulator",
        "aus",
        "gzdoom",
        "shivers",
        "balatro",
        "messenger",
        "undertale",
        "doom_ii",
        "hylics2",
        "tyrian",
        "against_the_storm",
        "ror2",
        "cuphead",
        "bumpstik",
        "osu",
        "subnautica",
        "ahit",
        "huniepop2",
        "dungeon_clawler",
        "meritous",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "celeste",
        "dark_souls_3",
        "minecraft",
        "crosscode",
        "residentevil2remake",
        "wargroove2",
        "heretic",
        "blasphemous",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "swr",
        "sc2",
        "cat_quest",
        "aquaria",
        "sonic_heroes",
        "overcooked2",
        "sims4",
        "lethal_company",
        "osrs",
        "ultrakill",
        "v6",
        "satisfactory",
        "oribf",
        "pseudoregalia",
        "factorio_saws",
        "brotato",
        "dark_souls_2",
        "sa2b",
        "residentevil3remake",
        "musedash",
        "shapez",
        "spire",
        "stardew_valley",
        "zork_grand_inquisitor",
        "terraria",
        "huniepop",
        "ufo50",
        "civ_6",
        "timespinner",
        "monster_sanctuary",
        "celeste64",
        "openrct2"
    ],
    "windows)": [
        "hk",
        "inscryption",
        "shorthike",
        "hades",
        "momodoramoonlitfarewell",
        "dontstarvetogether",
        "landstalker",
        "doronko_wanko",
        "animal_well",
        "rimworld",
        "trackmania",
        "ror1",
        "seaofthieves",
        "toontown",
        "sadx",
        "lingo",
        "placidplasticducksim",
        "rogue_legacy",
        "dsr",
        "raft",
        "enderlilies",
        "factorio",
        "noita",
        "tunic",
        "peaks_of_yore",
        "wargroove",
        "powerwashsimulator",
        "aus",
        "gzdoom",
        "shivers",
        "balatro",
        "messenger",
        "undertale",
        "doom_ii",
        "hylics2",
        "tyrian",
        "against_the_storm",
        "ror2",
        "cuphead",
        "bumpstik",
        "osu",
        "subnautica",
        "ahit",
        "huniepop2",
        "dungeon_clawler",
        "meritous",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "celeste",
        "dark_souls_3",
        "minecraft",
        "crosscode",
        "residentevil2remake",
        "wargroove2",
        "heretic",
        "blasphemous",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "swr",
        "sc2",
        "cat_quest",
        "aquaria",
        "sonic_heroes",
        "overcooked2",
        "sims4",
        "lethal_company",
        "osrs",
        "ultrakill",
        "v6",
        "satisfactory",
        "oribf",
        "pseudoregalia",
        "factorio_saws",
        "brotato",
        "dark_souls_2",
        "sa2b",
        "residentevil3remake",
        "musedash",
        "shapez",
        "spire",
        "stardew_valley",
        "zork_grand_inquisitor",
        "terraria",
        "huniepop",
        "ufo50",
        "civ_6",
        "timespinner",
        "monster_sanctuary",
        "celeste64",
        "openrct2"
    ],
    "playstation 5": [
        "tunic",
        "inscryption",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "powerwashsimulator",
        "hades",
        "balatro",
        "messenger",
        "momodoramoonlitfarewell",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "animal_well",
        "trackmania",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "subnautica",
        "placidplasticducksim",
        "raft",
        "satisfactory"
    ],
    "playstation": [
        "hk",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "dark_souls_2",
        "residentevil2remake",
        "sa2b",
        "wargroove",
        "powerwashsimulator",
        "hades",
        "sly1",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "momodoramoonlitfarewell",
        "dw1",
        "outer_wilds",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "fm",
        "animal_well",
        "apeescape",
        "trackmania",
        "ror1",
        "against_the_storm",
        "ror2",
        "kh1",
        "seaofthieves",
        "swr",
        "rac2",
        "sadx",
        "cuphead",
        "kh2",
        "cat_quest",
        "sotn",
        "subnautica",
        "ahit",
        "sonic_heroes",
        "v6",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "spyro3",
        "sims4",
        "dsr",
        "jakanddaxter",
        "timespinner",
        "chainedechoes",
        "monster_sanctuary",
        "celeste",
        "raft",
        "satisfactory",
        "enderlilies"
    ],
    "5": [
        "tunic",
        "inscryption",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "powerwashsimulator",
        "hades",
        "balatro",
        "messenger",
        "momodoramoonlitfarewell",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "animal_well",
        "trackmania",
        "against_the_storm",
        "ror2",
        "seaofthieves",
        "subnautica",
        "placidplasticducksim",
        "raft",
        "satisfactory"
    ],
    "nintendo switch": [
        "hk",
        "oribf",
        "factorio",
        "tunic",
        "inscryption",
        "shorthike",
        "brotato",
        "crosscode",
        "musedash",
        "wargroove",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "smo",
        "balatro",
        "stardew_valley",
        "messenger",
        "blasphemous",
        "momodoramoonlitfarewell",
        "hcniko",
        "dontstarvetogether",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "terraria",
        "undertale",
        "animal_well",
        "ror1",
        "against_the_storm",
        "ror2",
        "swr",
        "cuphead",
        "cat_quest",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "megamix",
        "dsr",
        "timespinner",
        "chainedechoes",
        "tboir",
        "monster_sanctuary",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "nintendo": [
        "hk",
        "ff1",
        "inscryption",
        "shorthike",
        "hades",
        "dkc2",
        "ffmq",
        "momodoramoonlitfarewell",
        "dkc3",
        "dontstarvetogether",
        "animal_well",
        "ladx",
        "ror1",
        "placidplasticducksim",
        "rogue_legacy",
        "oot",
        "papermario",
        "sm64ex",
        "dsr",
        "sms",
        "mario_kart_double_dash",
        "enderlilies",
        "factorio",
        "pokemon_rb",
        "tunic",
        "wargroove",
        "ctjot",
        "mk64",
        "powerwashsimulator",
        "balatro",
        "messenger",
        "sm",
        "undertale",
        "star_fox_64",
        "sm_map_rando",
        "against_the_storm",
        "ror2",
        "tetrisattack",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "subnautica",
        "ahit",
        "tloz_ooa",
        "megamix",
        "luigismansion",
        "alttp",
        "chainedechoes",
        "sm64hacks",
        "celeste",
        "banjo_tooie",
        "crosscode",
        "wargroove2",
        "smo",
        "tloz",
        "earthbound",
        "kdl3",
        "pmd_eos",
        "blasphemous",
        "diddy_kong_racing",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "dkc",
        "swr",
        "yoshisisland",
        "cat_quest",
        "smw",
        "sonic_heroes",
        "overcooked2",
        "mm_recomp",
        "zelda2",
        "mm2",
        "tboir",
        "tloz_oos",
        "smz3",
        "v6",
        "oribf",
        "k64",
        "brotato",
        "marioland2",
        "musedash",
        "wl4",
        "stardew_valley",
        "soe",
        "dw1",
        "terraria",
        "faxanadu",
        "albw",
        "lufia2ac",
        "cv64",
        "metroidprime",
        "dk64",
        "tww",
        "timespinner",
        "monster_sanctuary",
        "wl"
    ],
    "switch": [
        "hk",
        "oribf",
        "factorio",
        "tunic",
        "inscryption",
        "shorthike",
        "brotato",
        "crosscode",
        "musedash",
        "wargroove",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "smo",
        "balatro",
        "stardew_valley",
        "messenger",
        "blasphemous",
        "momodoramoonlitfarewell",
        "hcniko",
        "dontstarvetogether",
        "outer_wilds",
        "bomb_rush_cyberfunk",
        "terraria",
        "undertale",
        "animal_well",
        "ror1",
        "against_the_storm",
        "ror2",
        "swr",
        "cuphead",
        "cat_quest",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "megamix",
        "dsr",
        "timespinner",
        "chainedechoes",
        "tboir",
        "monster_sanctuary",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "base building": [
        "rimworld",
        "against_the_storm",
        "shapez",
        "satisfactory"
    ],
    "base": [
        "rimworld",
        "against_the_storm",
        "shapez",
        "satisfactory"
    ],
    "building": [
        "rimworld",
        "against_the_storm",
        "shapez",
        "satisfactory"
    ],
    "roguelite": [
        "ror1",
        "against_the_storm",
        "ror2",
        "noita",
        "dungeon_clawler",
        "brotato",
        "hades"
    ],
    "ahit": [
        "ahit"
    ],
    "a hat in time": [
        "ahit"
    ],
    "a": [
        "albw",
        "sm64ex",
        "shorthike",
        "alttp",
        "smo",
        "sm64hacks",
        "smz3",
        "ahit",
        "dark_souls_3"
    ],
    "hat": [
        "ahit"
    ],
    "in": [
        "smo",
        "earthbound",
        "ss",
        "sm",
        "sm_map_rando",
        "kh1",
        "albw",
        "metroidprime",
        "smw",
        "ahit",
        "tloz_ooa",
        "oot",
        "papermario",
        "sm64ex",
        "sms",
        "zelda2",
        "alttp",
        "tloz_oos",
        "sm64hacks",
        "dark_souls_3"
    ],
    "first person": [
        "minecraft",
        "inscryption",
        "powerwashsimulator",
        "heretic",
        "earthbound",
        "shivers",
        "yugiohddm",
        "zork_grand_inquisitor",
        "outer_wilds",
        "witness",
        "star_fox_64",
        "fm",
        "doom_ii",
        "huniepop",
        "hylics2",
        "trackmania",
        "swr",
        "seaofthieves",
        "metroidprime",
        "cv64",
        "doom_1993",
        "lingo",
        "subnautica",
        "ahit",
        "huniepop2",
        "sims4",
        "lethal_company",
        "ultrakill",
        "raft",
        "satisfactory"
    ],
    "first": [
        "minecraft",
        "inscryption",
        "powerwashsimulator",
        "heretic",
        "earthbound",
        "shivers",
        "yugiohddm",
        "zork_grand_inquisitor",
        "outer_wilds",
        "witness",
        "star_fox_64",
        "fm",
        "doom_ii",
        "huniepop",
        "hylics2",
        "trackmania",
        "swr",
        "seaofthieves",
        "metroidprime",
        "cv64",
        "doom_1993",
        "lingo",
        "subnautica",
        "ahit",
        "huniepop2",
        "sims4",
        "lethal_company",
        "ultrakill",
        "raft",
        "satisfactory"
    ],
    "person": [
        "inscryption",
        "gstla",
        "trackmania",
        "seaofthieves",
        "kh1",
        "toontown",
        "sadx",
        "kh2",
        "lingo",
        "placidplasticducksim",
        "oot",
        "papermario",
        "sm64ex",
        "dsr",
        "sms",
        "mario_kart_double_dash",
        "raft",
        "powerwashsimulator",
        "mk64",
        "gzdoom",
        "shivers",
        "yugiohddm",
        "xenobladex",
        "star_fox_64",
        "doom_ii",
        "hylics2",
        "ror2",
        "subnautica",
        "ahit",
        "huniepop2",
        "spyro3",
        "megamix",
        "luigismansion",
        "getting_over_it",
        "sm64hacks",
        "dark_souls_3",
        "banjo_tooie",
        "minecraft",
        "residentevil2remake",
        "smo",
        "heretic",
        "sly1",
        "earthbound",
        "diddy_kong_racing",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "witness",
        "apeescape",
        "swr",
        "rac2",
        "doom_1993",
        "cat_quest",
        "sonic_heroes",
        "mm_recomp",
        "sims4",
        "lethal_company",
        "ultrakill",
        "satisfactory",
        "pseudoregalia",
        "residentevil3remake",
        "dark_souls_2",
        "sa2b",
        "ss",
        "soe",
        "zork_grand_inquisitor",
        "dw1",
        "fm",
        "huniepop",
        "albw",
        "metroidprime",
        "cv64",
        "dk64",
        "tp",
        "tww",
        "jakanddaxter",
        "celeste64"
    ],
    "third person": [
        "banjo_tooie",
        "minecraft",
        "pseudoregalia",
        "residentevil3remake",
        "dark_souls_2",
        "residentevil2remake",
        "sa2b",
        "mk64",
        "smo",
        "gzdoom",
        "sly1",
        "gstla",
        "ss",
        "soe",
        "diddy_kong_racing",
        "dw1",
        "hcniko",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "star_fox_64",
        "hylics2",
        "apeescape",
        "trackmania",
        "swr",
        "ror2",
        "kh1",
        "albw",
        "toontown",
        "rac2",
        "sadx",
        "cv64",
        "kh2",
        "cat_quest",
        "dk64",
        "ahit",
        "sonic_heroes",
        "tp",
        "placidplasticducksim",
        "spyro3",
        "mm_recomp",
        "sims4",
        "megamix",
        "oot",
        "papermario",
        "sm64ex",
        "tww",
        "dsr",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "mario_kart_double_dash",
        "getting_over_it",
        "sm64hacks",
        "celeste64",
        "raft",
        "dark_souls_3"
    ],
    "third": [
        "banjo_tooie",
        "minecraft",
        "pseudoregalia",
        "residentevil3remake",
        "dark_souls_2",
        "residentevil2remake",
        "sa2b",
        "mk64",
        "smo",
        "gzdoom",
        "sly1",
        "gstla",
        "ss",
        "soe",
        "diddy_kong_racing",
        "dw1",
        "hcniko",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "star_fox_64",
        "hylics2",
        "apeescape",
        "trackmania",
        "swr",
        "ror2",
        "kh1",
        "albw",
        "toontown",
        "rac2",
        "sadx",
        "cv64",
        "kh2",
        "cat_quest",
        "dk64",
        "ahit",
        "sonic_heroes",
        "tp",
        "placidplasticducksim",
        "spyro3",
        "mm_recomp",
        "sims4",
        "megamix",
        "oot",
        "papermario",
        "sm64ex",
        "tww",
        "dsr",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "mario_kart_double_dash",
        "getting_over_it",
        "sm64hacks",
        "celeste64",
        "raft",
        "dark_souls_3"
    ],
    "platform": [
        "banjo_tooie",
        "hk",
        "oribf",
        "pseudoregalia",
        "k64",
        "marioland2",
        "sa2b",
        "peaks_of_yore",
        "aus",
        "smo",
        "gzdoom",
        "wl4",
        "dkc2",
        "sly1",
        "kdl3",
        "cvcotm",
        "messenger",
        "blasphemous",
        "sm",
        "momodoramoonlitfarewell",
        "hcniko",
        "dkc3",
        "terraria",
        "bomb_rush_cyberfunk",
        "mzm",
        "sm_map_rando",
        "hylics2",
        "animal_well",
        "apeescape",
        "dkc",
        "smz3",
        "faxanadu",
        "ror1",
        "yoshisisland",
        "rac2",
        "sadx",
        "metroidprime",
        "cv64",
        "ufo50",
        "zillion",
        "cuphead",
        "sotn",
        "smw",
        "dk64",
        "ahit",
        "aquaria",
        "sonic_heroes",
        "rogue_legacy",
        "spyro3",
        "wl",
        "sm64hacks",
        "sm64ex",
        "sms",
        "zelda2",
        "jakanddaxter",
        "timespinner",
        "dlcquest",
        "mm2",
        "getting_over_it",
        "monster_sanctuary",
        "celeste64",
        "ultrakill",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "action": [
        "hk",
        "ff1",
        "mmbn3",
        "hades",
        "dkc2",
        "gstla",
        "cvcotm",
        "ffmq",
        "momodoramoonlitfarewell",
        "dkc3",
        "dontstarvetogether",
        "landstalker",
        "mzm",
        "doronko_wanko",
        "animal_well",
        "trackmania",
        "ladx",
        "ror1",
        "seaofthieves",
        "kh1",
        "sadx",
        "kh2",
        "rogue_legacy",
        "oot",
        "papermario",
        "sm64ex",
        "dsr",
        "sms",
        "mario_kart_double_dash",
        "enderlilies",
        "tunic",
        "noita",
        "pokemon_rb",
        "peaks_of_yore",
        "ctjot",
        "aus",
        "mk64",
        "gzdoom",
        "messenger",
        "sm",
        "xenobladex",
        "star_fox_64",
        "sm_map_rando",
        "doom_ii",
        "tyrian",
        "ror2",
        "tetrisattack",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sotn",
        "osu",
        "ahit",
        "tloz_ooa",
        "spyro3",
        "dungeon_clawler",
        "luigismansion",
        "alttp",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "sm64hacks",
        "celeste",
        "dark_souls_3",
        "banjo_tooie",
        "crosscode",
        "residentevil2remake",
        "smo",
        "tloz",
        "sly1",
        "earthbound",
        "kdl3",
        "blasphemous",
        "diddy_kong_racing",
        "outer_wilds",
        "hcniko",
        "bomb_rush_cyberfunk",
        "apeescape",
        "dkc",
        "swr",
        "yoshisisland",
        "rac2",
        "sc2",
        "doom_1993",
        "cat_quest",
        "mlss",
        "smw",
        "sonic_heroes",
        "overcooked2",
        "mm_recomp",
        "sims4",
        "zelda2",
        "lethal_company",
        "mm2",
        "tloz_oos",
        "smz3",
        "ultrakill",
        "v6",
        "oribf",
        "pseudoregalia",
        "k64",
        "residentevil3remake",
        "brotato",
        "dark_souls_2",
        "marioland2",
        "sa2b",
        "musedash",
        "wl4",
        "ss",
        "soe",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "faxanadu",
        "albw",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "ufo50",
        "dk64",
        "tp",
        "tww",
        "jakanddaxter",
        "timespinner",
        "monster_sanctuary",
        "celeste64",
        "wl"
    ],
    "playstation 4": [
        "hk",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "wargroove",
        "powerwashsimulator",
        "hades",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "outer_wilds",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "trackmania",
        "ror1",
        "swr",
        "ror2",
        "cuphead",
        "kh2",
        "cat_quest",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "sims4",
        "dsr",
        "jakanddaxter",
        "timespinner",
        "chainedechoes",
        "monster_sanctuary",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "4": [
        "hk",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "wargroove",
        "powerwashsimulator",
        "hades",
        "wl4",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "outer_wilds",
        "dw1",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "trackmania",
        "ror1",
        "swr",
        "ror2",
        "cuphead",
        "kh2",
        "cat_quest",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "sims4",
        "dsr",
        "jakanddaxter",
        "timespinner",
        "chainedechoes",
        "monster_sanctuary",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "mac": [
        "hk",
        "factorio",
        "minecraft",
        "tunic",
        "inscryption",
        "shorthike",
        "factorio_saws",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "residentevil3remake",
        "musedash",
        "hades",
        "heretic",
        "shapez",
        "balatro",
        "stardew_valley",
        "blasphemous",
        "zork_grand_inquisitor",
        "dontstarvetogether",
        "terraria",
        "witness",
        "undertale",
        "landstalker",
        "doom_ii",
        "huniepop",
        "hylics2",
        "rimworld",
        "tyrian",
        "ror1",
        "swr",
        "toontown",
        "sc2",
        "cuphead",
        "cat_quest",
        "osu",
        "subnautica",
        "aquaria",
        "ahit",
        "huniepop2",
        "overcooked2",
        "rogue_legacy",
        "osrs",
        "sims4",
        "dungeon_clawler",
        "civ_6",
        "timespinner",
        "chainedechoes",
        "dlcquest",
        "getting_over_it",
        "monster_sanctuary",
        "celeste",
        "v6",
        "openrct2"
    ],
    "xbox one": [
        "hk",
        "oribf",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "wargroove",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "outer_wilds",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "trackmania",
        "ror1",
        "seaofthieves",
        "ror2",
        "swr",
        "cuphead",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "sims4",
        "dsr",
        "timespinner",
        "chainedechoes",
        "monster_sanctuary",
        "celeste",
        "enderlilies"
    ],
    "one": [
        "hk",
        "oribf",
        "tunic",
        "inscryption",
        "shorthike",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "wargroove",
        "powerwashsimulator",
        "wargroove2",
        "hades",
        "balatro",
        "stardew_valley",
        "dark_souls_3",
        "messenger",
        "blasphemous",
        "outer_wilds",
        "terraria",
        "bomb_rush_cyberfunk",
        "undertale",
        "witness",
        "trackmania",
        "ror1",
        "seaofthieves",
        "ror2",
        "swr",
        "cuphead",
        "subnautica",
        "ahit",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "sims4",
        "dsr",
        "timespinner",
        "chainedechoes",
        "monster_sanctuary",
        "celeste",
        "enderlilies"
    ],
    "time travel": [
        "pmd_eos",
        "mm_recomp",
        "oot",
        "outer_wilds",
        "timespinner",
        "ctjot",
        "tloz_ooa",
        "tloz_oos",
        "apeescape",
        "ahit",
        "earthbound"
    ],
    "travel": [
        "pmd_eos",
        "mm_recomp",
        "oot",
        "albw",
        "outer_wilds",
        "tloz_oos",
        "timespinner",
        "alttp",
        "ctjot",
        "tloz_ooa",
        "doom_ii",
        "apeescape",
        "ahit",
        "earthbound"
    ],
    "spaceship": [
        "metroidprime",
        "civ_6",
        "mzm",
        "star_fox_64",
        "ahit",
        "v6"
    ],
    "female protagonist": [
        "rogue_legacy",
        "shorthike",
        "metroidprime",
        "cv64",
        "sm",
        "hcniko",
        "dkc3",
        "timespinner",
        "mzm",
        "undertale",
        "earthbound",
        "sm_map_rando",
        "dkc2",
        "celeste64",
        "ahit",
        "celeste",
        "enderlilies"
    ],
    "female": [
        "rogue_legacy",
        "shorthike",
        "metroidprime",
        "cv64",
        "sm",
        "hcniko",
        "dkc3",
        "timespinner",
        "mzm",
        "undertale",
        "earthbound",
        "sm_map_rando",
        "dkc2",
        "celeste64",
        "ahit",
        "celeste",
        "enderlilies"
    ],
    "protagonist": [
        "hk",
        "k64",
        "shorthike",
        "dkc2",
        "earthbound",
        "gstla",
        "ss",
        "blasphemous",
        "sm",
        "hcniko",
        "dkc3",
        "undertale",
        "mzm",
        "sm_map_rando",
        "apeescape",
        "dkc",
        "ladx",
        "kh1",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "doom_1993",
        "mlss",
        "ahit",
        "sonic_heroes",
        "tloz_ooa",
        "rogue_legacy",
        "oot",
        "papermario",
        "zelda2",
        "jakanddaxter",
        "timespinner",
        "alttp",
        "tloz_oos",
        "celeste64",
        "ultrakill",
        "celeste",
        "enderlilies"
    ],
    "action-adventure": [
        "banjo_tooie",
        "hk",
        "minecraft",
        "crosscode",
        "dark_souls_2",
        "aus",
        "ss",
        "cvcotm",
        "sm",
        "dontstarvetogether",
        "terraria",
        "xenobladex",
        "landstalker",
        "sm_map_rando",
        "ladx",
        "seaofthieves",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "zillion",
        "sotn",
        "aquaria",
        "ahit",
        "tloz_ooa",
        "rogue_legacy",
        "mm_recomp",
        "tww",
        "oot",
        "sms",
        "zelda2",
        "luigismansion",
        "alttp",
        "timespinner",
        "tloz_oos",
        "dark_souls_3"
    ],
    "cute": [
        "sims4",
        "tunic",
        "shorthike",
        "hcniko",
        "musedash",
        "undertale",
        "animal_well",
        "ahit",
        "celeste"
    ],
    "snow": [
        "ffta",
        "minecraft",
        "albw",
        "metroidprime",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "terraria",
        "jakanddaxter",
        "mk64",
        "ahit",
        "celeste",
        "gstla",
        "dkc",
        "stardew_valley"
    ],
    "wall jump": [
        "cvcotm",
        "oribf",
        "sm",
        "sms",
        "mzm",
        "smo",
        "sm_map_rando",
        "ahit"
    ],
    "wall": [
        "ffta",
        "banjo_tooie",
        "oribf",
        "mk64",
        "smo",
        "dkc2",
        "cvcotm",
        "sm",
        "undertale",
        "mzm",
        "sm_map_rando",
        "doom_ii",
        "dkc",
        "ladx",
        "kh1",
        "mlss",
        "dk64",
        "ahit",
        "rogue_legacy",
        "oot",
        "papermario",
        "sms",
        "jakanddaxter"
    ],
    "jump": [
        "cvcotm",
        "oribf",
        "sm",
        "sms",
        "mzm",
        "smo",
        "sm_map_rando",
        "ahit"
    ],
    "3d platformer": [
        "sm64ex",
        "shorthike",
        "hcniko",
        "sms",
        "bomb_rush_cyberfunk",
        "sonic_heroes",
        "smo",
        "sm64hacks",
        "ahit"
    ],
    "3d": [
        "minecraft",
        "tunic",
        "k64",
        "shorthike",
        "dark_souls_2",
        "powerwashsimulator",
        "mk64",
        "smo",
        "sly1",
        "ss",
        "dw1",
        "hcniko",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "witness",
        "star_fox_64",
        "hylics2",
        "apeescape",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "lingo",
        "sotn",
        "dk64",
        "ahit",
        "sonic_heroes",
        "spyro3",
        "oot",
        "sm64ex",
        "dsr",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "sm64hacks",
        "v6",
        "dark_souls_3"
    ],
    "platformer": [
        "hk",
        "blasphemous",
        "sm64ex",
        "shorthike",
        "hcniko",
        "sms",
        "bomb_rush_cyberfunk",
        "sonic_heroes",
        "smo",
        "hylics2",
        "sm64hacks",
        "ahit",
        "v6"
    ],
    "swimming": [
        "banjo_tooie",
        "minecraft",
        "smo",
        "wl4",
        "dkc2",
        "hcniko",
        "dkc3",
        "terraria",
        "dkc",
        "kh1",
        "albw",
        "subnautica",
        "aquaria",
        "ahit",
        "tloz_ooa",
        "spyro3",
        "oot",
        "sm64ex",
        "sms",
        "jakanddaxter",
        "alttp",
        "sm64hacks"
    ],
    "steam greenlight": [
        "timespinner",
        "ror1",
        "ahit",
        "dlcquest"
    ],
    "steam": [
        "timespinner",
        "ror1",
        "ahit",
        "dlcquest"
    ],
    "greenlight": [
        "timespinner",
        "ror1",
        "ahit",
        "dlcquest"
    ],
    "crowdfunding": [
        "hk",
        "ror1",
        "crosscode",
        "timespinner",
        "ahit"
    ],
    "crowd funded": [
        "hk",
        "ror1",
        "crosscode",
        "timespinner",
        "ahit"
    ],
    "crowd": [
        "hk",
        "ror1",
        "crosscode",
        "timespinner",
        "ahit"
    ],
    "funded": [
        "hk",
        "ror1",
        "crosscode",
        "timespinner",
        "ahit"
    ],
    "collection marathon": [
        "banjo_tooie",
        "k64",
        "sms",
        "dk64",
        "ahit"
    ],
    "collection": [
        "banjo_tooie",
        "k64",
        "sms",
        "dk64",
        "ahit"
    ],
    "marathon": [
        "banjo_tooie",
        "k64",
        "sms",
        "dk64",
        "ahit"
    ],
    "albw": [
        "albw"
    ],
    "the legend of zelda: a link between worlds": [
        "albw"
    ],
    "legend": [
        "ladx",
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "tloz",
        "tloz_oos",
        "tp",
        "tloz_ooa",
        "ss"
    ],
    "of": [
        "ffta",
        "oribf",
        "peaks_of_yore",
        "tloz",
        "dkc2",
        "sly1",
        "earthbound",
        "ss",
        "cvcotm",
        "pmd_eos",
        "soe",
        "dkc3",
        "star_fox_64",
        "dkc",
        "ladx",
        "ror1",
        "seaofthieves",
        "ror2",
        "albw",
        "pokemon_emerald",
        "lufia2ac",
        "cv64",
        "sc2",
        "pokemon_crystal",
        "sotn",
        "dk64",
        "tp",
        "tloz_ooa",
        "rogue_legacy",
        "spyro3",
        "mm_recomp",
        "tww",
        "oot",
        "sms",
        "zelda2",
        "jakanddaxter",
        "luigismansion",
        "alttp",
        "tboir",
        "tloz_oos",
        "celeste64",
        "enderlilies"
    ],
    "zelda:": [
        "ladx",
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tp",
        "tloz_ooa",
        "ss"
    ],
    "link": [
        "ladx",
        "tww",
        "oot",
        "albw",
        "zelda2",
        "alttp",
        "tloz_oos",
        "smz3",
        "tp",
        "ss"
    ],
    "between": [
        "albw"
    ],
    "worlds": [
        "albw"
    ],
    "puzzle": [
        "oribf",
        "tunic",
        "inscryption",
        "crosscode",
        "wl4",
        "shapez",
        "shivers",
        "ss",
        "yugiohddm",
        "zork_grand_inquisitor",
        "outer_wilds",
        "hcniko",
        "witness",
        "undertale",
        "doom_ii",
        "huniepop",
        "animal_well",
        "ttyd",
        "ladx",
        "tetrisattack",
        "albw",
        "lufia2ac",
        "cv64",
        "metroidprime",
        "ufo50",
        "zillion",
        "lingo",
        "bumpstik",
        "tp",
        "tloz_ooa",
        "huniepop2",
        "placidplasticducksim",
        "rogue_legacy",
        "mm_recomp",
        "candybox2",
        "oot",
        "spyro3",
        "tww",
        "alttp",
        "tloz_oos",
        "v6"
    ],
    "historical": [
        "candybox2",
        "soe",
        "albw",
        "civ_6",
        "heretic",
        "fm",
        "ss"
    ],
    "sandbox": [
        "factorio",
        "minecraft",
        "noita",
        "factorio_saws",
        "powerwashsimulator",
        "smo",
        "shapez",
        "stardew_valley",
        "dontstarvetogether",
        "terraria",
        "xenobladex",
        "landstalker",
        "faxanadu",
        "albw",
        "placidplasticducksim",
        "sims4",
        "oot",
        "sms",
        "zelda2",
        "osrs",
        "satisfactory"
    ],
    "open world": [
        "minecraft",
        "pokemon_rb",
        "shorthike",
        "smo",
        "tloz",
        "gstla",
        "ss",
        "outer_wilds",
        "dontstarvetogether",
        "terraria",
        "witness",
        "xenobladex",
        "mzm",
        "seaofthieves",
        "albw",
        "toontown",
        "metroidprime",
        "lingo",
        "sotn",
        "subnautica",
        "mm_recomp",
        "oot",
        "sm64ex",
        "jakanddaxter",
        "osrs",
        "sm64hacks",
        "smz3",
        "satisfactory"
    ],
    "open": [
        "minecraft",
        "pokemon_rb",
        "shorthike",
        "smo",
        "tloz",
        "gstla",
        "ss",
        "outer_wilds",
        "dontstarvetogether",
        "terraria",
        "witness",
        "xenobladex",
        "mzm",
        "seaofthieves",
        "albw",
        "toontown",
        "metroidprime",
        "lingo",
        "sotn",
        "subnautica",
        "mm_recomp",
        "oot",
        "sm64ex",
        "jakanddaxter",
        "osrs",
        "sm64hacks",
        "smz3",
        "satisfactory"
    ],
    "world": [
        "yugioh06",
        "minecraft",
        "pokemon_rb",
        "shorthike",
        "dark_souls_2",
        "smo",
        "tloz",
        "dkc2",
        "earthbound",
        "gstla",
        "ss",
        "outer_wilds",
        "dw1",
        "dkc3",
        "dontstarvetogether",
        "terraria",
        "witness",
        "mzm",
        "xenobladex",
        "doom_ii",
        "dkc",
        "ladx",
        "seaofthieves",
        "albw",
        "toontown",
        "yoshisisland",
        "metroidprime",
        "pokemon_crystal",
        "lingo",
        "sotn",
        "smw",
        "subnautica",
        "aquaria",
        "mm_recomp",
        "oot",
        "sm64ex",
        "zelda2",
        "jakanddaxter",
        "alttp",
        "tloz_oos",
        "osrs",
        "sm64hacks",
        "smz3",
        "v6",
        "satisfactory",
        "dark_souls_3"
    ],
    "nintendo 3ds": [
        "ladx",
        "wl",
        "ff1",
        "pokemon_rb",
        "albw",
        "marioland2",
        "terraria",
        "zelda2",
        "pokemon_crystal",
        "mm2",
        "tloz",
        "tloz_oos",
        "wl4",
        "tloz_ooa",
        "v6"
    ],
    "3ds": [
        "ff1",
        "pokemon_rb",
        "marioland2",
        "wl4",
        "tloz",
        "dkc2",
        "earthbound",
        "sm",
        "dkc3",
        "terraria",
        "sm_map_rando",
        "dkc",
        "ladx",
        "albw",
        "pokemon_crystal",
        "smw",
        "tloz_ooa",
        "wl",
        "zelda2",
        "alttp",
        "mm2",
        "tloz_oos",
        "v6"
    ],
    "medieval": [
        "rogue_legacy",
        "candybox2",
        "soe",
        "albw",
        "dark_souls_2",
        "heretic",
        "ss",
        "dark_souls_3"
    ],
    "magic": [
        "ffta",
        "noita",
        "dark_souls_2",
        "ctjot",
        "heretic",
        "gstla",
        "cvcotm",
        "zork_grand_inquisitor",
        "terraria",
        "ladx",
        "faxanadu",
        "albw",
        "cv64",
        "cuphead",
        "sotn",
        "aquaria",
        "rogue_legacy",
        "candybox2",
        "dsr",
        "zelda2",
        "alttp",
        "tloz_oos"
    ],
    "minigames": [
        "rogue_legacy",
        "spyro3",
        "kh1",
        "albw",
        "k64",
        "oot",
        "pokemon_emerald",
        "toontown",
        "apeescape",
        "hcniko",
        "dkc3",
        "pokemon_crystal",
        "tloz_ooa",
        "wl4",
        "dk64",
        "gstla",
        "stardew_valley"
    ],
    "2.5d": [
        "albw",
        "k64",
        "doom_1993",
        "dkc3",
        "heretic",
        "doom_ii",
        "dkc"
    ],
    "archery": [
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "ss"
    ],
    "fairy": [
        "huniepop2",
        "ladx",
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "k64",
        "terraria",
        "zelda2",
        "alttp",
        "landstalker",
        "tloz",
        "tloz_oos",
        "dk64",
        "tloz_ooa",
        "stardew_valley"
    ],
    "princess": [
        "ladx",
        "kh1",
        "albw",
        "oot",
        "papermario",
        "sm64ex",
        "sms",
        "tloz_oos",
        "alttp",
        "mk64",
        "mario_kart_double_dash",
        "mlss",
        "smw",
        "sm64hacks",
        "tp",
        "tloz_ooa",
        "ss"
    ],
    "sequel": [
        "ffta",
        "banjo_tooie",
        "dark_souls_2",
        "mk64",
        "smo",
        "wl4",
        "dkc2",
        "gstla",
        "dw1",
        "dontstarvetogether",
        "hylics2",
        "doom_ii",
        "albw",
        "mm_recomp",
        "oot",
        "sms",
        "zelda2",
        "civ_6",
        "alttp",
        "mm2",
        "dark_souls_3"
    ],
    "sword & sorcery": [
        "ladx",
        "spyro3",
        "mm_recomp",
        "tww",
        "ffmq",
        "albw",
        "kh1",
        "oot",
        "dark_souls_2",
        "terraria",
        "heretic",
        "tloz_oos",
        "tloz_ooa",
        "ss",
        "dark_souls_3"
    ],
    "sword": [
        "ladx",
        "spyro3",
        "mm_recomp",
        "tww",
        "ffmq",
        "albw",
        "kh1",
        "oot",
        "dark_souls_2",
        "terraria",
        "heretic",
        "tloz_oos",
        "tloz_ooa",
        "ss",
        "dark_souls_3"
    ],
    "&": [
        "yugioh06",
        "inscryption",
        "dark_souls_2",
        "heretic",
        "spire",
        "ss",
        "balatro",
        "yugiohddm",
        "ffmq",
        "terraria",
        "fm",
        "ladx",
        "kh1",
        "albw",
        "rac2",
        "mlss",
        "tloz_ooa",
        "spyro3",
        "mm_recomp",
        "tww",
        "oot",
        "tloz_oos",
        "dark_souls_3"
    ],
    "sorcery": [
        "ladx",
        "spyro3",
        "mm_recomp",
        "tww",
        "ffmq",
        "albw",
        "kh1",
        "oot",
        "dark_souls_2",
        "terraria",
        "heretic",
        "tloz_oos",
        "tloz_ooa",
        "ss",
        "dark_souls_3"
    ],
    "darkness": [
        "ladx",
        "rogue_legacy",
        "minecraft",
        "albw",
        "sm",
        "dkc3",
        "terraria",
        "witness",
        "luigismansion",
        "alttp",
        "zelda2",
        "sm_map_rando",
        "doom_ii",
        "dkc2",
        "aquaria",
        "earthbound",
        "dkc"
    ],
    "digital distribution": [
        "banjo_tooie",
        "oribf",
        "factorio",
        "minecraft",
        "tunic",
        "crosscode",
        "musedash",
        "wl4",
        "heretic",
        "dkc2",
        "dontstarvetogether",
        "terraria",
        "witness",
        "doom_ii",
        "apeescape",
        "dkc",
        "ladx",
        "seaofthieves",
        "albw",
        "yoshisisland",
        "ufo50",
        "cuphead",
        "sotn",
        "mlss",
        "smw",
        "dk64",
        "huniepop2",
        "rogue_legacy",
        "oot",
        "sm64ex",
        "civ_6",
        "timespinner",
        "dlcquest",
        "tloz_oos",
        "getting_over_it",
        "sm64hacks",
        "celeste",
        "v6"
    ],
    "digital": [
        "banjo_tooie",
        "oribf",
        "factorio",
        "minecraft",
        "tunic",
        "crosscode",
        "musedash",
        "wl4",
        "heretic",
        "dkc2",
        "dontstarvetogether",
        "terraria",
        "witness",
        "doom_ii",
        "apeescape",
        "dkc",
        "ladx",
        "seaofthieves",
        "albw",
        "yoshisisland",
        "ufo50",
        "cuphead",
        "sotn",
        "mlss",
        "smw",
        "dk64",
        "huniepop2",
        "rogue_legacy",
        "oot",
        "sm64ex",
        "civ_6",
        "timespinner",
        "dlcquest",
        "tloz_oos",
        "getting_over_it",
        "sm64hacks",
        "celeste",
        "v6"
    ],
    "distribution": [
        "banjo_tooie",
        "oribf",
        "factorio",
        "minecraft",
        "tunic",
        "crosscode",
        "musedash",
        "wl4",
        "heretic",
        "dkc2",
        "dontstarvetogether",
        "terraria",
        "witness",
        "doom_ii",
        "apeescape",
        "dkc",
        "ladx",
        "seaofthieves",
        "albw",
        "yoshisisland",
        "ufo50",
        "cuphead",
        "sotn",
        "mlss",
        "smw",
        "dk64",
        "huniepop2",
        "rogue_legacy",
        "oot",
        "sm64ex",
        "civ_6",
        "timespinner",
        "dlcquest",
        "tloz_oos",
        "getting_over_it",
        "sm64hacks",
        "celeste",
        "v6"
    ],
    "anthropomorphism": [
        "banjo_tooie",
        "tunic",
        "k64",
        "mk64",
        "dkc2",
        "sly1",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "undertale",
        "star_fox_64",
        "apeescape",
        "dkc",
        "kh1",
        "albw",
        "cv64",
        "cuphead",
        "mlss",
        "dk64",
        "sonic_heroes",
        "tloz_ooa",
        "spyro3",
        "papermario",
        "sms",
        "jakanddaxter",
        "tloz_oos"
    ],
    "polygonal 3d": [
        "minecraft",
        "k64",
        "mk64",
        "sly1",
        "ss",
        "dw1",
        "xenobladex",
        "witness",
        "star_fox_64",
        "apeescape",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "spyro3",
        "oot",
        "sms",
        "jakanddaxter",
        "luigismansion"
    ],
    "polygonal": [
        "minecraft",
        "k64",
        "mk64",
        "sly1",
        "ss",
        "dw1",
        "xenobladex",
        "witness",
        "star_fox_64",
        "apeescape",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "spyro3",
        "oot",
        "sms",
        "jakanddaxter",
        "luigismansion"
    ],
    "bow and arrow": [
        "ffta",
        "ladx",
        "rogue_legacy",
        "ror1",
        "minecraft",
        "oot",
        "albw",
        "dark_souls_2",
        "terraria",
        "cuphead",
        "alttp",
        "tloz_oos",
        "ss"
    ],
    "bow": [
        "ffta",
        "ladx",
        "rogue_legacy",
        "ror1",
        "minecraft",
        "oot",
        "albw",
        "dark_souls_2",
        "terraria",
        "cuphead",
        "alttp",
        "tloz_oos",
        "ss"
    ],
    "and": [
        "ffta",
        "oribf",
        "minecraft",
        "dark_souls_2",
        "hades",
        "sly1",
        "ss",
        "blasphemous",
        "terraria",
        "ladx",
        "ror1",
        "albw",
        "cv64",
        "cuphead",
        "rogue_legacy",
        "oot",
        "civ_6",
        "jakanddaxter",
        "alttp",
        "tloz_oos",
        "smz3",
        "openrct2"
    ],
    "arrow": [
        "ffta",
        "ladx",
        "rogue_legacy",
        "ror1",
        "minecraft",
        "oot",
        "albw",
        "dark_souls_2",
        "terraria",
        "cuphead",
        "alttp",
        "tloz_oos",
        "ss"
    ],
    "damsel in distress": [
        "kh1",
        "albw",
        "oot",
        "papermario",
        "sm",
        "metroidprime",
        "sms",
        "tloz_oos",
        "zelda2",
        "alttp",
        "tloz_ooa",
        "sm_map_rando",
        "smw",
        "earthbound",
        "ss"
    ],
    "damsel": [
        "kh1",
        "albw",
        "oot",
        "papermario",
        "sm",
        "metroidprime",
        "sms",
        "tloz_oos",
        "zelda2",
        "alttp",
        "tloz_ooa",
        "sm_map_rando",
        "smw",
        "earthbound",
        "ss"
    ],
    "distress": [
        "kh1",
        "albw",
        "oot",
        "papermario",
        "sm",
        "metroidprime",
        "sms",
        "tloz_oos",
        "zelda2",
        "alttp",
        "tloz_ooa",
        "sm_map_rando",
        "smw",
        "earthbound",
        "ss"
    ],
    "upgradeable weapons": [
        "albw",
        "metroidprime",
        "cv64",
        "dark_souls_2",
        "mzm",
        "mm2",
        "dk64"
    ],
    "upgradeable": [
        "albw",
        "metroidprime",
        "cv64",
        "dark_souls_2",
        "mzm",
        "mm2",
        "dk64"
    ],
    "weapons": [
        "albw",
        "metroidprime",
        "cv64",
        "dark_souls_2",
        "mzm",
        "mm2",
        "dk64"
    ],
    "disorientation zone": [
        "ladx",
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa"
    ],
    "disorientation": [
        "ladx",
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa"
    ],
    "zone": [
        "ladx",
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa"
    ],
    "descendants of other characters": [
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "albw",
        "cv64",
        "sly1",
        "dkc3",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "star_fox_64",
        "sotn",
        "tloz_ooa",
        "dkc2",
        "dk64",
        "earthbound",
        "dkc"
    ],
    "descendants": [
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "albw",
        "cv64",
        "sly1",
        "dkc3",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "star_fox_64",
        "sotn",
        "tloz_ooa",
        "dkc2",
        "dk64",
        "earthbound",
        "dkc"
    ],
    "other": [
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "albw",
        "cv64",
        "sly1",
        "dkc3",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "star_fox_64",
        "sotn",
        "tloz_ooa",
        "dkc2",
        "dk64",
        "earthbound",
        "dkc"
    ],
    "characters": [
        "dark_souls_2",
        "dkc2",
        "sly1",
        "earthbound",
        "stardew_valley",
        "dkc3",
        "terraria",
        "xenobladex",
        "star_fox_64",
        "dkc",
        "albw",
        "cv64",
        "sotn",
        "dk64",
        "tloz_ooa",
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "sms",
        "jakanddaxter",
        "luigismansion",
        "dark_souls_3"
    ],
    "save point": [
        "dkc2",
        "earthbound",
        "gstla",
        "cvcotm",
        "sm",
        "dkc3",
        "mzm",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "sotn",
        "mlss",
        "aquaria",
        "papermario",
        "jakanddaxter",
        "luigismansion",
        "v6"
    ],
    "save": [
        "dkc2",
        "earthbound",
        "gstla",
        "cvcotm",
        "sm",
        "dkc3",
        "mzm",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "sotn",
        "mlss",
        "aquaria",
        "papermario",
        "jakanddaxter",
        "luigismansion",
        "v6"
    ],
    "point": [
        "dkc2",
        "earthbound",
        "gstla",
        "cvcotm",
        "sm",
        "dkc3",
        "mzm",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "sotn",
        "mlss",
        "aquaria",
        "papermario",
        "jakanddaxter",
        "luigismansion",
        "v6"
    ],
    "stereoscopic 3d": [
        "minecraft",
        "albw",
        "luigismansion",
        "sly1",
        "v6"
    ],
    "stereoscopic": [
        "minecraft",
        "albw",
        "luigismansion",
        "sly1",
        "v6"
    ],
    "side quests": [
        "ladx",
        "oot",
        "albw",
        "pokemon_emerald",
        "sc2",
        "dark_souls_2",
        "xenobladex",
        "pokemon_crystal",
        "alttp",
        "tloz_oos",
        "tloz_ooa"
    ],
    "side": [
        "hk",
        "oribf",
        "ff1",
        "noita",
        "pokemon_rb",
        "k64",
        "marioland2",
        "dark_souls_2",
        "musedash",
        "wargroove",
        "wargroove2",
        "aus",
        "wl4",
        "dkc2",
        "spire",
        "kdl3",
        "cvcotm",
        "ffmq",
        "blasphemous",
        "messenger",
        "sm",
        "pokemon_frlg",
        "momodoramoonlitfarewell",
        "dkc3",
        "terraria",
        "xenobladex",
        "mzm",
        "sm_map_rando",
        "hylics2",
        "animal_well",
        "dkc",
        "ladx",
        "faxanadu",
        "ror1",
        "tetrisattack",
        "albw",
        "yoshisisland",
        "pokemon_emerald",
        "lufia2ac",
        "sc2",
        "ufo50",
        "zillion",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sotn",
        "mlss",
        "smw",
        "aquaria",
        "tloz_ooa",
        "rogue_legacy",
        "wl",
        "megamix",
        "oot",
        "dungeon_clawler",
        "papermario",
        "zelda2",
        "timespinner",
        "alttp",
        "dlcquest",
        "mm2",
        "tloz_oos",
        "getting_over_it",
        "monster_sanctuary",
        "smz3",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "quests": [
        "ladx",
        "oot",
        "albw",
        "pokemon_emerald",
        "metroidprime",
        "sc2",
        "dark_souls_2",
        "xenobladex",
        "zelda2",
        "pokemon_crystal",
        "alttp",
        "tloz_oos",
        "tloz_ooa"
    ],
    "potion": [
        "ladx",
        "rogue_legacy",
        "minecraft",
        "kh1",
        "albw",
        "pokemon_emerald",
        "zelda2",
        "pokemon_crystal",
        "alttp",
        "tloz_oos",
        "gstla",
        "ss"
    ],
    "real-time combat": [
        "minecraft",
        "dark_souls_2",
        "ss",
        "sm",
        "xenobladex",
        "landstalker",
        "sm_map_rando",
        "doom_ii",
        "dkc",
        "ladx",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "doom_1993",
        "sotn",
        "dk64",
        "tloz_ooa",
        "spyro3",
        "oot",
        "sm64ex",
        "sms",
        "zelda2",
        "alttp",
        "tloz_oos",
        "sm64hacks"
    ],
    "real-time": [
        "minecraft",
        "dark_souls_2",
        "ss",
        "sm",
        "xenobladex",
        "landstalker",
        "sm_map_rando",
        "doom_ii",
        "dkc",
        "ladx",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "doom_1993",
        "sotn",
        "dk64",
        "tloz_ooa",
        "spyro3",
        "oot",
        "sm64ex",
        "sms",
        "zelda2",
        "alttp",
        "tloz_oos",
        "sm64hacks"
    ],
    "combat": [
        "minecraft",
        "dark_souls_2",
        "ss",
        "sm",
        "xenobladex",
        "landstalker",
        "sm_map_rando",
        "doom_ii",
        "dkc",
        "ladx",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "doom_1993",
        "sotn",
        "dk64",
        "tloz_ooa",
        "spyro3",
        "oot",
        "sm64ex",
        "sms",
        "zelda2",
        "alttp",
        "tloz_oos",
        "sm64hacks"
    ],
    "self-referential humor": [
        "papermario",
        "albw",
        "mlss",
        "dkc2",
        "earthbound"
    ],
    "self-referential": [
        "papermario",
        "albw",
        "mlss",
        "dkc2",
        "earthbound"
    ],
    "humor": [
        "papermario",
        "albw",
        "mlss",
        "dkc2",
        "earthbound"
    ],
    "multiple gameplay perspectives": [
        "minecraft",
        "albw",
        "metroidprime",
        "tloz_oos",
        "tloz_ooa"
    ],
    "multiple": [
        "minecraft",
        "k64",
        "wl4",
        "dkc2",
        "earthbound",
        "dkc3",
        "witness",
        "undertale",
        "mzm",
        "star_fox_64",
        "doom_ii",
        "apeescape",
        "dkc",
        "kh1",
        "albw",
        "metroidprime",
        "cv64",
        "cuphead",
        "sotn",
        "mlss",
        "dk64",
        "sonic_heroes",
        "tloz_ooa",
        "rogue_legacy",
        "spyro3",
        "civ_6",
        "tloz_oos"
    ],
    "gameplay": [
        "banjo_tooie",
        "minecraft",
        "kh1",
        "albw",
        "oot",
        "sm64ex",
        "sm64hacks",
        "metroidprime",
        "sms",
        "terraria",
        "smo",
        "mm2",
        "subnautica",
        "tloz_oos",
        "dkc2",
        "aquaria",
        "tloz_ooa",
        "dkc"
    ],
    "perspectives": [
        "minecraft",
        "albw",
        "metroidprime",
        "tloz_oos",
        "tloz_ooa"
    ],
    "rpg elements": [
        "banjo_tooie",
        "oribf",
        "minecraft",
        "albw",
        "dark_souls_2",
        "zelda2",
        "mzm",
        "sotn",
        "mlss"
    ],
    "rpg": [
        "banjo_tooie",
        "oribf",
        "minecraft",
        "albw",
        "dark_souls_2",
        "zelda2",
        "mzm",
        "sotn",
        "mlss"
    ],
    "elements": [
        "banjo_tooie",
        "oribf",
        "minecraft",
        "albw",
        "dark_souls_2",
        "zelda2",
        "mzm",
        "sotn",
        "mlss"
    ],
    "mercenary": [
        "oot",
        "albw",
        "sm",
        "metroidprime",
        "sc2",
        "dark_souls_2",
        "alttp",
        "sm_map_rando",
        "ss"
    ],
    "coming of age": [
        "ffta",
        "oribf",
        "oot",
        "albw",
        "pokemon_emerald",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp"
    ],
    "coming": [
        "ffta",
        "oribf",
        "oot",
        "albw",
        "pokemon_emerald",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp"
    ],
    "age": [
        "ffta",
        "oribf",
        "oot",
        "albw",
        "pokemon_emerald",
        "factorio_saws",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "dimension travel": [
        "alttp",
        "mm_recomp",
        "albw",
        "doom_ii"
    ],
    "dimension": [
        "alttp",
        "mm_recomp",
        "albw",
        "doom_ii"
    ],
    "androgyny": [
        "ffta",
        "oot",
        "albw",
        "sotn",
        "gstla",
        "ss"
    ],
    "fast traveling": [
        "hk",
        "oot",
        "albw",
        "pokemon_emerald",
        "undertale",
        "alttp"
    ],
    "fast": [
        "hk",
        "oot",
        "albw",
        "pokemon_emerald",
        "undertale",
        "alttp"
    ],
    "traveling": [
        "hk",
        "oot",
        "albw",
        "pokemon_emerald",
        "undertale",
        "alttp"
    ],
    "context sensitive": [
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa",
        "ss"
    ],
    "context": [
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa",
        "ss"
    ],
    "sensitive": [
        "oot",
        "albw",
        "alttp",
        "tloz_oos",
        "tloz_ooa",
        "ss"
    ],
    "living inventory": [
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "ss"
    ],
    "living": [
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "ss"
    ],
    "inventory": [
        "mm_recomp",
        "tww",
        "oot",
        "albw",
        "alttp",
        "ss"
    ],
    "bees": [
        "minecraft",
        "albw",
        "dontstarvetogether",
        "terraria",
        "alttp",
        "raft"
    ],
    "zelda": [
        "ladx",
        "tww",
        "oot",
        "albw",
        "zelda2",
        "alttp",
        "tloz",
        "tloz_oos",
        "tp",
        "ss"
    ],
    "legend of zelda": [
        "ladx",
        "tww",
        "oot",
        "albw",
        "tloz_oos",
        "tp",
        "ss"
    ],
    "alttp": [
        "alttp"
    ],
    "the legend of zelda: a link to the past": [
        "alttp"
    ],
    "to": [
        "alttp",
        "smz3"
    ],
    "past": [
        "alttp",
        "smz3"
    ],
    "satellaview": [
        "alttp",
        "yoshisisland"
    ],
    "super nintendo entertainment system": [
        "soe",
        "ffmq",
        "tetrisattack",
        "yoshisisland",
        "sm",
        "lufia2ac",
        "dkc3",
        "alttp",
        "ff4fe",
        "sm_map_rando",
        "smw",
        "dkc2",
        "smz3",
        "earthbound",
        "dkc",
        "kdl3"
    ],
    "super": [
        "marioland2",
        "smo",
        "dkc2",
        "earthbound",
        "kdl3",
        "soe",
        "ffmq",
        "sm",
        "dkc3",
        "sm_map_rando",
        "dkc",
        "tetrisattack",
        "yoshisisland",
        "lufia2ac",
        "ff4fe",
        "smw",
        "sm64ex",
        "sms",
        "alttp",
        "sm64hacks",
        "smz3",
        "wl"
    ],
    "entertainment": [
        "ff1",
        "tloz",
        "dkc2",
        "earthbound",
        "kdl3",
        "soe",
        "ffmq",
        "sm",
        "dkc3",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "tetrisattack",
        "yoshisisland",
        "lufia2ac",
        "ff4fe",
        "smw",
        "zelda2",
        "alttp",
        "smz3"
    ],
    "wii": [
        "ffta",
        "hk",
        "ff1",
        "k64",
        "mmbn3",
        "mk64",
        "wl4",
        "tloz",
        "dkc2",
        "earthbound",
        "gstla",
        "kdl3",
        "ss",
        "stardew_valley",
        "cvcotm",
        "pmd_eos",
        "ffmq",
        "sm",
        "dkc3",
        "terraria",
        "xenobladex",
        "landstalker",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "dkc",
        "faxanadu",
        "ff4fe",
        "mlss",
        "smw",
        "dk64",
        "tp",
        "mm_recomp",
        "oot",
        "papermario",
        "sm64ex",
        "zelda2",
        "alttp",
        "sm64hacks"
    ],
    "wii u": [
        "ffta",
        "hk",
        "ff1",
        "k64",
        "mmbn3",
        "mk64",
        "wl4",
        "tloz",
        "dkc2",
        "earthbound",
        "gstla",
        "kdl3",
        "ss",
        "stardew_valley",
        "cvcotm",
        "pmd_eos",
        "ffmq",
        "sm",
        "dkc3",
        "terraria",
        "xenobladex",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "dkc",
        "mlss",
        "smw",
        "dk64",
        "mm_recomp",
        "oot",
        "papermario",
        "sm64ex",
        "zelda2",
        "alttp",
        "sm64hacks"
    ],
    "u": [
        "ffta",
        "hk",
        "ff1",
        "k64",
        "mmbn3",
        "mk64",
        "wl4",
        "tloz",
        "dkc2",
        "earthbound",
        "gstla",
        "kdl3",
        "ss",
        "stardew_valley",
        "cvcotm",
        "pmd_eos",
        "ffmq",
        "sm",
        "dkc3",
        "terraria",
        "xenobladex",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "dkc",
        "mlss",
        "smw",
        "dk64",
        "mm_recomp",
        "oot",
        "papermario",
        "sm64ex",
        "zelda2",
        "alttp",
        "sm64hacks"
    ],
    "new nintendo 3ds": [
        "sm",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "smw",
        "dkc2",
        "earthbound",
        "dkc"
    ],
    "new": [
        "sm",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "smw",
        "dkc2",
        "earthbound",
        "dkc"
    ],
    "super famicom": [
        "ffmq",
        "yoshisisland",
        "sm",
        "lufia2ac",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "smw",
        "dkc2",
        "earthbound",
        "dkc",
        "kdl3"
    ],
    "famicom": [
        "ffmq",
        "yoshisisland",
        "sm",
        "lufia2ac",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "smw",
        "dkc2",
        "earthbound",
        "dkc",
        "kdl3"
    ],
    "ghosts": [
        "rogue_legacy",
        "ffmq",
        "papermario",
        "metroidprime",
        "cv64",
        "sms",
        "cuphead",
        "luigismansion",
        "alttp",
        "aus",
        "sotn",
        "mlss",
        "tloz_ooa",
        "wl4",
        "dkc2",
        "sly1",
        "earthbound",
        "v6"
    ],
    "mascot": [
        "ladx",
        "spyro3",
        "papermario",
        "k64",
        "jakanddaxter",
        "alttp",
        "mm2",
        "tloz_oos",
        "sly1",
        "kdl3"
    ],
    "death": [
        "ffta",
        "minecraft",
        "dark_souls_2",
        "mk64",
        "heretic",
        "sly1",
        "gstla",
        "cvcotm",
        "terraria",
        "mzm",
        "star_fox_64",
        "doom_ii",
        "dkc",
        "ladx",
        "kh1",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "tloz_ooa",
        "rogue_legacy",
        "oot",
        "papermario",
        "sms",
        "zelda2",
        "luigismansion",
        "alttp",
        "mm2",
        "tloz_oos",
        "openrct2",
        "v6",
        "dark_souls_3"
    ],
    "maze": [
        "ladx",
        "papermario",
        "cv64",
        "doom_1993",
        "witness",
        "alttp",
        "mzm",
        "openrct2"
    ],
    "backtracking": [
        "ffta",
        "banjo_tooie",
        "faxanadu",
        "cvcotm",
        "ladx",
        "kh1",
        "oot",
        "metroidprime",
        "cv64",
        "jakanddaxter",
        "undertale",
        "alttp",
        "mzm",
        "sotn",
        "witness",
        "tloz_oos"
    ],
    "undead": [
        "ladx",
        "ffmq",
        "oot",
        "papermario",
        "cv64",
        "dsr",
        "dark_souls_2",
        "terraria",
        "alttp",
        "sotn",
        "mlss",
        "heretic",
        "tloz_oos",
        "tloz_ooa"
    ],
    "campaign": [
        "ladx",
        "oot",
        "zelda2",
        "alttp",
        "tloz_oos",
        "tloz_ooa",
        "ss"
    ],
    "pixel art": [
        "crosscode",
        "wargroove",
        "wl4",
        "stardew_valley",
        "blasphemous",
        "sm",
        "hcniko",
        "terraria",
        "undertale",
        "mzm",
        "sm_map_rando",
        "animal_well",
        "tyrian",
        "ladx",
        "ror1",
        "sotn",
        "rogue_legacy",
        "zelda2",
        "timespinner",
        "alttp",
        "mm2",
        "tloz_oos",
        "celeste",
        "v6"
    ],
    "pixel": [
        "crosscode",
        "wargroove",
        "wl4",
        "stardew_valley",
        "blasphemous",
        "sm",
        "hcniko",
        "terraria",
        "undertale",
        "mzm",
        "sm_map_rando",
        "animal_well",
        "tyrian",
        "ladx",
        "ror1",
        "sotn",
        "rogue_legacy",
        "zelda2",
        "timespinner",
        "alttp",
        "mm2",
        "tloz_oos",
        "celeste",
        "v6"
    ],
    "art": [
        "crosscode",
        "wargroove",
        "wl4",
        "stardew_valley",
        "blasphemous",
        "sm",
        "hcniko",
        "terraria",
        "undertale",
        "mzm",
        "sm_map_rando",
        "animal_well",
        "tyrian",
        "ladx",
        "ror1",
        "sotn",
        "rogue_legacy",
        "zelda2",
        "timespinner",
        "alttp",
        "mm2",
        "tloz_oos",
        "celeste",
        "v6"
    ],
    "easter egg": [
        "ladx",
        "banjo_tooie",
        "rogue_legacy",
        "papermario",
        "alttp",
        "doom_ii",
        "apeescape",
        "openrct2"
    ],
    "easter": [
        "ladx",
        "banjo_tooie",
        "rogue_legacy",
        "papermario",
        "alttp",
        "doom_ii",
        "apeescape",
        "openrct2"
    ],
    "egg": [
        "ladx",
        "banjo_tooie",
        "rogue_legacy",
        "papermario",
        "alttp",
        "doom_ii",
        "apeescape",
        "openrct2"
    ],
    "teleportation": [
        "rogue_legacy",
        "pokemon_emerald",
        "cv64",
        "terraria",
        "tloz_oos",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "doom_ii",
        "earthbound",
        "v6"
    ],
    "giant insects": [
        "hk",
        "soe",
        "pokemon_emerald",
        "dkc3",
        "sms",
        "alttp",
        "mlss",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "giant": [
        "hk",
        "soe",
        "pokemon_emerald",
        "dkc3",
        "sms",
        "alttp",
        "mlss",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "insects": [
        "hk",
        "soe",
        "pokemon_emerald",
        "dkc3",
        "sms",
        "alttp",
        "mlss",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "silent protagonist": [
        "hk",
        "k64",
        "dkc2",
        "gstla",
        "ss",
        "blasphemous",
        "dkc",
        "ladx",
        "pokemon_emerald",
        "doom_1993",
        "mlss",
        "tloz_ooa",
        "oot",
        "papermario",
        "zelda2",
        "jakanddaxter",
        "alttp",
        "tloz_oos",
        "ultrakill"
    ],
    "silent": [
        "hk",
        "k64",
        "dkc2",
        "gstla",
        "ss",
        "blasphemous",
        "dkc",
        "ladx",
        "pokemon_emerald",
        "doom_1993",
        "mlss",
        "tloz_ooa",
        "oot",
        "papermario",
        "zelda2",
        "jakanddaxter",
        "alttp",
        "tloz_oos",
        "ultrakill"
    ],
    "explosion": [
        "ffta",
        "minecraft",
        "mk64",
        "dkc2",
        "ffmq",
        "sm",
        "dkc3",
        "terraria",
        "mzm",
        "sm_map_rando",
        "doom_ii",
        "metroidprime",
        "cv64",
        "cuphead",
        "sotn",
        "sonic_heroes",
        "tloz_ooa",
        "rogue_legacy",
        "sms",
        "zelda2",
        "alttp",
        "mm2",
        "openrct2"
    ],
    "block puzzle": [
        "alttp",
        "tloz_ooa",
        "oot",
        "tloz_oos"
    ],
    "block": [
        "alttp",
        "tloz_ooa",
        "oot",
        "tloz_oos"
    ],
    "monkey": [
        "ladx",
        "diddy_kong_racing",
        "apeescape",
        "dkc3",
        "alttp",
        "mk64",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "nintendo power": [
        "sm",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "dkc2",
        "earthbound",
        "dkc"
    ],
    "power": [
        "sm",
        "dkc3",
        "alttp",
        "sm_map_rando",
        "dkc2",
        "earthbound",
        "dkc"
    ],
    "world map": [
        "ladx",
        "oot",
        "metroidprime",
        "dkc3",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "tloz_oos",
        "dkc2",
        "aquaria",
        "v6",
        "dkc"
    ],
    "map": [
        "ladx",
        "oot",
        "metroidprime",
        "dkc3",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "tloz_oos",
        "dkc2",
        "aquaria",
        "v6",
        "dkc"
    ],
    "human": [
        "ladx",
        "papermario",
        "cv64",
        "sc2",
        "dark_souls_2",
        "sms",
        "terraria",
        "zelda2",
        "alttp",
        "sotn",
        "doom_ii",
        "apeescape",
        "gstla",
        "ss",
        "dark_souls_3"
    ],
    "shopping": [
        "yugiohddm",
        "pokemon_emerald",
        "cv64",
        "dw1",
        "cuphead",
        "pokemon_crystal",
        "alttp",
        "sotn",
        "mlss",
        "tloz_oos",
        "tloz_ooa"
    ],
    "ice stage": [
        "banjo_tooie",
        "oot",
        "metroidprime",
        "cv64",
        "dkc3",
        "terraria",
        "jakanddaxter",
        "alttp",
        "mk64",
        "wl4",
        "dkc2",
        "dkc"
    ],
    "ice": [
        "banjo_tooie",
        "oot",
        "metroidprime",
        "cv64",
        "dkc3",
        "terraria",
        "jakanddaxter",
        "alttp",
        "mk64",
        "wl4",
        "dkc2",
        "dkc"
    ],
    "stage": [
        "banjo_tooie",
        "spyro3",
        "oot",
        "metroidprime",
        "cv64",
        "dkc3",
        "terraria",
        "jakanddaxter",
        "alttp",
        "mk64",
        "wl4",
        "smw",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "saving the world": [
        "alttp",
        "earthbound",
        "dark_souls_2",
        "zelda2"
    ],
    "saving": [
        "alttp",
        "earthbound",
        "dark_souls_2",
        "zelda2"
    ],
    "secret area": [
        "rogue_legacy",
        "tunic",
        "sm",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_oos",
        "witness",
        "zelda2",
        "alttp",
        "star_fox_64",
        "sotn",
        "sm_map_rando",
        "heretic",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "secret": [
        "rogue_legacy",
        "soe",
        "tunic",
        "sm",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_oos",
        "witness",
        "zelda2",
        "alttp",
        "star_fox_64",
        "sotn",
        "sm_map_rando",
        "heretic",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "area": [
        "rogue_legacy",
        "tunic",
        "sm",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_oos",
        "witness",
        "zelda2",
        "alttp",
        "star_fox_64",
        "sotn",
        "sm_map_rando",
        "heretic",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "shielded enemies": [
        "rogue_legacy",
        "hk",
        "dkc3",
        "alttp",
        "tloz_ooa"
    ],
    "shielded": [
        "rogue_legacy",
        "hk",
        "dkc3",
        "alttp",
        "tloz_ooa"
    ],
    "enemies": [
        "rogue_legacy",
        "hk",
        "dkc3",
        "alttp",
        "tloz_ooa"
    ],
    "walking through walls": [
        "ladx",
        "oot",
        "tloz_oos",
        "alttp",
        "doom_ii",
        "tloz_ooa"
    ],
    "walking": [
        "ladx",
        "oot",
        "tloz_oos",
        "alttp",
        "doom_ii",
        "tloz_ooa"
    ],
    "through": [
        "ladx",
        "oot",
        "tloz_oos",
        "alttp",
        "doom_ii",
        "tloz_ooa"
    ],
    "walls": [
        "ladx",
        "oot",
        "tloz_oos",
        "alttp",
        "doom_ii",
        "tloz_ooa"
    ],
    "liberation": [
        "dkc2",
        "alttp",
        "sm",
        "sm_map_rando"
    ],
    "conveyor belt": [
        "alttp",
        "tloz_ooa",
        "mm2",
        "cuphead"
    ],
    "conveyor": [
        "alttp",
        "tloz_ooa",
        "mm2",
        "cuphead"
    ],
    "belt": [
        "alttp",
        "tloz_ooa",
        "mm2",
        "cuphead"
    ],
    "villain": [
        "banjo_tooie",
        "cvcotm",
        "kh1",
        "oot",
        "papermario",
        "zelda2",
        "alttp",
        "star_fox_64",
        "sotn",
        "mm2",
        "tloz_ooa",
        "tloz_oos",
        "gstla",
        "dkc"
    ],
    "recurring boss": [
        "banjo_tooie",
        "kh1",
        "papermario",
        "pokemon_emerald",
        "dkc3",
        "alttp",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "recurring": [
        "banjo_tooie",
        "kh1",
        "papermario",
        "pokemon_emerald",
        "dkc3",
        "alttp",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "boss": [
        "banjo_tooie",
        "rogue_legacy",
        "mm_recomp",
        "kh1",
        "oot",
        "papermario",
        "pokemon_emerald",
        "metroidprime",
        "dark_souls_2",
        "dkc3",
        "cuphead",
        "sms",
        "alttp",
        "doom_ii",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "been here before": [
        "ffta",
        "oot",
        "sms",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "been": [
        "ffta",
        "oot",
        "sms",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "here": [
        "ffta",
        "oot",
        "hcniko",
        "sms",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "before": [
        "ffta",
        "oot",
        "sms",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "sleeping": [
        "minecraft",
        "papermario",
        "sms",
        "pokemon_crystal",
        "alttp",
        "gstla"
    ],
    "merchants": [
        "yugiohddm",
        "faxanadu",
        "hk",
        "candybox2",
        "terraria",
        "timespinner",
        "alttp"
    ],
    "fetch quests": [
        "ladx",
        "metroidprime",
        "zelda2",
        "alttp",
        "tloz_oos"
    ],
    "fetch": [
        "ladx",
        "metroidprime",
        "zelda2",
        "alttp",
        "tloz_oos"
    ],
    "kidnapping": [
        "yoshisisland",
        "sms",
        "alttp",
        "earthbound",
        "openrct2"
    ],
    "poisoning": [
        "papermario",
        "pokemon_emerald",
        "cv64",
        "pokemon_crystal",
        "alttp",
        "tloz_oos"
    ],
    "time paradox": [
        "oot",
        "cv64",
        "jakanddaxter",
        "alttp",
        "tloz_ooa"
    ],
    "paradox": [
        "oot",
        "cv64",
        "jakanddaxter",
        "alttp",
        "tloz_ooa"
    ],
    "status effects": [
        "ladx",
        "pokemon_emerald",
        "dark_souls_2",
        "zelda2",
        "pokemon_crystal",
        "alttp",
        "tloz_ooa",
        "tloz_oos",
        "earthbound"
    ],
    "status": [
        "ladx",
        "pokemon_emerald",
        "dark_souls_2",
        "zelda2",
        "pokemon_crystal",
        "alttp",
        "tloz_ooa",
        "tloz_oos",
        "earthbound"
    ],
    "effects": [
        "ladx",
        "pokemon_emerald",
        "dark_souls_2",
        "zelda2",
        "pokemon_crystal",
        "alttp",
        "tloz_ooa",
        "tloz_oos",
        "earthbound"
    ],
    "hidden room": [
        "alttp",
        "dark_souls_2",
        "heretic",
        "doom_ii"
    ],
    "hidden": [
        "alttp",
        "dark_souls_2",
        "heretic",
        "doom_ii"
    ],
    "room": [
        "alttp",
        "dark_souls_2",
        "heretic",
        "doom_ii"
    ],
    "another world": [
        "ladx",
        "alttp",
        "mm_recomp",
        "doom_ii"
    ],
    "another": [
        "ladx",
        "alttp",
        "mm_recomp",
        "doom_ii"
    ],
    "damage over time": [
        "ffta",
        "oot",
        "pokemon_emerald",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "tloz_oos"
    ],
    "damage": [
        "ffta",
        "minecraft",
        "oot",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "terraria",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "tloz_oos"
    ],
    "over": [
        "ffta",
        "oot",
        "pokemon_emerald",
        "dkc3",
        "tloz_oos",
        "jakanddaxter",
        "pokemon_crystal",
        "alttp",
        "sotn",
        "doom_ii",
        "getting_over_it",
        "dk64",
        "dkc"
    ],
    "monomyth": [
        "alttp",
        "mm2",
        "ss",
        "zelda2"
    ],
    "buddy system": [
        "dkc3",
        "dkc2",
        "alttp",
        "dkc"
    ],
    "buddy": [
        "dkc3",
        "dkc2",
        "alttp",
        "dkc"
    ],
    "retroachievements": [
        "banjo_tooie",
        "k64",
        "mk64",
        "dkc2",
        "earthbound",
        "kdl3",
        "ffmq",
        "diddy_kong_racing",
        "dkc3",
        "star_fox_64",
        "dkc",
        "tetrisattack",
        "lufia2ac",
        "cv64",
        "ff4fe",
        "smw",
        "dk64",
        "sonic_heroes",
        "mm_recomp",
        "oot",
        "papermario",
        "sm64ex",
        "alttp",
        "sm64hacks"
    ],
    "popular": [
        "hk",
        "oot",
        "sm64ex",
        "pokemon_emerald",
        "sc2",
        "kh2",
        "alttp",
        "stardew_valley",
        "dark_souls_3"
    ],
    "animal_well": [
        "animal_well"
    ],
    "animal well": [
        "animal_well"
    ],
    "animal": [
        "ladx",
        "oot",
        "pokemon_emerald",
        "pokemon_crystal",
        "animal_well"
    ],
    "well": [
        "animal_well"
    ],
    "side view": [
        "hk",
        "oribf",
        "ff1",
        "noita",
        "pokemon_rb",
        "k64",
        "marioland2",
        "musedash",
        "wargroove",
        "wargroove2",
        "aus",
        "wl4",
        "dkc2",
        "spire",
        "kdl3",
        "cvcotm",
        "ffmq",
        "blasphemous",
        "messenger",
        "sm",
        "pokemon_frlg",
        "momodoramoonlitfarewell",
        "dkc3",
        "terraria",
        "mzm",
        "sm_map_rando",
        "hylics2",
        "animal_well",
        "dkc",
        "ladx",
        "faxanadu",
        "ror1",
        "tetrisattack",
        "yoshisisland",
        "pokemon_emerald",
        "lufia2ac",
        "zillion",
        "ufo50",
        "cuphead",
        "pokemon_crystal",
        "ff4fe",
        "sotn",
        "mlss",
        "smw",
        "aquaria",
        "rogue_legacy",
        "wl",
        "megamix",
        "papermario",
        "dungeon_clawler",
        "zelda2",
        "timespinner",
        "dlcquest",
        "mm2",
        "getting_over_it",
        "monster_sanctuary",
        "smz3",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "horror": [
        "cvcotm",
        "mm_recomp",
        "blasphemous",
        "inscryption",
        "cv64",
        "doom_1993",
        "residentevil3remake",
        "dontstarvetogether",
        "residentevil2remake",
        "terraria",
        "lethal_company",
        "luigismansion",
        "undertale",
        "sotn",
        "doom_ii",
        "getting_over_it",
        "animal_well",
        "shivers"
    ],
    "survival": [
        "yugioh06",
        "ror1",
        "factorio",
        "minecraft",
        "ror2",
        "dungeon_clawler",
        "factorio_saws",
        "residentevil3remake",
        "dontstarvetogether",
        "residentevil2remake",
        "terraria",
        "lethal_company",
        "subnautica",
        "animal_well",
        "rimworld",
        "raft"
    ],
    "mystery": [
        "pmd_eos",
        "inscryption",
        "outer_wilds",
        "witness",
        "animal_well"
    ],
    "exploration": [
        "tunic",
        "shorthike",
        "sm",
        "outer_wilds",
        "hcniko",
        "terraria",
        "witness",
        "sm_map_rando",
        "hylics2",
        "animal_well",
        "seaofthieves",
        "pokemon_emerald",
        "metroidprime",
        "cv64",
        "pokemon_crystal",
        "lingo",
        "subnautica",
        "aquaria",
        "rogue_legacy",
        "jakanddaxter",
        "lethal_company",
        "dlcquest",
        "celeste",
        "v6"
    ],
    "retro": [
        "minecraft",
        "messenger",
        "blasphemous",
        "ufo50",
        "terraria",
        "cuphead",
        "timespinner",
        "undertale",
        "smo",
        "dlcquest",
        "hylics2",
        "animal_well",
        "celeste",
        "v6",
        "stardew_valley"
    ],
    "dark": [
        "hk",
        "dsr",
        "dark_souls_2",
        "undertale",
        "animal_well",
        "dark_souls_3"
    ],
    "2d": [
        "hk",
        "musedash",
        "smo",
        "earthbound",
        "stardew_valley",
        "messenger",
        "blasphemous",
        "sm",
        "dontstarvetogether",
        "terraria",
        "undertale",
        "sm_map_rando",
        "hylics2",
        "animal_well",
        "cuphead",
        "sotn",
        "zelda2",
        "celeste",
        "v6"
    ],
    "metroidvania": [
        "hk",
        "oribf",
        "pseudoregalia",
        "dark_souls_2",
        "aus",
        "cvcotm",
        "messenger",
        "blasphemous",
        "sm",
        "momodoramoonlitfarewell",
        "mzm",
        "sm_map_rando",
        "animal_well",
        "faxanadu",
        "metroidprime",
        "zillion",
        "sotn",
        "aquaria",
        "rogue_legacy",
        "zelda2",
        "timespinner",
        "monster_sanctuary",
        "v6",
        "enderlilies"
    ],
    "atmospheric": [
        "hk",
        "tunic",
        "dontstarvetogether",
        "powerwashsimulator",
        "hylics2",
        "animal_well",
        "celeste"
    ],
    "relaxing": [
        "sims4",
        "shorthike",
        "hcniko",
        "powerwashsimulator",
        "animal_well",
        "stardew_valley"
    ],
    "controller support": [
        "hk",
        "tunic",
        "hcniko",
        "animal_well",
        "v6",
        "stardew_valley"
    ],
    "controller": [
        "hk",
        "tunic",
        "hcniko",
        "animal_well",
        "v6",
        "stardew_valley"
    ],
    "support": [
        "ffta",
        "hk",
        "tunic",
        "kh1",
        "cv64",
        "hcniko",
        "fm",
        "animal_well",
        "gstla",
        "v6",
        "stardew_valley"
    ],
    "apeescape": [
        "apeescape"
    ],
    "ape escape": [
        "apeescape"
    ],
    "ape": [
        "apeescape",
        "dkc3",
        "mk64",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "escape": [
        "apeescape"
    ],
    "playstation 3": [
        "rogue_legacy",
        "spyro3",
        "sadx",
        "dark_souls_2",
        "sa2b",
        "kh2",
        "terraria",
        "sotn",
        "apeescape"
    ],
    "3": [
        "rogue_legacy",
        "spyro3",
        "sadx",
        "mmbn3",
        "residentevil3remake",
        "dark_souls_2",
        "sa2b",
        "kh2",
        "terraria",
        "sotn",
        "apeescape",
        "wl",
        "kdl3"
    ],
    "playstation portable": [
        "spyro3",
        "apeescape",
        "sotn"
    ],
    "portable": [
        "spyro3",
        "apeescape",
        "sotn"
    ],
    "anime": [
        "huniepop2",
        "yugiohddm",
        "pokemon_emerald",
        "zillion",
        "dw1",
        "musedash",
        "pokemon_crystal",
        "wl4",
        "osu",
        "fm",
        "huniepop",
        "apeescape",
        "gstla"
    ],
    "dinosaurs": [
        "banjo_tooie",
        "yoshisisland",
        "sms",
        "smo",
        "smw",
        "apeescape",
        "earthbound"
    ],
    "collecting": [
        "banjo_tooie",
        "pokemon_rb",
        "pokemon_emerald",
        "pokemon_frlg",
        "zelda2",
        "pokemon_crystal",
        "mzm",
        "apeescape"
    ],
    "multiple endings": [
        "kh1",
        "k64",
        "metroidprime",
        "cv64",
        "apeescape",
        "cuphead",
        "civ_6",
        "tloz_oos",
        "mzm",
        "star_fox_64",
        "sotn",
        "undertale",
        "witness",
        "doom_ii",
        "wl4",
        "dkc2",
        "dk64"
    ],
    "endings": [
        "kh1",
        "k64",
        "metroidprime",
        "cv64",
        "apeescape",
        "cuphead",
        "civ_6",
        "tloz_oos",
        "mzm",
        "star_fox_64",
        "sotn",
        "undertale",
        "witness",
        "doom_ii",
        "wl4",
        "dkc2",
        "dk64"
    ],
    "amnesia": [
        "xenobladex",
        "witness",
        "apeescape",
        "sonic_heroes",
        "aquaria"
    ],
    "voice acting": [
        "huniepop2",
        "kh1",
        "cv64",
        "sly1",
        "dw1",
        "sms",
        "cuphead",
        "civ_6",
        "jakanddaxter",
        "witness",
        "star_fox_64",
        "xenobladex",
        "doom_ii",
        "apeescape",
        "sonic_heroes"
    ],
    "voice": [
        "huniepop2",
        "kh1",
        "cv64",
        "sly1",
        "dw1",
        "sms",
        "cuphead",
        "civ_6",
        "jakanddaxter",
        "witness",
        "star_fox_64",
        "xenobladex",
        "doom_ii",
        "apeescape",
        "sonic_heroes"
    ],
    "acting": [
        "huniepop2",
        "kh1",
        "cv64",
        "sly1",
        "dw1",
        "sms",
        "cuphead",
        "civ_6",
        "jakanddaxter",
        "witness",
        "star_fox_64",
        "xenobladex",
        "doom_ii",
        "apeescape",
        "sonic_heroes"
    ],
    "psone classics": [
        "spyro3",
        "apeescape",
        "sotn",
        "mm2"
    ],
    "psone": [
        "spyro3",
        "apeescape",
        "sotn",
        "mm2"
    ],
    "classics": [
        "spyro3",
        "apeescape",
        "sotn",
        "mm2"
    ],
    "moving platforms": [
        "k64",
        "wl4",
        "sly1",
        "cvcotm",
        "blasphemous",
        "dkc3",
        "apeescape",
        "dkc",
        "ladx",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "sonic_heroes",
        "spyro3",
        "papermario",
        "sms",
        "jakanddaxter",
        "mm2",
        "v6"
    ],
    "moving": [
        "k64",
        "wl4",
        "sly1",
        "cvcotm",
        "blasphemous",
        "dkc3",
        "apeescape",
        "dkc",
        "ladx",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "sonic_heroes",
        "spyro3",
        "papermario",
        "sms",
        "jakanddaxter",
        "mm2",
        "v6"
    ],
    "platforms": [
        "oribf",
        "k64",
        "wl4",
        "sly1",
        "cvcotm",
        "blasphemous",
        "sm",
        "dkc3",
        "sm_map_rando",
        "doom_ii",
        "apeescape",
        "dkc",
        "ladx",
        "metroidprime",
        "cv64",
        "sotn",
        "dk64",
        "sonic_heroes",
        "spyro3",
        "papermario",
        "sms",
        "zelda2",
        "jakanddaxter",
        "mm2",
        "v6"
    ],
    "spiky-haired protagonist": [
        "jakanddaxter",
        "apeescape",
        "sonic_heroes",
        "kh1"
    ],
    "spiky-haired": [
        "jakanddaxter",
        "apeescape",
        "sonic_heroes",
        "kh1"
    ],
    "time trials": [
        "spyro3",
        "diddy_kong_racing",
        "apeescape",
        "mk64",
        "sly1",
        "v6"
    ],
    "trials": [
        "spyro3",
        "diddy_kong_racing",
        "apeescape",
        "mk64",
        "sly1",
        "v6"
    ],
    "apsudoku": [
        "apsudoku"
    ],
    "multiplayer": [
        "paint",
        "generic",
        "jigsaw",
        "saving_princess",
        "checksfinder",
        "archipidle",
        "apsudoku",
        "tracker",
        "chatipelago",
        "yachtdice",
        "wordipelago",
        "clique"
    ],
    "archipelago": [
        "paint",
        "generic",
        "jigsaw",
        "saving_princess",
        "checksfinder",
        "archipidle",
        "apsudoku",
        "tracker",
        "chatipelago",
        "bumpstik",
        "yachtdice",
        "wordipelago",
        "clique"
    ],
    "hints": [
        "paint",
        "generic",
        "jigsaw",
        "saving_princess",
        "checksfinder",
        "archipidle",
        "apsudoku",
        "tracker",
        "chatipelago",
        "yachtdice",
        "wordipelago",
        "clique"
    ],
    "multiworld": [
        "paint",
        "generic",
        "jigsaw",
        "saving_princess",
        "checksfinder",
        "archipidle",
        "apsudoku",
        "tracker",
        "chatipelago",
        "yachtdice",
        "wordipelago",
        "clique"
    ],
    "aquaria": [
        "aquaria"
    ],
    "drama": [
        "undertale",
        "aquaria",
        "earthbound",
        "hades"
    ],
    "linux": [
        "hk",
        "factorio",
        "minecraft",
        "inscryption",
        "shorthike",
        "factorio_saws",
        "crosscode",
        "shapez",
        "stardew_valley",
        "blasphemous",
        "dontstarvetogether",
        "terraria",
        "undertale",
        "landstalker",
        "huniepop",
        "rimworld",
        "ror1",
        "doom_1993",
        "bumpstik",
        "cat_quest",
        "osu",
        "aquaria",
        "overcooked2",
        "rogue_legacy",
        "dungeon_clawler",
        "timespinner",
        "chainedechoes",
        "getting_over_it",
        "monster_sanctuary",
        "celeste64",
        "celeste",
        "v6",
        "openrct2"
    ],
    "android": [
        "osrs",
        "blasphemous",
        "dungeon_clawler",
        "brotato",
        "terraria",
        "musedash",
        "cat_quest",
        "osu",
        "shapez",
        "getting_over_it",
        "subnautica",
        "aquaria",
        "v6",
        "balatro",
        "stardew_valley"
    ],
    "ios": [
        "residentevil3remake",
        "brotato",
        "residentevil2remake",
        "musedash",
        "hades",
        "shapez",
        "balatro",
        "stardew_valley",
        "blasphemous",
        "terraria",
        "witness",
        "cat_quest",
        "osu",
        "subnautica",
        "aquaria",
        "getting_over_it",
        "dungeon_clawler",
        "osrs",
        "v6"
    ],
    "alternate costumes": [
        "kh1",
        "cv64",
        "sms",
        "smo",
        "aquaria"
    ],
    "alternate": [
        "kh1",
        "cv64",
        "sms",
        "smo",
        "aquaria"
    ],
    "costumes": [
        "kh1",
        "cv64",
        "sms",
        "smo",
        "aquaria"
    ],
    "underwater gameplay": [
        "banjo_tooie",
        "kh1",
        "oot",
        "sm64ex",
        "sm64hacks",
        "metroidprime",
        "sms",
        "terraria",
        "smo",
        "mm2",
        "subnautica",
        "dkc2",
        "aquaria",
        "dkc"
    ],
    "underwater": [
        "banjo_tooie",
        "kh1",
        "oot",
        "sm64ex",
        "sm64hacks",
        "metroidprime",
        "sms",
        "terraria",
        "smo",
        "mm2",
        "subnautica",
        "dkc2",
        "aquaria",
        "dkc"
    ],
    "shape-shifting": [
        "banjo_tooie",
        "mm_recomp",
        "k64",
        "metroidprime",
        "sotn",
        "aquaria",
        "kdl3"
    ],
    "plot twist": [
        "oot",
        "kh1",
        "cv64",
        "undertale",
        "aquaria"
    ],
    "plot": [
        "oot",
        "kh1",
        "cv64",
        "undertale",
        "aquaria"
    ],
    "twist": [
        "oot",
        "kh1",
        "cv64",
        "undertale",
        "aquaria"
    ],
    "archipidle": [
        "archipidle"
    ],
    "aus": [
        "aus"
    ],
    "an untitled story": [
        "aus"
    ],
    "an": [
        "aus"
    ],
    "untitled": [
        "aus"
    ],
    "story": [
        "undertale",
        "powerwashsimulator",
        "aus",
        "hades",
        "hylics2",
        "getting_over_it",
        "celeste"
    ],
    "balatro": [
        "balatro"
    ],
    "turn-based strategy (tbs)": [
        "ffta",
        "yugioh06",
        "ff1",
        "pokemon_rb",
        "wargroove",
        "wargroove2",
        "earthbound",
        "balatro",
        "yugiohddm",
        "pmd_eos",
        "pokemon_frlg",
        "undertale",
        "fm",
        "hylics2",
        "pokemon_emerald",
        "ff4fe",
        "papermario",
        "dungeon_clawler",
        "civ_6",
        "chainedechoes",
        "monster_sanctuary"
    ],
    "turn-based": [
        "ffta",
        "yugioh06",
        "ff1",
        "pokemon_rb",
        "wargroove",
        "wargroove2",
        "earthbound",
        "gstla",
        "balatro",
        "yugiohddm",
        "pmd_eos",
        "ffmq",
        "pokemon_frlg",
        "undertale",
        "fm",
        "hylics2",
        "pokemon_emerald",
        "pokemon_crystal",
        "ff4fe",
        "mlss",
        "papermario",
        "dungeon_clawler",
        "civ_6",
        "chainedechoes",
        "monster_sanctuary"
    ],
    "(tbs)": [
        "ffta",
        "yugioh06",
        "ff1",
        "pokemon_rb",
        "wargroove",
        "wargroove2",
        "earthbound",
        "balatro",
        "yugiohddm",
        "pmd_eos",
        "pokemon_frlg",
        "undertale",
        "fm",
        "hylics2",
        "pokemon_emerald",
        "ff4fe",
        "papermario",
        "dungeon_clawler",
        "civ_6",
        "chainedechoes",
        "monster_sanctuary"
    ],
    "card & board game": [
        "yugiohddm",
        "yugioh06",
        "inscryption",
        "fm",
        "spire",
        "balatro"
    ],
    "card": [
        "yugiohddm",
        "yugioh06",
        "inscryption",
        "fm",
        "spire",
        "balatro"
    ],
    "board": [
        "yugiohddm",
        "yugioh06",
        "inscryption",
        "fm",
        "spire",
        "balatro"
    ],
    "game": [
        "ffta",
        "yugioh06",
        "pokemon_rb",
        "inscryption",
        "mmbn3",
        "marioland2",
        "wl4",
        "dkc2",
        "spire",
        "earthbound",
        "gstla",
        "balatro",
        "yugiohddm",
        "cvcotm",
        "pokemon_frlg",
        "hcniko",
        "witness",
        "mzm",
        "fm",
        "doom_ii",
        "ladx",
        "pokemon_emerald",
        "pokemon_crystal",
        "mlss",
        "tloz_ooa",
        "rogue_legacy",
        "spyro3",
        "oot",
        "mm2",
        "tloz_oos",
        "wl"
    ],
    "roguelike": [
        "rogue_legacy",
        "pmd_eos",
        "ror1",
        "dungeon_clawler",
        "hades",
        "spire",
        "balatro"
    ],
    "banjo_tooie": [
        "banjo_tooie"
    ],
    "banjo-tooie": [
        "banjo_tooie"
    ],
    "quiz/trivia": [
        "banjo_tooie"
    ],
    "comedy": [
        "banjo_tooie",
        "musedash",
        "dkc2",
        "sly1",
        "messenger",
        "zork_grand_inquisitor",
        "diddy_kong_racing",
        "dw1",
        "hcniko",
        "undertale",
        "doronko_wanko",
        "huniepop",
        "kh1",
        "toontown",
        "rac2",
        "cuphead",
        "mlss",
        "dk64",
        "overcooked2",
        "placidplasticducksim",
        "rogue_legacy",
        "spyro3",
        "candybox2",
        "papermario",
        "sims4",
        "jakanddaxter",
        "lethal_company",
        "luigismansion",
        "dlcquest",
        "getting_over_it"
    ],
    "nintendo 64": [
        "banjo_tooie",
        "swr",
        "mm_recomp",
        "oot",
        "papermario",
        "k64",
        "sm64ex",
        "cv64",
        "diddy_kong_racing",
        "mk64",
        "star_fox_64",
        "sm64hacks",
        "dk64"
    ],
    "64": [
        "banjo_tooie",
        "swr",
        "mm_recomp",
        "oot",
        "papermario",
        "k64",
        "sm64ex",
        "cv64",
        "diddy_kong_racing",
        "mk64",
        "star_fox_64",
        "sm64hacks",
        "dk64"
    ],
    "aliens": [
        "banjo_tooie",
        "factorio",
        "sm",
        "metroidprime",
        "factorio_saws",
        "sc2",
        "hcniko",
        "xenobladex",
        "lethal_company",
        "mzm",
        "sm_map_rando",
        "earthbound"
    ],
    "animals": [
        "banjo_tooie",
        "minecraft",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "star_fox_64",
        "dkc2",
        "sly1",
        "dkc",
        "stardew_valley"
    ],
    "flight": [
        "banjo_tooie",
        "rogue_legacy",
        "spyro3",
        "shorthike",
        "diddy_kong_racing",
        "terraria",
        "xenobladex",
        "star_fox_64",
        "mm2",
        "wl4",
        "hylics2",
        "dkc"
    ],
    "witches": [
        "banjo_tooie",
        "cv64",
        "tloz_oos",
        "tloz_ooa",
        "enderlilies"
    ],
    "achievements": [
        "huniepop2",
        "banjo_tooie",
        "hk",
        "oribf",
        "minecraft",
        "tunic",
        "blasphemous",
        "dark_souls_2",
        "hcniko",
        "cuphead",
        "musedash",
        "sotn",
        "doom_ii",
        "sonic_heroes",
        "v6",
        "stardew_valley"
    ],
    "talking animals": [
        "banjo_tooie",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "star_fox_64",
        "dkc2",
        "sly1",
        "dkc"
    ],
    "talking": [
        "banjo_tooie",
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "star_fox_64",
        "dkc2",
        "sly1",
        "dkc"
    ],
    "breaking the fourth wall": [
        "ffta",
        "banjo_tooie",
        "ladx",
        "rogue_legacy",
        "papermario",
        "jakanddaxter",
        "undertale",
        "mlss",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "breaking": [
        "ffta",
        "banjo_tooie",
        "wl4",
        "dkc2",
        "sm",
        "undertale",
        "mzm",
        "sm_map_rando",
        "doom_ii",
        "dkc",
        "ladx",
        "metroidprime",
        "sotn",
        "mlss",
        "tloz_ooa",
        "rogue_legacy",
        "oot",
        "papermario",
        "jakanddaxter"
    ],
    "fourth": [
        "ffta",
        "banjo_tooie",
        "ladx",
        "rogue_legacy",
        "papermario",
        "jakanddaxter",
        "undertale",
        "mlss",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "cameo appearance": [
        "banjo_tooie",
        "spyro3",
        "oot",
        "jakanddaxter",
        "dkc2"
    ],
    "cameo": [
        "banjo_tooie",
        "spyro3",
        "oot",
        "jakanddaxter",
        "dkc2"
    ],
    "appearance": [
        "banjo_tooie",
        "spyro3",
        "oot",
        "jakanddaxter",
        "dkc2"
    ],
    "character growth": [
        "pokemon_crystal",
        "banjo_tooie",
        "dk64",
        "oot"
    ],
    "character": [
        "banjo_tooie",
        "oot",
        "dkc3",
        "pokemon_crystal",
        "dkc2",
        "dk64",
        "sonic_heroes",
        "dkc"
    ],
    "growth": [
        "pokemon_crystal",
        "banjo_tooie",
        "dk64",
        "oot"
    ],
    "invisible wall": [
        "banjo_tooie",
        "oot",
        "kh1",
        "mk64",
        "dk64"
    ],
    "invisible": [
        "banjo_tooie",
        "oot",
        "kh1",
        "mk64",
        "dk64"
    ],
    "temporary invincibility": [
        "banjo_tooie",
        "faxanadu",
        "rogue_legacy",
        "papermario",
        "cuphead",
        "jakanddaxter",
        "mk64",
        "doom_ii",
        "dkc2",
        "sonic_heroes"
    ],
    "temporary": [
        "banjo_tooie",
        "faxanadu",
        "rogue_legacy",
        "papermario",
        "cuphead",
        "jakanddaxter",
        "mk64",
        "doom_ii",
        "dkc2",
        "sonic_heroes"
    ],
    "invincibility": [
        "banjo_tooie",
        "faxanadu",
        "rogue_legacy",
        "papermario",
        "cuphead",
        "jakanddaxter",
        "mk64",
        "doom_ii",
        "dkc2",
        "sonic_heroes"
    ],
    "gliding": [
        "banjo_tooie",
        "spyro3",
        "kh1",
        "sms",
        "sly1"
    ],
    "lgbtq+": [
        "banjo_tooie",
        "rogue_legacy",
        "sims4",
        "timespinner",
        "celeste64",
        "celeste"
    ],
    "blasphemous": [
        "blasphemous"
    ],
    "role-playing (rpg)": [
        "ffta",
        "ff1",
        "noita",
        "pokemon_rb",
        "tunic",
        "mmbn3",
        "brotato",
        "crosscode",
        "dark_souls_2",
        "ctjot",
        "wargroove2",
        "hades",
        "tloz",
        "earthbound",
        "gstla",
        "stardew_valley",
        "cvcotm",
        "dark_souls_3",
        "pmd_eos",
        "ffmq",
        "blasphemous",
        "soe",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "undertale",
        "landstalker",
        "hylics2",
        "huniepop",
        "faxanadu",
        "ror1",
        "kh1",
        "toontown",
        "pokemon_emerald",
        "lufia2ac",
        "ufo50",
        "kh2",
        "pokemon_crystal",
        "ff4fe",
        "cat_quest",
        "mlss",
        "sotn",
        "tloz_ooa",
        "rogue_legacy",
        "candybox2",
        "papermario",
        "sims4",
        "dungeon_clawler",
        "dsr",
        "meritous",
        "zelda2",
        "timespinner",
        "chainedechoes",
        "tloz_oos",
        "osrs",
        "monster_sanctuary",
        "enderlilies"
    ],
    "role-playing": [
        "ffta",
        "ff1",
        "noita",
        "pokemon_rb",
        "tunic",
        "mmbn3",
        "brotato",
        "crosscode",
        "dark_souls_2",
        "ctjot",
        "wargroove2",
        "hades",
        "tloz",
        "earthbound",
        "gstla",
        "stardew_valley",
        "cvcotm",
        "dark_souls_3",
        "pmd_eos",
        "ffmq",
        "blasphemous",
        "soe",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "undertale",
        "landstalker",
        "hylics2",
        "huniepop",
        "faxanadu",
        "ror1",
        "kh1",
        "toontown",
        "pokemon_emerald",
        "lufia2ac",
        "ufo50",
        "kh2",
        "pokemon_crystal",
        "ff4fe",
        "cat_quest",
        "mlss",
        "sotn",
        "tloz_ooa",
        "rogue_legacy",
        "candybox2",
        "papermario",
        "sims4",
        "dungeon_clawler",
        "dsr",
        "meritous",
        "zelda2",
        "timespinner",
        "chainedechoes",
        "tloz_oos",
        "osrs",
        "monster_sanctuary",
        "enderlilies"
    ],
    "(rpg)": [
        "ffta",
        "ff1",
        "noita",
        "pokemon_rb",
        "tunic",
        "mmbn3",
        "brotato",
        "crosscode",
        "dark_souls_2",
        "ctjot",
        "wargroove2",
        "hades",
        "tloz",
        "earthbound",
        "gstla",
        "stardew_valley",
        "cvcotm",
        "dark_souls_3",
        "pmd_eos",
        "ffmq",
        "blasphemous",
        "soe",
        "pokemon_frlg",
        "dw1",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "undertale",
        "landstalker",
        "hylics2",
        "huniepop",
        "faxanadu",
        "ror1",
        "kh1",
        "toontown",
        "pokemon_emerald",
        "lufia2ac",
        "ufo50",
        "kh2",
        "pokemon_crystal",
        "ff4fe",
        "cat_quest",
        "mlss",
        "sotn",
        "tloz_ooa",
        "rogue_legacy",
        "candybox2",
        "papermario",
        "sims4",
        "dungeon_clawler",
        "dsr",
        "meritous",
        "zelda2",
        "timespinner",
        "chainedechoes",
        "tloz_oos",
        "osrs",
        "monster_sanctuary",
        "enderlilies"
    ],
    "hack and slash/beat 'em up": [
        "ror1",
        "cv64",
        "hades",
        "blasphemous"
    ],
    "hack": [
        "ror1",
        "cv64",
        "hades",
        "blasphemous"
    ],
    "slash/beat": [
        "ror1",
        "cv64",
        "hades",
        "blasphemous"
    ],
    "'em": [
        "ror1",
        "cv64",
        "hades",
        "blasphemous"
    ],
    "up": [
        "cvcotm",
        "ror1",
        "kh1",
        "blasphemous",
        "papermario",
        "pokemon_emerald",
        "cv64",
        "dark_souls_2",
        "dw1",
        "zelda2",
        "pokemon_crystal",
        "undertale",
        "landstalker",
        "hades",
        "sotn",
        "earthbound",
        "gstla"
    ],
    "bloody": [
        "blasphemous",
        "metroidprime",
        "cv64",
        "residentevil2remake",
        "sotn",
        "heretic",
        "doom_ii",
        "ultrakill"
    ],
    "difficult": [
        "ror1",
        "tunic",
        "messenger",
        "blasphemous",
        "dontstarvetogether",
        "zelda2",
        "hades",
        "getting_over_it",
        "celeste"
    ],
    "side-scrolling": [
        "rogue_legacy",
        "blasphemous",
        "k64",
        "yoshisisland",
        "sm",
        "dkc3",
        "cuphead",
        "musedash",
        "zelda2",
        "mzm",
        "sotn",
        "mm2",
        "sm_map_rando",
        "hylics2",
        "dkc2",
        "dkc",
        "kdl3"
    ],
    "crossover": [
        "kh1",
        "blasphemous",
        "diddy_kong_racing",
        "hcniko",
        "mk64",
        "smz3"
    ],
    "religion": [
        "oot",
        "blasphemous",
        "cv64",
        "civ_6",
        "earthbound"
    ],
    "nudity": [
        "huniepop2",
        "blasphemous",
        "musedash",
        "sotn",
        "huniepop"
    ],
    "2d platformer": [
        "hk",
        "blasphemous",
        "smo",
        "hylics2",
        "v6"
    ],
    "great soundtrack": [
        "tunic",
        "blasphemous",
        "shorthike",
        "bomb_rush_cyberfunk",
        "undertale",
        "hylics2",
        "getting_over_it",
        "ultrakill",
        "celeste"
    ],
    "great": [
        "tunic",
        "blasphemous",
        "shorthike",
        "bomb_rush_cyberfunk",
        "undertale",
        "hylics2",
        "getting_over_it",
        "ultrakill",
        "celeste"
    ],
    "soundtrack": [
        "tunic",
        "blasphemous",
        "shorthike",
        "bomb_rush_cyberfunk",
        "undertale",
        "hylics2",
        "getting_over_it",
        "ultrakill",
        "celeste"
    ],
    "parrying": [
        "hk",
        "blasphemous",
        "dark_souls_2",
        "cuphead",
        "dark_souls_3"
    ],
    "soulslike": [
        "dark_souls_3",
        "tunic",
        "blasphemous",
        "dsr",
        "dark_souls_2",
        "enderlilies"
    ],
    "you can pet the dog": [
        "overcooked2",
        "seaofthieves",
        "sims4",
        "blasphemous",
        "terraria",
        "undertale",
        "hades"
    ],
    "you": [
        "overcooked2",
        "seaofthieves",
        "sims4",
        "blasphemous",
        "terraria",
        "undertale",
        "hades"
    ],
    "can": [
        "overcooked2",
        "seaofthieves",
        "sims4",
        "blasphemous",
        "terraria",
        "undertale",
        "hades"
    ],
    "pet": [
        "overcooked2",
        "seaofthieves",
        "sims4",
        "blasphemous",
        "terraria",
        "undertale",
        "hades"
    ],
    "dog": [
        "overcooked2",
        "seaofthieves",
        "sims4",
        "oot",
        "blasphemous",
        "soe",
        "cv64",
        "hcniko",
        "terraria",
        "undertale",
        "star_fox_64",
        "hades",
        "smo",
        "doronko_wanko",
        "tloz_oos",
        "sly1"
    ],
    "interconnected-world": [
        "hk",
        "blasphemous",
        "sm",
        "dsr",
        "dark_souls_2",
        "luigismansion",
        "mzm",
        "sotn",
        "sm_map_rando",
        "dark_souls_3"
    ],
    "bomb_rush_cyberfunk": [
        "bomb_rush_cyberfunk"
    ],
    "bomb rush cyberfunk": [
        "bomb_rush_cyberfunk"
    ],
    "bomb": [
        "bomb_rush_cyberfunk"
    ],
    "rush": [
        "bomb_rush_cyberfunk"
    ],
    "cyberfunk": [
        "bomb_rush_cyberfunk"
    ],
    "sport": [
        "bomb_rush_cyberfunk",
        "trackmania"
    ],
    "science fiction": [
        "factorio",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "ctjot",
        "earthbound",
        "soe",
        "sm",
        "pokemon_frlg",
        "outer_wilds",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "witness",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "doom_ii",
        "rimworld",
        "tyrian",
        "ror1",
        "swr",
        "ror2",
        "rac2",
        "metroidprime",
        "sc2",
        "doom_1993",
        "zillion",
        "subnautica",
        "jakanddaxter",
        "lethal_company",
        "mm2",
        "ultrakill",
        "v6",
        "satisfactory"
    ],
    "science": [
        "factorio",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "ctjot",
        "earthbound",
        "soe",
        "sm",
        "pokemon_frlg",
        "outer_wilds",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "witness",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "doom_ii",
        "rimworld",
        "tyrian",
        "ror1",
        "swr",
        "ror2",
        "rac2",
        "metroidprime",
        "sc2",
        "doom_1993",
        "zillion",
        "subnautica",
        "jakanddaxter",
        "lethal_company",
        "mm2",
        "ultrakill",
        "v6",
        "satisfactory"
    ],
    "fiction": [
        "factorio",
        "mmbn3",
        "factorio_saws",
        "brotato",
        "crosscode",
        "ctjot",
        "earthbound",
        "soe",
        "sm",
        "pokemon_frlg",
        "outer_wilds",
        "terraria",
        "xenobladex",
        "bomb_rush_cyberfunk",
        "witness",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "doom_ii",
        "rimworld",
        "tyrian",
        "ror1",
        "swr",
        "ror2",
        "rac2",
        "metroidprime",
        "sc2",
        "doom_1993",
        "zillion",
        "subnautica",
        "jakanddaxter",
        "lethal_company",
        "mm2",
        "ultrakill",
        "v6",
        "satisfactory"
    ],
    "spiritual successor": [
        "bomb_rush_cyberfunk",
        "papermario",
        "mlss",
        "xenobladex"
    ],
    "spiritual": [
        "bomb_rush_cyberfunk",
        "papermario",
        "mlss",
        "xenobladex"
    ],
    "successor": [
        "bomb_rush_cyberfunk",
        "papermario",
        "mlss",
        "xenobladex"
    ],
    "brotato": [
        "brotato"
    ],
    "fighting": [
        "brotato"
    ],
    "shooter": [
        "noita",
        "residentevil3remake",
        "brotato",
        "crosscode",
        "residentevil2remake",
        "heretic",
        "sm",
        "mzm",
        "star_fox_64",
        "sm_map_rando",
        "doom_ii",
        "tyrian",
        "ror1",
        "ror2",
        "rac2",
        "metroidprime",
        "doom_1993",
        "ufo50",
        "cuphead",
        "tboir",
        "ultrakill"
    ],
    "arcade": [
        "overcooked2",
        "megamix",
        "messenger",
        "dungeon_clawler",
        "noita",
        "brotato",
        "ufo50",
        "cuphead",
        "mk64",
        "mario_kart_double_dash",
        "osu",
        "smw",
        "tyrian",
        "trackmania",
        "ultrakill",
        "v6"
    ],
    "bumpstik": [
        "bumpstik"
    ],
    "bumper stickers archipelago edition": [
        "bumpstik"
    ],
    "bumper": [
        "bumpstik"
    ],
    "stickers": [
        "bumpstik"
    ],
    "edition": [
        "bumpstik",
        "minecraft"
    ],
    "candybox2": [
        "candybox2"
    ],
    "candy box 2": [
        "candybox2"
    ],
    "candy": [
        "candybox2"
    ],
    "box": [
        "candybox2"
    ],
    "2": [
        "overcooked2",
        "candybox2",
        "kh1",
        "ror2",
        "rac2",
        "dw1",
        "residentevil2remake",
        "kh2",
        "jakanddaxter",
        "wargroove2",
        "smo",
        "hylics2",
        "sly1",
        "sonic_heroes"
    ],
    "text": [
        "huniepop2",
        "yugioh06",
        "candybox2",
        "osrs",
        "huniepop"
    ],
    "web browser": [
        "ttyd",
        "candybox2"
    ],
    "web": [
        "ttyd",
        "candybox2"
    ],
    "browser": [
        "ttyd",
        "candybox2"
    ],
    "management": [
        "ffta",
        "candybox2",
        "sims4",
        "civ_6",
        "rimworld"
    ],
    "cat_quest": [
        "cat_quest"
    ],
    "cat quest": [
        "cat_quest"
    ],
    "cat": [
        "minecraft",
        "kh1",
        "cuphead",
        "cat_quest",
        "wl4",
        "tloz_oos",
        "dkc2"
    ],
    "quest": [
        "dkc2",
        "ffmq",
        "cat_quest",
        "dlcquest"
    ],
    "celeste": [
        "celeste64",
        "celeste"
    ],
    "google stadia": [
        "ror2",
        "celeste",
        "terraria"
    ],
    "google": [
        "ror2",
        "celeste",
        "terraria"
    ],
    "stadia": [
        "ror2",
        "celeste",
        "terraria"
    ],
    "story rich": [
        "undertale",
        "powerwashsimulator",
        "hades",
        "hylics2",
        "getting_over_it",
        "celeste"
    ],
    "rich": [
        "undertale",
        "powerwashsimulator",
        "hades",
        "hylics2",
        "getting_over_it",
        "celeste"
    ],
    "conversation": [
        "undertale",
        "celeste",
        "v6",
        "enderlilies"
    ],
    "celeste64": [
        "celeste64"
    ],
    "celeste 64: fragments of the mountain": [
        "celeste64"
    ],
    "64:": [
        "celeste64",
        "k64"
    ],
    "fragments": [
        "celeste64"
    ],
    "mountain": [
        "celeste64"
    ],
    "chainedechoes": [
        "chainedechoes"
    ],
    "chained echoes": [
        "chainedechoes"
    ],
    "chained": [
        "chainedechoes"
    ],
    "echoes": [
        "chainedechoes"
    ],
    "jrpg": [
        "ffta",
        "pmd_eos",
        "ff1",
        "ffmq",
        "chainedechoes",
        "ff4fe",
        "hylics2"
    ],
    "chatipelago": [
        "chatipelago"
    ],
    "checksfinder": [
        "checksfinder"
    ],
    "civ_6": [
        "civ_6"
    ],
    "sid meier's civilization iv": [
        "civ_6"
    ],
    "sid": [
        "civ_6"
    ],
    "meier's": [
        "civ_6"
    ],
    "civilization": [
        "metroidprime",
        "civ_6",
        "jakanddaxter",
        "gstla",
        "ss"
    ],
    "iv": [
        "civ_6"
    ],
    "educational": [
        "civ_6"
    ],
    "4x (explore, expand, exploit, and exterminate)": [
        "civ_6",
        "openrct2"
    ],
    "4x": [
        "civ_6",
        "openrct2"
    ],
    "(explore,": [
        "civ_6",
        "openrct2"
    ],
    "expand,": [
        "civ_6",
        "openrct2"
    ],
    "exploit,": [
        "civ_6",
        "openrct2"
    ],
    "exterminate)": [
        "civ_6",
        "openrct2"
    ],
    "construction": [
        "civ_6",
        "minecraft",
        "terraria",
        "xenobladex"
    ],
    "mining": [
        "civ_6",
        "minecraft",
        "terraria",
        "stardew_valley"
    ],
    "loot gathering": [
        "cv64",
        "xenobladex",
        "terraria",
        "civ_6",
        "dk64"
    ],
    "loot": [
        "cv64",
        "xenobladex",
        "terraria",
        "civ_6",
        "dk64"
    ],
    "gathering": [
        "cv64",
        "xenobladex",
        "terraria",
        "civ_6",
        "dk64"
    ],
    "royalty": [
        "civ_6",
        "rogue_legacy",
        "earthbound",
        "mlss"
    ],
    "ambient music": [
        "soe",
        "metroidprime",
        "cv64",
        "dkc3",
        "civ_6",
        "mzm",
        "dkc2",
        "dkc"
    ],
    "ambient": [
        "soe",
        "metroidprime",
        "cv64",
        "dkc3",
        "civ_6",
        "mzm",
        "dkc2",
        "dkc"
    ],
    "music": [
        "ffta",
        "musedash",
        "dkc2",
        "gstla",
        "soe",
        "ffmq",
        "dkc3",
        "mzm",
        "doom_ii",
        "dkc",
        "metroidprime",
        "cv64",
        "sotn",
        "osu",
        "sonic_heroes",
        "placidplasticducksim",
        "megamix",
        "civ_6",
        "ultrakill"
    ],
    "clique": [
        "clique"
    ],
    "crosscode": [
        "crosscode"
    ],
    "16-bit": [
        "rogue_legacy",
        "sm",
        "crosscode",
        "sm_map_rando",
        "earthbound"
    ],
    "a.i. companion": [
        "oot",
        "kh1",
        "crosscode",
        "star_fox_64",
        "sotn"
    ],
    "a.i.": [
        "oot",
        "kh1",
        "crosscode",
        "star_fox_64",
        "sotn"
    ],
    "companion": [
        "oot",
        "kh1",
        "crosscode",
        "star_fox_64",
        "sotn"
    ],
    "ctjot": [
        "ctjot"
    ],
    "chrono trigger": [
        "ctjot"
    ],
    "chrono": [
        "ctjot"
    ],
    "trigger": [
        "ctjot"
    ],
    "nintendo ds": [
        "ctjot",
        "pmd_eos"
    ],
    "ds": [
        "ctjot",
        "pmd_eos"
    ],
    "cuphead": [
        "cuphead"
    ],
    "pirates": [
        "seaofthieves",
        "kh1",
        "metroidprime",
        "cuphead",
        "mzm",
        "wargroove2",
        "tloz_oos",
        "dkc2",
        "tloz_ooa"
    ],
    "shark": [
        "jakanddaxter",
        "raft",
        "dkc",
        "cuphead"
    ],
    "robots": [
        "swr",
        "sms",
        "cuphead",
        "xenobladex",
        "star_fox_64",
        "ultrakill",
        "mm2",
        "sonic_heroes",
        "earthbound"
    ],
    "dancing": [
        "dkc2",
        "tloz_ooa",
        "dkc3",
        "cuphead"
    ],
    "violent plants": [
        "rogue_legacy",
        "metroidprime",
        "sms",
        "cuphead",
        "terraria",
        "ss"
    ],
    "violent": [
        "rogue_legacy",
        "metroidprime",
        "sms",
        "cuphead",
        "terraria",
        "ss"
    ],
    "plants": [
        "rogue_legacy",
        "metroidprime",
        "sms",
        "cuphead",
        "terraria",
        "ss"
    ],
    "auto-scrolling levels": [
        "k64",
        "dkc3",
        "cuphead",
        "star_fox_64",
        "dkc2",
        "v6",
        "dkc"
    ],
    "auto-scrolling": [
        "k64",
        "dkc3",
        "cuphead",
        "star_fox_64",
        "dkc2",
        "v6",
        "dkc"
    ],
    "levels": [
        "k64",
        "dkc3",
        "cuphead",
        "star_fox_64",
        "dkc2",
        "v6",
        "dkc"
    ],
    "boss assistance": [
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "papermario",
        "metroidprime",
        "dark_souls_2",
        "sms",
        "cuphead",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "assistance": [
        "rogue_legacy",
        "mm_recomp",
        "oot",
        "papermario",
        "metroidprime",
        "dark_souls_2",
        "sms",
        "cuphead",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "cv64": [
        "cv64"
    ],
    "castlevania": [
        "cv64"
    ],
    "summoning support": [
        "ffta",
        "kh1",
        "cv64",
        "fm",
        "gstla"
    ],
    "summoning": [
        "ffta",
        "kh1",
        "cv64",
        "fm",
        "gstla"
    ],
    "horse": [
        "rogue_legacy",
        "cvcotm",
        "minecraft",
        "oot",
        "cv64",
        "sotn"
    ],
    "multiple protagonists": [
        "rogue_legacy",
        "spyro3",
        "cv64",
        "dkc3",
        "sotn",
        "mlss",
        "dkc2",
        "dk64",
        "sonic_heroes",
        "earthbound",
        "dkc"
    ],
    "protagonists": [
        "rogue_legacy",
        "spyro3",
        "cv64",
        "dkc3",
        "sotn",
        "mlss",
        "dkc2",
        "dk64",
        "sonic_heroes",
        "earthbound",
        "dkc"
    ],
    "traps": [
        "rogue_legacy",
        "minecraft",
        "cv64",
        "dark_souls_2",
        "doom_ii"
    ],
    "bats": [
        "cvcotm",
        "cv64",
        "terraria",
        "zelda2",
        "pokemon_crystal",
        "mk64",
        "sotn"
    ],
    "day/night cycle": [
        "mm_recomp",
        "minecraft",
        "oot",
        "tww",
        "cv64",
        "terraria",
        "xenobladex",
        "jakanddaxter",
        "pokemon_crystal",
        "sotn",
        "dk64",
        "ss",
        "stardew_valley"
    ],
    "day/night": [
        "mm_recomp",
        "minecraft",
        "oot",
        "tww",
        "cv64",
        "terraria",
        "xenobladex",
        "jakanddaxter",
        "pokemon_crystal",
        "sotn",
        "dk64",
        "ss",
        "stardew_valley"
    ],
    "cycle": [
        "mm_recomp",
        "minecraft",
        "oot",
        "tww",
        "cv64",
        "terraria",
        "xenobladex",
        "jakanddaxter",
        "pokemon_crystal",
        "sotn",
        "dk64",
        "ss",
        "stardew_valley"
    ],
    "skeletons": [
        "cvcotm",
        "seaofthieves",
        "cv64",
        "terraria",
        "undertale",
        "sotn",
        "heretic",
        "sly1"
    ],
    "falling damage": [
        "minecraft",
        "oot",
        "metroidprime",
        "cv64",
        "terraria"
    ],
    "falling": [
        "minecraft",
        "oot",
        "metroidprime",
        "cv64",
        "terraria"
    ],
    "unstable platforms": [
        "cvcotm",
        "oribf",
        "sm",
        "metroidprime",
        "cv64",
        "sms",
        "zelda2",
        "sm_map_rando",
        "doom_ii",
        "sly1",
        "v6",
        "dkc"
    ],
    "unstable": [
        "cvcotm",
        "oribf",
        "sm",
        "metroidprime",
        "cv64",
        "sms",
        "zelda2",
        "sm_map_rando",
        "doom_ii",
        "sly1",
        "v6",
        "dkc"
    ],
    "melee": [
        "ffta",
        "cvcotm",
        "kh1",
        "papermario",
        "k64",
        "pokemon_emerald",
        "cv64",
        "doom_1993",
        "dark_souls_2",
        "terraria",
        "pokemon_crystal",
        "sotn",
        "wl4",
        "heretic",
        "doom_ii",
        "sly1",
        "gstla",
        "kdl3"
    ],
    "male antagonist": [
        "cv64",
        "earthbound",
        "mm2",
        "sms"
    ],
    "male": [
        "cv64",
        "earthbound",
        "mm2",
        "sms"
    ],
    "antagonist": [
        "cv64",
        "earthbound",
        "mm2",
        "sms"
    ],
    "instant kill": [
        "cv64",
        "mm2",
        "dkc2",
        "v6",
        "dkc"
    ],
    "instant": [
        "cv64",
        "mm2",
        "dkc2",
        "v6",
        "dkc"
    ],
    "kill": [
        "cv64",
        "mm2",
        "dkc2",
        "v6",
        "dkc"
    ],
    "difficulty level": [
        "minecraft",
        "metroidprime",
        "cv64",
        "musedash",
        "mzm",
        "mk64",
        "star_fox_64",
        "mm2",
        "osu",
        "doom_ii"
    ],
    "difficulty": [
        "minecraft",
        "metroidprime",
        "cv64",
        "musedash",
        "mzm",
        "mk64",
        "star_fox_64",
        "mm2",
        "osu",
        "doom_ii"
    ],
    "level": [
        "minecraft",
        "kh1",
        "oot",
        "metroidprime",
        "cv64",
        "sms",
        "musedash",
        "mzm",
        "mk64",
        "star_fox_64",
        "mm2",
        "osu",
        "doom_ii",
        "dkc2",
        "dkc"
    ],
    "cvcotm": [
        "cvcotm"
    ],
    "castlevania: circle of the moon": [
        "cvcotm"
    ],
    "castlevania:": [
        "cvcotm",
        "sotn"
    ],
    "circle": [
        "cvcotm"
    ],
    "moon": [
        "cvcotm"
    ],
    "game boy advance": [
        "ffta",
        "yugioh06",
        "cvcotm",
        "yugiohddm",
        "pokemon_emerald",
        "mmbn3",
        "pokemon_frlg",
        "mzm",
        "mlss",
        "wl4",
        "earthbound",
        "gstla"
    ],
    "boy": [
        "ffta",
        "yugioh06",
        "pokemon_rb",
        "mmbn3",
        "marioland2",
        "wl4",
        "earthbound",
        "gstla",
        "yugiohddm",
        "cvcotm",
        "pokemon_frlg",
        "mzm",
        "ladx",
        "pokemon_emerald",
        "pokemon_crystal",
        "mlss",
        "tloz_ooa",
        "mm2",
        "tloz_oos",
        "wl"
    ],
    "advance": [
        "ffta",
        "yugioh06",
        "cvcotm",
        "yugiohddm",
        "pokemon_emerald",
        "mmbn3",
        "pokemon_frlg",
        "mzm",
        "mlss",
        "wl4",
        "earthbound",
        "gstla"
    ],
    "gravity": [
        "cvcotm",
        "oot",
        "papermario",
        "metroidprime",
        "dkc3",
        "mzm",
        "star_fox_64",
        "sotn",
        "dkc2",
        "dk64",
        "v6",
        "dkc"
    ],
    "wolf": [
        "rogue_legacy",
        "cvcotm",
        "minecraft",
        "star_fox_64",
        "sotn"
    ],
    "leveling up": [
        "cvcotm",
        "kh1",
        "papermario",
        "pokemon_emerald",
        "dark_souls_2",
        "dw1",
        "zelda2",
        "pokemon_crystal",
        "undertale",
        "landstalker",
        "sotn",
        "earthbound",
        "gstla"
    ],
    "leveling": [
        "cvcotm",
        "kh1",
        "papermario",
        "pokemon_emerald",
        "dark_souls_2",
        "dw1",
        "zelda2",
        "pokemon_crystal",
        "undertale",
        "landstalker",
        "sotn",
        "earthbound",
        "gstla"
    ],
    "dark_souls_2": [
        "dark_souls_2"
    ],
    "dark souls ii": [
        "dark_souls_2"
    ],
    "souls": [
        "dark_souls_2",
        "dark_souls_3"
    ],
    "ii": [
        "dark_souls_2",
        "kh2",
        "ff4fe",
        "mm2",
        "spire"
    ],
    "xbox 360": [
        "sadx",
        "dark_souls_2",
        "sa2b",
        "terraria",
        "sotn",
        "dlcquest"
    ],
    "360": [
        "sadx",
        "dark_souls_2",
        "sa2b",
        "terraria",
        "sotn",
        "dlcquest"
    ],
    "spider": [
        "oribf",
        "minecraft",
        "dark_souls_2",
        "zelda2",
        "dkc2",
        "sly1"
    ],
    "customizable characters": [
        "dark_souls_3",
        "dark_souls_2",
        "xenobladex",
        "terraria",
        "stardew_valley"
    ],
    "customizable": [
        "dark_souls_3",
        "dark_souls_2",
        "xenobladex",
        "terraria",
        "stardew_valley"
    ],
    "checkpoints": [
        "dark_souls_2",
        "dkc3",
        "jakanddaxter",
        "smo",
        "mm2",
        "dkc2",
        "sly1",
        "sonic_heroes",
        "v6",
        "dkc"
    ],
    "sliding down ladders": [
        "k64",
        "dark_souls_2",
        "wl4",
        "dark_souls_3"
    ],
    "sliding": [
        "k64",
        "dark_souls_2",
        "wl4",
        "dark_souls_3"
    ],
    "down": [
        "k64",
        "dark_souls_2",
        "wl4",
        "dark_souls_3"
    ],
    "ladders": [
        "k64",
        "dark_souls_2",
        "wl4",
        "dark_souls_3"
    ],
    "fire manipulation": [
        "rogue_legacy",
        "minecraft",
        "papermario",
        "pokemon_emerald",
        "dark_souls_2",
        "pokemon_crystal",
        "earthbound",
        "gstla"
    ],
    "fire": [
        "rogue_legacy",
        "minecraft",
        "papermario",
        "pokemon_emerald",
        "dark_souls_2",
        "pokemon_crystal",
        "earthbound",
        "gstla"
    ],
    "manipulation": [
        "rogue_legacy",
        "minecraft",
        "oot",
        "papermario",
        "pokemon_emerald",
        "sm",
        "dark_souls_2",
        "pokemon_crystal",
        "timespinner",
        "earthbound",
        "sm_map_rando",
        "gstla"
    ],
    "dark_souls_3": [
        "dark_souls_3"
    ],
    "dark souls iii": [
        "dark_souls_3"
    ],
    "iii": [
        "zillion",
        "dark_souls_3"
    ],
    "pick your gender": [
        "pokemon_crystal",
        "pokemon_emerald",
        "terraria",
        "dark_souls_3"
    ],
    "pick": [
        "pokemon_crystal",
        "pokemon_emerald",
        "terraria",
        "dark_souls_3"
    ],
    "your": [
        "pokemon_crystal",
        "pokemon_emerald",
        "terraria",
        "dark_souls_3"
    ],
    "gender": [
        "pokemon_crystal",
        "pokemon_emerald",
        "terraria",
        "dark_souls_3"
    ],
    "entering world in a painting": [
        "sm64ex",
        "sm64hacks",
        "smo",
        "dark_souls_3"
    ],
    "entering": [
        "sm64ex",
        "sm64hacks",
        "smo",
        "dark_souls_3"
    ],
    "painting": [
        "sm64ex",
        "sm64hacks",
        "smo",
        "dark_souls_3"
    ],
    "diddy_kong_racing": [
        "diddy_kong_racing"
    ],
    "diddy kong racing": [
        "diddy_kong_racing"
    ],
    "diddy": [
        "diddy_kong_racing"
    ],
    "kong": [
        "diddy_kong_racing",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "racing": [
        "swr",
        "diddy_kong_racing",
        "jakanddaxter",
        "mk64",
        "mario_kart_double_dash",
        "trackmania"
    ],
    "go-kart": [
        "diddy_kong_racing",
        "mk64",
        "mario_kart_double_dash",
        "toontown"
    ],
    "behind the waterfall": [
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_ooa",
        "smo",
        "sotn",
        "gstla",
        "ss"
    ],
    "behind": [
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_ooa",
        "smo",
        "sotn",
        "gstla",
        "ss"
    ],
    "waterfall": [
        "diddy_kong_racing",
        "hcniko",
        "dkc3",
        "tloz_ooa",
        "smo",
        "sotn",
        "gstla",
        "ss"
    ],
    "dk64": [
        "dk64"
    ],
    "donkey kong 64": [
        "dk64"
    ],
    "donkey": [
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "artificial intelligence": [
        "metroidprime",
        "sly1",
        "jakanddaxter",
        "mk64",
        "star_fox_64",
        "doom_ii",
        "dk64"
    ],
    "artificial": [
        "metroidprime",
        "sly1",
        "jakanddaxter",
        "mk64",
        "star_fox_64",
        "doom_ii",
        "dk64"
    ],
    "intelligence": [
        "metroidprime",
        "sly1",
        "jakanddaxter",
        "mk64",
        "star_fox_64",
        "doom_ii",
        "dk64"
    ],
    "death match": [
        "dk64",
        "mk64",
        "heretic",
        "doom_ii"
    ],
    "match": [
        "dk64",
        "mk64",
        "heretic",
        "doom_ii"
    ],
    "gorilla": [
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "franchise reboot": [
        "ffta",
        "dk64",
        "ffmq",
        "dkc"
    ],
    "franchise": [
        "ffta",
        "dk64",
        "ffmq",
        "dkc"
    ],
    "reboot": [
        "ffta",
        "dk64",
        "ffmq",
        "dkc"
    ],
    "western games based on japanese ips": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "western": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "games": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "based": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "on": [
        "metroidprime",
        "dkc3",
        "doom_ii",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "japanese": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "ips": [
        "metroidprime",
        "dkc3",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "over 100% completion": [
        "dkc3",
        "sotn",
        "doom_ii",
        "dk64",
        "dkc"
    ],
    "100%": [
        "dkc3",
        "sotn",
        "doom_ii",
        "dk64",
        "dkc"
    ],
    "completion": [
        "metroidprime",
        "dkc3",
        "mzm",
        "sotn",
        "doom_ii",
        "dkc2",
        "dk64",
        "dkc"
    ],
    "completion percentage": [
        "metroidprime",
        "mzm",
        "sotn",
        "dkc2",
        "dk64"
    ],
    "percentage": [
        "metroidprime",
        "mzm",
        "sotn",
        "dkc2",
        "dk64"
    ],
    "mine cart sequence": [
        "dkc2",
        "dk64",
        "ss",
        "dkc"
    ],
    "mine": [
        "dkc2",
        "dk64",
        "ss",
        "dkc"
    ],
    "cart": [
        "dkc2",
        "dk64",
        "ss",
        "dkc"
    ],
    "sequence": [
        "oot",
        "sm",
        "metroidprime",
        "mzm",
        "sotn",
        "sm_map_rando",
        "wl4",
        "doom_ii",
        "dkc2",
        "dk64",
        "tloz_ooa",
        "ss",
        "dkc"
    ],
    "invisibility": [
        "papermario",
        "sly1",
        "doom_1993",
        "doom_ii",
        "dk64"
    ],
    "foreshadowing": [
        "metroidprime",
        "dk64",
        "mzm",
        "sms"
    ],
    "dkc": [
        "dkc"
    ],
    "donkey kong country": [
        "dkc"
    ],
    "country": [
        "dkc3",
        "dkc2",
        "dkc"
    ],
    "frog": [
        "hcniko",
        "jakanddaxter",
        "star_fox_64",
        "dkc2",
        "dkc"
    ],
    "overworld": [
        "ffta",
        "ffmq",
        "dkc3",
        "zelda2",
        "tloz",
        "dkc2",
        "gstla",
        "dkc"
    ],
    "bonus stage": [
        "spyro3",
        "dkc3",
        "smw",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "bonus": [
        "spyro3",
        "dkc3",
        "smw",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "crocodile": [
        "dkc3",
        "dkc2",
        "sly1",
        "dkc"
    ],
    "water level": [
        "oot",
        "kh1",
        "sms",
        "mm2",
        "dkc2",
        "dkc"
    ],
    "water": [
        "oot",
        "kh1",
        "sms",
        "mm2",
        "dkc2",
        "dkc"
    ],
    "speedrun": [
        "sm64ex",
        "metroidprime",
        "sotn",
        "sm64hacks",
        "dkc"
    ],
    "villain turned good": [
        "sotn",
        "gstla",
        "kh1",
        "dkc"
    ],
    "turned": [
        "sotn",
        "gstla",
        "kh1",
        "dkc"
    ],
    "good": [
        "sotn",
        "gstla",
        "kh1",
        "dkc"
    ],
    "resized enemy": [
        "dkc2",
        "oot",
        "dkc",
        "rogue_legacy"
    ],
    "resized": [
        "dkc2",
        "oot",
        "dkc",
        "rogue_legacy"
    ],
    "enemy": [
        "dkc2",
        "oot",
        "dkc",
        "rogue_legacy"
    ],
    "on-the-fly character switching": [
        "dkc3",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "on-the-fly": [
        "dkc3",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "switching": [
        "dkc3",
        "dkc2",
        "sonic_heroes",
        "dkc"
    ],
    "dkc2": [
        "dkc2"
    ],
    "donkey kong country 2: diddy's kong quest": [
        "dkc2"
    ],
    "2:": [
        "huniepop2",
        "yoshisisland",
        "marioland2",
        "sa2b",
        "dkc2"
    ],
    "diddy's": [
        "dkc2"
    ],
    "climbing": [
        "terraria",
        "sms",
        "jakanddaxter",
        "tloz_oos",
        "dkc2",
        "sly1",
        "tloz_ooa"
    ],
    "game reference": [
        "rogue_legacy",
        "spyro3",
        "oot",
        "hcniko",
        "witness",
        "doom_ii",
        "dkc2"
    ],
    "reference": [
        "placidplasticducksim",
        "rogue_legacy",
        "spyro3",
        "oot",
        "hcniko",
        "witness",
        "doom_ii",
        "dkc2"
    ],
    "sprinting mechanics": [
        "mm_recomp",
        "soe",
        "oot",
        "sm64hacks",
        "sm64ex",
        "pokemon_emerald",
        "sms",
        "pokemon_crystal",
        "wl4",
        "dkc2"
    ],
    "sprinting": [
        "mm_recomp",
        "soe",
        "oot",
        "sm64hacks",
        "sm64ex",
        "pokemon_emerald",
        "sms",
        "pokemon_crystal",
        "wl4",
        "dkc2"
    ],
    "mechanics": [
        "mm_recomp",
        "soe",
        "oot",
        "sm64hacks",
        "sm64ex",
        "pokemon_emerald",
        "sms",
        "pokemon_crystal",
        "wl4",
        "dkc2"
    ],
    "fireworks": [
        "dkc2",
        "sly1",
        "mlss",
        "k64"
    ],
    "dkc3": [
        "dkc3"
    ],
    "donkey kong country 3: dixie kong's double trouble!": [
        "dkc3"
    ],
    "3:": [
        "dkc3"
    ],
    "dixie": [
        "dkc3"
    ],
    "kong's": [
        "dkc3"
    ],
    "double": [
        "huniepop2",
        "mario_kart_double_dash",
        "dkc3"
    ],
    "trouble!": [
        "dkc3"
    ],
    "snowman": [
        "sm64hacks",
        "papermario",
        "dkc3",
        "sm64ex"
    ],
    "dlcquest": [
        "dlcquest"
    ],
    "dlc quest": [
        "dlcquest"
    ],
    "dlc": [
        "dlcquest"
    ],
    "deliberately retro": [
        "minecraft",
        "ufo50",
        "terraria",
        "timespinner",
        "smo",
        "dlcquest",
        "v6",
        "stardew_valley"
    ],
    "deliberately": [
        "minecraft",
        "ufo50",
        "terraria",
        "timespinner",
        "smo",
        "dlcquest",
        "v6",
        "stardew_valley"
    ],
    "punctuation mark above head": [
        "rogue_legacy",
        "pokemon_emerald",
        "pokemon_crystal",
        "dlcquest",
        "tloz_ooa"
    ],
    "punctuation": [
        "rogue_legacy",
        "pokemon_emerald",
        "pokemon_crystal",
        "dlcquest",
        "tloz_ooa"
    ],
    "mark": [
        "rogue_legacy",
        "pokemon_emerald",
        "pokemon_crystal",
        "dlcquest",
        "tloz_ooa"
    ],
    "above": [
        "rogue_legacy",
        "pokemon_emerald",
        "pokemon_crystal",
        "dlcquest",
        "tloz_ooa"
    ],
    "head": [
        "rogue_legacy",
        "pokemon_emerald",
        "pokemon_crystal",
        "dlcquest",
        "tloz_ooa"
    ],
    "dontstarvetogether": [
        "dontstarvetogether"
    ],
    "don't starve together": [
        "dontstarvetogether"
    ],
    "don't": [
        "dontstarvetogether"
    ],
    "starve": [
        "dontstarvetogether"
    ],
    "together": [
        "dontstarvetogether"
    ],
    "crafting": [
        "seaofthieves",
        "factorio",
        "minecraft",
        "factorio_saws",
        "dontstarvetogether",
        "terraria",
        "raft",
        "satisfactory",
        "stardew_valley"
    ],
    "funny": [
        "huniepop2",
        "sims4",
        "shorthike",
        "dontstarvetogether",
        "undertale",
        "powerwashsimulator",
        "getting_over_it"
    ],
    "survival horror": [
        "lethal_company",
        "residentevil3remake",
        "dontstarvetogether",
        "residentevil2remake"
    ],
    "doom_1993": [
        "doom_1993"
    ],
    "doom": [
        "doom_1993",
        "doom_ii"
    ],
    "windows mobile": [
        "doom_1993"
    ],
    "windows": [
        "doom_1993",
        "terraria"
    ],
    "mobile": [
        "doom_1993"
    ],
    "pc-9800 series": [
        "doom_1993",
        "doom_ii"
    ],
    "pc-9800": [
        "doom_1993",
        "doom_ii"
    ],
    "dos": [
        "tyrian",
        "doom_1993",
        "heretic",
        "doom_ii"
    ],
    "doom_ii": [
        "doom_ii"
    ],
    "doom ii: hell on earth": [
        "doom_ii"
    ],
    "ii:": [
        "lufia2ac",
        "sc2",
        "zelda2",
        "doom_ii"
    ],
    "hell": [
        "doom_ii"
    ],
    "earth": [
        "doom_ii"
    ],
    "tapwave zodiac": [
        "doom_ii"
    ],
    "tapwave": [
        "doom_ii"
    ],
    "zodiac": [
        "doom_ii"
    ],
    "pop culture reference": [
        "witness",
        "placidplasticducksim",
        "rogue_legacy",
        "doom_ii"
    ],
    "pop": [
        "witness",
        "placidplasticducksim",
        "rogue_legacy",
        "doom_ii"
    ],
    "culture": [
        "witness",
        "placidplasticducksim",
        "rogue_legacy",
        "doom_ii"
    ],
    "stat tracking": [
        "ffta",
        "rogue_legacy",
        "kh1",
        "witness",
        "osu",
        "doom_ii"
    ],
    "stat": [
        "ffta",
        "rogue_legacy",
        "kh1",
        "witness",
        "osu",
        "doom_ii"
    ],
    "tracking": [
        "ffta",
        "rogue_legacy",
        "kh1",
        "witness",
        "osu",
        "doom_ii"
    ],
    "rock music": [
        "ffta",
        "ffmq",
        "ultrakill",
        "sotn",
        "doom_ii",
        "sonic_heroes",
        "gstla"
    ],
    "rock": [
        "ffta",
        "ffmq",
        "ultrakill",
        "sotn",
        "doom_ii",
        "sonic_heroes",
        "gstla"
    ],
    "sequence breaking": [
        "oot",
        "sm",
        "metroidprime",
        "mzm",
        "sotn",
        "sm_map_rando",
        "wl4",
        "doom_ii",
        "tloz_ooa"
    ],
    "doronko_wanko": [
        "doronko_wanko"
    ],
    "doronko wanko": [
        "doronko_wanko"
    ],
    "doronko": [
        "doronko_wanko"
    ],
    "wanko": [
        "doronko_wanko"
    ],
    "dsr": [
        "dsr"
    ],
    "dark souls: remastered": [
        "dsr"
    ],
    "souls:": [
        "dsr"
    ],
    "remastered": [
        "dsr"
    ],
    "dungeon_clawler": [
        "dungeon_clawler"
    ],
    "dungeon clawler": [
        "dungeon_clawler"
    ],
    "dungeon": [
        "yugiohddm",
        "dungeon_clawler"
    ],
    "clawler": [
        "dungeon_clawler"
    ],
    "dw1": [
        "dw1"
    ],
    "digimon world 4": [
        "dw1"
    ],
    "digimon": [
        "dw1"
    ],
    "nintendo gamecube": [
        "tww",
        "metroidprime",
        "dw1",
        "sms",
        "luigismansion",
        "mario_kart_double_dash",
        "sonic_heroes"
    ],
    "gamecube": [
        "tww",
        "metroidprime",
        "dw1",
        "sms",
        "luigismansion",
        "mario_kart_double_dash",
        "sonic_heroes"
    ],
    "playstation 2": [
        "kh1",
        "rac2",
        "dw1",
        "kh2",
        "jakanddaxter",
        "sly1",
        "sonic_heroes"
    ],
    "earthbound": [
        "earthbound"
    ],
    "party system": [
        "ffta",
        "kh1",
        "ffmq",
        "papermario",
        "pokemon_emerald",
        "xenobladex",
        "pokemon_crystal",
        "earthbound",
        "mlss",
        "gstla"
    ],
    "party": [
        "ffta",
        "overcooked2",
        "placidplasticducksim",
        "kh1",
        "ffmq",
        "papermario",
        "pokemon_emerald",
        "xenobladex",
        "pokemon_crystal",
        "mk64",
        "earthbound",
        "mlss",
        "gstla"
    ],
    "censored version": [
        "earthbound",
        "oot",
        "residentevil2remake",
        "xenobladex"
    ],
    "censored": [
        "earthbound",
        "oot",
        "residentevil2remake",
        "xenobladex"
    ],
    "version": [
        "oot",
        "pokemon_rb",
        "pokemon_emerald",
        "pokemon_frlg",
        "residentevil2remake",
        "xenobladex",
        "pokemon_crystal",
        "earthbound"
    ],
    "enderlilies": [
        "enderlilies"
    ],
    "ender lilies: quietus of the knights": [
        "enderlilies"
    ],
    "ender": [
        "enderlilies"
    ],
    "lilies:": [
        "enderlilies"
    ],
    "quietus": [
        "enderlilies"
    ],
    "knights": [
        "enderlilies"
    ],
    "forest": [
        "oribf",
        "tunic",
        "hcniko",
        "enderlilies"
    ],
    "factorio": [
        "factorio"
    ],
    "factorio_saws": [
        "factorio_saws"
    ],
    "factorio: space age": [
        "factorio_saws"
    ],
    "factorio:": [
        "factorio_saws"
    ],
    "space": [
        "sc2",
        "factorio_saws",
        "marioland2",
        "getting_over_it",
        "v6"
    ],
    "faxanadu": [
        "faxanadu"
    ],
    "family computer": [
        "faxanadu",
        "ff1",
        "tloz"
    ],
    "family": [
        "faxanadu",
        "sims4",
        "ff1",
        "tunic",
        "shorthike",
        "zelda2",
        "powerwashsimulator",
        "tloz"
    ],
    "computer": [
        "faxanadu",
        "ff1",
        "tloz",
        "zelda2"
    ],
    "nintendo entertainment system": [
        "faxanadu",
        "ff1",
        "tloz",
        "zelda2"
    ],
    "ff1": [
        "ff1"
    ],
    "final fantasy": [
        "ff1"
    ],
    "final": [
        "ffta",
        "ff4fe",
        "ff1",
        "ffmq"
    ],
    "kids": [
        "overcooked2",
        "placidplasticducksim",
        "pmd_eos",
        "minecraft",
        "ff1",
        "pokemon_rb",
        "tetrisattack",
        "yoshisisland",
        "pokemon_emerald",
        "pokemon_frlg",
        "pokemon_crystal",
        "mk64",
        "mario_kart_double_dash"
    ],
    "ff4fe": [
        "ff4fe"
    ],
    "final fantasy ii": [
        "ff4fe"
    ],
    "ffmq": [
        "ffmq"
    ],
    "final fantasy: mystic quest": [
        "ffmq"
    ],
    "fantasy:": [
        "ffmq"
    ],
    "mystic": [
        "ffmq"
    ],
    "casual": [
        "placidplasticducksim",
        "sims4",
        "ffmq",
        "shorthike",
        "musedash",
        "getting_over_it"
    ],
    "ninja": [
        "ffta",
        "rogue_legacy",
        "ffmq",
        "messenger"
    ],
    "ffta": [
        "ffta"
    ],
    "final fantasy tactics advance": [
        "ffta"
    ],
    "tactics": [
        "ffta"
    ],
    "tactical": [
        "ffta",
        "wargroove",
        "overcooked2"
    ],
    "grinding": [
        "ffta",
        "seaofthieves",
        "kh1",
        "tloz_oos",
        "osrs"
    ],
    "random encounter": [
        "ffta",
        "kh1",
        "pokemon_emerald",
        "pokemon_crystal",
        "gstla"
    ],
    "random": [
        "ffta",
        "kh1",
        "pokemon_emerald",
        "pokemon_crystal",
        "gstla"
    ],
    "encounter": [
        "ffta",
        "kh1",
        "pokemon_emerald",
        "pokemon_crystal",
        "gstla"
    ],
    "fm": [
        "fm"
    ],
    "yu-gi-oh! forbidden memories": [
        "fm"
    ],
    "yu-gi-oh!": [
        "yugiohddm",
        "yugioh06",
        "fm"
    ],
    "forbidden": [
        "fm"
    ],
    "memories": [
        "fm"
    ],
    "generic": [
        "generic"
    ],
    "getting_over_it": [
        "getting_over_it"
    ],
    "getting over it with bennett foddy": [
        "getting_over_it"
    ],
    "getting": [
        "getting_over_it"
    ],
    "it": [
        "getting_over_it"
    ],
    "with": [
        "getting_over_it"
    ],
    "bennett": [
        "getting_over_it"
    ],
    "foddy": [
        "getting_over_it"
    ],
    "psychological horror": [
        "getting_over_it",
        "lethal_company",
        "mm_recomp",
        "undertale"
    ],
    "psychological": [
        "getting_over_it",
        "lethal_company",
        "mm_recomp",
        "undertale"
    ],
    "gstla": [
        "gstla"
    ],
    "golden sun: the lost age": [
        "gstla"
    ],
    "golden": [
        "marioland2",
        "gstla"
    ],
    "sun:": [
        "gstla"
    ],
    "lost": [
        "gstla"
    ],
    "ancient advanced civilization technology": [
        "jakanddaxter",
        "metroidprime",
        "gstla",
        "ss"
    ],
    "ancient": [
        "jakanddaxter",
        "metroidprime",
        "gstla",
        "ss"
    ],
    "advanced": [
        "jakanddaxter",
        "metroidprime",
        "gstla",
        "ss"
    ],
    "technology": [
        "jakanddaxter",
        "metroidprime",
        "gstla",
        "ss"
    ],
    "battle screen": [
        "papermario",
        "pokemon_emerald",
        "pokemon_crystal",
        "mlss",
        "gstla"
    ],
    "battle": [
        "papermario",
        "pokemon_emerald",
        "mmbn3",
        "sa2b",
        "pokemon_crystal",
        "mlss",
        "gstla"
    ],
    "screen": [
        "papermario",
        "pokemon_emerald",
        "pokemon_crystal",
        "mlss",
        "gstla"
    ],
    "gzdoom": [
        "gzdoom"
    ],
    "gzdoom sm64": [
        "gzdoom"
    ],
    "sm64": [
        "gzdoom"
    ],
    "hades": [
        "hades"
    ],
    "stylized": [
        "tunic",
        "hcniko",
        "hades",
        "hylics2",
        "ultrakill"
    ],
    "hcniko": [
        "hcniko"
    ],
    "here comes niko!": [
        "hcniko"
    ],
    "comes": [
        "hcniko"
    ],
    "niko!": [
        "hcniko"
    ],
    "fishing": [
        "ladx",
        "minecraft",
        "shorthike",
        "hcniko",
        "terraria",
        "stardew_valley"
    ],
    "heretic": [
        "heretic"
    ],
    "hk": [
        "hk"
    ],
    "hollow knight": [
        "hk"
    ],
    "hollow": [
        "hk"
    ],
    "knight": [
        "hk"
    ],
    "creature compendium": [
        "metroidprime",
        "hk",
        "sotn",
        "pokemon_emerald"
    ],
    "creature": [
        "metroidprime",
        "hk",
        "sotn",
        "pokemon_emerald"
    ],
    "compendium": [
        "metroidprime",
        "hk",
        "sotn",
        "pokemon_emerald"
    ],
    "huniepop": [
        "huniepop",
        "huniepop2"
    ],
    "visual novel": [
        "huniepop",
        "huniepop2"
    ],
    "visual": [
        "huniepop",
        "huniepop2"
    ],
    "novel": [
        "huniepop",
        "huniepop2"
    ],
    "erotic": [
        "huniepop",
        "huniepop2"
    ],
    "romance": [
        "huniepop",
        "stardew_valley",
        "huniepop2",
        "sims4"
    ],
    "huniepop2": [
        "huniepop2"
    ],
    "huniepop 2: double date": [
        "huniepop2"
    ],
    "date": [
        "huniepop2"
    ],
    "hylics2": [
        "hylics2"
    ],
    "hylics 2": [
        "hylics2"
    ],
    "hylics": [
        "hylics2"
    ],
    "inscryption": [
        "inscryption"
    ],
    "jakanddaxter": [
        "jakanddaxter"
    ],
    "jak and daxter: the precursor legacy": [
        "jakanddaxter"
    ],
    "jak": [
        "jakanddaxter"
    ],
    "daxter:": [
        "jakanddaxter"
    ],
    "precursor": [
        "jakanddaxter"
    ],
    "legacy": [
        "jakanddaxter",
        "rogue_legacy"
    ],
    "language selection": [
        "jakanddaxter",
        "sly1",
        "minecraft",
        "yugiohddm"
    ],
    "language": [
        "jakanddaxter",
        "sly1",
        "minecraft",
        "yugiohddm"
    ],
    "selection": [
        "jakanddaxter",
        "sly1",
        "minecraft",
        "yugiohddm"
    ],
    "auto-saving": [
        "jakanddaxter",
        "spyro3",
        "witness",
        "minecraft"
    ],
    "jigsaw": [
        "jigsaw"
    ],
    "k64": [
        "k64"
    ],
    "kirby 64: the crystal shards": [
        "k64"
    ],
    "kirby": [
        "k64"
    ],
    "crystal": [
        "pokemon_crystal",
        "k64"
    ],
    "shards": [
        "k64"
    ],
    "kid friendly": [
        "pokemon_crystal",
        "pokemon_emerald",
        "openrct2",
        "k64"
    ],
    "kid": [
        "pokemon_crystal",
        "pokemon_emerald",
        "openrct2",
        "k64"
    ],
    "friendly": [
        "sims4",
        "tunic",
        "k64",
        "pokemon_emerald",
        "shorthike",
        "pokemon_crystal",
        "powerwashsimulator",
        "openrct2"
    ],
    "whale": [
        "marioland2",
        "kh1",
        "kdl3",
        "k64"
    ],
    "kdl3": [
        "kdl3"
    ],
    "kirby's dream land 3": [
        "kdl3"
    ],
    "kirby's": [
        "kdl3"
    ],
    "dream": [
        "kdl3"
    ],
    "land": [
        "marioland2",
        "wl",
        "kdl3",
        "wl4"
    ],
    "kh1": [
        "kh1"
    ],
    "kingdom hearts": [
        "kh1"
    ],
    "kingdom": [
        "kh1",
        "kh2"
    ],
    "hearts": [
        "kh1",
        "kh2"
    ],
    "kh2": [
        "kh2"
    ],
    "kingdom hearts ii": [
        "kh2"
    ],
    "ladx": [
        "ladx"
    ],
    "the legend of zelda: link's awakening dx": [
        "ladx"
    ],
    "link's": [
        "ladx"
    ],
    "awakening": [
        "ladx"
    ],
    "dx": [
        "ladx",
        "sadx"
    ],
    "game boy color": [
        "ladx",
        "tloz_oos",
        "tloz_ooa",
        "pokemon_crystal"
    ],
    "color": [
        "ladx",
        "tloz_oos",
        "tloz_ooa",
        "pokemon_crystal"
    ],
    "chicken": [
        "ladx",
        "minecraft",
        "oot",
        "stardew_valley"
    ],
    "tentacles": [
        "ladx",
        "papermario",
        "pokemon_emerald",
        "metroidprime",
        "sms",
        "pokemon_crystal",
        "mlss"
    ],
    "animal cruelty": [
        "ladx",
        "pokemon_emerald",
        "oot",
        "pokemon_crystal"
    ],
    "cruelty": [
        "ladx",
        "pokemon_emerald",
        "oot",
        "pokemon_crystal"
    ],
    "landstalker": [
        "landstalker"
    ],
    "sega mega drive/genesis": [
        "landstalker"
    ],
    "sega": [
        "zillion",
        "landstalker"
    ],
    "mega": [
        "mm2",
        "landstalker",
        "mmbn3",
        "megamix"
    ],
    "drive/genesis": [
        "landstalker"
    ],
    "lethal_company": [
        "lethal_company"
    ],
    "lethal company": [
        "lethal_company"
    ],
    "lethal": [
        "lethal_company"
    ],
    "company": [
        "lethal_company"
    ],
    "monsters": [
        "yugiohddm",
        "yugioh06",
        "minecraft",
        "pokemon_frlg",
        "lethal_company",
        "stardew_valley"
    ],
    "lingo": [
        "lingo"
    ],
    "lufia2ac": [
        "lufia2ac"
    ],
    "lufia ii: rise of the sinistrals": [
        "lufia2ac"
    ],
    "lufia": [
        "lufia2ac"
    ],
    "rise": [
        "lufia2ac"
    ],
    "sinistrals": [
        "lufia2ac"
    ],
    "luigismansion": [
        "luigismansion"
    ],
    "luigi's mansion": [
        "luigismansion"
    ],
    "luigi's": [
        "luigismansion"
    ],
    "mansion": [
        "luigismansion"
    ],
    "italian accent": [
        "luigismansion",
        "mk64",
        "mlss",
        "sms"
    ],
    "italian": [
        "luigismansion",
        "mk64",
        "mlss",
        "sms"
    ],
    "accent": [
        "luigismansion",
        "mk64",
        "mlss",
        "sms"
    ],
    "marioland2": [
        "marioland2"
    ],
    "super mario land 2: 6 golden coins": [
        "marioland2"
    ],
    "mario": [
        "papermario",
        "sm64ex",
        "yoshisisland",
        "marioland2",
        "sms",
        "mk64",
        "smo",
        "mlss",
        "mario_kart_double_dash",
        "smw",
        "sm64hacks",
        "wl"
    ],
    "6": [
        "marioland2"
    ],
    "coins": [
        "marioland2"
    ],
    "game boy": [
        "wl",
        "marioland2",
        "mm2",
        "pokemon_rb"
    ],
    "turtle": [
        "papermario",
        "marioland2",
        "sms",
        "mk64",
        "mlss",
        "sly1"
    ],
    "mario_kart_double_dash": [
        "mario_kart_double_dash"
    ],
    "mario kart: double dash!!": [
        "mario_kart_double_dash"
    ],
    "kart:": [
        "mario_kart_double_dash"
    ],
    "dash!!": [
        "mario_kart_double_dash"
    ],
    "yoshi": [
        "yoshisisland",
        "mario_kart_double_dash",
        "sms",
        "smw"
    ],
    "princess peach": [
        "sm64ex",
        "sms",
        "mlss",
        "mario_kart_double_dash",
        "sm64hacks"
    ],
    "peach": [
        "sm64ex",
        "sms",
        "mlss",
        "mario_kart_double_dash",
        "sm64hacks"
    ],
    "megamix": [
        "megamix"
    ],
    "hatsune miku: project diva mega mix": [
        "megamix"
    ],
    "hatsune": [
        "megamix"
    ],
    "miku:": [
        "megamix"
    ],
    "project": [
        "megamix"
    ],
    "diva": [
        "megamix"
    ],
    "mix": [
        "megamix"
    ],
    "meritous": [
        "meritous"
    ],
    "messenger": [
        "messenger"
    ],
    "the messenger": [
        "messenger"
    ],
    "metroidprime": [
        "metroidprime"
    ],
    "metroid prime": [
        "metroidprime"
    ],
    "metroid": [
        "sm",
        "metroidprime",
        "sm_map_rando",
        "smz3"
    ],
    "prime": [
        "metroidprime"
    ],
    "time limit": [
        "rogue_legacy",
        "ror1",
        "sm",
        "metroidprime",
        "sms",
        "witness",
        "sm_map_rando",
        "wl4"
    ],
    "limit": [
        "rogue_legacy",
        "ror1",
        "sm",
        "metroidprime",
        "sms",
        "witness",
        "sm_map_rando",
        "wl4"
    ],
    "countdown timer": [
        "rogue_legacy",
        "oot",
        "sm",
        "metroidprime",
        "mzm",
        "sm_map_rando",
        "wl4"
    ],
    "countdown": [
        "rogue_legacy",
        "oot",
        "sm",
        "metroidprime",
        "mzm",
        "sm_map_rando",
        "wl4"
    ],
    "timer": [
        "rogue_legacy",
        "oot",
        "sm",
        "metroidprime",
        "mzm",
        "sm_map_rando",
        "wl4"
    ],
    "auto-aim": [
        "mm_recomp",
        "tww",
        "oot",
        "metroidprime",
        "ss"
    ],
    "linear gameplay": [
        "sm64hacks",
        "metroidprime",
        "sms",
        "sm64ex"
    ],
    "linear": [
        "sm64hacks",
        "metroidprime",
        "sms",
        "sm64ex"
    ],
    "meme origin": [
        "mm_recomp",
        "minecraft",
        "metroidprime",
        "zelda2",
        "star_fox_64",
        "sotn",
        "tloz"
    ],
    "meme": [
        "mm_recomp",
        "minecraft",
        "metroidprime",
        "zelda2",
        "star_fox_64",
        "sotn",
        "tloz"
    ],
    "origin": [
        "mm_recomp",
        "minecraft",
        "metroidprime",
        "zelda2",
        "star_fox_64",
        "sotn",
        "tloz"
    ],
    "isolation": [
        "sm",
        "metroidprime",
        "mzm",
        "sotn",
        "sm_map_rando"
    ],
    "minecraft": [
        "minecraft"
    ],
    "minecraft: java edition": [
        "minecraft"
    ],
    "minecraft:": [
        "minecraft"
    ],
    "java": [
        "minecraft"
    ],
    "virtual reality": [
        "subnautica",
        "minecraft"
    ],
    "virtual": [
        "subnautica",
        "minecraft"
    ],
    "reality": [
        "subnautica",
        "minecraft"
    ],
    "procedural generation": [
        "witness",
        "rogue_legacy",
        "minecraft",
        "terraria"
    ],
    "procedural": [
        "witness",
        "rogue_legacy",
        "minecraft",
        "terraria"
    ],
    "generation": [
        "witness",
        "rogue_legacy",
        "minecraft",
        "terraria"
    ],
    "mk64": [
        "mk64"
    ],
    "mario kart 64": [
        "mk64"
    ],
    "kart": [
        "mk64"
    ],
    "mlss": [
        "mlss"
    ],
    "mario & luigi: superstar saga": [
        "mlss"
    ],
    "luigi:": [
        "mlss"
    ],
    "superstar": [
        "mlss"
    ],
    "saga": [
        "mlss"
    ],
    "super-ness": [
        "sm64hacks",
        "mlss",
        "sms",
        "sm64ex"
    ],
    "wiggler": [
        "sm64ex",
        "sms",
        "smo",
        "mlss",
        "sm64hacks"
    ],
    "mm2": [
        "mm2"
    ],
    "mega man ii": [
        "mm2"
    ],
    "man": [
        "mmbn3",
        "mm2"
    ],
    "mmbn3": [
        "mmbn3"
    ],
    "mega man battle network 3 blue": [
        "mmbn3"
    ],
    "network": [
        "mmbn3"
    ],
    "blue": [
        "mmbn3"
    ],
    "mm_recomp": [
        "mm_recomp"
    ],
    "the legend of zelda: majora's mask": [
        "mm_recomp"
    ],
    "majora's": [
        "mm_recomp"
    ],
    "mask": [
        "mm_recomp"
    ],
    "64dd": [
        "mm_recomp",
        "oot"
    ],
    "momodoramoonlitfarewell": [
        "momodoramoonlitfarewell"
    ],
    "momodora: moonlit farewell": [
        "momodoramoonlitfarewell"
    ],
    "momodora:": [
        "momodoramoonlitfarewell"
    ],
    "moonlit": [
        "momodoramoonlitfarewell"
    ],
    "farewell": [
        "momodoramoonlitfarewell"
    ],
    "monster_sanctuary": [
        "monster_sanctuary"
    ],
    "monster sanctuary": [
        "monster_sanctuary"
    ],
    "monster": [
        "monster_sanctuary"
    ],
    "sanctuary": [
        "monster_sanctuary"
    ],
    "musedash": [
        "musedash"
    ],
    "muse dash": [
        "musedash"
    ],
    "muse": [
        "musedash"
    ],
    "dash": [
        "musedash"
    ],
    "mzm": [
        "mzm"
    ],
    "metroid: zero mission": [
        "mzm"
    ],
    "metroid:": [
        "mzm"
    ],
    "zero": [
        "mzm"
    ],
    "mission": [
        "mzm"
    ],
    "noita": [
        "noita"
    ],
    "oot": [
        "oot"
    ],
    "the legend of zelda: ocarina of time": [
        "oot"
    ],
    "ocarina": [
        "oot"
    ],
    "time manipulation": [
        "rogue_legacy",
        "oot",
        "sm",
        "timespinner",
        "sm_map_rando"
    ],
    "openrct2": [
        "openrct2"
    ],
    "business": [
        "stardew_valley",
        "powerwashsimulator",
        "openrct2"
    ],
    "oribf": [
        "oribf"
    ],
    "ori and the blind forest": [
        "oribf"
    ],
    "ori": [
        "oribf"
    ],
    "blind": [
        "oribf"
    ],
    "thriller": [
        "sm",
        "oribf",
        "sm_map_rando"
    ],
    "osrs": [
        "osrs"
    ],
    "old school runescape": [
        "osrs"
    ],
    "old": [
        "osrs"
    ],
    "school": [
        "osrs"
    ],
    "runescape": [
        "osrs"
    ],
    "osu": [
        "osu"
    ],
    "osu!": [
        "osu"
    ],
    "auditory": [
        "osu"
    ],
    "outer_wilds": [
        "outer_wilds"
    ],
    "outer wilds": [
        "outer_wilds"
    ],
    "outer": [
        "outer_wilds"
    ],
    "wilds": [
        "outer_wilds"
    ],
    "overcooked2": [
        "overcooked2"
    ],
    "overcooked! 2": [
        "overcooked2"
    ],
    "overcooked!": [
        "overcooked2"
    ],
    "paint": [
        "paint"
    ],
    "papermario": [
        "papermario"
    ],
    "paper mario": [
        "papermario"
    ],
    "paper": [
        "ttyd",
        "papermario"
    ],
    "gambling": [
        "pokemon_crystal",
        "pokemon_emerald",
        "papermario",
        "rogue_legacy"
    ],
    "peaks_of_yore": [
        "peaks_of_yore"
    ],
    "peaks of yore": [
        "peaks_of_yore"
    ],
    "peaks": [
        "peaks_of_yore"
    ],
    "yore": [
        "peaks_of_yore"
    ],
    "placidplasticducksim": [
        "placidplasticducksim"
    ],
    "placid plastic duck simulator": [
        "placidplasticducksim"
    ],
    "placid": [
        "placidplasticducksim"
    ],
    "plastic": [
        "placidplasticducksim"
    ],
    "duck": [
        "placidplasticducksim"
    ],
    "pmd_eos": [
        "pmd_eos"
    ],
    "pok\u00e9mon mystery dungeon: explorers of sky": [
        "pmd_eos"
    ],
    "pok\u00e9mon": [
        "pmd_eos",
        "pokemon_rb",
        "pokemon_emerald",
        "pokemon_frlg",
        "pokemon_crystal"
    ],
    "dungeon:": [
        "pmd_eos"
    ],
    "explorers": [
        "pmd_eos"
    ],
    "sky": [
        "pmd_eos"
    ],
    "pokemon_crystal": [
        "pokemon_crystal"
    ],
    "pok\u00e9mon crystal version": [
        "pokemon_crystal"
    ],
    "pokemon_emerald": [
        "pokemon_emerald"
    ],
    "pok\u00e9mon emerald version": [
        "pokemon_emerald"
    ],
    "emerald": [
        "pokemon_emerald"
    ],
    "pokemon_frlg": [
        "pokemon_frlg"
    ],
    "pok\u00e9mon leafgreen version": [
        "pokemon_frlg"
    ],
    "leafgreen": [
        "pokemon_frlg"
    ],
    "pokemon_rb": [
        "pokemon_rb"
    ],
    "pok\u00e9mon red version": [
        "pokemon_rb"
    ],
    "red": [
        "pokemon_rb"
    ],
    "powerwashsimulator": [
        "powerwashsimulator"
    ],
    "powerwash simulator": [
        "powerwashsimulator"
    ],
    "powerwash": [
        "powerwashsimulator"
    ],
    "family friendly": [
        "shorthike",
        "powerwashsimulator",
        "sims4",
        "tunic"
    ],
    "pseudoregalia": [
        "pseudoregalia"
    ],
    "pseudoregalia: jam ver.": [
        "pseudoregalia"
    ],
    "pseudoregalia:": [
        "pseudoregalia"
    ],
    "jam": [
        "pseudoregalia"
    ],
    "ver.": [
        "pseudoregalia"
    ],
    "rac2": [
        "rac2"
    ],
    "ratchet & clank: going commando": [
        "rac2"
    ],
    "ratchet": [
        "rac2"
    ],
    "clank:": [
        "rac2"
    ],
    "going": [
        "rac2"
    ],
    "commando": [
        "rac2"
    ],
    "raft": [
        "raft"
    ],
    "residentevil2remake": [
        "residentevil2remake"
    ],
    "resident evil 2": [
        "residentevil2remake"
    ],
    "resident": [
        "residentevil3remake",
        "residentevil2remake"
    ],
    "evil": [
        "residentevil3remake",
        "residentevil2remake"
    ],
    "residentevil3remake": [
        "residentevil3remake"
    ],
    "resident evil 3": [
        "residentevil3remake"
    ],
    "rimworld": [
        "rimworld"
    ],
    "rogue_legacy": [
        "rogue_legacy"
    ],
    "rogue legacy": [
        "rogue_legacy"
    ],
    "rogue": [
        "rogue_legacy"
    ],
    "playstation vita": [
        "rogue_legacy",
        "ror1",
        "terraria",
        "timespinner",
        "undertale",
        "v6",
        "stardew_valley"
    ],
    "vita": [
        "rogue_legacy",
        "ror1",
        "terraria",
        "timespinner",
        "undertale",
        "v6",
        "stardew_valley"
    ],
    "ror1": [
        "ror1"
    ],
    "risk of rain": [
        "ror1"
    ],
    "risk": [
        "ror1",
        "ror2"
    ],
    "rain": [
        "ror1",
        "ror2"
    ],
    "ror2": [
        "ror2"
    ],
    "risk of rain 2": [
        "ror2"
    ],
    "sa2b": [
        "sa2b"
    ],
    "sonic adventure 2: battle": [
        "sa2b"
    ],
    "sonic": [
        "sadx",
        "sonic_heroes",
        "sa2b"
    ],
    "sadx": [
        "sadx"
    ],
    "sonic adventure: sonic adventure dx upgrade": [
        "sadx"
    ],
    "adventure:": [
        "sadx"
    ],
    "upgrade": [
        "sadx"
    ],
    "satisfactory": [
        "satisfactory"
    ],
    "saving_princess": [
        "saving_princess"
    ],
    "sc2": [
        "sc2"
    ],
    "starcraft ii: wings of liberty": [
        "sc2"
    ],
    "starcraft": [
        "sc2"
    ],
    "wings": [
        "sc2"
    ],
    "liberty": [
        "sc2"
    ],
    "warfare": [
        "wargroove",
        "wargroove2",
        "sc2"
    ],
    "seaofthieves": [
        "seaofthieves"
    ],
    "sea of thieves": [
        "seaofthieves"
    ],
    "sea": [
        "seaofthieves"
    ],
    "thieves": [
        "seaofthieves"
    ],
    "shapez": [
        "shapez"
    ],
    "shivers": [
        "shivers"
    ],
    "point-and-click": [
        "zork_grand_inquisitor",
        "shivers"
    ],
    "shorthike": [
        "shorthike"
    ],
    "a short hike": [
        "shorthike"
    ],
    "short": [
        "shorthike"
    ],
    "hike": [
        "shorthike"
    ],
    "sims4": [
        "sims4"
    ],
    "the sims 4": [
        "sims4"
    ],
    "sims": [
        "sims4"
    ],
    "sly1": [
        "sly1"
    ],
    "sly cooper and the thievius raccoonus": [
        "sly1"
    ],
    "sly": [
        "sly1"
    ],
    "cooper": [
        "sly1"
    ],
    "thievius": [
        "sly1"
    ],
    "raccoonus": [
        "sly1"
    ],
    "stealth": [
        "sly1"
    ],
    "sm": [
        "sm"
    ],
    "super metroid": [
        "sm",
        "sm_map_rando"
    ],
    "sm64ex": [
        "sm64ex"
    ],
    "super mario 64": [
        "sm64hacks",
        "sm64ex"
    ],
    "rabbit": [
        "sm64ex",
        "terraria",
        "smo",
        "sm64hacks",
        "sonic_heroes",
        "tloz_ooa"
    ],
    "sm64hacks": [
        "sm64hacks"
    ],
    "smo": [
        "smo"
    ],
    "super mario odyssey": [
        "smo"
    ],
    "odyssey": [
        "smo"
    ],
    "nintendo switch 2": [
        "smo"
    ],
    "sms": [
        "sms"
    ],
    "super mario sunshine": [
        "sms"
    ],
    "sunshine": [
        "sms"
    ],
    "smw": [
        "smw"
    ],
    "super mario world": [
        "smw"
    ],
    "smz3": [
        "smz3"
    ],
    "super metroid and a link to the past crossover randomizer": [
        "smz3"
    ],
    "randomizer": [
        "smz3"
    ],
    "sm_map_rando": [
        "sm_map_rando"
    ],
    "soe": [
        "soe"
    ],
    "secret of evermore": [
        "soe"
    ],
    "evermore": [
        "soe"
    ],
    "sonic_heroes": [
        "sonic_heroes"
    ],
    "sonic heroes": [
        "sonic_heroes"
    ],
    "heroes": [
        "sonic_heroes"
    ],
    "sotn": [
        "sotn"
    ],
    "castlevania: symphony of the night": [
        "sotn"
    ],
    "symphony": [
        "sotn"
    ],
    "night": [
        "sotn"
    ],
    "spire": [
        "spire"
    ],
    "slay the spire ii": [
        "spire"
    ],
    "slay": [
        "spire"
    ],
    "spyro3": [
        "spyro3"
    ],
    "spyro: year of the dragon": [
        "spyro3"
    ],
    "spyro:": [
        "spyro3"
    ],
    "year": [
        "spyro3"
    ],
    "dragon": [
        "spyro3"
    ],
    "ss": [
        "ss"
    ],
    "the legend of zelda: skyward sword": [
        "ss"
    ],
    "skyward": [
        "ss"
    ],
    "stardew_valley": [
        "stardew_valley"
    ],
    "stardew valley": [
        "stardew_valley"
    ],
    "stardew": [
        "stardew_valley"
    ],
    "valley": [
        "stardew_valley"
    ],
    "star_fox_64": [
        "star_fox_64"
    ],
    "star fox 64": [
        "star_fox_64"
    ],
    "star": [
        "swr",
        "star_fox_64"
    ],
    "fox": [
        "star_fox_64"
    ],
    "subnautica": [
        "subnautica"
    ],
    "steamvr": [
        "subnautica"
    ],
    "oculus rift": [
        "subnautica"
    ],
    "oculus": [
        "subnautica"
    ],
    "rift": [
        "subnautica"
    ],
    "swr": [
        "swr"
    ],
    "star wars: episode i - racer": [
        "swr"
    ],
    "wars:": [
        "swr"
    ],
    "episode": [
        "swr"
    ],
    "i": [
        "swr"
    ],
    "-": [
        "swr"
    ],
    "racer": [
        "swr"
    ],
    "dreamcast": [
        "swr"
    ],
    "tboir": [
        "tboir"
    ],
    "the binding of isaac: repentance": [
        "tboir"
    ],
    "binding": [
        "tboir"
    ],
    "isaac:": [
        "tboir"
    ],
    "repentance": [
        "tboir"
    ],
    "terraria": [
        "terraria"
    ],
    "windows phone": [
        "terraria"
    ],
    "phone": [
        "terraria"
    ],
    "tetrisattack": [
        "tetrisattack"
    ],
    "tetris attack": [
        "tetrisattack"
    ],
    "tetris": [
        "tetrisattack"
    ],
    "attack": [
        "tetrisattack"
    ],
    "timespinner": [
        "timespinner"
    ],
    "tloz": [
        "tloz"
    ],
    "the legend of zelda": [
        "tloz"
    ],
    "family computer disk system": [
        "tloz",
        "zelda2"
    ],
    "disk": [
        "tloz",
        "zelda2"
    ],
    "tloz_ooa": [
        "tloz_ooa"
    ],
    "the legend of zelda: oracle of ages": [
        "tloz_ooa"
    ],
    "oracle": [
        "tloz_ooa",
        "tloz_oos"
    ],
    "ages": [
        "tloz_ooa"
    ],
    "tloz_oos": [
        "tloz_oos"
    ],
    "the legend of zelda: oracle of seasons": [
        "tloz_oos"
    ],
    "seasons": [
        "tloz_oos"
    ],
    "toontown": [
        "toontown"
    ],
    "toontown online": [
        "toontown"
    ],
    "online": [
        "toontown"
    ],
    "tp": [
        "tp"
    ],
    "the legend of zelda: twilight princess": [
        "tp"
    ],
    "twilight": [
        "tp"
    ],
    "tracker": [
        "tracker"
    ],
    "trackmania": [
        "trackmania"
    ],
    "ttyd": [
        "ttyd"
    ],
    "paper mario: the thousand-year door": [
        "ttyd"
    ],
    "mario:": [
        "ttyd"
    ],
    "thousand-year": [
        "ttyd"
    ],
    "door": [
        "ttyd"
    ],
    "tunic": [
        "tunic"
    ],
    "tww": [
        "tww"
    ],
    "the legend of zelda: the wind waker": [
        "tww"
    ],
    "wind": [
        "tww"
    ],
    "waker": [
        "tww"
    ],
    "tyrian": [
        "tyrian"
    ],
    "tyrian 2000": [
        "tyrian"
    ],
    "2000": [
        "tyrian"
    ],
    "ufo50": [
        "ufo50"
    ],
    "ufo 50": [
        "ufo50"
    ],
    "ufo": [
        "ufo50"
    ],
    "50": [
        "ufo50"
    ],
    "ultrakill": [
        "ultrakill"
    ],
    "undertale": [
        "undertale"
    ],
    "v6": [
        "v6"
    ],
    "vvvvvv": [
        "v6"
    ],
    "ouya": [
        "v6"
    ],
    "wargroove": [
        "wargroove",
        "wargroove2"
    ],
    "wargroove2": [
        "wargroove2"
    ],
    "wargroove 2": [
        "wargroove2"
    ],
    "witness": [
        "witness"
    ],
    "the witness": [
        "witness"
    ],
    "wl": [
        "wl"
    ],
    "wario land: super mario land 3": [
        "wl"
    ],
    "wario": [
        "wl",
        "wl4"
    ],
    "land:": [
        "wl"
    ],
    "wl4": [
        "wl4"
    ],
    "wario land 4": [
        "wl4"
    ],
    "wordipelago": [
        "wordipelago"
    ],
    "xenobladex": [
        "xenobladex"
    ],
    "xenoblade chronicles x": [
        "xenobladex"
    ],
    "xenoblade": [
        "xenobladex"
    ],
    "chronicles": [
        "xenobladex"
    ],
    "x": [
        "xenobladex"
    ],
    "yachtdice": [
        "yachtdice"
    ],
    "yoshisisland": [
        "yoshisisland"
    ],
    "super mario world 2: yoshi's island": [
        "yoshisisland"
    ],
    "yoshi's": [
        "yoshisisland"
    ],
    "island": [
        "yoshisisland"
    ],
    "yugioh06": [
        "yugioh06"
    ],
    "yu-gi-oh! ultimate masters: world championship tournament 2006": [
        "yugioh06"
    ],
    "ultimate": [
        "yugioh06"
    ],
    "masters:": [
        "yugioh06"
    ],
    "championship": [
        "yugioh06"
    ],
    "tournament": [
        "yugioh06"
    ],
    "2006": [
        "yugioh06"
    ],
    "yugiohddm": [
        "yugiohddm"
    ],
    "yu-gi-oh! dungeon dice monsters": [
        "yugiohddm"
    ],
    "dice": [
        "yugiohddm"
    ],
    "zelda2": [
        "zelda2"
    ],
    "zelda ii: the adventure of link": [
        "zelda2"
    ],
    "zillion": [
        "zillion"
    ],
    "sega master system/mark iii": [
        "zillion"
    ],
    "master": [
        "zillion"
    ],
    "system/mark": [
        "zillion"
    ],
    "zork_grand_inquisitor": [
        "zork_grand_inquisitor"
    ],
    "zork: grand inquisitor": [
        "zork_grand_inquisitor"
    ],
    "zork:": [
        "zork_grand_inquisitor"
    ],
    "grand": [
        "zork_grand_inquisitor"
    ],
    "inquisitor": [
        "zork_grand_inquisitor"
    ]
} # type: ignore