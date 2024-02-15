# Definition for a binary tree node.                     # 이진 트리 노드에 대한 정의
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):  # TreeNode 클래스의 생성자
#         self.val = val                                 # param val: 노드의 값
#         self.left = left                               # param left: 왼쪽 자식 노드에 대한 참조
#         self.right = right                             # param right: 오른쪽 자식 노드에 대한 참조
class Solution(object):
    def inorderTraversal(self, root):                    # 이진 트리의 중위 순회 결과를 반환하는 함수
        """
        :type root: TreeNode                             # param root: 이진 트리의 루트 노드 (TreeNode)
        :rtype: List[int]                                # return: 중위 순회 결과를 담은 리스트 (List[int])
        """
        # 빈 결과 리스트 생성
        answer = []
        def dfs(node):
            # 노드가 존재하는 경우에만 중위 순회 수행
            if node != None:
                # 왼쪽 서브트리를 중위 순회
                dfs(node.left)
                # 현재 노드의 값을 결과 리스트에 추가
                answer.append(node.val)
                # 오른쪽 서브트리를 중위 순회
                dfs(node.right)
        # DFS를 통해 중위 순회 수행
        dfs(root)
        return answer
