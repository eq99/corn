一、二叉排序树
1、定义
二叉排序树(也称二叉查找树)或者是一棵空树，或者是具有下列特性的二叉树:

若左子树非空，则左子树上所有结点的值均小于根结点的值。
若右子树非空，则右子树上所有结点的值均大于根结点的值。
左、右子树也分别是一棵二叉排序树。
根据二叉排序树的定义，左子树结点值<根结点值<右子树结点值，所以对二叉排序树进行中序遍历，可以得到一个递增的有序序列。例如，下图所示二叉排序树的中序遍历序列为123468。


2、二叉排序树的常见操作
构造一个二叉树的结构：

/*二叉树的二叉链表结点结构定义*/
typedef struct BiTNode
{
	int data;	//结点数据
	struct BiTNode *lchild, *rchild;	//左右孩子指针
} BiTNode, *BiTree;
1
2
3
4
5
6
（1）查找操作
/*
递归查找二叉排序树T中是否存在key
指针f指向T的双亲，其初始调用值为NULL
若查找成功，则指针p指向该数据元素结点，并返回TRUE
否则指针p指向查找路径上访问的最后一个结点并返回FALSE
*/
bool SearchBST(BiTree T, int key, BiTree f, BiTree *p){
	if(!T){
		*p = f;
		return FALSE;
	}else if(key == T->data){
		//查找成功
		*p = T;
		return TRUE;
	}else if(key < T->data){
		return SearchBST(T->lchild, key, T, p);	//在左子树继续查找
	}else{
		return SearchBST(T->rchild, key, T, p);	//在右子树继续查找
	}
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
（2）插入操作
有了二叉排序树的查找函数，那么所谓的二叉排序树的插入，其实也就是将关键字放到树中的合适位置而已。

/*
当二叉排序树T中不存在关键字等于key的数据元素时
插入key并返回TRUE，否则返回FALSE
*/
bool InsertBST(BiTree *T, int key){
	BiTree p, s;
	if(!SearchBST(*T, key, NULL, &p)){
		//查找不成功
		s = (BiTree)malloc(sizeof(BiTNode));
		s->data = key;
		s->lchild = s->rchild = NULL;
		if(!p){
			*T = s;	//插入s为新的根节点
		}else if(key < p->data){
			p->lchild = s;	//插入s为左孩子
		}else{
			p->rchild = s;	//插入s为右孩子
		}
		return TRUE;
		}else{
			return FALSE;	//树种已有关键字相同的结点，不再插入
		}
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
有了二叉排序树的插入代码，我们要实现二叉排序树的构建就非常容易了，几个例子：

int i;
int a[10] = {62, 88, 58, 47, 35, 73, 51, 99, 37, 93};
BiTree T = NULL;
for(i = 0; i<10; i++){
	InsertBST(&T, a[i]);
}
1
2
3
4
5
6
上面的代码就可以创建一棵下图这样的树。


（3）删除操作
二叉排序树的查找和插入都很简单，但是删除操作就要复杂一些，此时要删除的结点有三种情况：

叶子结点；
仅有左或右子树的结点；
左右子树都有的结点；
前两种情况都很简单，第一种只需删除该结点不需要做其他操作；第二种删除后需让被删除结点的直接后继接替它的位置；复杂就复杂在第三种，此时我们需要遍历得到被删除结点的直接前驱或者直接后继来接替它的位置，然后再删除。
第三种情况如下图所示：


代码如下：

/*
若二叉排序树T中存在关键字等于key的数据元素时，则删除该数据元素结点，
并返回TRUE;否则返回FALSE
*/
bool DeleteBST(BiTree *T, int key){
	if(!*T){
		return FALSE; 
	}else{
		if(key == (*T)->data){
			//找到关键字等于key的数据元素
			return Delete(T);
		}else if(key < (*T) -> data){
			return DeleteBST((*T) -> lchild, key);
		}else{
			return DeleteBST((*T) -> rchild, key);
		}
	}
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
下面是Delete()方法：

/*从二叉排序树中删除结点p，并重接它的左或右子树。*/
bool Delete(BiTree *p){
	BiTree q, s;
	if(p->rchild == NULL){
		//右子树为空则只需重接它的左子树
		q = *p;
		*p = (*p)->lchild;
		free(q);
	}else if((*p)->lchild == NULL){
		//左子树为空则只需重接它的右子树
		q = *p;
		*p = (*p)->rchild;
		free(q);
	}else{
		//左右子树均不空
		q = *p;
		s = (*p)->lchild;	//先转左
		while(s->rchild){//然后向右到尽头，找待删结点的前驱
			q = s;
			s = s->rchild;
		}
		//此时s指向被删结点的直接前驱，p指向s的父母节点
		p->data = s->data;	//被删除结点的值替换成它的直接前驱的值
		if(q != *p){
			q->rchild = s->lchild;	//重接q的右子树
		}else{
			q->lchild = s->lchild;	//重接q的左子树
		}
		pree(s);
	}
	return TRUE;
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

————————————————
版权声明：本文为CSDN博主「UniqueUnit」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Real_Fool_/article/details/113930623