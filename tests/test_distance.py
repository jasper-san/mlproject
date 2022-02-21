# test haversine

from mlproject.distance import haversine

def test_haversine():
    assert haversine(48.865070, 2.380009, -22.776582524748576, -41.91630652054015) > 5000
