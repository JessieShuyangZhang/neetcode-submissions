class Solution:
    def isValid(self,q0:List[int],q1:List[int]) -> bool:
        if (q0[0] == q1[0]) or q0[1] == q1[1] or abs(q1[0]-q0[0]) == abs(q1[1]-q0[1]):
            return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [['.' for i in range(n)] for j in range(n)]
        res, qpos = [],[]
        
        def dfs(qcnt): # qcnt is current len(qpos), also its the row that should be worked on
            if qcnt == n:
                bo = []
                for qp in qpos: 
                    st = '.'*qp[1] + 'Q' + '.'*(n-qp[1]-1)
                    bo.append(st)                
                res.append(bo)
                return
            for j in range(n): # check each spot in row qcnt against every existing q
                newq= [qcnt,j]
                newqvalid = True
                for qpo in qpos:
                    if not self.isValid(newq, qpo):
                        newqvalid = False
                        break
                if newqvalid:
                    qpos.append(newq)
                    dfs(qcnt+1)
                    qpos.pop()
        dfs(0)
        return res