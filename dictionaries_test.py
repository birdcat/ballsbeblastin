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
from vars import bc1, bc2, bc3, bc4, bc5, bc6, bb1, bb2, bb3, bb4, bb5, bb6
cannon_dict = {
    "c1": {"mainimg": "images/cannons/c1main.png",
           "boughtimg":"images/cannons/c1bought.png",
           "notboughtimg": "images/cannons/c1bought.png",
           "m": 10,
           "cost": 0,
           "bought": bc1},
    "c2": {"mainimg": "images/cannons/c2main.png",
           "boughtimg":"images/cannons/c2bought.png",
           "notboughtimg": "images/cannons/c2notbought.png",
           "m": 8,
           "cost": 20,
           "bought": bc2},
    "c3": {"mainimg": "images/cannons/c3main.png",
           "boughtimg":"images/cannons/c3bought.png",
           "notboughtimg": "images/cannons/c3notbought.png",
           "m": 7,
           "cost": 70,
           "bought": bc3},
    "c4": {"mainimg": "images/cannons/c4main.png",
            "boughtimg":"images/cannons/c4bought.png",
            "notboughtimg": "images/cannons/c4notbought.png",
            "m": 6,
            "cost": 150,
           "bought": bc4},
    "c5": {"mainimg": "images/cannons/c5main.png",
           "boughtimg":"images/cannons/c5bought.png",
           "notboughtimg": "images/cannons/c5notbought.png",
           "m": 2,
           "cost": 200,
           "bought": bc5},
    "c6": {"mainimg": "images/cannons/c6main.png",
           "boughtimg":"images/cannons/c6bought.png",
           "notboughtimg": "images/cannons/c6notbought.png",
           "m": 5,
           "cost": 700,
           "bought": bc6}}

ball_dict = {
    "b1": {"mainimg": "images/balls/b1main.png",
           "boughtimg":"images/balls/b1bought.png",
           "notboughtimg": "images/balls/b1bought.png",
           "m": 5,
           "v": 2,
           "cost": 0,
           "bought": bb1},
    "b2": {"mainimg": "images/balls/b2main.png",
           "boughtimg":"images/balls/b2bought.png",
           "notboughtimg": "images/balls/b2notbought.png",
           "m": 8,
           "v": 6,
           "cost": 40,
           "bought": bb2},
    "b3": {"mainimg": "images/balls/b3main.png",
           "boughtimg":"images/balls/b3bought.png",
           "notboughtimg": "images/balls/b3notbought.png",
           "m": 6,
           "v": 9,
           "cost": 120,
           "bought": bb3},
    "b4": {"mainimg": "images/balls/b4main.png",
           "boughtimg":"images/balls/b4bought.png",
           "notboughtimg": "images/balls/b4notbought.png",
           "m": 15,
           "v": 4,
           "cost": 180,
           "bought": bb4},
    "b5": {"mainimg": "images/balls/b5main.png",
           "boughtimg":"images/balls/b5bought.png",
           "notboughtimg": "images/balls/b5notbought.png",
           "m": 10,
           "v": 8,
           "cost": 250,
           "bought": bb5},
    "b6": {"mainimg": "images/balls/b6main.png",
           "boughtimg":"images/balls/b6bought.png",
           "notboughtimg": "images/balls/b6notbought.png",
           "m": 10,
           "v": 20,
           "cost": 1000,
           "bought": bb6}}

monster_dict = {
    "m1": {
        "imagefolder": "images/monsters/blueslime",
        "mass": 1,
        "velocity": 0,
        "clickcount": 2,
        "coins": 20
    },
    "m2": {
        "imagefolder": "images/monsters/greenslime",
        "mass": 2,
        "velocity": 0,
        "clickcount": 1,
        "coins": 10
    },
    "m3": {
        "imagefolder": "images/monsters/redslime",
        "mass": 3,
        "velocity": 0,
        "clickcount": 1,
        "coins": 20
    }


}



