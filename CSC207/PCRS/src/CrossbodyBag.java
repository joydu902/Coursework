class CrossbodyBag extends Bag {
    private int straps;

    public CrossbodyBag(String color, int capacity, int straps) {
        super(color, capacity);
        this.straps = straps;
    }
    public int getNumberOfStraps() {
        return straps;
    }

    public void enhance() {
        super.update(2);
    }

    public static void main(String[] args) {
        int [][] aa = {{1,2}, {3}};
        int [][] bb = aa.clone();

        bb[0] = new int[] {1, 2};
        bb[0][0] = 99;
        bb[1][0] = 99;

        System.out.println(bb[0][0]);
        System.out.println(bb[1][0]);

        System.out.println(aa[0][0]);
        System.out.println(aa[1][0]);
    }

}