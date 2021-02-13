#include <stdio.h>
#include <string.h>
#define SIZE 10

//linked list for the person 
typedef struct person  {
    char name[10];
    int age ;
    struct person * next;
}person ; 


//The hash table is a array of pointer to person
person * H_T[SIZE];


//The Main Hash Function
int hash(char * str){
    int val = 0,n = strlen(str);
    for (int i=1;i<n;i++){
        val +=str[i];
    }
    return val % SIZE;
}

void init_hash_table(){
    for (int i=0;i<SIZE;i++){
        H_T[i] = NULL;
    }

}

void print_hash_table(){
    for (int i=0;i<SIZE ;i++){
        if (H_T[i]!=NULL){
            person * curr= H_T[i];
            printf("\t%d\t",i+1);
            while (curr!=NULL){
                printf("%s--",curr->name);
                curr= curr->next;
            }
            printf("\n");
            
        }else{
            printf("\t%d\t---\n",i+1);
        }
    }
}


void  insert_to_hash_table(person * p){
    int index = hash(p->name);
    person * curr = (person *)H_T[index];
    if (H_T[index] == NULL){
        H_T[index] = p;
        H_T[index]-> next = NULL;
    }else{
        while (curr->next != NULL){
            curr = curr->next;
        }
        curr->next = p;
    }
}

int main (){
    init_hash_table();
    print_hash_table();
    person minick = {.name ="Minick Ame",.age=21,.next=NULL};
    person utkarsh = {.name ="Utkarsh",.age=11,.next=NULL};
    person akash = {.name ="Akash",.age=10,.next=NULL};
    person prakash = {.name ="Prakash",.age=19,.next=NULL};
    person rithik = {.name ="Rithik",.age=19,.next=NULL};
    person rayuga = {.name ="Rayuga",.age=19,.next=NULL};
    person shivani= {.name ="Shivani",.age=19,.next=NULL};
    person kiyoka = {.name ="Kiyoka",.age=19,.next=NULL};

    printf("Inserting Members \n");



    insert_to_hash_table(&minick);
    insert_to_hash_table(&utkarsh);
    insert_to_hash_table(&akash);
    insert_to_hash_table(&prakash);
    insert_to_hash_table(&rithik);
    insert_to_hash_table(&rayuga);
    insert_to_hash_table(&shivani);
    insert_to_hash_table(&kiyoka);



    



    printf("After Inserting \n");
    print_hash_table();
    // printf("hash(%s) = %d\n",minick.name,hash(minick.name));
    // printf("hash(%s) = %d\n",akash.name,hash(akash.name));

}