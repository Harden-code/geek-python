# 专业学习
PS=[('PS','专业学习','#calRatio({#DK,7.0,#MT,3.0})','ROOT','PS'),
  ('BK','基础知识','#calRatio({#DBK,7.0,#MBK,3.0})','PS','PS'),
          ('DBK','病种基础知识','#calRatio({#DBKT,7.0,#DBKV,3.0})','BK','PS'),
            ('DBKT','病种基础知识考试','','DBK','PS'),
            ('DBKV','成交量','','DBK','PS'),
          ('MBK','药品基础知识','#calRatio({#MBKT,7.0,#MBKV,3.0})','BK','PS'),
            ('MBKT','药品基础知识','','MBK','PS'),
            ('MBKV','成交量','','MBK','PS'),
  ('DK','底蕴知识','#calRatio({#DDK,7.0,#MDK,3.0})','PS','PS'),
          ('DDK','病种底蕴知识','#calRatio({#DDKT,7.0,#DDKV,3.0})','DK','PS'),
            ('DDKT','病种底蕴知识考试','','DDK','PS'),
            ('DDKV','病种底蕴知识成交量','','DDK','PS'),
          ('MDK','药品底蕴知识','#calRatio({#MDKT,7.0,#MDKV,3.0})','DK','PS'),
            ('MDKT','药品底蕴知识考试','','MDK','PS'),
            ('MDKV','药品底蕴知识成交量','','MDK','PS')]


# -- 2.商品营销 - marketing and sales
MDS=[('MDS','商品营销','','ROOT','MDS'),
  ('SM','卖得多','','MDS','MDS'),
      ('SC','品类多','','SM','MDS'),
          ('MC/EM','品类多/考试成绩','','SC','MDS'),
          ('MC/SM','品类多/销售指标','','SC','MDS'),
              ('OAOC','一单一品率','','MC/SM','MDS'),
              ('A1C','A1关联搭配率','','MC/SM','MDS'),
      ('MQ','数量多','','SM','MDS'),
          ('MQ/EM','数量多/考试成绩','','MQ','MDS'),
          ('MQ/SM','数量多/销售指标','','MQ','MDS'),
            ('CM','客品数','','MQ/SM','MDS'),
            ('POO','套餐订单成交量','','MQ/SM','MDS'),
  ('SE','卖得贵/好','','MDS','MDS'),
      ('A1SOU','A1销售量占比','','SE','MDS'),
      ('A1SOV','A1销售额占比','','SE','MDS')]


# -- 3.客户接待 - receptionist

Re=[('R','客户接待','','ROOT','R'),
      ('RP','接待流程','','R','R'),
          ('R/EM','接待流程/考试指标','','RP','R'),
          ('R/SM','接待流程/销售指标','','RP','R'),
              ('V','成交量','','R/SM','R'),
              ('NMDV','新会员动销率','','R/SM','R'),
              ('FCV','客户好评率','','R/SM','R'),
       ('RA','接待态度','','R','R')]


# -- 4.流量配置 - flow arrangement

FA= [('FA','流量维护','','ROOT','FA'),
      ('MN','维护数量','','FA','FA'),
          ('MN/EM','维护数量/考试指标','','MN','FA'),
          ('MN/MM','维护数量/维护指标','','MN','FA'),
              ('NMN','会员拉新人数','','MN/MM','FA'),
              ('WFN','企微好友数','','MN/MM','FA'),
              ('AWFN','企微好友添加人数','','MN/MM','FA'),
      ('MQ','维护质量','','FA','FA'),
          ('FM','首次维护','','MQ','FA'),
              ('NMVR','非会员成交量占比','','FM','FA'),
              ('NWVR','非企微好友成交量占比','','FM','FA'),
          ('AM','再次维护','','MQ','FA'),
              ('RR','复购率','','AM','FA'),
              ('PRR','专人复购率','','AM','FA')]


from anytree import Node, RenderTree
import random

def findRoot(arr:list) -> Node:
    for tuples in arr:
        if(tuples[3]=='ROOT'):
            return Node(tuples[0])
    raise Exception("NO-ROOT")

# root = Node(rootValue['name'])
# node = Node(v['name'], parent=rootNode)
def dfs(arr:list,root:Node):
    for ele in arr:
        if(ele[3]==root.name):
            node = Node(ele[0],parent=root,line=ele)
            dfs(arr,node)

def cheker(data):
    rootNode=findRoot(data)
    dfs(data,rootNode)
    print(RenderTree(rootNode))


# 0 code ; 1 name ; 2 scope ;  3 parent ; 4 root
#


def graph_code_sql(arr:list)->list:
    result=[]
    for ele in arr:
        a = list(ele)
        a.append('harden')
        a.append('2305')
        for _,i in zip(a,range(len(a))):
            a[i]=f"'{_}'"
        a[2]=str(random.randint(1, 5))
        data=','.join(a)
        result.append(f'INSERT INTO EMPLOYER_RECORD_HISTORY (graph_code,graph_name,scope_record,parent_graph_code,root_graph_code,employer_id,version) VALUES ({data});\n')
    return result


# cheker(PS)
# cheker(MDS)
# cheker(FA)
# cheker(Re)

sql = graph_code_sql(Re)
with open("sql.txt",'a',encoding='utf-8',newline='\n') as fd:
    for _ in sql:
        fd.writelines(_)

