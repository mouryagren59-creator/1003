#include<stdio.h>
#include<stdlib.h>
struct node {
    struct node* prev;
    int data;
    struct node* next;
};
struct node* creatlist(struct node* head){
    struct node *temp=NULL,*newnode=NULL;
    int i=0;
    int size;
    printf("enter no of elements you want to enter :");
    scanf("%d",&size);
    while(i<size){
        
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("enter the data : ");
        scanf("%d",&newnode->data);
        if(head==NULL){
            head=temp=newnode;
        }
        else{
            temp->next=newnode;
            newnode->prev=temp;
            temp=newnode;
        }
        i+=1;
    }
    return head;
}
int count_node(struct node *temp){
    int count=0;
    while(temp!=NULL){
        temp=temp->next;
        count++;
    }
    return count;
}
void display(struct node *temp){
    printf("display : ");
    while(temp!=NULL){
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
void rev_display(struct node *temp){
    struct node *tempt=NULL;
    printf("reverse display : ");
    while(temp!=NULL){
        tempt=temp;
        temp=temp->next;
    }
    while(tempt!=NULL){
        printf("%d ",tempt->data);
        tempt=tempt->prev;
    }
}
struct node* insert_at_beggining(struct node *head){
    struct node *newnode=NULL;
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("\nenter the element you want to enter in beggining :");
    scanf("%d",&newnode->data);
    newnode->next=head;
    head->prev=newnode;
    newnode->prev=NULL;
    return newnode;
}
struct node* insert_at_ending(struct node *head){
    struct node *temp=head,*tempt=NULL,*newnode=NULL;
    while(temp!=NULL){
        tempt=temp;
        temp=temp->next;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the element you want to enter in ending :");
    scanf("%d",&newnode->data);
    tempt->next=newnode;
    newnode->prev=tempt;
    return head;
}
struct node* insert_at_position(struct node *head){
    int specific_place=0;
    struct node *temp=NULL,*newnode=NULL,*tempt=NULL;
    printf("\nenter the place you want to enter the element : ");
    scanf("%d",&specific_place);
    if (specific_place>count_node(head) || specific_place<=0){
        printf("Invalid Position\n");
    }
    temp=head;
    int i=0;
    if (specific_place-1==0){
        head=insert_at_beggining(head);
        return head;
    }
    else{
    while(i!=specific_place-1){
        tempt=temp;
        temp=temp->next;
        i++;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the element : ");
    scanf("%d",&newnode->data);
    tempt->next=newnode;
    newnode->prev=tempt;
    newnode->next=temp;
    temp->prev=newnode;
    temp=head;}
    return head;
}
struct node* delete_at_beggining(struct node *head){
    printf("deleting first element \n");
    head=head->next;
    free(head->prev);
    head->prev=NULL;
    return head;
}
void delete_at_ending(struct node *head){
    printf("deleting last element \n");
    struct node *temp=head,*tempt=NULL;
    while(temp!=NULL){
        tempt=temp;
        temp=temp->next;
    }
    tempt->prev->next=NULL;
    free(tempt);
}
struct node* delete_at_position(struct node *head){
    int specific_place=0;
    struct node *temp=NULL,*tempt=NULL;
    printf("\nenter the place you want to deleat the element : ");
    scanf("%d",&specific_place);
    if (specific_place>count_node(head) || specific_place<=0){
        printf("Invalid Position\n");
    }
    temp=head;
    int i=0;
    if(specific_place-1==0){
        head=delete_at_beggining(head);
        return head;
    }
    else if(specific_place==count_node(head)){
        delete_at_ending(head);
    }
    else{
        do{
        tempt=temp;
        temp=temp->next;
        i++;
    }while(i!=specific_place-1);
    tempt->next=temp->next;
    temp->next->prev=tempt;
    free(temp);}
    return head;
}
int main(){
    struct node *head=NULL;
    head=creatlist(head);
    //returning head because we need head adress
    display(head);
    printf("%d",head->data);
    head=insert_at_beggining(head);
    //returning head because changing the first element
    display(head);
    head=insert_at_ending(head);
    display(head);
    head=insert_at_position(head);
    //returning head becaue if user insert at head first element adress changes so return new head adress or else return original head adress
    display(head);
    head=delete_at_beggining(head);
    //returning head because changing the first element
    display(head);
    delete_at_ending(head);
    display(head);
    head=delete_at_position(head);
    //returning head becaue if user delete at head first element adress changes so return new head adress or else return original head adress
    display(head);
    rev_display(head);
    printf("\nno of node's = %d",count_node(head));
}