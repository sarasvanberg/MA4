#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		int fib();

		void set(int);
	private:
	    int val;
		int fib_(int);
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}

int Integer::fib(){
	return fib(val);
    }

int Integer::fib_(int n){
	if (n <= 1){
	return n;
	}
	else:{
	return(fib_(n-1) + fib_(n-2));
	}

    }
 
void Integer::set(int n){
	val = n;
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}