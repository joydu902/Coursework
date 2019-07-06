public class fruitmain {
    public static void main(String[] arg){
        Fruit v1 = new Fruit("first fruit");
        Fruit v2 = new Apple(1, "Macintosh");
        Apple v3 = new Apple(2, "Fuji");
        Apple v4 = (Apple)v2;
        Fruit v5 = v3;
        int a = 5;
        int b = 5;
        Integer x = new Integer(5);
        Integer y = new Integer(5);

        System.out.println(Fruit.pick(v4));

    }
}
