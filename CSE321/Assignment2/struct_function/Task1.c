#include <stdio.h>

struct food
{
    int quantity;
    int unit_price;
};

int main(){
    struct food Partha;
    struct food Vegetables;
    struct food Mineral_water;

    int num_people;
    int total_price;
    float price;
    
    printf("Quantity of Paratha: ");
    scanf("%d", &Partha.quantity);

    printf("Unit Price: ");
    scanf("%d", &Partha.unit_price);

    printf("Quantity of Vegetables: ");
    scanf("%d", &Vegetables.quantity);

    printf("Unit Price: ");
    scanf("%d", &Vegetables.unit_price);

    printf("Quantity of Mineral Water: ");
    scanf("%d", &Mineral_water.quantity);

    printf("Unit Price ");
    scanf("%d", &Mineral_water.unit_price);

    printf("Number of people: ");
    scanf("%d", &num_people);

    total_price = Partha.quantity*Partha.unit_price + Vegetables.quantity*Vegetables.unit_price + Mineral_water.quantity*Mineral_water.unit_price;
    price = total_price/num_people;

    printf("Individual people will pay: %f", price);
} 
