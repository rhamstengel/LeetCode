class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons by their end points
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for balloon in points:
            if balloon[0] > current_end:
                # If the start point of the next balloon is beyond the end point
                # of the current balloon, shoot a new arrow
                arrows += 1
                current_end = balloon[1]

        return arrows
