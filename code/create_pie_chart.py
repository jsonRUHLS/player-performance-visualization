import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart():
    """Creates a pie chart for milestone distribution."""
    # Load the dataset
    data_path = "../data/player_performance.csv"
    data = pd.read_csv(data_path)

    # Extract metadata
    sport = data["Sport"].iloc[0]
    league = data["League"].iloc[0]
    team = data["Team"].iloc[0]
    player = data["Player"].iloc[0]

    # Calculate milestone distribution
    milestone_counts = data["Milestone"].value_counts()

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        milestone_counts,
        labels=milestone_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=["lightcoral", "lightgreen"]
    )
    plt.title(f"{player}'s Milestone Distribution ({team}, {league}, {sport})", fontsize=14)

    # Save the plot
    chart_path = f"../charts/{sport}_{league}_{team}_{player}_milestone_distribution.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Pie chart saved to {chart_path}")

if __name__ == "__main__":
    create_pie_chart()
