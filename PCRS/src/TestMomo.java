public class TestMomo {

    public static void main(String[] args) {
        AlienAnimal mm = new Momo(1000);
        Tradable t1 = (Tradable) mm;
        System.out.println(t1 instanceof AlienAnimal);
    }
}
