import pandas as pd
import random

def generate_mock_data():
    """Generates a mock dataset for player performance."""
    games = [f"Game {i+1}" for i in range(10)]
    goals = [random.randint(0, 3) for _ in range(10)]
    milestones = ["Yes" if g >= 2 else "No" for g in goals]

    data = pd.DataFrame({
        "Game": games,
        "Goals": goals,
        "Milestone": milestones
    })

    data.to_csv("../data/player_performance.csv", index=False)
    print("Mock data saved to ../data/player_performance.csv")

if __name__ == "__main__":
    generate_mock_data()
