#include<iostream>
#include<fstream>

using namespace std;

class shooping{
    private:
        int pcode;
        float price;
        float dis;
        string pname;

    public:
        void menu();
        void administrator();
        void buyer();
        void add();
        void rem();
        void edit();
        void list();
        void recipt();
};

void shooping :: menu(){
    n:
    int choice;
    string email;
    string password;

    cout<<"\t\t\t\t_____________________________________________\n";
    cout<<"\t\t\t\t                                             \n";
    cout<<"\t\t\t\t           Supermarket main menu             \n";
    cout<<"\t\t\t\t                                             \n";
    cout<<"\t\t\t\t_____________________________________________\n";
    cout<<"\t\t\t\t|   1) Administrator   |\n";
    cout<<"\t\t\t\t|                      |\n";
    cout<<"\t\t\t\t|   2) Buyer           |\n";
    cout<<"\t\t\t\t|                      |\n";
    cout<<"\t\t\t\t|   3) Exit            |\n";
    cout<<"\t\t\t\t|                      |\n";
    cout<<"\t\t\t\t Please select an option!";
    cin>>choice;

    switch (choice)
    {
    case 1:
        cout<<"\t\t\t Please Login \n";
        cout<<"\t\t\t Enter Email  \n";
        cin>>email;

        cout<<"\t\t\t Enter Your Password!\n";
        cin>>password;

        if(email =="admin@gmail.com" && password =="admin@123"){
            administrator();
        }else{
            cout<<"Invalid Email or Password";
        }

        break;
    
    case 2:
        {
            buyer();
            break;
        }
    case 3:
    {
        exit(0);
        break;
    }
    
    default:{
        cout<<"Please select from the given option";
        goto n;
        }
    }
}

void shooping :: administrator(){
    no:
    int choice;
    cout<<"\n\n\n\t\t\t Administrator menu\n";
    cout<<"|                                   |";
    cout<<"\n\t\t\t|_____1) Add the product____|";
    cout<<"|                                   |";
    cout<<"\n\t\t\t|_____2) Delete  product____|";
    cout<<"|                                   |";
    cout<<"\n\t\t\t|_____3) Back to main menu__|";

    cout<<"\n\n\t Please enter your choice";
    cin>>choice;

    switch (choice)
    {
    case 1:
        add();
        break;
    case 2:
        edit();
        break;
    case 3:
        rem();
        break;
    case 4:
        menu();
    default:
    cout<<"Invalid choice!";
    goto no;
    }
}
void shooping:: buyer(){
    noo:
    int choice;
    cout<<"\t\t\t\t Buyer  \n";
    cout<<"\t\t\t___________________";
    cout<<"                       \n";
    cout<<"\t\t\t 1) Buy product  \n";
    cout<<"                       \n";
    cout<<"\t\t\t 2) go back      \n";
    cout<<"\t\t\tEnter your choice\n";

    cin>>choice;

    switch (choice)
    {
    case 1:
        recipt();
        break;
    case 2:
        menu();
    default:
        cout<<"invalid choice";
        goto noo;
    }

}

void shooping:: add(){
    m:
    fstream data;

    int c;
    int token=0;
    float p;
    float d;
    string n;

    cout<<"\n\n\t\t\t Add new product";
    cout<<"\n\n\t Product code";
    cin>>pcode;
    cout<<"\n\n\tName of product ";
    cin>>pname;
    cout<<"\n\n\tPrice of the product";
    cin>>price;
    cout<<"\n\n\t Discount on product";
    cin>>dis;

    data.open("database.txt", ios::in);

    if(!data){
        data.open("database.txt", ios::app|ios::out);
        data<<" "<<pcode<<" "<<pname<<" "<<price<<" "<<dis<<endl;
        data.close();
    }else{
        data>>c>>n>>d;

        while(!data.eof()){
            if(c==pcode){
                token++;
            }
            data>>c>>n>>p>>d;
        }
        data.close();
    
    if(token==1){
        goto m;
    }
    else{
        data.open("database.txt", ios::app|ios::out);
        data<<" "<<pcode<<" "<<pname<<" "<<price<<" "<<dis<<endl;
        data.close();
    }}
    cout<<"\n\n\t\t record inserted!";
}

void shooping::edit(){
    fstream data, data1;
    int pkey;
    int token=0;
    int c;
    float p;
    float d;
    string n;

    cout<<"\n\t\t\t Modify the record";
    cout<<"\n\t\t\t Product code";
    cin>>pkey;

    data.open("database.txt", ios::in);
    if(!data){
        cout<<"\n\nFile doesn't exist!";
    }else{
        data1.open("database1.txt", ios::app|ios::out);

        data>>pcode>>pname>>price>>dis;

        while(!data.eof()){
            if(pkey==pcode){
                cout<<"\n\t\t New product code ";
                cin>>c;
                cout<<"\n\t\t Name of product ";
                cin>>n;
                cout<<"\n\t\t Price ";
                cin>>p;
                cout<<"\n\t\t Discount ";
                cin>>d;

                data1<<" "<<c<<" "<<n<<" "<<p<<" "<<d<<endl;
                cout<<"Record edited succesfull!";
                token ++;
            }
            else{
                data1<<" "<<pcode<<" "<<pname<<" "<<price<<" "<<dis<<endl;

            }
            data>>pcode>>pname>>price>>dis;

        }
        data.close();
        data1.close();

        remove("database.txt");
        rename("database1.txt", "database.txt");

        if(token ==0){
            cout<<"\n\nRecord not found";
        }
    }
}

void shooping::rem(){
    fstream data, data1;

    int pkey;
    int token=0;
    cout<<"\n\n\t Delete product";
    cout<<"\n\n\t Product code ";
    cin>>pkey;

    data.open("database.txt", ios::in);
    if(!data){
        cout<<"File doesn't exist!";
    }else{
        data1.open("database.txt",ios::app|ios::out);
        data>>pcode>>pname>>price>>dis;

        while (!data.eof())
        {
            if(pcode == pkey){
                cout<<"\n\n\t Product deleted succesfully";
                token ++;
            }
            else{
                data1<<" "<<pcode<<" "<<price<<" "<<dis<<endl;
            }
            data>>pcode>>pname>>price>>dis;
        }
        data.close();
        data1.close();

        remove("database.txt");
        rename("database1.txt","database.txt");

        if (token==0)
        {
            cout<<"\n\n Record not found";
        }
        
        
    }
}

void shooping::list(){
    fstream data;
    data.open("database.txt", ios::in);
    cout<<"\n\n______________________________________________\n";
    cout<<"prNo\t\tName\t\tPrice\n";
    cout<<"\n\n______________________________________________\n";

    data>>pcode>>pname>>price>>dis;
    while (!data.eof())
    {
        cout<<pcode<<"\t\t"<<pname<<"\t\t"<<price<<endl;
        data>>pcode>>pname>>price>>dis;

    }
    data.close();
}

void shooping::recipt(){
    m:
    fstream data;

    int arrc[100];
    int arrq[100];
    char choice;
    int c=0;
    float amount=0;
    float dis=0;
    float total=0;

    cout<<"\n\n\t\t\t RECEIPT ";
    data.open("database.txt", ios::in);
    if(!data){
        cout<<"\n\n Empty Database";
    }else{
        data.close();

        list();
        cout<<"\n__________________________________\n";
        cout<<"\n|                                 \n";
        cout<<"\n|      please enter the order     \n";
        cout<<"\n|                                 \n";
        cout<<"\n__________________________________\n";

        do
        {
           cout<<"\n\nEnter Product code :";
           cin>>arrc[c];
           cout<<"enter product quantity :";
           cin>>arrc[c];
           for(int i=0; i<c; i++){
            if(arrc[c] == arrc[i]){
                cout<<"\n\n Duplicate product code. Please try again!";
                goto m;
            }
           }
           c++;
           cout<<"\n\n Do you want to buy another product (y/n)";
           cin>>choice;
        } while (choice == 'y');


        cout<<"\n\n\t\t\t_____________________________RECEIPT______________________\n";
        cout<<"\nProduct No\t Product Name\t Product quantiny\tPrice\tAmount with discount\n";

        for(int i=0; i<c; i++){
            data.open("database.txt, ios::in");
            data>>pcode>>pname>>price>>dis;
            while (!data.eof())
            {
                if(pcode==arrc[i]){
                    amount=price*arrq[i];
                    dis=amount-(amount*dis/100);
                    total += dis;
                    cout<<"\n"<<pcode<<"\t\t"<<pname<<"\t\t"<<arrq[i]<<"\t\t"<<price<<"\t"<<amount<<"\t\t"<<dis;
                }
                data>>pcode>>pname>>price>>dis;
            }
            data.close();
        }
    }
        cout<<"\n\n___________________________________________________";
        cout<<"\n Total Amount : "<<total;
}
int main (){
    shooping s;
    s.menu();
}