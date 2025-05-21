import sys
sys.path.append('../')
from utils import get_center_of_bbox, measure_distance

class PlayerBallAssigner():
    def __init__(self):
        self.max_player_ball_distance = 70
        
    def assign_ball_to_player(self, players, ball_bbox):
        ball_position = get_center_of_bbox(ball_bbox)
        
        minimum_distance = 99999
        assigned_player = -1
        
        for player_id, player in players.items():
            player_bbox = player['bbox']
            
            
            distence_left = measure_distance((player_bbox[0], player_bbox[-1]), ball_position)
            distence_right = measure_distance((player_bbox[2], player_bbox[-1]), ball_position)
            distence = min(distence_left, distence_right)   
            
            if distence < self.max_player_ball_distance:
                if distence < minimum_distance:
                    minimum_distance = distence
                    assigned_player = player_id
                    
                    
        return assigned_player         
    