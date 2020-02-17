class Plane:
    def __init__(self, origin, dim):
        self.origin = origin
        self.dim = dim

    #   self.set(cam.dimCanv.copy().divide(2).subtract(self))
    #         self.set(cam.origin.copy().subtract(self))

    def transform_to_plane(self, vector, plane_to):
        vector.subtract(plane_to.origin)

    def transform_by_ratio(self, vector, plane_to):
        vector.multiply_vector(plane_to.dim.copy().divide_vector(self.dim))

    def center_to_plane(self, vector, plane_to):
        vector.add(plane_to.origin)
