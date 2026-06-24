class Solution(object):
    def preorderTraversal(self, root):
        fin=[]
        def order(rot):
            if rot:
                # print(rot.val)
                fin.append(rot.val)
                if rot.left:
                    order(rot.left)
                if rot.right:
                    order(rot.right)
        order(root)
        return(fin)