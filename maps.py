class sand:
  type = 0
  file = "sand_tile"
  sub_type = 0
class lake_water:
  type = 1
  file = "lake_tile"
map = [1,2,3,4,5,6]
map[0] = sand()
map[1] = sand()
map[2] = sand()
map[3] = lake_water()
map[4] = lake_water()
map[5] = lake_water()
