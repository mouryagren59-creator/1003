#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};
void count_node(struct node *head){
    int count=1;
    struct node *temp=head->next;
    while(temp!=head){
        temp=temp->next;
        count++;
    }
    printf("no of node's = %d\n",count);
}
void display(struct node *head){
    struct node *temp=head->next;
    printf("%d ",head->data);
    while(temp!=head){
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
void rev_display(struct node *head){
    struct node *head2=head,*temp=head->next,*temp2=head,*temp3=temp;
    while(temp!=head){
        temp=temp->next;
        temp3->next=temp2;
        temp2=temp3;
        temp3=temp;
    }
    head=temp2;
    temp->next=head;
    temp=head->next;
    printf("%d ",head->data);
    while(temp!=head){
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
struct node* create_list(){
    struct node *head=NULL,*temp=NULL,*newnode=NULL;
    int size,i=0;
    printf("enter no of elements you want to enter :");
    scanf("%d",&size);
    while(i<size){
        i++;
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("enter the data : ");
        scanf("%d",&newnode->data);
        if(head==NULL){
            head=temp=newnode;
        }
        else{
            temp->next=newnode;
            temp=newnode;
        }
    }
    temp->next=head;
    return head;
}
struct node* input_at_beggining(struct node *head){
    struct node *temp=head->next,*newnode=NULL;
    while(temp->next!=head){
        temp=temp->next;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the data at the beggining :");
    scanf("%d",&newnode->data);
    temp->next=newnode;
    newnode->next=head;
    head=newnode;
    return head;
}
struct node* input_at_end(struct node *head){
    struct node *temp=head->next,*newnode=NULL;
    while(temp->next!=head){
        temp=temp->next;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the data at the end :");
    scanf("%d",&newnode->data);
    temp->next=newnode;
    newnode->next=head;
    return head;
}
struct node* input_at_position(struct node *head){
    struct node *temp=head->next,*newnode=NULL;
    int pos,i=1;
    printf("enter the position :");
    scanf("%d",&pos);
    while(temp->next!=head && i<pos-1){
        temp=temp->next;
        i++;
    }
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("enter the data :");
    scanf("%d",&newnode->data);
    newnode->next=temp->next;
    temp->next=newnode;
    return head;
}
struct node* delete_from_beggining(struct node *head){
    struct node *temp=head;
    while(temp->next!=head){
        temp=temp->next;
    }
    head=head->next;
    free(temp->next);
    temp->next=head;
    printf("deleted element from beggining\n");
    return head;
}
struct node* delete_from_end(struct node *head){
    struct node *temp=head->next,*tempt=NULL;
    while(temp->next!=head){
        tempt=temp;
        temp=temp->next;
    }
    tempt->next=head;
    printf("deleted node from ending\n");
    free(temp);
    return head;
}
struct node* delete_from_position(struct node *head){
    struct node *temp=head->next,*tempt=NULL;
    int pos,i=1;
    printf("enter the position :");
    scanf("%d",&pos);
    while(temp->next!=head && i<pos-1){
        tempt=temp;
        temp=temp->next;
        i++;
    }
    tempt->next=temp->next;
    free(temp);
    return head;
}
int main(){
    struct node *head=NULL;
    head=create_list();
    head=input_at_beggining(head);
    display(head);
    head=input_at_end(head);
    display(head);
    head=input_at_position(head);
    display(head);
    head=delete_from_beggining(head);
    display(head);
    head=delete_from_end(head);
    display(head);
    head=delete_from_position(head);
    display(head);
    rev_display(head);
    count_node(head);
}