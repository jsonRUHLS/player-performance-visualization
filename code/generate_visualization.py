import pandas as pd
import matplotlib.pyplot as plt

def create_visualization():
    """Creates a line chart for player performance trends."""
    # Load the dataset
    data_path = "../data/player_performance.csv"
    data = pd.read_csv(data_path)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(data["Game"], data["Goals"], marker='o', label="Goals Scored")
    plt.axhline(y=data["Goals"].mean(), color='r', linestyle='--', label="Average Goals")
    plt.title("Player Performance: Goals Across Games", fontsize=14)
    plt.xlabel("Game", fontsize=12)
    plt.ylabel("Goals Scored", fontsize=12)
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    chart_path = "../charts/player_performance_trends.png"
    plt.savefig(chart_path)
    plt.show()

    print(f"Visualization saved to {chart_path}")

if __name__ == "__main__":
    create_visualization()
