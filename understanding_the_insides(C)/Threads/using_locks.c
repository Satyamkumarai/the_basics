#include <stdio.h>
#include <stdint.h>
#include <pthread.h>  //Threads lib
#include <unistd.h>   //unix std lib for sleep



#define  BIG 1000000000UL
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

//The shared Variable 
uint32_t counter = 0;  


void * count_to_big(void * arg){
    for (uint32_t i=0;i<BIG;i++){
        // pthread_mutex_lock(&lock);
        counter++;
        // pthread_mutex_unlock(&lock);

    }
    return NULL;
}


int main (){
    pthread_t t;
    pthread_create(&t,NULL,count_to_big,NULL);
    // count_to_big(NULL);
    sleep(2);
    pthread_join(t,NULL);
    printf("Done! answer is %f\n",(double) counter/BIG);

}