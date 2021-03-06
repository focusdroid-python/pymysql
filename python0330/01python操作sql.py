
from pymysql import connect

class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user='root', password='focusdroid', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    def search(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = "select * from goods"
        self.search(sql)

    def show_one_items(self):
        sql = 'select name from goods_cates'
        self.search(sql)

    def show_two_items(self):
        sql = 'select name from goods_brand'
        self.search(sql)

    @staticmethod
    def print_muem():
        print('----京东----')
        print('所有的商品')
        print('所有的商品分类')
        print('所有的商品品牌分类')
        return input('请输入对应的功能')

    def run(self):
        while True:
            num = self.print_muem()
            if num == '1':
                # 查询所有的方法
                self.show_all_items()
            elif num == '2':
                # 查询分类
                self.show_one_items()
            elif num == '3':
                # 查询品牌分类
                self.show_two_items()
            elif num == '4':
                return
            else:
                print('**********输入有误************')


def main():
    # 1. 创建京东商城对象
    jd = JD()

    #2. 调用这个对象的run方法
    jd.run()

if __name__ == '__main__':
    main()