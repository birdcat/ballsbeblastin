'''
cannon_dictionary = {
    # example: cannonname : [mainimage, boughtimage, notboughtimage, mass, coincount, boughtornot]
    "c1": ["images/cannons/c1main", "images/cannons/c1bought", "images/cannons/c1notbought", 10, 0, True],
    "c2": ["images/cannons/c2main", "images/cannons/c2bought", "images/cannons/c2notbought", 8, 30, False],
    "c3": ["images/cannons/c3main", "images/cannons/c3bought", "images/cannons/c3notbought", 8, 20, False],
    "c4": ["images/cannons/c4main", "images/cannons/c4bought", "images/cannons/c4notbought", 6, 100, False],
    "c5": ["images/cannons/c5main", "images/cannons/c5bought", "images/cannons/c5notbought", 5, 200, False],
    "c6": ["images/cannons/c6main", "images/cannons/c6bought", "images/cannons/c6notbought", 2, 500, False]
}

ball_dictionary = {
    #example = ballname : [mainimage, boughtimage, notboughtimage, mass, velocity, coincountm, boughtornot]
    "b1": ["images/balls/b1main", "images/balls/b1bought", "images/balls/b1notbought", 10, 2, 0, True],
}
'''
cannon_dict = {
    "c1": {"mainimg": "images/cannons/c1main",
           "boughtimg":"images/cannons/c1bought",
           "notboughtimg": "images/cannons/DNE",
           "m": 10,
           "cost": 0,
           "bought": True},
    "c2": {"mainimg": "images/cannons/c2main",
           "boughtimg":"images/cannons/c2bought",
           "notboughtimg": "images/cannons/c2notbought",
           "m": 9,
           "cost": 20,
           "bought": True},
    "c3": {"mainimg": "images/cannons/c3main",
           "boughtimg":"images/cannons/c3bought",
           "notboughtimg": "images/cannons/c3notbought",
           "m": 8,
           "cost": 70,
           "bought": True},
    "c4": {"mainimg": "images/cannons/c4main",
            "boughtimg":"images/cannons/c4bought",
            "notboughtimg": "images/cannons/c4notbought",
            "m": 6,
            "cost": 150,
           "bought": True},
    "c5": {"mainimg": "images/cannons/c5main",
           "boughtimg":"images/cannons/c5bought",
           "notboughtimg": "images/cannons/c5notbought",
           "m": 5,
           "cost": 200,
           "bought": True},
    "c6": {"mainimg": "images/cannons/c6main",
           "boughtimg":"images/cannons/c6bought",
           "notboughtimg": "images/cannons/c6notbought",
           "m": 2,
           "cost": 500,
           "bought": True}}

ball_dict = {
    "b1": {"mainimg": "images/cannons/b1main",
           "boughtimg":"images/cannons/b1bought",
           "notboughtimg": "images/cannons/b1notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True},
    "b2": {"mainimg": "images/cannons/b2main",
           "boughtimg":"images/cannons/b2bought",
           "notboughtimg": "images/cannons/b2notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True},
    "b3": {"mainimg": "images/cannons/b3main",
           "boughtimg":"images/cannons/b3bought",
           "notboughtimg": "images/cannons/b3notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True},
    "b4": {"mainimg": "images/cannons/b4main",
           "boughtimg":"images/cannons/b4bought",
           "notboughtimg": "images/cannons/b4notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True},
    "b5": {"mainimg": "images/cannons/b5main",
           "boughtimg":"images/cannons/b5bought",
           "notboughtimg": "images/cannons/b5notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True},
    "b6": {"mainimg": "images/cannons/b6main",
           "boughtimg":"images/cannons/b6bought",
           "notboughtimg": "images/cannons/b6notbought",
           "m": 10,
           "v": 2,
           "cost": 0,
           "bought": True}}

print(cannon_dict["c1"["m"]])