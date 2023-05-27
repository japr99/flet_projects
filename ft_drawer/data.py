""" the data dictionary will be provided on GitHub """


def ReturnData():
    return {
        1: {
            # we call these in the main.py logic
            "colors": [
                "#14b8a6",
                "#0d9488",
                "#0f766e",
                "#115e59",
                "#134e4a",
                "#1e3e3b",
                "#1a3734",
                "#182726",
            ],
            "title": "Spotify",
            "subtitle": "Individual Plan",
            "price": "$23.99",
            "icon": "../assets/spotify.png",
            "card_icon": "../assets/apple.png",
            "card_type": "Apple Card",
            "card_number": "**** 1234",
        },
        2: {
            "colors": [
                "#f472b6",
                "#ec4899",
                "#db2777",
                "#be185d",
                "#9d174d",
                "#831843",
                "#691e3b",
                "#5c1a33",
            ],
            "title": "Dribble",
            "subtitle": "Pro Subscription",
            "price": "$99.99",
            "icon": "./assets/dribble.png",
            "card_icon": "./assets/mastercard.png",
            "card_type": "Credit Card",
            "card_number": "**** 8732",
        },
        3: {
            "colors": [
                "#94a3b8",
                "#64748b",
                "#475569",
                "#334155",
                "#1e293b",
                "#0f172a",
            ],
            "title": "Netflix",
            "subtitle": "Basic Subscription",
            "price": "$19.99",
            "icon": "./assets/netflix.png",
            "card_icon": "./assets/mastercard.png",
            "card_type": "Debit Card",
            "card_number": "**** 6322",
        },
    }
