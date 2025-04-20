import os
from parse import parse
from plot import plot_song_wps, plot_lyricist, plot_album_wps
from compute import compute_wps, compute_avg_wps, compute_wps_p_lyricist

long_names = ["For the First Time", "Ants From Up There", "Live at Bush Hall", "Forever Howlong"]
short_names = ["ftft", "ants", "bushhall", "fh"]

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data = parse(os.path.join(base_dir, "data"), short_names)
    
    if len(data) != len(short_names):
        print(f"Did not process all the folders")
        exit

    plot_dir = os.path.join(base_dir, "plot")
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    for album_name, plot_file_name, d in zip(long_names, short_names, data):
        plot_song_wps(compute_wps(d), compute_avg_wps(d), plot_dir, plot_file_name, album_name)

    wps_lyricist_data = compute_wps_p_lyricist(sum(data, []), "Isaac-era")
    plot_lyricist(wps_lyricist_data, plot_dir)

    wps_album_data = [(album_name, compute_avg_wps(d)) for album_name, d in zip(long_names, data)]
    plot_album_wps(wps_album_data, compute_avg_wps(sum(data, [])), plot_dir)
