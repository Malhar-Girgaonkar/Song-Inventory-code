"""import eyed3

# Replace 'your_mp3_file.mp3' with the path to your MP3 file
mp3_file_path = "D:\CS Project\Projects\AI projects\MP3-metadata\WhatsApp Audio 2023-09-06 at 16.12.52.mp3"

# Open the MP3 file
audiofile = eyed3.load(mp3_file_path)

# Check if the MP3 file has metadata
if audiofile.tag is not None:
    # Read and print the metadata
    print(f"Title: {audiofile.tag.title}")
    print(f"Artist: {audiofile.tag.artist}")
    print(f"Album: {audiofile.tag.album}")
    print(f"Genre: {audiofile.tag.genre}")
    print(f"Track Number: {audiofile.tag.track_num}")
    print(f"Year: {audiofile.tag.getBestDate()}")
else:
    print("No metadata found in the MP3 file.")"""
