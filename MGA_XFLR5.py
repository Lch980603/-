# 東海大学
# 工学研究科　機械工学専攻
# 稲田研究室　
# 1CEMM106　李春暉

import pandas as pd             #36行使った、xflr5出力したデータを読み込みため
import numpy as np              #計算の核　（重要！）
import pyautogui as py          #自動化ライブラリ、インタネットで調べると使い方がすぐ出る、簡単です
import time                     #パソコン計算は速いから、xflr5の計算を待つため使う


CROSS_RATE = 0.6                 #交差率（感染率）
MUTATION_RATE = 0.03             #突然変異率　      （今後この2つのパラメーターは自動適応を目指す、資料を調べてください）
WHOLE_DNA_SIZE=60                #進化全体のDNAの長さ　　　パラメーターを増やすと長さを増加する
PARAMETER_DNA_SIZE=15            #各パラメーターのDNAの長さ
POP_SIZE = 10                    #一世代の子供の個体数
Wing1_span_BOUND = [0, 10]       #範囲設定
Wing2_span_BOUND = [0, 10]       #範囲設定
DisFaB_BOUND=[-3,3]              #範囲設定
DisUaD_BOUND=[-1,1]              #範囲設定
GENERATIONS_N = 0                #循環記録
NUMBER_OF_CALCULATIONS=100       #世代数



class XFLR5(object):
    def get_value(self,line):
        string = line[0]
        list_str = string.split(' ')
        list_float = [float(s) for s in list_str if s]
        return list_float[2] / list_float[5]

    def get_MaxLD(self):
        time.sleep(2)
        max_value = 0
        df = pd.read_csv('D:\\pythonProject1\\venv\\串型飛行機\\数据\\text1\\7...txt') #xflr5分析した結果の保存ルート（Macはどのような形はわかりません）
        for i in range(4, df.shape[0]):
            value = self.get_value(df.values[i, :])
            if not max_value:
                max_value = value
            else:
                if max_value < value:
                    max_value = value
        print('xflr5計算結果',max_value)
        return max_value                           #←　　ここまではxflr5計算した結果のTXTファイルを分析して最大揚抗比を計算です

    def fit(self):
        Martix = np.zeros((1, POP_SIZE), dtype=float)
        FIT = open('揚抗比計算世代' + str(GENERATIONS_N) + '.txt')  #記録と同時に以後計算のとき読み込む
        lines = FIT.readlines()
        Martix_row = 0
        for line in lines:
            list = line.split(' ')
            Martix[Martix_row:] = list[0:POP_SIZE]
            Martix_row += 1
        return (Martix)

    def xflr5(self,x,y,z,k):           #xflr5の自動操作

        py.click(296, 73)
        py.rightClick(696, 363)
        py.moveTo(1026, 387, duration=0.5, tween=py.easeInOutQuad)
        py.click(1009, 417, duration=0.5, tween=py.easeInOutQuad)
        py.click(608, 539, duration=0.5, tween=py.easeInOutQuad)
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.typewrite(str(x))  # 前翼角度

        py.click(993, 538, duration=0.5, tween=py.easeInOutQuad)
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.typewrite(str(y))  # 後翼角度


        py.click(986, 473, duration=0.5, tween=py.easeInOutQuad)
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.typewrite(str(z)) #　前後距離

        py.click(999, 510, duration=0.5, tween=py.easeInOutQuad)
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.keyDown('delete')
        py.typewrite(str(k))  # 上下距離

        py.click(1032, 854, duration=0.5, tween=py.easeInOutQuad)
        py.click(979, 552, duration=0.5, tween=py.easeInOutQuad)
        py.click(203, 218, duration=0.5, tween=py.easeInOutQuad)
        py.click(1758, 337, duration=0.5, tween=py.easeInOutQuad)
        py.click(1387, 852, duration=2, tween=py.easeInOutQuad)
        
        py.rightClick(500, 600, )
        py.moveTo(600, 650, duration=0.5, tween=py.easeInOutQuad)
        py.moveTo(800, 650, duration=0.5, tween=py.easeInOutQuad)
        py.click(935, 900, duration=0.5, tween=py.easeInOutQuad)
        py.typewrite('7..')                                       #xflr5の計算結果のファイル名（簡単して方がいい、読み込むときし易い）
        py.click(1033, 683, duration=0.5, tween=py.easeInOutQuad)
        py.click(1706, 722, duration=0.5, tween=py.easeInOutQuad)
        py.click(1030, 528, duration=0.5, tween=py.easeInOutQuad) #↑ここまで自分のパソコンに合うよに（「座標確定」プログラムを使用）（外部スクリン使用をおすすめです）



        CL_CD = self.get_MaxLD()    #33行の揚抗比計算を呼び出す


        f = open('揚抗比計算世代' + str(GENERATIONS_N) + '.txt', "a+")  #MGA計算のとき読み込むから、プログラムと同じファイルを保存
        f.write(str(CL_CD) + ' ')                                    #データの間間隔を開けて、EXCEL変更し易い
        f.close()
        f = open("揚抗比記録.txt", "a+")
        f.write('前翼角度' +'  '+ str(x)+'  ' +'後翼角度' +'  '+ str(y)+'  '+'前後距離' +'  '+ str(z)+'  '+'上下距離' +'  '+ str(k)+'  '+'最大揚抗比' +'  '+ str(CL_CD) + '  ')
        f.close()                                                     # 今後パラメーターを増やすときここ忘れない

class MGA(object):                    #MGA(pythonのClass部分を勉強して)
    def __init__(self,WHOLE_DNA_size,PARAMETER_DNA_size,DNA_bound,cross_rate,mutatuon_rate,pop_size):
        self.WHOLE_DNA_size=WHOLE_DNA_size
        self.PARAMETER_DNA_size=PARAMETER_DNA_size
        DNA_bound[1]+=1
        self.DNA_bound=DNA_bound
        self.cross_rate=cross_rate
        self.mutation_rate=mutatuon_rate
        self.pop_size = pop_size
        self.pop= np.random.randint(2, size=(POP_SIZE, WHOLE_DNA_SIZE)) #コーディング（ランダム初期値、1行で実現できる）

    def F(self):
        fit = XFLR5().fit()
        fit_array = []
        for i in fit:
            for j in i:
                fit_array.append(j)
        GROUP_CLCD = np.array(fit_array)  #xflr5の計算結果を行列化

        return GROUP_CLCD


    def decode_w1span_DNA(self, Wing1_spanpop):           #デコード（論文の3.2.2に参考する、公式がある）（↓ここはややこしい、僕のミスです、一つにまとめことができると思います、自分でやってみよう）
        return Wing1_span_BOUND[0]+Wing1_spanpop.dot(2 ** np.arange(self.PARAMETER_DNA_size)[::-1]) * (Wing1_span_BOUND[1]-Wing1_span_BOUND[0])\
               / float(2 ** self.PARAMETER_DNA_size - 1)

    def decode_w2span_DNA(self, Wing2_spanpop):
        return Wing2_span_BOUND[0]+Wing2_spanpop.dot(2 ** np.arange(self.PARAMETER_DNA_size)[::-1]) * (Wing2_span_BOUND[1]-Wing2_span_BOUND[0] )\
               / float(2 ** self.PARAMETER_DNA_size - 1)

    def decode_DISFaB_DNA(self, DISFaBpop):
        return DisFaB_BOUND[0]+DISFaBpop.dot(2 ** np.arange(self.PARAMETER_DNA_size)[::-1])*(DisFaB_BOUND[1]-DisFaB_BOUND[0]) \
               / float(2 ** self.PARAMETER_DNA_size - 1)
    def decode_DISUaD_DNA(self, DISUaDpop):
        return DisUaD_BOUND[0]+DISUaDpop.dot(2 ** np.arange(self.PARAMETER_DNA_size)[::-1])*(DisUaD_BOUND[1]-DisUaD_BOUND[0])\
               / float(2 ** self.PARAMETER_DNA_size - 1)

    def get_fitness(self,prouduct):
        return prouduct

    def crossover(self, loser_winner):   #交差（感染）　　核心！！！
        cross_idx = np.empty((self.WHOLE_DNA_size,)).astype(np.bool_)
        for i in range(self.WHOLE_DNA_size):
            cross_idx[i] = True if np.random.rand() < self.cross_rate else False
        loser_winner[0, cross_idx] = loser_winner[1, cross_idx]
        return loser_winner

    def mutate(self, loser_winner):     #突然変異　　　　核心！！！
        mutation_idx = np.empty((self.WHOLE_DNA_size,)).astype(np.bool_)
        for i in range(self.WHOLE_DNA_size):
            mutation_idx[i] = True if np.random.rand() < self.mutation_rate else False
        loser_winner[0, mutation_idx] = ~loser_winner[0, mutation_idx].astype(np.bool_)
        return loser_winner

    def microbial(self, n):

        raw = self.pop
        index = np.random.permutation(10)
        pop_random    = raw[index]
        Wing1_spanpop = pop_random[:, 0:15]    #各パラメーター（パラメーターを増やすとこここ忘れない）
        Wing2_spanpop = pop_random[:, 15:30]
        DISFaBpop     = pop_random[:, 30:45]
        DISUaDpop     = pop_random[:, 45:60]
        print('前翼角度', self.decode_w1span_DNA(Wing1_spanpop))
        print('後翼角度', self.decode_w2span_DNA(Wing2_spanpop))
        print('前後距離', self.decode_DISFaB_DNA(DISFaBpop))
        print('上下距離', self.decode_DISUaD_DNA(DISUaDpop))
        MENBER_CODE = -1
        for _ in range(self.pop_size):
            MENBER_CODE = MENBER_CODE + 1
            W1_span = round(self.decode_w1span_DNA(Wing1_spanpop)[MENBER_CODE], 3)
            W2_span = round(self.decode_w2span_DNA(Wing2_spanpop)[MENBER_CODE], 3)
            DisFaB =round(self.decode_DISFaB_DNA(DISFaBpop)[MENBER_CODE], 3)
            DisUaD = round(self.decode_DISUaD_DNA(DISUaDpop)[MENBER_CODE], 3)
            f = open('前翼世代' + str(GENERATIONS_N) + '.txt', "a+")
            f.write(str(W1_span) + ' ')
            f.close()
            f = open('後翼世代' + str(GENERATIONS_N) + '.txt', "a+")
            f.write(str(W2_span) + ' ')
            f.close()
            f = open('距離前後' + str(GENERATIONS_N) + '.txt', "a+")
            f.write(str(DisFaB) + ' ')
            f.close()
            f = open('距離上下' + str(GENERATIONS_N) + '.txt', "a+")
            f.write(str(DisUaD) + ' ')
            XFLR5().xflr5(W1_span, W2_span,DisFaB,DisUaD)   #デコードした数字を記録とxflr5の入力
            pick1=-2
            pick2=-1
        for _ in range(n):

            fitness=self.get_fitness(self.F())
            print(fitness)
            time.sleep(1)                    #順番で比較
            pick1 = pick1 + 2
            pick2 = pick2 + 2

            sub_pop_idx = [pick1, pick2]
            sub_pop =pop_random [(sub_pop_idx)]
            fitness_sort=fitness[sub_pop_idx]

            loser_winner_idx = np.argsort(fitness_sort)
            loser_winner = sub_pop[loser_winner_idx]

            loser_winner = self.crossover(loser_winner)    #Class(MGA)呼び出す
            loser_winner = self.mutate(loser_winner)
            self.pop[(sub_pop_idx)] = loser_winner


        W1_S = self.decode_w1span_DNA(Wing1_spanpop)
        W2_S = self.decode_w2span_DNA(Wing2_spanpop)
        DIS_FaB=  self.decode_DISFaB_DNA(DISFaBpop)
        Dis_UaD=self.decode_DISUaD_DNA(DISUaDpop)
        pred = fitness
        time.sleep(1)

        return W1_S,W2_S ,DIS_FaB,Dis_UaD,pred                     #パラメーターを増やすときここ忘れない

ga=MGA(WHOLE_DNA_size=WHOLE_DNA_SIZE,PARAMETER_DNA_size=PARAMETER_DNA_SIZE,DNA_bound=[0,1],cross_rate=CROSS_RATE,mutatuon_rate=MUTATION_RATE,pop_size=POP_SIZE)

for _ in range(NUMBER_OF_CALCULATIONS):
    GENERATIONS_N = GENERATIONS_N + 1


    print('第',GENERATIONS_N,'世代')


    f = open("揚抗比記録.txt", "a+")
    f.write('\n')
    f.close()
    W1_S,W2_S,DIS_FaB,DIS_UaD,pred=ga.microbial(5)          #パラメーターを増やすときここ忘れない
