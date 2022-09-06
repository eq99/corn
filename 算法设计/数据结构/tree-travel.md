二、遍历二叉树
二叉树的遍历( traversing binary tree )是指从根结点出发，按照某种次序依次访问二叉树中所有结点，使得每个结点被访问一次且仅被访问一次。

1、先序遍历
先序遍历(PreOrder) 的操作过程如下：
若二叉树为空，则什么也不做，否则，
1)访问根结点;
2)先序遍历左子树;
3)先序遍历右子树。


对应的递归算法如下:

void PreOrder(BiTree T){
	if(T != NULL){
		visit(T);	//访问根节点
		PreOrder(T->lchild);	//递归遍历左子树
		PreOrder(T->rchild);	//递归遍历右子树
	}
}
1
2
3
4
5
6
7
2、中序遍历
中序遍历( InOrder)的操作过程如下：
若二叉树为空，则什么也不做，否则，
1)中序遍历左子树;
2)访问根结点;
3)中序遍历右子树。


对应的递归算法如下:

void InOrder(BiTree T){
	if(T != NULL){
		InOrder(T->lchild);	//递归遍历左子树
		visit(T);	//访问根结点
		InOrder(T->rchild);	//递归遍历右子树
	}
}
1
2
3
4
5
6
7
3、后序遍历
后序遍历(PostOrder) 的操作过程如下：
若二叉树为空，则什么也不做，否则，
1)后序遍历左子树;
2)后序遍历右子树;
3)访问根结点。


对应的递归算法如下:

void PostOrder(BiTree T){
	if(T != NULL){
		PostOrder(T->lchild);	//递归遍历左子树
		PostOrder(T->rchild);	//递归遍历右子树
		visit(T);	//访问根结点
	}
}
1
2
3
4
5
6
7
三种遍历算法中,递归遍历左、右子树的顺序都是固定的，只是访问根结点的顺序不同。不管采用哪种遍历算法，每个结点都访问一次且仅访问一次，故时间复杂度都是O(n)。在递归遍历中，递归工作栈的栈深恰好为树的深度，所以在最坏情况下，二叉树是有n个结点且深度为n的单支树，遍历算法的空间复杂度为O(n)。



5、层次遍历
下图为二叉树的层次遍历，即按照箭头所指方向，按照1,2,3, 4的层次顺序，对二叉树中的各个结点进行访问。


要进行层次遍历，需要借助一个队列。先将二叉树根结点入队，然后出队，访问出队结点，若它有左子树，则将左子树根结点入队;若它有右子树，则将右子树根结点入队。然后出队，访问出队结…如此反复，直至队列为空。
二叉树的层次遍历算法如下:

void LevelOrder(BiTree T){
	InitQueue(Q);	//初始化辅助队列
	BiTree p;
	EnQueue(Q, T);	//将根节点入队
	while(!IsEmpty(Q)){	//队列不空则循环
		DeQueue(Q, p);	//队头结点出队
		visit(p);	//访问出队结点
		if(p->lchild != NULL){
			EnQueue(Q, p->lchild);	//左子树不空，则左子树根节点入队
		}
		if(p->rchild != NULL){
			EnQueue(Q, p->rchild);	//右子树不空，则右子树根节点入队
		}
	}
}
————————————————
版权声明：本文为CSDN博主「UniqueUnit」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Real_Fool_/article/details/113930623

————————————————
版权声明：本文为CSDN博主「UniqueUnit」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Real_Fool_/article/details/113930623