Brute force.py
Function部分
union : 用來將兩個不同的itemset做聯集
support:計算該itemset的support值
confidence:計算 itemset_a  => itemset(a&b) 的confidence值






Apriori.py

Function部分
create_C1 :用來初始化引入的itemset
is_apriori: 用來測試是否滿足先驗的條件
	Ck_item :  candidate k-itemsets
	Lksub1: Lk-1 
generate_Lk_by_Ck: 由候選的frequent_itemset 找出滿足條件的下一層Lk
generate_L: 列出所有滿足條件的frequent itemset (>min_support)
generate_big_rules:列出所有Big Rules

主程式部分:
可以調整的參數有
k (輸出結果中最長的itemset長度為k)
min_support
min_conf

FP_Growth.py

請參考該程式中的說明
