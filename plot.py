import matplotlib.pyplot as plt
import os


def _plot_wps(wps_data, avg_wps, output_path, filename, title):
    """
    Plots a line graph for a list of (name, words_per_second) tuples,
    labels each point, and adds a horizontal line for average WPS.
    Saves the plot to the specified path and filename.

    Parameters:
        wps_data (list): List of (name, words_per_second) tuples.
        avg_wps_data (list): Average words per seconds
        output_path (str): Directory to save the plot.
        filename (str): Name of the output image file.
        title (str): Title for the plot.
    """
    song_names = [title for title, _ in wps_data]
    wps_values = [wps for _, wps in wps_data]

    plt.figure(figsize=(12, 6))
    plt.plot(song_names, wps_values, marker='o', linestyle='-')
    
    # Label each point with its WPS value
    for i, (x, y) in enumerate(zip(song_names, wps_values)):
        plt.text(i, y + 0.01, f"{y:.2f}", ha='center', va='bottom', fontsize=8)

    # Plot average line
    plt.axhline(y=avg_wps, color='r', linestyle='--', label=f"Avg: {avg_wps:.2f}")

    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Words per Second")
    plt.title(title)
    plt.legend()
    plt.tight_layout()

    os.makedirs(output_path, exist_ok=True)
    full_path = os.path.join(output_path, filename + ".jpeg")
    plt.savefig(full_path)
    plt.close()


def plot_song_wps(wps_data, avg_wps, output_path, filename, album_name):
    _plot_wps(wps_data, avg_wps, output_path, filename, "Words per seconds of songs in: " + album_name)


def plot_album_wps(wps_data, avg_wps, output_path):
    _plot_wps(wps_data, avg_wps, output_path, "album_wps", "Words per seconds of albums")


def plot_lyricist(lyricist_data, output_path):
    """
    Plots a line graph for a list of (lyricist, words_per_second) tuples,
    labels each point.
    Saves the plot to the specified path and filename.

    Parameters:
        lyricist_data (list): List of (lyricist_name, words_per_second) tuples.
        output_path (str): Directory to save the plot.
    """
    lyricist_names = [l for l, _ in lyricist_data]
    wps_values = [wps for _, wps in lyricist_data]

    plt.figure(figsize=(12, 6))
    plt.plot(lyricist_names, wps_values, marker='o', linestyle=' ')
    
    # Label each point with its WPS value
    for i, (x, y) in enumerate(zip(lyricist_names, wps_values)):
        plt.text(i, y + 0.01, f"{y:.2f}", ha='center', va='bottom', fontsize=8)

    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Words per Second")
    plt.title("Words per seconds of songs per lyricist")
    plt.tight_layout()

    os.makedirs(output_path, exist_ok=True)
    full_path = os.path.join(output_path, "lyricist_wps.jpeg")
    plt.savefig(full_path)
    plt.close()


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    mock_wps_data = [("song_0", 1), ("song_1", 0.5), ("song_3", 0.6)]
    plot_wps(mock_wps_data, base_dir, "mock", "Mock album")

    mock_lyricist_data = [("John", 1), ("Jane", 0.5)]
    plot_lyricist(mock_lyricist_data, base_dir)
