public class Fruit {
    private String type;
    private double price;

    public Fruit(String type) {
        this.type = type;
        this.price = 5;
    }

    public Fruit(String type, double price) {
        this.type = type;
        this.price = price;
    }

    public String getType() {
        return this.type;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double newPrice) {
        this.price = newPrice;
    }

    @Override
    public String toString() {
        return "$" + price + " " + type;
    }
}
