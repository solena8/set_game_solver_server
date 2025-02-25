import functions_framework
from flask import jsonify
from card import Card
from selection import Selection


@functions_framework.http
def set_game_api(request):
    headers = {
        'Access-Control-Allow-Origin': '*',  # Autoriser toutes les origines
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
        'Access-Control-Max-Age': '3600',
        'Content-Type': 'application/json'
    }

    if request.method == 'OPTIONS':
        return ('', 204, headers)

    if request.path == '/':
        return (jsonify({"Hello": "World"}), 200, headers)

    if request.path.startswith('/cards/'):
        cards = request.path.split('/cards/')[1]
        l_cards = cards.split(",")
        selection_instance = Selection()

        for param in l_cards:
            try:
                card = Card(*param)
                selection_instance.selection_cards.append(card)
            except Exception as e:
                return (jsonify({"error": f"Invalid card format: {param}", "details": str(e)}), 400, headers)

        found_set = selection_instance.find_set()

        if found_set:
            return (jsonify([str(found_set.card1), str(found_set.card2), str(found_set.card3)]), 200, headers)
        else:
            return (jsonify(None), 200, headers)

    return (jsonify({"error": "Route not found"}), 404, headers)
