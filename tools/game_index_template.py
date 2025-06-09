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
        
        # Get initial set of matching games
        for term in query_terms:
            for indexed_term, games in self.search_index.items():
                if term in indexed_term:
                    if not matching_games:
                        matching_games = games.copy()
                    else:
                        matching_games &= games
        
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
GAMES_DATA = {GAMES_DATA_PLACEHOLDER}

SEARCH_INDEX = {SEARCH_INDEX_PLACEHOLDER} 