class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        
        # measures angle of the directional segment from trees[anchor] to trees[ind]
        # in radians, between [-pi/2 to 3/2 pi], with 0 being the positive x axis
        def angle(anchor, ind):
            p = trees[ind]
            a = trees[anchor]
            dx = p[0] - a[0]
            dy = p[1] - a[1]
            
            # convert arc tangent to full circle
            if dx == 0:
                q = math.inf if dy > 0 else -math.inf
            else:
                q = dy / dx
            
            rot = 0 if dx > 0 else math.pi
            ang = math.atan(q) + rot
            print(dx, dy, ang / math.pi)
            return ang
            
        def dist2(anchor, ind):
            return (
                (trees[anchor][0] - trees[ind][0]) ** 2 +
                (trees[anchor][1] - trees[ind][1]) ** 2
            )
        
        
        anchors = []

        # finds the lowest of the left-most trees
        begin = min(range(n), key=lambda i: (trees[i][0], trees[i][1]))
        anchors.append(begin)
        anchor = begin
        ref_angle = - math.pi / 2.0
        
        #for _ in range(n):
        while True:
            angs = map(lambda i: (angle(anchor, i)), range(n))
            min_ang, min_dist2, min_ind = 2 * math.pi, float('inf'), -1
            for i, ang in enumerate(angs):
                if i == anchor or ang < ref_angle:
                    continue
                    
                if ang <= min_ang:
                    d2 = dist2(anchor, i)
                    
                if ang < min_ang or ang == min_ang and d2 < min_dist2:
                    min_dist2 = min(min_dist2, d2)
                    min_ang, min_ind = ang, i
                
                print('min_ang: ', min_ang / math.pi)
                            
            anchor = min_ind
            ref_angle = min_ang
            if anchor == begin:
                break
            anchors.append(min_ind)
                    
        # print(anchors)
        return [trees[i] for i in anchors]
    
    
"""
This O(N^2) solution still has bugs, but I came up with it after 4 hours or so.  I then read the
given solutions and saw there is an O(N log N) solution called Graham Scan.

I'm deciding to not bother to fix these bugs, and then will re-implement this using the Graham Scan.

"""
