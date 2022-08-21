from kivy.config import Config
Config.set('graphics', 'width', '410')
Config.set('graphics', 'height', '900')


from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
from numpy import inf
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window



node_location = {#### MAIN FLOOR 0
                 'M0A': [150,230], 'M0B': [150,335], 'M0C': [150,444], 'M0D': [125,444], 'M0E': [125,510], 'M0F': [250, 720], 'M0G': [150, 295],
                 
                 'Dining Hall': [72,230], 'Sixth Form Common Room': [230,335], "Fred's Office": [245,335], 'Staff Room': [150,510],
                 'Picture Gallery': [125,720], 'Reception': [250,810],

                 'MS1L0_U': [104,463], 'MS2L0_U': [125,295], 'MS3L0_U': [220,620],

                 'ME1_OUT': [345,810], 'ME2_OUT': [380,335], 'ME3_OUT': [35,440],


                 #### MAIN FLOOR 1
                 'M1A': [150,160], 'M1B': [150,230], 'M1C': [150,300], 'M1D': [150,370], 'M1E': [120,370], 'M1F': [120,485], 
                 'M1G': [120,535], 'M1H': [120,580], 'M1I': [120,820], 'M1J': [230,820], 'M1K': [300,820], 'M1L': [230,580],

                 '101': [110,300], '102': [110,230], '103': [185,210], '104': [275,230], '105': [275,230], '106': [275,230], 
                 '107': [275,230], '108': [275,230], '109': [275,230], '110': [200,370], '111': [150,535], '112': [230,655], 
                 '114': [300,820], '115': [300,820], '116': [95,840], '117': [120,760], '118': [120,680], '119': [120,620],
                 '120': [95,500], '121': [95,480],
                 
                 'A1': [200,300], 'A2': [170,390], 'A4': [230,820], 'A5': [95,840],
                 
                 'MS1L1_U': [65,385], 'MS1L1_D': [65,355], 'MS2L1_D': [100,160], 'MS3L1_U': [255,585], 'MS3L1_D': [255,695],
                 
                 #### MAIN FLOOR 2

                 'ART': [195,140], '202': [195,215], '204': [195,280], 'M2A': [195,380], '201': [147,380], 'MS1L2_D': [90,360],
                 'M2B': [147, 525], '206': [180,525], '207': [125,535], 'M2C': [147,640], '209': [147, 690], '210': [147,760],
                 '211': [147, 860], 'MS3L2_D': [310, 640], 

                 #### OUTSIDE

                 'OA': [180,115], 'OB': [180,250], 'OC': [55,500], 'OD': [270,115], 'OE': [270,530], 'OF': [270,755],

                 'ME1_IN': [175,830], 'ME2_IN': [250,530], 'ME3_IN': [55,675], 'SCIENCE_IN': [200,115], 'THEATRE': [305,755], 'MUSIC': [305,755],

                 #### SCIENCE FLOOR 0

                 'S0A': [265,690], 'S0B': [265,665], 'S0C': [265,305], 'S0D': [230,260],

                 '9': [120,665], '10': [305,270], '11': [315,690],

                 'SCIENCE_OUT': [230,185], 'SBS_U': [130,260],

                 #### SCIENCE FLOOR 1

                 'S1A': [175,235], 'S1B': [175,310],

                 '129': [130,310], '130': [175, 160], '131': [235,320],

                 'SBS_D': [145,235]
                 }

window_size = Window.size

windox = window_size[0]
windoy = window_size[1]

for key, value in node_location.items():
    value[0] = value[0]/410*windox
    value[1] = value[1]/900*windoy


node_floor =   {'0th_Floor_Main.png': ['M0A', 'M0B', 'M0C', 'M0D', 'M0E', 'M0F', 'M0G',
                
                                        'Dining Hall', 'Sixth Form Common Room', "Fred's Office", 'Staff Room',
                                        'Picture Gallery', 'Reception',

                                        'MS1L0_U', 'MS2L0_U', 'MS3L0_U',

                                        'ME1_OUT', 'ME2_OUT', 'ME3_OUT'],
    
    
    
                '1st_Floor_Main.png': ['M1A', 'M1B', 'M1C' ,'M1D' ,'M1E','M1F', 
                                        'M1G', 'M1H', 'M1I', 'M1J','M1K', 'M1L',
                                        
                                        '101','102','103','104','105', '106', '107', '108', '109',
                                        '110','111','112','114','115','116','117', '118', '119',
                                        '120','121',

                                        'MS1L1_U', 'MS1L1_D', 'MS2L1_D', 'MS3L1_U', 'MS3L1_D',

                                        'A1', 'A2', 'A4', 'A5'],
                        
                '2nd_Floor_Main.png': ['ART', '202', '204', 'M2A', '201', 'MS1L2_D',
                                           'M2B', '206', '207', 'M2C', '209', '210',
                                           '211', 'MS3L2_D'],

                'outside.png': ['OA', 'OB', 'OC', 'OD', 'OE', 'OF',

                                'ME1_IN', 'ME2_IN', 'ME3_IN', 'SCIENCE_IN', 'THEATRE', 'MUSIC'],

                '0th_Science.png': ['S0A', 'S0B', 'S0C', 'S0D', '9', '10', '11', 'SCIENCE_OUT', 'SBS_U'],

                '1st_Science.png': ['S1A', 'S1B', '129', '130', '131', 'SBS_D']
                }


map_connections = [#stairs
                    'MS1L0_U', 'MS1L1_U', 'MS1L1_D', 'MS1L2_D', 'MS2L0_U', 'MS2L1_D', 'MS3L0_U', 'MS3L1_U', 'MS3L1_D', 'MS3L2_D', 'SBS_U', 'SBS_D',
                   #exits
                   'ME1_OUT', 'ME2_OUT', 'ME3_OUT', 'ME1_IN', 'ME2_IN', 'ME3_IN', 'SCIENCE_IN', 'SCIENCE_OUT'
                    ]

def resetgraph():
    global graph
    global costs
    global node_ran
    node_ran = []

    graph = {#MAIN GROUND FLOOR
            'M0A': {'M0G': 65, 'Dining Hall': 78},
            'M0B': {'M0G': 40, 'M0C': 109,'Sixth Form Common Room':80},
            'M0C': {'M0B': 109, 'M0D':25},
            'M0D': {'M0C': 25, 'M0E': 66, 'ME3_OUT': 90, 'MS1L0_U': 28},
            'M0E': {'M0D': 66, 'Staff Room': 25, 'Picture Gallery': 210},
            'M0F': {'Picture Gallery': 125, 'MS3L0_U':104, 'Reception': 110},
            'M0G': {'M0A': 65, 'M0B': 40, 'MS2L0_U':25},


            'Reception': {'M0F': 110, 'ME1_OUT': 125},
            'Picture Gallery': {'M0E': 210, 'M0F': 125},
            'Staff Room': {'M0E': 25},
            'Sixth Form Common Room': {'M0B': 80, "Fred's Office": 30},
            'Dining Hall': {'M0A': 78},
            "Fred's Office": {'Sixth Form Common Room': 30, 'ME2_OUT': 125},

            'MS1L0_U': {'M0D':28, 'MS1L1_D':100},
            'MS2L0_U': {'M0G': 25, 'MS2L1_D': 100},
            'MS3L0_U': {'M0F': 104, 'MS3L1_D': 100},
            'ME1_OUT': {'Reception': 125, 'ME1_IN': 100},
            'ME2_OUT': {"Fred's Office": 125, 'ME2_IN': 100},
            'ME3_OUT': {'M0D': 90, 'ME3_IN': 100},
        
        
            #MAIN FIRST FLOOR
            'M1A': {'MS2L1_D': 50, 'M1B': 70}, 
            'M1B': {'M1A': 70, 'M1C': 70, '102': 40, '103': 40, '104': 125, '105': 125, '106': 125, '107': 125, '108': 125, '109': 125},
            'M1C': {'M1B': 70, 'M1D': 70, '101': 40, 'A1': 50},
            'M1D': {'M1C': 70, 'M1E': 30, '110': 50, 'A2': 28},
            'M1E': {'M1D': 30, 'M1F': 115, 'MS1L1_U': 57, 'MS1L1_D': 57},
            'M1F': {'M1E': 115, 'M1G': 50, '120': 29, '121': 25}, 
            'M1G': {'M1F': 50, 'M1H': 30, '111': 45},
            'M1H': {'M1G': 30, 'M1L': 110, '119': 40}, 
            'M1I': {'117': 60, 'M1J': 110, '116': 32, 'A5': 32}, 
            'M1J': {'M1I': 110, 'M1K': 70, '112': 165, 'A4': 0},
            'M1K': {'M1J': 70, '114': 0, '115': 0}, 
            'M1L': {'112': 75, 'M1H': 110, 'MS3L1_U': 25, 'MS3L1_D': 50},

            '101': {'M1C': 40},
            '102': {'M1B': 40},
            '103': {'M1B': 40},
            '104': {'M1B': 125},
            '105': {'M1B': 125}, 
            '106': {'M1B': 125}, 
            '107': {'M1B': 125}, 
            '108': {'M1B': 125}, 
            '109': {'M1B': 125},
            '110': {'M1D': 50},
            '111': {'M1G': 45},
            '112': {'M1J': 165, 'M1L': 75},
            '114': {'M1K': 0},
            '115': {'M1K': 0},
            '116': {'M1I': 32},
            '117': {'118': 80, 'M1I': 60},
            '118': {'119': 60, '117': 80},
            '119': {'M1H': 40, '118': 60},
            '120': {'M1F': 29},
            '121': {'M1F': 25},

            'MS1L1_U': {'M1E': 57, 'MS1L2_D': 100},
            'MS1L1_D': {'M1E': 57, 'MS1L0_U': 100},
            'MS2L1_D': {'M1A': 50, 'MS2L0_U': 100},
            'MS3L1_U': {'M1L': 25, 'MS3L2_D': 100},
            'MS3L1_D': {'MS3L0_U': 100, 'M1L': 50},


            'A1': {'M1C': 50},
            'A2': {'M1D': 28},
            'A4': {'M1J': 0},
            'A5': {'M1I': 32},

            #MAIN SECOND FLOOR
            'ART': {'202': 75}, '202':{'ART': 75, '204': 65}, '204':{'202': 65, 'M2A': 100}, 'M2A':{'204': 100, '201': 48}, '201':{'M2A': 48, 'MS1L2_D': 60, 'M2B': 145},
            'M2B': {'201': 145, '206': 33, '207': 24, 'M2C': 115}, '206':{'M2B': 33}, '207':{'M2B': 24}, 'M2C':{'M2B': 115, '209': 50, 'MS3L2_D': 163}, '209':{'M2C':50, '210': 70},
            '210':{'209': 70, '211': 100}, '211':{'210': 100}, 

            'MS3L2_D':{'M2C': 163, 'MS3L1_U': 100}, 
            'MS1L2_D':{'201': 60, 'MS1L1_U': 100},

            #OUTSIDE
            'OA': {'OB':135, 'SCIENCE_IN': 20}, 'OB': {'OA':135, 'OC': 280}, 'OC': {'OB': 280, 'ME3_IN': 350}, 'OD': {'SCIENCE_IN': 70, 'OE': 415}, 'OE': {'OD': 415, 'ME2_IN':20, 'OF': 225}, 'OF': {'OE': 225, 'THEATRE': 35, 'MUSIC': 35, 'ME1_IN': 121},
            'THEATRE': {'OF': 35}, 'MUSIC': {'OF': 35},

            'ME1_IN': {'OF': 121, 'ME1_OUT': 100}, 'ME2_IN': {'OE':20, 'ME2_OUT': 100}, 'ME3_IN':{'ME3_OUT': 100, 'OC': 350}, 'SCIENCE_IN': {'OA': 20, 'OD': 70, 'SCIENCE_OUT': 100},

            #SCIENCE BLOCK GROUND FLOOR
            'S0A': {'S0B': 25, '11': 50}, 'S0B': {'S0A': 25, '9': 145, 'S0C': 360}, 'S0C': {'S0B': 360, '10': 53, 'S0D': 57}, 'S0D': {'S0C': 57, 'SBS_U': 100, 'SCIENCE_OUT': 75},

            '9': {'S0B': 145}, '10': {'S0C': 53}, '11': {'S0A': 50},

            'SCIENCE_OUT': {'S0D': 75, 'SCIENCE_IN': 100}, 'SBS_U': {'S0D': 100, 'SBS_D': 100},

            #SCIENCE 1ST FLOOR
            'S1A': {'S1B': 75, 'SBS_D': 30, '130': 75}, 'S1B': {'S1A': 75, '129': 45, '131': 65},

            '129': {'S1B': 45}, '130': {'S1A': 75}, '131': {'S1B': 65},

            'SBS_D': {'S1A': 30, 'SBS_U': 100}

        }

    costs = {}
    for key, items in node_location.items():
        costs[key] = inf


resetgraph()

def setStartpoint(startpoint):
    for key, value in costs.items():
        costs[key] = inf

    costs[startpoint] = 0

parents = {}


def search(source, target, graph, costs, parents):
    
    nextNode = source
    
    while nextNode != target:        
        try:
        
            for neighbour in graph[nextNode]:
                
                if graph[nextNode][neighbour] + costs[nextNode] < costs[neighbour]:
                    
                    costs[neighbour] = graph[nextNode][neighbour] + costs[nextNode]
                    
                    parents[neighbour] = nextNode
                del graph[neighbour][nextNode]
                
            del costs[nextNode]

            node_ran.append(nextNode)
            
            nextNode = min(costs, key=costs.get)

        except KeyError:
            temp_key_holder = min(costs, key = lambda k: costs[k])
            temp_holder = {temp_key_holder: costs[temp_key_holder]}
            del costs[temp_key_holder]

            nextNode = min(costs, key=costs.get)

            costs.update(temp_holder)

    return parents


def backpedal(source, target, searchResult):
    
    node = target
    
    backpath = [target]
    
    path = []
    
    while node != source:
        
        backpath.append(searchResult[node])
        
        node = searchResult[node]
        
    for i in range(len(backpath)):
        
        path.append(backpath[-i - 1])
        
    return path


class DepartureWindow(Screen):
    def dp_roomsubmit(self):
        global dp_roomnumber
        dp_roomnumber = self.ids.dpRoomNumberInput.text
    
    def dp_quickroomsubmit(self, location):
        global dp_roomnumber
        dp_roomnumber = location

class ArrivalWindow(Screen):
    def ar_roomsubmit(self):
        global ar_roomnumber
        ar_roomnumber = self.ids.arRoomNumberInput.text

    def ar_quickroomsubmit(self, location):
        global ar_roomnumber
        ar_roomnumber = location

class ErrorScreen(Screen):
    pass


map_connections_count = 0
map_page = 0
point1 = []
map_split_point = []
same_floor_count = 0

class MainFirstWindow(Screen):

    def __init__(self, **kwargs):
        super(MainFirstWindow, self).__init__(**kwargs)
    
        with self.canvas:
            Color(1,1,1,1, mode = "rgba")
            self.mapimage = Rectangle(pos = (0,100/900*windoy), size = (410/410*windox,800/900*windoy), source = 'loading_screen.png')        

            Color(32/255.0, 84/255.0, 147/255.0, 1, mode = "rgba")
            self.rect = Line(pos = (0,0), size = (100/410*windox,100/410*windoy))

            Color(190/255.0, 159/255.0, 84/255.0, 1, mode = "rgba")
            self.start_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))

            Color(0/255.0, 35/255.0, 94/255.0, 1, mode = "rgba")
            self.end_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))

    def different_floor(self):
        global map_index
        global floors_required_node
        global map_connections_count
        global map_split_point

        map_connections_count = 0
        map_split_point = []
        floors_required_node = []
        map_index = []
        map_page = 0

        map_split_point.append(0) #to have function for return

        for items in drawer: #find connecting points
            if items in map_connections:
                map_split_point.append(drawer.index(items) + 1)
                floors_required_node.append(items)
                map_connections_count += 0.5
        
        floors_required_node_ending = point1.index(point1[-1]) + 1
        map_split_point.append(floors_required_node_ending)

        for items in floors_required_node: #map index
            for key, value in node_floor.items():
                if items in value:
                    if key not in map_index:
                        map_index.append(key)

        clear = (point1[0:map_split_point[1]])
        self.rect.points = clear
        self.start_rect.pos = clear[0]
        self.end_rect.pos = clear[-1]



    def drawLines(self):
        global map_page
        global point1
        global map_split_point
        global drawer
        global map_connections_count
        global same_floor_count

        if dp_roomnumber == ar_roomnumber:
            self.manager.current = "error"
        elif all(x in (node_location) for x in [dp_roomnumber, ar_roomnumber]) == False:
            self.manager.current = "error" 
        else:
            if map_connections_count >= 1.0:
                try:
                    map_page += 1
                    clear = point1[map_split_point[map_page * 2]-1:map_split_point[map_page * 2 + 1]]
                    self.mapimage.source = map_index[map_page]
                    self.rect.points = clear
                    self.start_rect.pos = clear[0]
                    self.end_rect.pos = clear[-1]

                except IndexError:
                    map_connections_count = 0
                    map_page = 0
                    clear = []

                    self.rect.points = inf,inf
                    self.start_rect.pos = inf,inf
                    self.end_rect.pos = inf,inf
                    self.mapimage.source = "loading_screen.png"
                    
                    self.manager.current = "departure"

            else:
                setStartpoint(dp_roomnumber)
                result = search(dp_roomnumber,ar_roomnumber, graph, costs, parents)
                drawer = backpedal(dp_roomnumber, ar_roomnumber, result)

                point1 = []
                for items in drawer:
                    coord_retrieval = node_location[items]
                    point1.append(coord_retrieval)

                resetgraph()

                for key, value in node_floor.items():
                    for items in value:
                        if items == dp_roomnumber:
                            start_floor = key
                        if items == ar_roomnumber:
                            end_floor = key
                        if items == dp_roomnumber:
                            shown_image = key

                if start_floor == end_floor:
                    if same_floor_count == 0:
                        self.mapimage.source = shown_image
                        self.rect.points = point1
                        self.start_rect.pos = point1[0]
                        self.end_rect.pos = point1[-1]
                        same_floor_count = 1

                    else:
                        same_floor_count = 0
                        with self.canvas:
                            Color(1,1,1,1, mode = "rgba")
                            self.mapimage = Rectangle(pos = (0,100/900*windoy), size = (410/410*windox,800/900*windoy), source = 'loading_screen.png')

                            Color(32/255.0,84/255.0,147/255.0,1, mode = "rgba")
                            self.rect = Line(pos = (0,0), size = (100/410*windox,100/410*windoy))

                            Color(190/255.0, 159/255.0, 84/255.0, 1, mode = "rgba")
                            self.start_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))

                            Color(0/255.0, 35/255.0, 94/255.0, 1, mode = "rgba")
                            self.end_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))
                        self.manager.current = "departure"


                else:
                    self.different_floor()
                    self.mapimage.source = shown_image


    def backwards(self):
        global map_page
        global map_connections_count
        global same_floor_count
        map_page = map_page - 1
        if map_page > 0:

            clear = point1[map_split_point[map_page * 2] - 1:map_split_point[map_page * 2 + 1]]

            self.mapimage.source = map_index[map_page]
            self.rect.points = clear
            self.start_rect.pos = clear[0]
            self.end_rect.pos = clear[-1]

        elif map_page == 0:
            clear = point1[0:map_split_point[1]]

            self.mapimage.source = map_index[map_page]
            self.rect.points = clear
            self.start_rect.pos = clear[0]
            self.end_rect.pos = clear[-1]
            
        else:
            map_connections_count = 0
            map_page = 0
            same_floor_count = 0
            with self.canvas:
                Color(1,1,1,1, mode = "rgba")
                self.mapimage = Rectangle(pos = (0,100/900*windoy), size = (410/410*windox,800/900*windoy), source = 'loading_screen.png')

                Color(32/255.0,84/255.0,147/255.0,1, mode = "rgba")
                self.rect = Line(pos = (0,0), size = (100/410*windox,100/410*windoy))

                Color(190/255.0, 159/255.0, 84/255.0, 1, mode = "rgba")
                self.start_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))

                Color(0/255.0, 35/255.0, 94/255.0, 1, mode = "rgba")
                self.end_rect = Rectangle(pos = (windox,0), size = (10/410*windox,10/900*windoy))
            self.manager.current = "departure"
            #insert back to beginning screen


class HelpScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager(transition = NoTransition())
        sm.add_widget(DepartureWindow(name='departure'))
        sm.add_widget(ArrivalWindow(name='arrival'))
        sm.add_widget(MainFirstWindow(name="map"))
        sm.add_widget(ErrorScreen(name="error"))
        sm.add_widget(HelpScreen(name="help"))
        
        return sm


if __name__ == "__main__":
    MainApp().run()
