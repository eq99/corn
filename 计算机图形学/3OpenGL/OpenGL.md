# Sierpinski 镂垫

在坐标系内有三个不共线的点，Sierpinski 镂垫构造过程如下：

- 在三角形内随机的选取一个初始点 $p$
- 随机选取3个顶点之一
- 找出 $p$ 和这个顶点的中点 $q$，并显示
- 用这个中点 $q$ 代替 $p$
- 转到第二步，重复。



它的伪代码可以表示为：

```c
main(){
  initialize_the_system();
  p = find_initial_point();
  for(some_number_of_points){
    q=generate_a_point(p);
    store_the_point(q);
    p=q;
  }
  send_all_points_to_GPU();
  display_data_on_GPU();
  cleanup();
}
```

以上算法有两个核心部分：生成点和显示点。因此引出两个问题：

- 怎样表示空间中点？
- 应该使用二维表示，三维表示还是其他表示？

