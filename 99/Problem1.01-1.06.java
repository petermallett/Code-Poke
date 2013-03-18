/* 1.01 (*) Find the last element of a list. */
/* 1.02 (*) Find the last but one element of a list. */
/* 1.03 (*) Find the K'th element of a list. */
/* 1.04 (*) Find the number of elements of a list. */
/* 1.05 (*) Reverse a list. */

class Problems {
    public static void main(String args[]) {
        int[] aList = {1, 2, 5, 8, 9};
        int k = 3;

        System.out.println("The list: " + stringList(aList));
        System.out.println(getLast(aList));
        System.out.println(getLastButOne(aList));
        System.out.println("K = " + k + ", " + getElement(aList, k));
        System.out.println("list length: " + aList.length);
        System.out.println("reversed: : " + stringList(reverseList(aList)));
    }

    public static String stringList(int[] a) {
        String result = "";

        for (int n: a) {
            result += n + " ";
        }

        return result;
    }

    public static int getLast(int[] a) {
        return a[a.length-1];
    }

    public static int getLastButOne(int[] a) {
        return a[a.length-2];
    }

    public static int getElement(int[] a, int k) {
        return a[k-1];
    }

    public static int[] reverseList(int[] a) {
        int[] b = new int[a.length];
        int i2 = 0;

        for (int i = a.length - 1; i >= 0; i--) {
            b[i2] = a[i];
            i2 += 1;
        }

        return b;
    }
}
