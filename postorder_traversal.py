class Solution(object):
    def postorderTraversal(self, root):
        fin=[]
        def order(rot):
            if rot:
                if rot.left:
                    order(rot.left)
                if rot.right:
                    order(rot.right)
                fin.append(rot.val)
        order(root)
        return(fin) 