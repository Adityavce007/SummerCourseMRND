#include<stdio.h>
#include<map>

using namespace std;

struct node{
	int data;
	struct node* next, *random;
};
typedef struct node Node;

static struct node* create_node(int data)
{
	Node* temp = (Node*)malloc(sizeof(*temp));
	temp->data = data;
	temp->next = NULL;
	temp->random = NULL;
	return temp;
}

static struct node* clone_nh(struct node* head)
{
	struct node* clone_head = NULL, *temp = head, *clone_temp = NULL;
	map <Node*, Node*> hash;

	while (temp)
	{
		if (!clone_temp)
		{
			clone_head = clone_temp = create_node(temp->data);

		}
		else
		{
			clone_temp->next = create_node(temp->data);
			clone_temp = clone_temp->next;
		}
		hash.insert(pair<Node*, Node*>(temp, clone_temp));
		temp = temp->next;
	}


	temp = head;
	clone_temp = clone_head;
	while (temp)
	{
		clone_temp->random = hash[temp->random];
		temp = temp->next;
		clone_temp = clone_temp->next;
	}
	return clone_head;
}

static void findclone()
{
	Node* start = create_node(1);
	start->next = create_node(2);
	start->next->next = create_node(3);
	start->next->next->next = create_node(4);
	start->next->next->next->next = create_node(5);

	start->random = start->next->next;
	start->next->random = start;
	start->next->next->random = start->next->next->next->next;
	start->next->next->next->random = start->next->next->next->next;
	start->next->next->next->next->random = start->next;

	Node* clone_head = clone_nh(start);
	while (start)
	{
		if (start->data != clone_head->data)
		{
			printf("not same");
			//getchar();
			return;
		}
		if (start->random->data != clone_head->random->data)
		{
			printf("not same random ptr");
			getchar();
			return;
		}
		start = start->next;
		clone_head = clone_head->next;
	}
	printf("Cloned succesfully\nEnter any key to continue...");
	//getchar();
	return;
}