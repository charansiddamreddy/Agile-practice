import java.util.Scanner;
class Main 
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        boolean[] a = new boolean[42];
        char c;
        for(int i=0;i<8;i++)
        {
            if(i%2!=0)
            {
                c = 'b';
            }
            else
            {
                c='a';
            }
            System.out.println("Enter position: ");
            int pos = s.nextInt();
            a[pos] = true;
            if(a[pos]== true && a[pos+1]==true && a[pos+2]==true && a[pos+3]==true)
            {
                System.out.println("Player " +c+ " is winner");
            }
        }
    }
}
