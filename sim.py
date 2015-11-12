import json
import random

def load_cards():
	cards_json_file = 'AllSets.json'
	json_data=open(cards_json_file).read()
	data = json.loads(json_data)
	return data

def make_deck():
	# just use basic set for now
	card_data = load_cards()['Basic'] 
	deck = list() 
	while len(deck) < 30:
		rand_card = card_data[random.randint(1,len(card_data)-1)]
		# TODO limit max 2 per deck, restrict cards per hero class
		# make smarter choices
		deck.append(rand_card)
	return deck

def main():
	deck_A = make_deck()
	deck_B = make_deck()
	players = {'A': {'life':20, 'card_count':30, 'turn':0}, 'B': {'life':20, 'card_count':30, 'turn':0}}
	turn = 0
	current_player= 'A' if random.randint(1,2) == 1 else 'B'
	# make decks

	while True:

		turn += 1
		players[current_player]['card_count'] += -1
		mana = turn
		if mana > 10:
			mana = 10
		print current_player + '\'s turn: ' + str(turn) + ', mana: ' + str(mana)

		# temporary
		if players[current_player]['card_count'] == 0:
			break

		# win condition
		if players['A']['life'] == 0:
			print 'player B wins'
			break
		if players['B']['life'] == 0:
			print 'player A wins'
			break
		next_player = 'B' if current_player == 'A' else 'A'
		current_player = next_player


if __name__=='__main__':
	main()
	