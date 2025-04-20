def compute_wps(track_data):
    """
    Given a list of (track_title, lyricist, duration_in_seconds, word_count),
    returns a list of (track_title, words_per_second) tuples.
    """
    wps_list = []

    for track in track_data:
        title, _, duration, count = track
        if duration > 0:
            wps = count / duration
        else:
            wps = 0  # Avoid division by zero

        wps_list.append((title, wps))

    return wps_list


def compute_avg_wps(track_data):
    """
    Given a list of (track_title, lyricist, duration_in_seconds, word_count),
    return average words per seconds
    """

    time = sum([t for _, _, t, _ in track_data])
    return sum([c for _, _, _, c in track_data]) / time if time != 0 else 0


def compute_wps_p_lyricist(track_data, default_lyricist):
    """
    Given a list of (track_title, lyricist, duration_in_seconds, word_count) and default_lyricist,
    returns a list of (lyricist, avg_words_per_second) tuples.
    """

    time_dict = {}
    word_dict = {}

    for track in track_data:
        title, lyricist, duration, count = track
        lyricist = lyricist if lyricist else default_lyricist

        if lyricist in time_dict:
            time_dict[lyricist].append(duration)
        else:
            time_dict[lyricist] = [duration]

        if lyricist in word_dict:
            word_dict[lyricist].append(count)
        else:
            word_dict[lyricist] = [count]

    wps_list = []

    for lyricist in time_dict:
        wps_list.append((lyricist, sum(word_dict[lyricist]) / sum(time_dict[lyricist])))

    return wps_list
