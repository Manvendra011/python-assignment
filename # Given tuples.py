# Given tuples
gamesRamesh = ('lawn tennis', 'cricket')
gamesSuresh = ('cricket', 'hockey', 'badminton')

# Games played by Suresh but not Ramesh
games_only_suresh = tuple(game for game in gamesSuresh if game not in gamesRamesh)

# Games that are common to both of them
common_games = tuple(set(gamesRamesh) & set(gamesSuresh))

# All games played by either of them
all_games = tuple(set(gamesRamesh) | set(gamesSuresh))

# Games that are not common to both of them
games_not_common = tuple(set(gamesRamesh) ^ set(gamesSuresh))

# Print the results
print("Games played by Suresh but not Ramesh:", games_only_suresh)
print("Games that are common to both of them:", common_games)
print("All games played by either of them:", all_games)
print("Games that are not common to both of them:", games_not_common)
