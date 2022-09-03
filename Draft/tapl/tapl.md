# OCaml

案例

链表去重

```ocaml
let rec compress = function
    | a :: (b :: _ as t) -> if a = b then compress t else a :: compress t
    | smaller -> smaller;;
    
# compress ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"];;
- : string list = ["a"; "b"; "c"; "a"; "d"; "e"]
```

元素个数统计及

```ocaml
# let encode list =
    List.map (fun l -> (List.length l, List.hd l)) (pack list);;
val encode : 'a list -> (int * 'a) list = <fun>
    
# encode ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"];;
- : (int * string) list =
[(4, "a"); (1, "b"); (2, "c"); (2, "a"); (1, "d"); (4, "e")]

```



重复元素个数

```ocaml
# let replicate list n =
    let rec prepend n acc x =
      if n = 0 then acc else prepend (n-1) (x :: acc) x in
    let rec aux acc = function
      | [] -> acc
      | h :: t -> aux (prepend n acc h) t in
    (* This could also be written as:
       List.fold_left (prepend n) [] (List.rev list) *)
    aux [] (List.rev list);;
    
# replicate ["a"; "b"; "c"] 3;;
- : string list = ["a"; "a"; "a"; "b"; "b"; "b"; "c"; "c"; "c"]
```

链表元素排列组合

```ocaml
# let rec permutation list =
    let rec extract acc n = function
      | [] -> raise Not_found
      | h :: t -> if n = 0 then (h, acc @ t) else extract (h :: acc) (n - 1) t
    in
    let extract_rand list len =
      extract [] (Random.int len) list
    in
    let rec aux acc list len =
      if len = 0 then acc else
        let picked, rest = extract_rand list len in
        aux (picked :: acc) rest (len - 1)
    in
    aux [] list (List.length list);;
    
# permutation ["a"; "b"; "c"; "d"; "e"; "f"];;
- : string list = ["a"; "e"; "f"; "b"; "d"; "c"]
```

质数检测

```ocaml
# let is_prime n =
    let n = abs n in
    let rec is_not_divisor d =
      d * d > n || (n mod d <> 0 && is_not_divisor (d + 1)) in
    n <> 1 && is_not_divisor 2;;

```

二叉树

```ocaml
# type 'a binary_tree =
    | Empty
    | Node of 'a * 'a binary_tree * 'a binary_tree;;
type 'a binary_tree = Empty | Node of 'a * 'a binary_tree * 'a binary_tree

# let example_tree =
    Node ('a', Node ('b', Node ('d', Empty, Empty), Node ('e', Empty, Empty)),
         Node ('c', Empty, Node ('f', Node ('g', Empty, Empty), Empty)));;
val example_tree : char binary_tree =
  Node ('a', Node ('b', Node ('d', Empty, Empty), Node ('e', Empty, Empty)),
   Node ('c', Empty, Node ('f', Node ('g', Empty, Empty), Empty)))
# let example_int_tree =
    Node (1, Node (2, Node (4, Empty, Empty), Node (5, Empty, Empty)),
         Node (3, Empty, Node (6, Node (7, Empty, Empty), Empty)));;
val example_int_tree : int binary_tree =
  Node (1, Node (2, Node (4, Empty, Empty), Node (5, Empty, Empty)),
   Node (3, Empty, Node (6, Node (7, Empty, Empty), Empty)))
```



修改变量

![image-20220425073327063](image-20220425073327063.png)

快速排序

![image-20220425073405327](image-20220425073405327.png)

![image-20220425073437167](image-20220425073437167.png)

![image-20220425073552638](image-20220425073552638.png)

# 无类型算术表达式

语法树结点个数 size(t)：

![image-20220425073835413](image-20220425073835413.png)

语法书结点深度：

![image-20220425073914814](image-20220425073914814.png)

# Lambda 演算

三种规约方式：

Full beta-reduction：

![image-20220425074304538](image-20220425074304538.png)

正则顺序：每次选择最左、最外侧的redex

![image-20220425074322942](image-20220425074322942.png)

传名：严格从外侧归约，函数抽象中不进行归约

![image-20220425074350629](image-20220425074350629.png)

传值：函数参数先归约，也就是说先参数求值再计算函数

![image-20220425074435196](image-20220425074435196.png)

## Church encodes

![image-20220425074700280](image-20220425074700280.png)

![image-20220425074713979](image-20220425074713979.png)

![image-20220425075007761](image-20220425075007761.png)

![image-20220425075038817](image-20220425075038817.png)



![image-20220425075100629](image-20220425075100629.png)



![image-20220425075108028](image-20220425075108028.png)



![image-20220425075123093](image-20220425075123093.png)

![image-20220425075137649](image-20220425075137649.png)

![image-20220425075442033](image-20220425075442033.png)

![image-20220425075507202](image-20220425075507202.png)

## 替换规则

![image-20220425075608790](image-20220425075608790.png)

# 简单类型表达式



**引理**：类型关系的倒置 (Inversion of the type relation)

![image-20220425075841197](image-20220425075841197.png)

性质：

可靠性/安全性/Soundness/Safty

- Well-typed terms求值不会出错
- 不会到达stuck state

由两个定理来保证可靠性：

- Progress: A well-typed term is not stuck. 要么是一个value，要么存在一条规则进行求值
- Preservation: 一个well-typed term经过若干次求值得到的新term也是well-typed的

例：推断 (λx:Bool .x) true的类型

![image-20220425080257146](image-20220425080257146.png)

**引理**：类型关系的倒置

![image-20220425080323291](image-20220425080323291.png)

# 简单扩展

## 基本类型

使用抽象的A,B,C这样的符号表示不同的基本类型

![image-20220425080516639](image-20220425080516639.png)

例：

λx:A. x

λx:B. x

λf:A→A. λx:A. f(f(x))

## The Unit Types

![image-20220425080616754](image-20220425080616754.png)

$t_1;t_2$ 可以看作 $(λx:Unit. t_2 ) t_1$ 的缩写，是一种派生型(derived form)，又称为语法糖(syntactic sugar) 

**通配符(Wildcard)**

- 一种语法糖

- 表示不会在函数抽象中使用到的参数

- 用通配符”_”表示这样的参数

- $λ\_:S. t$ 是 $λx:S. t$ 的缩写，其中 x 不在 t 中出现

## 类型归属(Ascription)

![image-20220425080942782](image-20220425080942782.png)

## Let 绑定 (Let Bindings)

![image-20220425081116071](image-20220425081116071.png)

## Pairs

![image-20220425081137850](image-20220425081137850.png)

## Tuples

![image-20220425081204931](image-20220425081204931.png)

## 记录

![image-20220425081226821](image-20220425081226821.png)

## Sums

![image-20220425081301019](image-20220425081301019.png)

## Variants

将sum types加上标签，可以泛化为variants

$T_1+T_2⟹<l_1:T_1,l_2:T_2>$

$inl\;t \; as\; T_1+T_2⟹<l_1=t>as<l_1:T_1,l_2:T_2>$

![image-20220425081901304](image-20220425081901304.png)



## 链表

![image-20220425081951576](image-20220425081951576.png)



## 引用

![image-20220425082037174](image-20220425082037174.png)

![image-20220425082101285](image-20220425082101285.png)

## 异常处理

![image-20220425082132914](image-20220425082132914.png)

# 子类型

## 性质

引理：

- 如果 $S<:T_1→T_2$，那么 $S$ 具有 $S_1→S_2$ 的形式，其中 $T_1<:S_1，S_2<:T_2$ 。

- 如果 $S<:\{l_i:T_i^{(i∈1..n)}\}$，那么S具有 $\{k_j:S_j^{(j∈1..m)}\}$ 的形式，其中 $\{l_i^{(i∈1..n)}\}⊆ \{k_j^{(j∈1..m)}\}$，且对每个共同的标签 $l_i=k_j$ 都有 $S_j<:T_i$。

# 递归类型

利用运算符μ表示递归与重复的部分

【例】

- $NatList=μX. <nil:Unit, const\;\{Nat,X\}>;$

- 令 NatList 为一个无穷类型，满足方程 $X=<nil:Unit, const\;\{Nat,X\}>$



![image-20220425083522772](image-20220425083522772.png)

【例】

一个hungry函数，接收一个参数，然后返回一个函数，返回的函数仍然是一个hungry函数：

 $Hungry=μA. Nat→A;$

![image-20220425083619096](image-20220425083619096.png)

【例】

$Stream=μA. Unit→\{Nat,A\};$

![image-20220425083831461](image-20220425083831461.png)

![image-20220425083939883](image-20220425083939883.png)

![image-20220425084001852](image-20220425084001852.png)



## 形式化定义

![image-20220425084227411](image-20220425084227411.png)

【例】

![image-20220425084239975](image-20220425084239975.png)

# 多态

类型变量与替换。为了实现多态，可以使用一些变量作为占位符，需要的时候再替换成实际的类型。

类型的替换由两部分组成：

- 声明一个映射σ，将类型变量映射到具体的类型

- 应用一次映射T，得到一个实例σ T

【例】

$σ=[X↦Bool,Y↦Nat,Z↦Nat→Bool]$

$σ (X→X)=Bool→Bool$

## System F

![image-20220425084918399](image-20220425084918399.png)





【例】多态链表

![image-20220425084850171](image-20220425084850171.png)

![image-20220425084822794](image-20220425084822794.png)

【例】二叉树

![image-20220425085034018](image-20220425085034018.png)

![image-20220425085049875](image-20220425085049875.png)

# 求值规则

![image-20220425073948600](image-20220425073948600.png)

![image-20220425074005461](image-20220425074005461.png)



![image-20220425075633102](image-20220425075633102.png)



![image-20220425075719465](image-20220425075719465.png)

![image-20220425075738464](image-20220425075738464.png)

![image-20220425080217670](image-20220425080217670.png)

## 子类型

![image-20220425082329021](image-20220425082329021.png)

![image-20220425082341750](image-20220425082341750.png)

![image-20220425082346014](image-20220425082346014.png)



## lso-recursive 

![image-20220425084044818](image-20220425084044818.png)

## 约束求解

![image-20220425084707029](image-20220425084707029.png)

![image-20220425084730611](image-20220425084730611.png)

![image-20220425084750821](image-20220425084750821.png)





