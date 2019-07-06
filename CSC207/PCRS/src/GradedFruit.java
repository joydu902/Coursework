public class GradedFruit extends Fruit{
    private double rating;
    public GradedFruit(String type, double rating) {
        super(type);
        this.rating = rating;
    }
    public GradedFruit(String type, double price, double rating) {
        super(type, price);
        this.rating = rating;
    }
    @Override
    public double getPrice() {
        return super.getPrice() * this.rating;
    }
    @Override
    public String toString() {
        return "(" + this.getType() + "," + super.getPrice() + "," + this.getPrice() + ")";
    }
    public double getRating() {
        return this.rating;
    }

    public void setRating(double newRating) {
        this.rating = newRating;
    }
}