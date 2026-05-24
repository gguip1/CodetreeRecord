import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        boolean[][] visited = new boolean[n][m];
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{0, 0});

        while (!stack.isEmpty()) {
            int[] node = stack.pop();

            if (node[0] + 1 < n) {
                if (!visited[node[0] + 1][node[1]] && grid[node[0] + 1][node[1]] == 1) {
                    stack.push(new int[]{node[0] + 1, node[1]});
                    visited[node[0] + 1][node[1]] = true;
                }
            }

            if (node[1] + 1 < m) {
                if (!visited[node[0]][node[1] + 1] && grid[node[0]][node[1] + 1] == 1) {
                    stack.push(new int[]{node[0], node[1] + 1});
                    visited[node[0]][node[1] + 1] = true;
                }
            }
        }

        if (visited[n - 1][m - 1]) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}