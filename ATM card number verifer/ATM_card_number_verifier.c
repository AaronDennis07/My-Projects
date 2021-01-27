#include<stdio.h>
#include<cs50.h>

void checksum(void);
void check_card_type(int a[],int length);
int get_length(long card_num);
int main(void)
{
    checksum();
}

void checksum(void)
{
    long card_number=0;
    int a[16];
    int sum=0;
    int sum1 = 0;
    int sum2 = 0;
    card_number = get_long("Enter the card number: ");


    int length= get_length(card_number);

    long remaining_numbers = card_number;
    for(int i = (length-1) ; i>=0;i--)
    {
        a[i] = remaining_numbers % 10;
        remaining_numbers = (remaining_numbers - a[i]) / 10;
    }


    int i = 0;
    int m[2];
    int temp;
    while(i<length)
    {
        if(2*a[i] > 9)
        {
            m[1] = 2*a[i];
            m[1] = m[1]%10;
            temp = 2*a[i] - m[1];
            m[0] = temp/10;
            sum1 += m[1];
            sum1 += m[0];

        }else
        {
            sum1+=2*a[i];
        }

        i=i+2;

    }

    int j =1;


    while(j<length)
    {
        sum2 += a[j];

        j=j+2;

    }


    printf("sum1 %i \n",sum1);
    printf("sum2 %i \n",sum2);
    sum = sum1+sum2;
    printf("sum %i \n",sum);
    if(sum%10 == 0)
    {
        printf("Checksum is successfull \n");
        check_card_type(a,length);
    }
    else{
        printf("INVALID CARD NUMBER \n");

    }
    }


void check_card_type(int a[],int length)
{
    if((a[0]==3) && (a[1]==4 || a[1]==7) && (length==15))
    {
        printf(" AMERICAN EXPRESS CARD");
    }
    else
        if((a[0]==4) && (length==13 || length == 16))
        {
            printf(" VISA CARD ");
        }
    else
        if((a[0]==5) && (a[1]==1 || a[1]==2 || a[1]==3 || a[1]==4 || a[1]==5)&& (length==15))
        {
            printf(" MASTER CARD ");
        }
    else{

        printf("INVALID! CARD NUMBER");

}
}

int get_length(long card_num)
{
    int len = 0;
    long n = card_num;
    while(n != 0)
    {
        n = n/10;
        len++;
    }
    return len;
}