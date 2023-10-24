import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int n = input.nextInt();
            int k = input.nextInt();
            int[] a = new int[n];
            for (int j = 0; j < n; j++) {
                a[j] = input.nextInt();
            }
            PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
                public int compare(int[] x, int[] y) {
                    return Integer.compare(y[0], x[0]);
                }
            });
            for (int j = 0; j < n; j++) {
                heap.offer(new int[] {-a[j], j});
            }
            List<Integer> ans = new ArrayList<>();
            while (!heap.isEmpty()) {
                int[] cur = heap.poll();
                int value = -cur[0];
                int index = cur[1];
                if (value > k) {
                    heap.offer(new int[] {-(value - k), index});
                } else {
                    ans.add(index + 1);
                }
            }
            for (int j = 0; j < ans.size(); j++) {
                System.out.print(ans.get(j) + " ");
            }
            System.out.println();
        }
    }
}