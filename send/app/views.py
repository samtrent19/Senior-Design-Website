from app import app

from flask import render_template, request, redirect, jsonify, make_response, flash

from datetime import datetime

import time


class RoomMap:
    def __init__(self, name):
        self.name = name
        self.nodes = ()
        self.pairs = {}
        self.dist = {}
        self.allnodes = False

    def find_nodes(self):
        self.nodes = ("IP1 - Node 1", "IP2 - Node 2", "IP3 - Node 3")
        return self.nodes

    def pair_nodes(self):
        self.pairs = {}
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    self.pairs[f'{node1} + {node2}'] = 30

    def calculate_dist(self):
        self.dist = {}

        for node in self.nodes:
            data = []
            for i in range(10):
                data.append(i)
            self.dist[node] = data

        return self.dist


myMap = RoomMap(name="Test")

@app.route("/")
def index():
    global myMap
    print(myMap.name)
    return render_template("public/index.html", myMap=myMap)

@app.route("/start", methods=["POST"])
def start():
    global myMap
    
    args = request.args
    start = True
    myMap.find_nodes()

    pair = False
    measure = False
    slam = False

    if args.get("pair") == "true":
        myMap.pair_nodes()
        pair = True
    if args.get("measure") == "true":
        myMap.calculate_dist()
        measure = True
    if args.get("slam") == "true":
        slam = True
    print(args)

    
    return render_template(
        "public/index.html", myMap=myMap, start=start,
        pair=pair, measure=measure, slam=slam
        )

@app.route("/about")
def about():
    return render_template("public/about.html")
