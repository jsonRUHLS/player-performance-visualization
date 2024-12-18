import pandas as pd
import matplotlib.pyplot as plt

def create_scatter_plot():
    """Creates a scatter plot for performance vs. game order."""
    # Load the dataset
    data_path = "../data/player_performance.csv"
    data = pd.read_csv(data_path)

    # Extract metadata
    sport = data["Sport"].iloc[0]
    league = data["League"].iloc[0]
    team = data["Team"].iloc[0]
    player = data["Player"].iloc[0]

    metric = "Touchdowns" if sport.lower() == "football" else "Goals"

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Game"], data[metric], color='darkblue', alpha=0.8)
    plt.title(f"{player}'s {metric} vs. Game Order ({team}, {league}, {sport})", fontsize=14)
    plt.xlabel("Game", fontsize=12)
    plt.ylabel(metric, fontsize=12)
    plt.grid(True)

    # Save the plot
    chart_path = f"../charts/{sport}_{league}_{team}_{player}_{metric.lower()}_scatter.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Scatter plot saved to {chart_path}")

if __name__ == "__main__":
    create_scatter_plot()
