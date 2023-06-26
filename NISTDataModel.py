import csv
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Control(dict):
    identifier: str
    name: str
    control_text: str
    discussion: str
    related: str
    low: Optional[bool] = False
    moderate: Optional[bool] = False
    high: Optional[bool] = False
    spoofing: Optional[bool] = False
    tampering: Optional[bool] = False
    repudiation: Optional[bool] = False
    information_disclosure: Optional[bool] = False
    denial_of_service: Optional[bool] = False
    elevation_of_privilege: Optional[bool] = False
    lateral_movement: Optional[bool] = False

    def dict(self):
        return {
            'identifier': self.identifier,
            'name': self.name,
            'control_text': self.control_text,
            'discussion': self.discussion,
            'related': self.related,
            'low': self.low,
            'moderate': self.moderate,
            'high': self.high,
            'spoofing': self.spoofing,
            'tampering': self.tampering,
            'repudiation': self.repudiation,
            'information_disclosure': self.information_disclosure,
            'denial_of_service': self.denial_of_service,
            'elevation_of_privilege': self.elevation_of_privilege,
            'lateral_movement': self.lateral_movement
        }

@dataclass
class Control_STRIDE:
    id : str 
    name : str 
    low : str 
    moderate : str 
    high : str 
    spoofing : str 
    tampering : str 
    repudiation : str 
    information_disclosure : str 
    denial_of_service : str 
    elevation_of_privilege : str 
    lateral_movement : str 


class CSF_Tools:
    
    def __init__(self, path_to_csv) -> None:
        self.data = self.load_data(path_to_csv=path_to_csv)
    
    def load_data(self, path_to_csv) -> Optional[List[Control]]:
        data : List[Control] = []
        with open(file=path_to_csv, mode='r') as csv_file:
            csv_reader = csv.DictReader(fieldnames=[
            "id",
            "name",
            "low",
            "moderate",
            "high",
            "spoofing",
            "tampering",
            "repudiation",
            "information_disclosure",
            "denial_of_service",
            "elevation_of_privilege",
            "lateral_movement"
            ], 
            f=csv_file)
            next(csv_reader)
            for row in csv_reader:
                control = Control_STRIDE(
                    id = row.get('id'),
                    name = row.get('name'),
                    low = row.get('low'),
                    moderate = row.get('moderate'),
                    high = row.get('high'),
                    spoofing = row.get('spoofing'),
                    tampering = row.get('tampering'),
                    repudiation = row.get('repudiation'),
                    information_disclosure = row.get('information_disclosure'),
                    denial_of_service = row.get('denial_of_service'),
                    elevation_of_privilege = row.get('elevation_of_privilege'),
                    lateral_movement = row.get('lateral_movement')
                    )
                data.append(control)
        return data

    def get(self, id:str) -> Control_STRIDE:
        try:
            return list(filter(lambda x: x.id == id, self.data))[0]
        except IndexError:
            print(f"Got nothing for id {id}")
            return False

class NIST_80053:
    @classmethod
    def load_data(cls, path_to_csv) -> Optional[List[Control]]:
        data : List[Control] = []
        
        with open(file=path_to_csv, mode='r') as csv_file:
            csv_reader = csv.DictReader(fieldnames=[
                'identifier',
                'name',
                'control_text',
                'discussion',
                'related'
            ], f=csv_file)
            next(csv_reader)

            for row in csv_reader:
                control = Control(
                    identifier=row.get('identifier'),
                    name=row.get('name'),
                    control_text=row.get('control_text'),
                    discussion=row.get('discussion'),
                    related=row.get('related')
                    )
                data.append(control)
        return data
        

