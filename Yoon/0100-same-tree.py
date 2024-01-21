# Definition for a binary tree node.                     # 이진 트리 노드를 위한 정의
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):  # TreeNode 클래스의 생성자
#         self.val = val                                 # param val: 노드의 값
#         self.left = left                               # param left: 왼쪽 자식 노드에 대한 참조
#         self.right = right                             # param right: 오른쪽 자식 노드에 대한 참조
class Solution(object):
    def isSameTree(self, p, q):                          # 두 이진 트리가 동일한지 확인하는 함수
        """
        :type p: TreeNode                                # param p: 첫 번째 이진 트리의 루트 노드
        :type q: TreeNode                                # param q: 두 번째 이진 트리의 루트 노드
        :rtype: bool                                     # return: 두 트리가 동일하면 True, 아니면 False
        """
        # 두 노드가 모두 None인 경우(빈 트리), 동일한 것으로 간주
        if not p and not q:
            return True
        # 두 노드 중 하나가 None이고 다른 하나가 아니거나, 두 값을 비교한 값이 다르면 트리는 동일하지 않음
        if not p or not q or p.val != q.val:
            return False
        # 두 트리 값이 같다면 재귀적으로 왼쪽 및 오른쪽 서브트리가 동일한지 확인
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
