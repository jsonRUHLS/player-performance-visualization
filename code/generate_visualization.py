import pandas as pd
import matplotlib.pyplot as plt

def create_visualization():
    """Creates a line chart for player performance trends."""
    # Load the dataset
    data_path = "../data/player_performance.csv"
    data = pd.read_csv(data_path)

    # Extract metadata
    sport = data["Sport"].iloc[0]
    league = data["League"].iloc[0]
    team = data["Team"].iloc[0]
    player = data["Player"].iloc[0]

    # Determine the metric (Touchdowns for Football, Goals otherwise)
    metric = "Touchdowns" if sport.lower() == "football" else "Goals"

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(data["Game"], data[metric], marker='o', label=f"{metric} Scored")
    plt.axhline(y=data[metric].mean(), color='r', linestyle='--', label=f"Average {metric}")
    plt.title(f"{player}'s Performance: {team} ({league}, {sport})", fontsize=14)
    plt.xlabel("Game", fontsize=12)
    plt.ylabel(f"{metric} Scored", fontsize=12)
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    chart_path = f"../charts/{sport}_{league}_{team}_{player}_{metric.lower()}_performance.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Visualization saved to {chart_path}")

if __name__ == "__main__":
    create_visualization()
