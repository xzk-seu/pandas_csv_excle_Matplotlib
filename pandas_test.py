import pandas as pd
import matplotlib.pyplot as plt


def merge_stat():
    data_dict = dict()
    for y in range(2008, 2018+1):
        data = pd.read_csv('Statistic/%d.csv' % y)
        data_dict[y] = data['count']
    merge_df = pd.DataFrame(data_dict)
    merge_df.to_excel('stat.xlsx', sheet_name='Sheet1')


def stat_year(year):
    df = pd.read_csv('Statistic/%d.csv' % year)
    df['date'] = pd.to_datetime(df['date'])
    plt.plot(df['date'], df['count'], '.', label=str(year))  # 折线1
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()


def pic_gen(start, end):
    # 生成一张图片
    for y in range(start, end+1):
        df = pd.read_csv('Statistic/%d.csv' % y)
        df['date'] = pd.to_datetime(df['date'])
        plt.plot(df['date'], df['count'], '.', label=str(y))
    plt.xticks(rotation=45)  # 控制x轴数据旋转角度
    plt.legend(loc='best')
    plt.grid(True)
    if start != end:
        plt.savefig('pic\%d-%d.png' % (start, end), dpi=500)
    else:
        plt.savefig('pic\%d.png' % start, dpi=500)
    plt.show()
    plt.cla()


if __name__ == '__main__':
    s = input('start: ')
    s = int(s)
    e = input('end: ')
    e = int(e)
    pic_gen(s, e)
    # for i in range(2008, 2018):
    #     print(i)
    #     pic_gen(i, i)
    # for i in range(1, 6):
    #     s = 2008
    #     while s+i <= 2018:
    #         print('%d-%d' % (s, s+i))
    #         pic_gen(s, s+i)
    #         s += i
