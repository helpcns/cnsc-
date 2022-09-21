client
# include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

int connectToServer(const char* ip, int port)
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port),inet_addr(ip)};
    
    if(connect(sock, (struct sockaddr *) &addr, sizeof(addr)) < 0 ){
        cout << "\nRun server program first." << endl; exit(0);
    }else{
        cout << "\nClient is connected to Server." << endl; 
    }
    return sock;
}

int randInRange(int low, int high) // excluding high and low
{
    return rand()%(high-(low+1)) + (low+1) ;
}

long powermod(long a, long b, long  q)
{
	long res=1;
	for(long i=0;i<b;i++)
	{
		res=(res*a)%q;
	}
	return res;
}

int main()
{
    char ip[50]; 
	cout << "\nEnter server's IP address: "; 
	cin >> ip;
    int port;    
	cout << "Enter port : "; 
	cin >> port;
    int sock = connectToServer(ip, port);
    
	long q, alpha;
	cout<<"\nEnter a prime number, q : "; cin >> q;
	cout<<"Enter primitive root of q, alpha : "; cin >> alpha;
	
	srand(time(NULL));
	long Xc = randInRange(1, q); // client's private key (1<Xa<q)
	cout<< "\nClient's private key, Xc = " << Xc <<endl;
	
	long Yc = powermod(alpha, Xc, q); // client's public key
	send(sock, &Yc, sizeof(Yc), 0);	 // send client's public key
	cout<< "Client's public key,  Yc = " << Yc <<endl;
	
	long Ys; 
	recv(sock, &Ys, sizeof(Ys), 0);	 // recv server's public key
	cout<< "\nServer's public key,  Ys = " << Ys <<endl;
	
	long k = powermod(Ys,Xc,q);	
	cout<<"\nSecret Key, k = "<<k<<endl;

	long cipher;	
	recv(sock, &cipher, sizeof(cipher), 0);
	cout<<"\nMessage received from Server  : " << cipher << endl;
	
	long decipher = cipher ^ k;	// decryption
	cout << "Decrpyted message : " << decipher << endl << endl;
}

server
# include <bits/stdc++.h>
# include <arpa/inet.h> 
using namespace std;

// TCP connection
int createServer(int port)  
{
	int sersock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {AF_INET, htons(port), INADDR_ANY};
    
    bind(sersock, (struct sockaddr *) &addr, sizeof(addr));
    cout << "\nServer Online. Waiting for client...." << endl;
    
    listen(sersock, 5);
    int sock = accept(sersock, NULL, NULL);
    cout << "Connection Established." << endl;
    return sock;
}

int randInRange(int low, int high) // excluding high and low
{
    return rand()%(high-(low+1)) + (low+1) ;
}

long powermod(long a, long b, long  q)
{
	long res=1;
	for(long i=0; i<b; i++)
	{
		res=(res*a)%q;
	}
	return res;
}

int main()
{
    int port; 
    cout << "\nEnter port : "; 
    cin >> port;
    int sock = createServer(port);
	
	long q, alpha;
	cout<<"\nEnter a prime number, q : "; 
    cin >> q;
	cout<<"Enter primitive root of q, alpha : "; 
    cin >> alpha;
	
	long Yc; 
	recv(sock, &Yc, sizeof(Yc), 0);	 // recv client's public key
	cout<< "\nClient's public key,  Yc = " << Yc <<endl;
	
	srand(time(NULL));
	long Xs = randInRange(1, q); // server's private key
	cout<< "\nServer's private key, Xs = " << Xs <<endl;
	
	long Ys = powermod(alpha, Xs, q); // server's public key
	send(sock, &Ys, sizeof(Ys), 0);	 // send server's public key
	cout<< "Server's public key,  Ys = " << Ys <<endl;
	
	long k = powermod(Yc,Xs,q);	
	cout<<"\nSecret Key, k = "<<k<<endl;

	long msg;
	cout<<"\nEnter a message(number) to send : "; 
    cin >> msg;
	
	long cipher = msg ^ k; // encryption
	send(sock, &cipher, sizeof(cipher), 0);
	cout << "Encrypted msg sent to client: " << cipher << endl << endl;
    return 0;
}