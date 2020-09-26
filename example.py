import os

from walkmapper.routes import MultipleRoutes

files = ["examples/data/{}".format(i) for i in os.listdir("examples/data")]

rts = MultipleRoutes(files)

rts.heat_map("examples/maps/Portland_45.5372_m122.5831_45.4761_m122.7077.png")

rts.basic_route_animation(
    map_file_path="examples/maps/Portland_45.5372_m122.5831_45.4761_m122.7077.png")
