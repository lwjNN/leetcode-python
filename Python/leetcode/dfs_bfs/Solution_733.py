from _ast import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srLen = len(image)
        scLen = len(image[0])
        if image[sr][sc] == newColor:
            return image

        def dfs(image1: List[List[int]], sr1, sc1, tarColor, newColor):
            if sr1 >= srLen or sc1 >= scLen or sr1 < 0 or sc1 < 0 or image1[sr1][sc1] != tarColor:
                return
            image1[sr1][sc1] = newColor
            dfs(image1, sr1 + 1, sc1, tarColor, newColor)
            dfs(image1, sr1 - 1, sc1, tarColor, newColor)
            dfs(image1, sr1, sc1 + 1, tarColor, newColor)
            dfs(image1, sr1, sc1 - 1, tarColor, newColor)

        dfs(image, sr, sc, newColor)
        return image
