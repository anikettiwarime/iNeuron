#include <stdio.h>


int main()
{
    float r, a;
    printf("Enter radius of circle : ");
    scanf("%f", &r);
    a = r * r * 3.14;
    printf("Area of circle is %f having the radius %f", a, r);

    
    return 0;
}