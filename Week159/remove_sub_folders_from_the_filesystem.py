class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort(key=len)
        res = set()
        def helper(f):
            fs = f.strip().split('/')
            ss = fs[0]
            if ss in res: return True
            for s in fs[1:]:
                ss+='/'+s
                if ss in res: return True
            return False
        
        for f in folder:
            if not helper(f):
                res.add(f)
        return list(res)
