import os


def _parse_tracklist_file(tracklist_path):
    """
    Parses a tracklist.txt file and returns a list of (track_name, duration_in_seconds) pairs.
    Each line is expected to look like:
    1.    "Track Name"    Lyrics    mm:ss
    """
    tracks = []

    try:
        with open(tracklist_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    title_part = parts[1].strip().strip('"')
                    lyrics_part = parts[-2].strip() if len(parts) >= 4 else ""
                    time_part = parts[-1].strip()

                    # Convert mm:ss to seconds
                    try:
                        minutes, seconds = map(int, time_part.split(':'))
                        total_seconds = minutes * 60 + seconds
                        tracks.append((title_part, lyrics_part, total_seconds))
                    except ValueError:
                        print(f"Could not parse time in line: {line.strip()}")
                        print(f"time_part: {time_part}")
    except Exception as e:
        print(f"Error reading {tracklist_path}: {e}")

    return tracks


def _count_words_in_file(file_path, skip_duplicate_lines=True):
    """
    Returns the number of words in a text file after:
    - removing dashes/hyphens
    - filtering out filler words
    - optional: Skip duplicate lines
    """
    filler_words = {'ah', 'oh'}  # Add more if needed
    seen_lines = set()
    total_words = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()

                # Skip if we've already seen this line
                if skip_duplicate_lines:
                    if clean_line.lower() in seen_lines:
                        continue
                    seen_lines.add(clean_line.lower())

                # Replace dashes/hyphens with space
                clean_line = clean_line.replace('-', ' ').replace('—', ' ')

                # Split into words and filter
                words = clean_line.split()
                filtered = [word for word in words if word.lower() not in filler_words]

                total_words += len(filtered)

        return total_words
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0


def parse(base_directory, folder_names):
    """
    Loops through all subfolders and files.
    For each folder, loads tracklist.txt and pairs each track with word count from matching N.txt.
    Returns a list of (track_name, lyricist, duration_in_s, word_count).
    """
    word_counts = []

    for folder_name in folder_names:
        word_count = []

        folder_path = os.path.join(base_directory, folder_name)

        if not os.path.isdir(folder_path):
            continue  # Skip non-directories

        tracklist_file_name = "tracklist.txt"
        tracklist_path = os.path.join(folder_path, tracklist_file_name)
        tracklist = _parse_tracklist_file(tracklist_path)

        for i, (title, lyrics, duration) in enumerate(tracklist):
            file_name = f"{i}.txt"
            file_path = os.path.join(folder_path, file_name)

            count = _count_words_in_file(file_path)
            word_count.append((title, lyrics, duration, count))

        word_counts.append(word_count)

    return word_counts


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(base_dir, "data")
    word_count = parse(base_dir)
    print(word_count)
