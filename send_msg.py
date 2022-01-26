import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-435046985394-3004455722741-fpIQQHskeFNILHcT3hGoPIF7");
channel_id="wordle"

is_solved = True
guesses = []
with open("tmp", "r") as f:

	for line in f:
		line = line.strip()
		if line == "IMPOSSIBLE":
			is_solved = False
			continue

		if line == "DONE":
			continue

		print(line)
		guesses.append(line)

map_ = {'x': ':black_large_square:', 'y': ':large_blue_square:', 'g': ":large_orange_square:"}

text=f'Wordle 220 {len(guesses)}/6\n\n'
for guess in guesses:

	for cell in guess:
		text+=map_[cell]

	text+="\n"
		

print(guesses)

try:
    # Call the conversations.list method using the WebClient
    result = client.chat_postMessage(
    	username="wordlebot",
    	icon_emoji=":large_green_square",
        channel=channel_id,
        text=text
        # You could also use a blocks[] array to send richer content
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
	print(f"Error: {e}")
