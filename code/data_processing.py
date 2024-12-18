import pandas as pd
import random

def generate_mock_data(sport, league, team, player):
    """Generates a mock dataset for player performance."""
    games = [f"Game {i+1}" for i in range(10)]
    if sport.lower() == "football":
        touchdowns = [random.randint(0, 3) for _ in range(10)]
        milestones = ["Yes" if t >= 2 else "No" for t in touchdowns]
        data = pd.DataFrame({
            "Sport": [sport] * 10,
            "League": [league] * 10,
            "Team": [team] * 10,
            "Player": [player] * 10,
            "Game": games,
            "Touchdowns": touchdowns,
            "Milestone": milestones
        })
    else:
        goals = [random.randint(0, 3) for _ in range(10)]
        milestones = ["Yes" if g >= 2 else "No" for g in goals]
        data = pd.DataFrame({
            "Sport": [sport] * 10,
            "League": [league] * 10,
            "Team": [team] * 10,
            "Player": [player] * 10,
            "Game": games,
            "Goals": goals,
            "Milestone": milestones
        })

    data.to_csv("../data/player_performance.csv", index=False)
    print(f"Mock data for {player} ({team}, {league}, {sport}) saved to ../data/player_performance.csv")

if __name__ == "__main__":
    # Accept inputs for sport type, league, team name, and player name
    sport = input("Enter the sport type (e.g., Soccer, Basketball, Football): ")
    league = input("Enter the league name (e.g., Premier League, NFL): ")
    team = input("Enter the team name: ")
    player = input("Enter the player's name: ")

    generate_mock_data(sport, league, team, player)
