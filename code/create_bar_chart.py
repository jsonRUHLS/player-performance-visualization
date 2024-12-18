import pandas as pd
import matplotlib.pyplot as plt

def create_bar_chart():
    """Creates a bar chart for performance per game."""
    # Load the dataset
    data_path = "../data/player_performance.csv"
    data = pd.read_csv(data_path)

    # Extract metadata
    sport = data["Sport"].iloc[0]
    league = data["League"].iloc[0]
    team = data["Team"].iloc[0]
    player = data["Player"].iloc[0]

    metric = "Touchdowns" if sport.lower() == "football" else "Goals"

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(data["Game"], data[metric], color='skyblue', alpha=0.8)
    plt.title(f"{player}'s {metric} Per Game ({team}, {league}, {sport})", fontsize=14)
    plt.xlabel("Game", fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the plot
    chart_path = f"../charts/{sport}_{league}_{team}_{player}_{metric.lower()}_per_game.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Bar chart saved to {chart_path}")

if __name__ == "__main__":
    create_bar_chart()
