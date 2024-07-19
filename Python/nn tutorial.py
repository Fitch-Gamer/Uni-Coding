
import numpy as np
import nnfs
import random

nnfs.init()
np.random.seed(0)



class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)

class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs-np.max(inputs,axis=1,keepdims=True))
        probabilities = exp_values/np.sum(exp_values,axis=1,keepdims=True)
        self.output = probabilities

class Loss:
    def calculate(self,output,y):
        sample_losses = self.forward(output,y)
        data_loss = np.mean(sample_losses)
        return data_loss
    

class Loss_CategoricalCrossentropy(Loss):
    def forward(self,y_pred,y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if(len(y_true.shape)==1):
            correct_confidences = y_pred_clipped[range(samples),y_true]

        elif(len(y_true.shape)==2):
            correct_confidences = np.sum(y_pred_clipped*y_true,axis = 1)
        
        negative_log_liklihoods = -np.log(correct_confidences)
        return negative_log_liklihoods

def RandArr(a:int,Chance):
    out = np.zeros(shape = a,dtype=float)
    x = 0
    for j in out:
        if(random.randrange(0,100)>Chance*100):
            out[x] = 1.0
        else:
            out[x] = 0.0
        x+=1
    return out

TrainingData = np.loadtxt(open("C:\\Users\\fitch\\Downloads\\spamclassifier\\data\\testing.csv"), delimiter=",").astype(int)
TestingData = np.loadtxt(open("C:\\Users\\fitch\\Downloads\\spamclassifier\\data\\testing_spam.csv"), delimiter=",").astype(int)
XnNP = []
ynNP = []

InputNum = 54

NeuronNum = [16,32,32,16]

Training = False

Layers:Layer_Dense = []

Activations:Activation_Softmax = []

if (Training):
    for t in TrainingData:
        ynNP.append(t[0])
        XnNP.append(t[1:])
else:
    for t in TestingData:
        ynNP.append(t[0])
        XnNP.append(t[1:])

X = np.array(XnNP)
y = np.array(ynNP)

for i in range(0,len(NeuronNum)):
    if(i==0):
        Layers.append(Layer_Dense(InputNum,NeuronNum[i]))
    else:
        Layers.append(Layer_Dense(NeuronNum[i-1],NeuronNum[i]))
    Activations.append(Activation_Softmax())

if(not Training):
    
    Layers[0].weights = np.array([[-2.132434,0.5824581,-0.92290163,-1.0762962,1.706211,-1.0814365,-1.009226,-0.8012276,-1.3725691,0.944866,1.5803599,-1.7348794,1.1333082,0.632979,-3.0349653,1.3044068],[-1.507524,-0.18035468,-1.0100821,0.12526178,-0.07623053,0.023032669,-0.57257956,0.11589782,-0.6141138,1.9396693,-1.3600101,1.2563202,0.47844073,-1.3779299,0.23246258,2.699886],[-0.58385885,2.6772826,-0.043790214,-0.0995716,1.5287871,1.8642803,-0.25677475,1.1040653,-0.14545779,-1.3655436,0.069502406,-1.2011522,-2.3239677,-0.06339254,2.3849049,-0.68328136],[0.8328929,0.77305067,2.5777493,1.0032293,-0.67962015,-0.10468233,0.3910927,0.5654801,1.4348471,4.0232763,-0.48469004,1.2598938,0.7810209,0.7272392,-0.19383976,-0.19746412],[1.4447283,2.6631463,-0.34668553,0.9873159,-1.298388,-2.5157182,-0.49738634,0.30183536,-2.3494325,0.3308786,0.2201694,0.03170204,0.033238087,-1.0267987,-0.7060753,0.6933114],[-0.5849867,3.1072857,0.042351108,0.013748653,0.16397272,-0.3765297,0.440164,-0.09553237,-0.943856,-0.38188085,-0.90285504,1.0848714,1.7842451,-0.7820952,-0.2569024,-1.3977814],[1.9943562,-1.0825964,2.3613157,3.2976327,-1.1810837,-2.2442985,1.207643,-1.1962317,-1.8660845,-1.0009063,0.60042673,-1.2545664,-0.3297956,-2.702736,-1.1189892,1.396662],[-0.4893921,2.8213356,2.3590553,0.3328445,0.3764918,-1.0366408,-0.25892437,-0.7787495,-1.3026403,-2.009236,1.9484041,1.8352798,-1.838764,1.454053,-0.467535,0.46547574],[-0.37870046,-1.7602136,1.0735544,0.9549015,1.8384817,2.7718878,0.9396886,-1.1046588,0.59758055,1.117501,-2.279587,-0.091312066,-0.01834155,1.073398,0.9436244,-0.027541563],[-1.1182841,-0.19949177,0.07609807,0.28664982,-0.11559161,-0.20747715,-0.5647786,-0.37784454,0.91010654,-2.4511664,-0.8317157,1.7821193,1.4208608,0.8976499,0.5220069,-3.9662874],[-1.2981042,0.21648134,1.3557383,1.2757528,-1.9753703,0.9603597,1.8927459,-0.019692877,-0.5876535,2.2199128,-0.52674335,1.0156392,-1.4515045,0.6241545,-0.57501686,1.0368798],[-1.4924994,-0.9694112,0.86183214,-0.55623716,-1.3977381,2.3899388,-1.2746975,-1.2186484,-1.3805947,0.8986212,-0.42871818,-0.4209947,0.52661335,0.71856457,-1.2785867,1.1418892],[-0.73913604,2.0439827,0.77036774,-0.8270508,1.9491752,0.84617776,1.8110253,0.35565346,0.09767594,0.7463027,0.94742304,-1.1081836,0.13460866,0.927529,0.6531016,1.085084],[1.8457189,0.45453256,-2.4534714,0.4433465,0.6679783,0.18483308,-0.7989104,-0.104094766,0.7882192,0.08702189,-1.4349809,-0.3209106,2.4952786,2.0187416,0.4891458,1.098304],[1.0198386,0.55689263,1.216211,0.035959456,-1.254934,0.15711053,-2.58831,-0.6252425,1.2905667,-2.0831897,-0.40804303,0.76693183,0.032412652,-0.7644923,-2.1114287,-0.28366724],[-1.5728105,0.8479388,-1.2657305,1.7684202,1.1929247,-0.13909839,0.95869684,-0.40070432,-2.342078,-0.46936697,0.77152497,-0.98289776,1.007439,-0.47291782,1.1872778,1.784809],[-3.2773159,-1.4914902,0.5517089,1.3032587,1.8369005,-0.8533825,-2.4374082,0.6446403,-0.55959934,-1.519222,0.7282341,-0.3890135,-0.061499573,0.72833335,-1.2675185,-0.3286295],[-0.06265851,1.0470285,1.1660016,0.30255526,-0.41202164,-0.19259238,4.8652945,-0.046227515,-1.346358,1.4052266,1.7577723,0.17341128,-0.49055102,0.6303823,1.832341,-2.4063718],[-0.8303826,-2.7615657,-2.5277634,-0.44560447,-2.3989909,-0.5533098,-1.1063492,0.28155005,0.34874624,-3.8636427,-0.82822603,0.013057354,-1.5997258,-0.37007532,-0.86767626,-0.97025746],[-0.4038275,-0.3051524,0.9826888,2.0973048,-2.4239988,-0.5732995,-0.19313884,1.0181471,-0.20146963,0.05947242,-0.6963563,1.0792816,-0.84408313,-1.2477517,-0.7137064,2.5483367],[1.4494642,-2.4960291,-0.55476177,1.047918,0.029219437,-1.4622577,-0.9226419,1.7503086,1.4182992,-0.5303262,0.7941556,-1.870272,0.47946972,-0.3462231,-2.266424,-1.2307076],[0.16611978,-0.93797743,0.055618342,1.8868628,0.13475205,0.43344817,0.016095966,-0.47452286,-0.22831228,1.2932018,0.5706813,1.1373355,-0.93312716,0.7719534,-1.3678951,-0.1812404],[0.32006022,0.93670297,0.5223264,2.1520035,-1.2314117,-0.24498925,-0.3620051,1.9700656,-1.768522,0.84120595,0.5881085,-2.448624,-0.67943084,2.6574934,2.7914941,-0.21767765],[1.0581887,-2.7415035,0.17718205,1.428942,1.2346921,-0.42091313,0.14737186,-1.7971333,0.8986649,-2.8101335,-0.57476157,0.3660185,-0.2744505,-0.18115447,0.83437145,-0.17586264],[-1.2901402,-0.094533354,-0.12376187,-2.0396943,0.6508778,-2.7218828,-0.2698182,1.6966668,-2.0992746,0.6153988,-0.4598432,0.34769967,-0.28517264,2.750836,-2.0874598,2.9039087],[1.6023536,-0.68449676,0.9900806,1.3012439,1.2102922,1.7004014,-2.692558,-0.887151,0.11843373,-1.9270234,0.5838047,1.83246,-1.7299905,3.8510685,-1.2425627,0.47601005],[-0.15265162,1.1286958,1.0042977,-1.0091877,-0.3413348,0.37626562,0.12478492,4.3128166,0.5119819,1.6388284,-0.8621103,0.6371973,0.14967711,2.0176353,-1.0584577,0.61790603],[-3.6562433,4.5185156,-1.1688806,-1.4290512,-1.1862626,0.3535154,0.7127398,0.11042023,0.05220417,-0.57373095,-2.9124513,0.27717987,1.23667,0.4996304,-1.9036181,0.2145706],[-0.67837393,-1.4412,0.16259748,-0.92973226,-0.4562216,-0.6069966,3.4758842,0.6723434,0.8532549,-2.074319,-0.59779525,0.96164674,0.13327053,0.1283788,-0.2763182,-1.0942655],[-1.4165212,2.370248,0.47311255,0.3924601,-1.5030441,-0.96619225,-2.1443474,0.4826665,-0.6796,-1.7649784,2.3159873,0.18237047,1.2794632,1.877259,-0.39604682,-1.4051802],[-0.61536676,2.6096106,-0.5052244,0.8190703,-0.8432776,0.8358307,0.62321407,1.6391313,-0.43099532,-0.17361832,-1.3712653,0.8977234,-2.9180565,1.2321148,2.5073647,2.5400362],[1.1832212,0.27439153,0.29004088,-2.2712271,0.72190297,0.4861113,1.288952,0.20243365,0.7274666,-0.56767064,0.94817865,0.1040735,0.2794639,0.9232548,-0.48084635,0.6649686],[1.0949881,1.9255606,0.19244492,0.15316404,0.37452376,-0.019948518,-1.433411,-1.1238484,-2.9055014,-1.1200243,0.013140134,0.2650325,2.69356,0.66688937,0.83832586,-0.90476614],[2.7328267,-0.81650794,-2.6679127,-1.1326864,-1.6880274,0.26273906,-1.6232954,-2.0658824,-2.184266,0.22768112,1.5262866,-0.5793134,1.578901,0.82708484,-0.5969775,-1.806904],[-0.92964715,1.4788291,0.009007055,-0.7880002,0.5667121,0.5230428,2.4923368,0.9377354,2.274926,-1.9313507,-1.5721347,0.34720495,0.08315456,-0.8606807,0.72191316,-2.6910272],[-2.2959752,1.9130843,-1.2273185,-0.09814448,0.38241827,-1.4855295,0.3543109,-0.66198057,-1.7430816,0.66847837,-2.9417613,-3.2849393,0.91134113,0.18410556,-0.631925,-1.0529253],[-1.8416344,-1.5024079,-1.6168957,0.656734,-2.072871,-0.0060836785,-1.8324447,2.941632,0.38181335,0.5155254,-1.3228658,-2.0392714,-1.6495565,-2.62767,-0.6512097,1.4814777],[-0.3834368,0.23987019,0.6095127,0.29641291,1.0274917,-0.19741705,-3.076675,1.450398,-1.1438885,0.9179717,3.22829,1.0768093,1.3433427,-0.93853915,0.807895,0.33065653],[0.88666904,-1.1269526,-1.5393462,-0.5088172,1.6907264,0.5178782,-0.78345937,0.9026762,2.7376893,0.31053793,0.37377954,0.061031826,-0.262938,0.23942323,-0.53617865,0.0056954473],[-0.010313608,0.31439012,2.2274685,0.20517412,0.7460897,-1.1004928,-0.5635351,-1.3473775,-2.3698258,-0.7061134,-1.9810525,0.99931,-0.46315822,0.51718557,-0.41526833,0.5312288],[-1.4357445,0.6186235,2.4772823,-2.9050915,-1.5317668,1.6225886,0.46395802,2.7275908,0.060549878,-1.0570115,0.8196908,-0.03395734,0.4254096,-1.2930446,-0.87708265,0.38389078],[-2.35332,1.6607186,0.6281258,-2.7394385,-0.07304609,-3.6179993,-1.7763038,1.0010653,-0.7151405,1.0312998,-0.2472724,0.9455444,0.11906996,-1.2184557,0.24728243,-0.26241657],[1.0916137,2.4154115,1.4770858,-0.37730604,0.32205,-0.030099213,0.82943475,-2.455879,0.37796268,0.94192564,-0.108642355,-0.9963861,2.4050171,-1.5598562,-1.3323251,-1.2278925],[0.23373707,-2.038123,-1.8984401,-2.330979,0.34368527,0.6929873,1.1581032,-0.3165656,0.26663572,-2.8873355,-0.25262097,-0.5171806,1.6664059,0.18238586,-0.6018494,-0.6760604],[1.4852966,0.017167628,0.12139445,0.9241799,-1.0380688,0.34016943,-3.4924355,3.3065135,1.9877038,0.4446046,-1.0526108,2.0235562,-1.1745821,0.38157457,-0.37581527,-0.20927058],[0.40278044,-1.9559317,0.7801682,-4.421017,-0.64775354,4.3793283,-0.13530296,3.434774,-0.73806304,0.9843531,0.93179727,-2.2940962,0.23261775,0.3079613,1.9322351,-0.031224195],[0.6234972,1.6418087,-0.24394464,1.5379449,0.35506496,-0.82893115,-2.6187308,0.11073957,3.5951722,1.3344204,0.32437813,1.0713857,0.80485624,1.281306,-1.0997856,0.048028447],[-0.6915084,0.25721136,1.7617258,-1.3150645,-0.03967371,1.4806778,0.6466915,0.64892566,2.6922083,-1.2279077,0.7621516,1.5747331,0.38197586,-0.46132058,-0.24221815,-1.9889796],[1.6169418,0.15862393,-0.17093183,0.583278,1.0781611,0.4190607,-1.6755632,0.40600634,-1.0322429,-1.9557484,2.5302467,1.0677506,-0.876283,-2.028113,-1.2548302,-0.3810869],[-1.8346944,-3.1073003,-1.4162036,-0.2570456,-0.75195616,3.1271026,-1.0921344,0.40929967,-0.66315156,-0.04603435,-2.0875034,0.22807091,-0.0013678186,1.2702141,-2.0012805,-0.5972372],[-0.2586324,0.7858921,1.4767479,1.2743378,-0.16743971,-0.8998169,1.2074533,1.3950065,-2.377342,1.7958335,1.2018045,-0.6750275,0.008459061,-0.24474494,-0.009368021,1.5210452],[3.6595192,-0.267303,0.5975937,0.7367304,-1.1232455,-2.245999,-1.2246192,-0.042020265,-0.25160614,1.1086495,-1.571828,1.857511,-0.18107097,-3.6815078,-0.6668256,-1.099666],[-1.0641185,-4.098037,-0.055571787,0.5086031,0.84884524,-1.6999178,-2.287269,-0.5445211,1.1832501,0.8034961,-0.56042993,-1.2551891,1.4327201,-1.9671625,0.7826958,-0.090899915],[-1.9284593,-2.0062845,-2.1483338,-1.950168,-0.38974074,0.3423748,-1.8605758,0.032291107,-0.8546757,-0.559261,1.2160751,0.83691645,-0.72754836,0.8728275,-1.4423256,-0.9685878]])

    Layers[0].biases = np.array([[-1.1074306,-0.9160727,0.8423353,1.7985464,-2.6765642,2.4095006,-1.1111047,-0.8271746,0.4556658,-0.50895447,-0.58909905,-1.4827538,-3.3179934,-0.5651257,-1.9767461,1.7728807]])

    Layers[1].weights = np.array([[-0.69729626,-2.3120313,0.4176873,-0.29721484,-0.4576451,-0.56554973,3.2565439,-0.3349905,0.53672576,0.6531887,-1.2601258,-0.1584678,-1.9401675,-0.062429804,0.05392412,-0.36356342,2.2409554,0.6926571,0.7681327,2.521573,-2.1154075,-2.7120135,-2.2328687,0.99390686,0.3947946,0.077604935,-1.3733903,-1.8915441,-1.3694326,-0.970615,0.5020944,1.0332698],[-2.297766,-0.3069904,2.2826407,0.49110556,-1.3338815,2.243734,0.22782248,-1.8516349,1.8620797,-0.82912004,-0.6208948,0.81679547,2.7897387,-0.65641683,-0.36687,-1.5654832,1.8170038,2.865397,-0.8147299,1.4317292,-1.1786033,1.121378,-0.93917483,-0.012797519,-0.9997647,-0.019857831,0.25487965,2.6678443,0.62350523,2.3222318,0.14446071,-0.8523832],[2.0979137,1.5867952,0.9265089,-0.7660874,-0.42175475,-1.8676466,0.20800704,-0.24050121,-1.318562,1.4452224,-0.15051816,-2.3415778,-0.5914921,-0.5249683,0.65222776,-0.48800716,0.44418493,0.33248624,-2.236912,-0.20075664,0.60818887,0.10823779,0.124894395,0.98678505,-1.8900583,-0.7633924,1.9023645,-2.3615112,-0.6943224,-0.5951214,-1.079523,0.15105054],[-1.7959872,0.4019377,1.6496339,-1.2059953,-2.2011814,2.3335872,-1.3856424,1.7633435,0.94292617,-2.5915241,-0.065536335,1.2094457,-2.0415213,2.5536463,-1.3607484,-0.050231773,-2.1481755,-0.9495528,-1.0866369,-1.3395606,0.21963555,-0.5200385,0.4757558,1.6072766,-1.255017,5.9640694,-0.40212798,-0.8335445,-0.26747596,-0.6686549,-1.7765956,1.0629777],[-0.67585635,0.1145214,0.42445347,-0.054047987,0.61519265,-0.21637765,-1.5992978,-0.89746577,0.60202473,-0.60907,0.43570837,-2.8543084,0.2912907,1.1906328,1.1990238,0.72864413,-1.1196243,-0.010582987,-0.26115853,0.1886823,2.5659509,-1.6396617,0.29025152,0.99610984,-1.4774691,1.0598367,-2.9187748,1.7709559,-1.0804834,0.43995076,-1.96957,-2.1752834],[0.8705551,-1.4753598,-0.08586858,-0.74515694,-0.3223923,2.6798987,-1.0732887,-1.0582834,0.32394028,-1.3240122,-0.9810827,0.23945138,-0.7726833,-0.5479307,-0.9070741,2.7931244,1.2153744,-0.9712105,0.67446226,-0.99544674,1.6586063,-0.7977611,-0.8192041,-0.7680945,-0.37258902,0.30630547,-0.99390924,0.534648,-1.0909554,0.6532071,-2.3327448,-0.52145916],[-1.8407224,-1.4516166,-0.5242798,-0.16527028,-0.27495337,-0.828356,1.8308109,0.30229092,0.0029909536,0.63370615,-1.1568123,1.4070832,3.5919077,-1.6436621,0.7294455,-0.11498895,-3.6592383,0.2872731,-1.2209938,0.846373,-0.18725829,0.2175256,-0.49011528,0.67513,3.3870685,0.47137582,1.5927097,0.06844024,-0.24461216,1.1673584,-1.052378,-0.16426557],[0.7095198,4.0883436,-0.7208321,0.3482088,-0.55152893,2.0659165,-0.28971213,1.1450249,1.1621845,0.4485017,-0.15015787,3.3407161,-0.1671823,-1.6612027,0.76599,-0.18865395,2.7832327,2.3387256,1.6907467,0.55116034,-2.181806,-0.5127777,0.5172455,-0.32157576,-1.457615,-1.406614,-0.2352457,0.20424247,0.022980906,1.8926935,1.2829719,-1.007051],[0.43048057,0.62226135,-0.92827684,-1.7156669,-0.8118586,-1.6074384,0.49258614,-1.3726854,-0.8459411,-0.9227513,0.10013622,1.2164955,0.50257796,-1.9119685,-0.88507044,-1.8948423,-0.70909226,1.0172815,-0.18161525,0.24848786,-0.7762752,1.781893,-0.92543334,-3.2227595,0.54470086,-0.15024158,-1.7610874,1.5088767,1.2776433,-0.38138187,1.0133414,0.5126554],[-0.8757794,-0.89691406,-2.7522447,1.2476244,-0.15405548,-0.0010151248,-0.44520476,-0.5618364,0.71821016,-0.85759366,1.2821966,1.4028472,3.9251041,1.4501762,-3.3185084,-3.1493526,-2.064223,1.1364964,-0.7480005,0.27650878,0.86580014,0.9651501,-2.2190738,0.04771874,0.98020566,0.64889914,-1.7110149,0.2168146,0.23029089,0.47753665,0.72975016,-3.0729697],[1.1679466,0.84254044,-0.7798223,1.791863,1.0929931,2.0487945,-0.37685165,-1.5124111,-0.42563158,-0.5803245,-1.8122303,-1.2107615,2.0913148,-0.9433089,0.37320167,-0.02150016,-0.17751096,0.46350682,1.0135976,1.7426245,-0.9180739,-1.7076061,-1.7036312,0.3921224,1.3182495,0.58015215,-0.08161951,-1.7899652,-0.14980166,-0.7865377,0.65150404,0.4388185],[0.05603478,0.17346135,0.4765747,1.3323466,1.4110603,0.36093372,1.734125,1.2934384,2.676373,0.8777068,1.1799065,1.64308,0.38512534,0.11675328,1.1135908,0.5624668,-1.6308864,0.026090156,-1.0502082,-0.34024873,-1.4434488,-0.60656816,0.23110095,-0.2502837,-0.7623878,-1.4757539,-0.17226845,-0.5751946,0.23399532,-2.922989,-1.866269,-2.072223],[-3.3865697,1.9987868,1.4158369,1.0382376,2.6704183,-1.4872088,-0.04483495,-2.4851844,0.7079969,0.1712434,-0.12341119,1.5147467,-0.37601888,0.33479047,-0.7887497,-1.4586157,-0.15229613,-0.44874328,-1.149185,-0.3964097,-1.322429,0.36973405,-0.89503425,1.2417059,0.5237751,-2.5999162,0.0192228,-1.8260452,1.922373,-0.47801405,-0.36099574,-1.384813],[1.1870673,0.25081375,0.554091,-0.28225365,0.31830624,-1.9630872,0.45511493,-0.5914359,2.4948084,-3.382314,0.5004007,0.8441211,2.5850132,-1.221858,-1.0265872,-3.6349936,0.829832,1.8141916,-1.0632406,-1.976331,-1.036515,-2.829257,0.8047089,-0.6501904,-2.4221148,0.1058664,-2.7184706,-0.3788945,0.30470636,-0.18143255,-3.2552986,-0.89584374],[1.70021,2.745056,1.4788306,0.5123115,-1.1331241,-0.47176293,-1.8350031,-0.11452632,-1.6345965,1.0992297,1.3014667,-0.20361954,0.5715275,1.546169,-0.8080904,3.337328,0.025964485,-1.3412806,-0.9380606,-0.18003957,1.5121582,-0.12590958,0.4242047,-1.651332,-0.8305136,-1.2480186,-2.1299458,1.0277249,-1.9743081,-0.8878372,-0.38671044,1.4488853],[0.64319956,0.45845234,2.2224023,-0.3788249,1.839771,-1.232804,1.658705,0.7722606,-0.4729142,-1.2113117,0.68802583,1.2839622,-0.30976298,1.124251,-1.0183175,1.2054148,-2.059689,2.0607452,-1.0659946,0.6598661,1.5007098,-0.16751856,1.7449634,-0.5768213,-2.7331085,0.6903021,1.987528,1.6814615,0.92044795,-3.355014,-1.2408988,-0.49537855]])

    Layers[1].biases = np.array([[0.2708075,1.3633009,-0.6788059,0.64230406,1.4404247,-0.5628973,-0.31271687,-1.403934,-1.7881683,2.0035686,-0.03831473,0.12493869,-1.0660391,-1.5292181,2.5626702,0.20415847,-1.7219824,3.9308476,0.4842021,-3.4923012,0.20436333,0.6815572,0.4664904,-0.37633833,1.7092578,2.0703485,0.40830034,0.8614022,-1.099176,0.92260635,0.28001642,0.7446052]])

    Layers[2].weights = np.array([[0.7403893,-1.731081,-0.900304,0.6769222,0.36638242,-0.45900616,-1.331959,1.4032387,-0.79792345,1.487177,0.9378137,1.7425747,2.0625906,-1.6392316,-2.4552577,-0.6297775,-2.1911867,0.08519156,-1.7530214,0.5110539,0.60316694,-0.4351918,-0.24163269,1.538988,-1.2146263,1.8483902,0.31305423,0.7730401,0.536965,3.399533,3.641669,-1.7013836],[0.17313701,1.5131868,1.2883891,-1.3412465,-0.8709728,-1.6359872,0.9923687,0.9424075,-0.85187286,1.8043792,0.7936126,1.0666327,0.88596576,0.7711009,-0.77032894,2.0256019,-0.7584575,-2.2752836,0.14667186,0.6512358,-4.634809,-2.904833,-0.7732893,0.20761627,-0.21147154,-1.0261419,-2.7622166,2.1982331,-0.8265014,-0.9018435,-0.40023258,0.6462429],[-0.2201694,-2.2152934,1.4774319,0.124498054,-0.8092486,0.8988879,-1.2514381,-0.6236076,0.32425457,0.46149215,-0.3108468,0.93902814,4.259953,-0.7743477,1.6432534,-1.9212697,-1.3710515,1.705625,-0.47069442,-0.5100388,-1.6694814,-1.8211472,0.9338571,1.1827232,1.1545024,-0.26353213,-0.50120986,1.2549138,-0.20566423,-1.5859519,0.31974506,1.8705921],[0.44940126,0.37569344,0.40396124,2.8849514,0.5389272,-0.23578016,-0.57336134,-0.24542561,3.0578313,-0.20963494,1.684887,-0.014216751,-1.543447,-1.8119284,-0.060510315,0.6526616,-0.7080254,0.05765826,-0.7403996,1.1799945,0.0077363625,-0.45124182,0.583119,-0.22592464,0.5398511,0.1572287,-0.68326175,0.9259225,-1.9985869,0.7787695,-1.1226203,-1.5777738],[0.47885498,-0.8556169,1.9859898,2.1989899,0.38359693,-0.43737143,0.92640334,0.74924016,0.55973226,0.4002244,1.1499535,0.47673252,2.2534516,-0.53680956,1.6622112,-0.6635385,-1.2154675,1.5656649,-0.15669377,0.3301082,0.20429587,1.4203423,-0.98180014,0.5330431,1.5475751,-1.862398,-0.24402113,0.9177623,-0.6783099,0.49882114,2.3259618,-0.009721413],[2.7072482,-0.6920532,0.97013885,-0.4354642,0.06385785,0.49829212,1.6205146,2.293169,-0.5694962,1.0782298,-0.845046,-0.024118572,-0.76166254,-0.32644764,-0.37851763,1.4799762,-1.4964981,0.93140066,-1.209307,2.223291,0.73181057,-2.1443336,-2.7758737,-1.8173465,1.7266556,1.5439824,-2.204329,-0.41817868,-0.37428173,-1.1826034,1.1971318,2.5309176],[-2.2659788,-1.1051264,0.9821244,0.5826971,-1.6822485,1.3927548,1.1674695,-0.48011765,-0.16837622,-1.2672769,1.357982,-1.4034655,2.7333813,-3.1450145,0.7486376,2.43079,-0.28787434,-0.76599437,1.8555619,0.5642626,-0.72037107,-1.3807614,0.32875982,-0.34409258,-0.37863395,1.7916971,1.495767,0.47699004,1.0117517,-0.33301127,1.549344,0.80207145],[4.033808,-2.1049328,-1.9154843,0.24291095,1.3271948,0.38747263,1.0836842,-0.1485952,-1.414571,-0.5672037,-1.2898219,0.5824378,-0.86572176,1.3312484,-0.42571422,-0.05824174,-0.07560652,1.0965179,0.99520147,0.881099,0.40822113,0.90968674,-0.14853115,0.43727976,-0.20930874,-1.1517605,-0.75897896,-0.98443687,3.5076594,-1.6143607,-1.2780348,-2.6717358],[-0.14106704,0.18626621,-1.2352473,-0.8505185,0.7894012,-2.288658,-0.92025524,-0.56126845,0.21942116,1.5072335,-0.7171053,0.537451,1.5389922,1.1451811,0.62455565,1.8415352,-0.3494933,1.3810507,-2.990608,1.5345403,-0.81191957,0.871247,-2.3613732,0.93956983,2.166511,0.78015023,0.04392803,0.8015306,0.9526799,-2.084743,0.60271937,-0.6533937],[1.014788,-0.86349356,0.2237416,-1.40965,-1.560181,-1.8463575,0.3874846,-0.18568629,-0.7018928,-3.46461,0.6190479,-2.7377243,-0.8078034,1.6440755,0.47026804,-0.823313,-0.45692798,-1.3288184,-1.0819037,1.6736012,0.6859088,0.24866456,-0.34683508,-1.0044518,0.6818335,1.3375835,-0.44484872,0.025976297,0.999216,1.9763399,-0.6040878,0.5605985],[0.055381574,-0.71978647,1.1249615,-0.89972997,-0.14888501,-0.2219441,-0.68868965,-0.9015849,-3.8524733,-2.6889508,-0.069123656,-0.6526066,-0.269896,-1.1102359,-0.2937543,0.38867486,1.1572999,-0.5029506,1.025804,1.3905637,1.2112312,0.62645185,-0.4772876,1.4699663,-2.152885,2.8082855,0.3797438,0.26626617,1.5434017,0.44637516,1.1084248,0.04945156],[-0.17510627,2.6999433,0.84243673,-1.3126016,-3.1374009,1.4048816,-1.2656487,0.33466563,1.9609463,-0.037114933,-0.5868358,-0.14309095,0.12967695,-1.6287203,1.414684,1.6479605,-0.57829654,-2.085054,-2.8265424,0.019117428,-1.545481,-1.4797482,-0.3365422,0.5471808,2.7125173,2.212589,-1.6484318,-1.5314599,1.5011595,-0.73547524,-1.0809125,-5.2631307],[-2.1090024,-0.19707881,2.292489,-1.1807171,-1.0757804,-1.2467446,2.206107,-0.5574698,-0.78335893,-0.3430601,-1.8121827,-0.89885145,1.3217812,-1.2485249,0.11101407,0.1665598,0.3507715,-0.90403986,0.43819988,0.50674665,-1.2371609,0.39275047,-1.7783265,-0.24938276,-1.1318392,0.28445882,2.375752,0.79875165,-0.19379123,0.8634514,1.9881072,1.021715],[0.110926256,0.38851264,-0.9414339,-1.0094279,-1.2800436,0.75249434,-0.9693605,-0.33219212,0.3104214,3.2047842,0.98898005,2.1236384,-0.6237643,0.062438924,-1.289819,-0.43525887,0.20069784,-1.2232945,0.69219196,-1.055021,1.0426409,-1.5756302,0.10240961,0.011874236,0.8334109,1.2787819,-1.1140931,0.16366062,-1.6497053,1.3834127,2.301136,-2.632293],[2.2252636,0.36181724,-0.81976783,1.0670967,-0.27410793,-0.14398988,-1.5848663,-0.3511829,-0.78811246,-1.6499015,-1.5844638,0.7519106,0.9851177,-1.2452135,1.0033585,-2.409255,-1.7750386,-2.7663934,-1.9984767,0.13495265,1.4049317,1.4104364,-0.099504255,-2.410183,-0.2450561,-3.5823796,2.9428365,1.6896003,-0.23097439,0.49037752,-0.024933862,-0.5417437],[0.38436973,-0.9117471,0.696597,0.64241457,-0.74356085,-0.1963654,1.6261973,1.4244281,0.1417289,1.7359033,1.1393265,0.67890376,-0.6657858,1.9534485,1.2507006,0.27362847,1.5866382,-1.2873131,-0.87601566,0.6032264,-2.6038923,-0.54472804,0.06378183,1.9246631,1.3512925,-2.311942,0.15876502,-0.13356699,1.5325887,-0.3994693,-3.4984586,-0.94451123],[-0.024580427,-0.55112976,0.3555754,-1.2977717,0.61684966,-0.8722464,-0.9319496,-1.4575725,-0.031900607,0.99995947,-0.3000894,0.7950467,-0.29129988,1.178447,0.83256495,-0.90468466,1.2561158,-0.26989403,-0.47514078,-0.31005988,-0.5244544,0.3613683,-2.2559896,-0.70793724,0.49016637,-0.3282718,0.89586216,0.7632425,0.63816035,-0.8531141,0.23067594,-0.07339434],[-2.059921,2.515438,0.23589785,1.3790594,1.0082767,0.087217234,0.25929785,0.63679534,-1.7685432,-0.22942296,1.1495786,1.0705439,4.3898873,0.86989117,0.7952148,1.9336339,-1.4222472,-1.4893324,0.45310524,-1.1077635,1.4864316,-0.9761659,0.77149856,0.2578419,1.383451,1.9811497,0.50865525,0.038119584,1.8932326,0.92443275,-1.4365584,-0.46921638],[1.9472749,2.555995,1.1637967,-1.0946255,2.334047,-0.71724015,0.20179142,0.044193633,0.54390806,1.8146654,0.1010425,1.8123337,0.12841648,2.0377805,-0.13896945,-1.24832,0.53418636,0.9594842,0.9127628,1.3662943,3.123836,0.12677094,1.5467879,0.1100876,-0.12778002,0.3658771,-0.13001332,1.9173332,0.9657813,-1.2029219,-0.33316538,-1.8698956],[1.3461772,-1.6553375,1.121445,0.22805011,-2.8394003,0.97876555,0.07164231,1.8217782,-1.101732,-0.3105158,0.27299717,0.40887192,1.1474435,-0.63336354,1.6177742,-0.33993122,-2.6629152,0.2947029,-1.2646639,-0.23472045,-0.09794611,0.44352335,-0.4880174,0.77127534,-0.44786182,0.81508654,-0.16518614,0.7590874,-0.87486094,1.2219921,-0.8836288,-1.393781],[2.9446044,-0.6523478,0.9196159,0.46339437,0.6806165,0.21335189,-0.08022621,0.4479586,-0.4752246,3.698023,-0.6225385,1.8576002,0.45250633,0.57937694,0.47669312,0.14131977,0.6289026,0.29886794,0.014695182,0.7860974,1.6485782,-0.29918727,2.0148935,2.1879408,-2.0680275,-1.3103518,-1.2591949,-0.28829336,0.53446007,1.0802346,-0.551179,-2.3183935],[-0.028878205,1.1019728,1.2735258,0.60450006,0.1309169,1.9243959,-1.712992,2.000193,0.40771157,-0.69816476,0.97750044,-0.22466631,0.4469991,1.2688187,0.8165657,1.2668767,2.9986691,0.104831554,-1.1114428,-1.0354387,-1.4138545,0.12987967,1.2138833,0.7391826,-1.0622494,-0.9285006,-1.0638219,1.2607211,-1.2983016,0.9943837,3.0286179,1.3378533],[0.93086284,1.1558508,-2.1094007,0.7690363,-2.1688704,0.35471576,-0.8279201,0.5620513,1.1426779,-0.61798024,-0.8753356,-1.6175181,-1.2720984,-1.5978192,-1.7182204,0.8839359,0.65537196,0.70739925,-0.28068876,0.44229537,0.7737705,-0.3350361,0.09511615,1.2339134,1.6460018,1.353941,-0.44814765,0.31168982,-1.0237175,-0.2553841,0.98703194,2.174262],[-0.7705425,0.22726619,-0.8443927,2.4762223,-0.8289995,0.63238436,-0.20249346,-0.52838576,3.4498203,0.27242312,-0.34754077,-1.0369607,-0.3375846,0.99265474,-2.2665997,0.54635215,-0.42443275,0.11868696,-3.3125691,-2.060123,-1.9209576,-1.1268041,0.07268078,0.8484898,0.07088609,-2.2145805,2.476951,-1.3549192,0.98723704,0.8585673,0.9074497,0.8944819],[-1.0400362,-0.9413238,0.119167864,1.1437224,2.0423946,-0.30948696,-0.21931769,-1.28457,0.14078237,0.72188896,-0.054391295,1.1568456,0.61674994,0.21110272,-0.11031439,1.3901494,-1.2782886,-2.1782343,-1.0067096,1.22743,0.19755532,-2.117383,-0.22387266,2.933645,-0.19594063,0.8840983,-1.2452998,-1.2655058,0.17416972,-0.8721642,0.27478904,0.46667004],[-1.2741783,-0.777248,2.119398,-0.9497066,-0.18332331,0.30632472,0.85660803,0.48942584,4.5197268,-1.7235833,2.2386382,-0.8857031,-1.397132,2.2441332,0.9754168,-0.6771722,-1.5366309,0.64031273,-0.08901908,-0.6034259,0.023345808,-1.1115987,-1.2738543,-1.8207194,-2.276893,-1.3426347,-1.8510079,-2.9233837,-0.86384916,-1.6496855,-0.9881727,0.33573112],[-2.0258403,-2.1337087,-0.9776587,0.23409642,-0.09476048,1.341489,-1.453154,-1.172206,1.1305082,1.1114513,-1.5175148,-0.21908475,0.26182416,-0.12558787,1.3987244,-0.29368538,1.5251722,-1.6519972,0.60603905,-1.2952557,0.44662195,-0.49152565,-1.611563,-0.8917262,-1.3057586,-1.3425682,1.6784291,-2.0377529,-1.839538,0.34740835,-2.0430133,1.4366509],[0.43025768,-2.4337945,-0.08046096,-2.1055722,0.45593634,-1.5068698,-1.2793843,-2.058608,-1.5132688,0.38705188,0.73283356,0.47963357,0.065260746,-0.03328042,0.7424128,-1.4016641,-1.1867567,0.2647604,0.55580896,0.78209645,-0.82347906,0.4712528,0.7492949,0.51939094,0.841408,-2.015507,-0.7360191,-0.28086945,-0.82721984,-1.4680716,-0.73521805,-1.7784457],[0.4877637,1.3271159,-0.7803217,-0.5704034,-0.15305743,1.7603618,1.61154,1.4861149,-0.9557311,0.8262892,0.27760407,2.4945827,-0.945189,-1.1176344,0.614913,-2.5608175,-2.4319625,-0.90185493,0.20657215,-0.31636512,-0.5552364,0.818387,4.5567026,1.4815941,1.3038847,-0.90085167,-0.026388753,-0.10717202,-0.86725676,-2.3408372,0.30452082,1.6622798],[-0.028489018,-0.5672384,0.56542146,0.21290067,0.06409613,-2.7987921,-0.23631895,-2.0316782,0.47996196,1.6243765,-0.057648364,-0.29284367,0.057547886,0.034799397,-1.5751843,-1.8864481,1.7843771,-1.6479018,2.004565,-0.5056302,0.01926442,-0.20030175,0.13191098,0.22981367,-0.11707678,-1.3999103,-0.41477537,0.74237174,2.5629654,-2.507699,0.6263688,-1.0126104],[-0.7873913,0.78091156,-0.027701667,0.047643755,0.24700448,-0.8335534,-2.973786,0.50506854,-0.71503854,0.8594311,3.7154255,-1.7509675,-0.30546364,-0.87728584,-1.6453942,-1.402295,-0.05286518,-1.4673381,-0.6755255,-1.0915529,1.6949356,2.142076,-1.9259294,1.5845116,0.89460206,0.41065988,-0.9154831,-2.5874434,-0.4915282,-0.10743229,-0.15307076,1.5664824],[3.1732626,1.9421086,0.3308962,2.6133943,1.6686753,0.95182604,-0.2582018,-0.44922552,-4.027468,-0.57501686,-2.0474234,-2.3838491,2.0319333,-0.7464437,-2.6532266,-0.46310502,-0.41094297,-0.47350472,-0.7897812,-0.87633145,0.3075213,0.47354284,1.6316917,-0.8793198,-0.43434972,0.5829564,1.507128,2.1920733,1.0117716,-1.170761,-0.823992,1.2728972]])

    Layers[2].biases = np.array([[-0.003350371,0.3255505,-0.9724754,-0.29667547,-3.3101008,-0.3186052,-0.16938496,0.55799127,4.084786,1.9722279,-0.30342525,0.2885181,3.464895,-1.169812,0.4960003,0.57658726,-0.8401427,0.36762038,-1.6270117,0.35097754,0.08658477,-1.6234615,-0.7742958,-1.4564141,0.9893768,0.89084196,2.2184184,1.4569288,-2.4310877,-0.7748928,-0.13844223,-1.4885626]])

    Layers[3].weights = np.array([[-0.9788215,0.92459536,0.7801037,1.0740824,1.1393698,-1.8069904,0.87341934,0.1460988,-1.7741576,1.2288574,-0.771621,1.7036223,1.3970637,-4.0507565,-1.1932176,-1.8868415],[-0.4983696,1.6579512,-0.024860606,-0.059649196,-0.98344684,-0.5101042,1.2354457,0.035843365,-1.0008645,2.3634973,1.0867972,0.9095778,-1.4781824,-1.0859244,-2.8953114,0.18873191],[1.4300165,-0.62011087,0.8136088,-1.9008932,-0.7696013,-2.6181107,-1.6041263,0.5728324,-0.23264986,-0.6578472,-0.45180824,0.11689711,0.3692765,-0.62044406,-0.9334588,-1.7030761],[-1.7043542,0.56581306,-0.9318011,-0.56420547,-3.4294696,2.6812894,0.20415865,0.6949771,0.9531446,3.450768,2.4288719,0.16183637,0.723177,0.37888542,0.5665334,-0.68155885],[-0.17462233,1.4496688,0.053606175,-0.35427395,0.8213615,0.12924907,-1.1784502,0.6634803,2.751257,0.011747293,-2.644609,2.0947852,-0.60840726,1.3742925,-1.3298483,0.5591434],[0.22710623,1.3331463,3.5378237,-0.640283,-0.96286845,-2.0319486,0.94162995,-1.68136,-1.7880065,-0.7024136,-0.7851126,-0.4556664,0.53822196,-1.5540204,-0.49507415,0.26717538],[3.8406901,-3.2109902,-1.0485818,0.82488155,1.1800256,1.8548546,-3.1188426,-0.033625107,2.3471212,-2.724245,-0.78264296,1.1878238,-0.09814701,0.675673,2.7347567,0.50010794],[2.4782531,3.0229964,-1.951696,0.47458267,-0.28677666,2.0677927,-0.6810335,-3.70148,-1.5547497,1.4502918,-0.69649965,1.703807,1.0441917,1.6633341,0.2894176,-1.5880944],[-2.0321984,3.8140755,1.061844,1.3685213,0.6784728,-0.6627308,-0.8317019,1.2291898,0.69976324,-0.26284528,-1.4948299,0.80037606,0.3243428,-2.822899,-1.4574716,-0.8474928],[1.534816,0.46544802,1.2963712,-1.6554666,1.2363485,3.2985168,0.26957488,0.10526043,0.31218424,0.043585148,0.9079001,-0.193374,0.663599,0.99392,-0.899199,1.2153221],[-0.23531663,0.55618787,-0.043625195,-0.27220803,-1.2411095,2.4880955,1.6983414,-2.2609627,-2.1225686,-0.78689754,1.198861,-0.4952411,-0.3541152,2.0651824,0.48208782,-0.5919423],[1.8069795,-0.69951105,-1.0283977,0.27475497,0.28190726,-1.0783211,-1.1490234,-0.62708384,-1.057397,-0.28538266,-3.428288,0.9340241,-0.13175024,1.1089131,-0.4096595,-0.6212623],[2.7589946,-1.9324198,-0.77973676,-2.368827,-0.32408848,-1.524275,-0.1691575,0.65049857,0.6768371,-0.28503045,-0.03438789,-1.0978281,0.1364142,-0.6195191,-0.61965275,1.6776502],[0.25581363,0.20661722,0.49045846,-2.436212,-0.66674125,-0.06338537,-0.477076,-0.101447195,-0.13690934,0.37200585,-0.93190116,0.55296665,-0.94244665,-1.8869929,1.5780094,-2.3134923],[2.038189,-1.2297962,-2.26964,-0.991097,-2.5059323,-2.9754906,-1.9925467,0.93776953,-2.0081358,-1.5883185,-0.9204822,-1.347184,-2.3783393,-0.33205187,1.124534,-0.28130123],[-0.17102456,-1.4041958,1.8192112,3.3433492,-3.5492632,1.083707,-0.5764326,-2.541567,-1.2547668,-0.36298826,-0.41477954,-1.6841043,3.07414,-0.34633768,-1.4430656,-0.1591752],[0.3946024,2.7312863,-0.23458956,1.8724952,-0.47865394,0.1884825,1.9998387,0.25539428,-0.15456747,0.6224401,2.3034844,1.5487577,-1.4003559,1.4802836,0.46266067,-0.4539066],[-2.0307786,0.62994605,-0.305237,-1.690222,-2.199381,0.6044989,-1.5504134,-0.57250154,1.84088,2.0782902,-1.5288596,0.24050209,-0.76921827,2.7548327,0.85714126,1.8112769],[0.41401374,2.1641963,1.4922818,1.0880711,1.3409231,0.9073255,1.4091406,-2.0689228,-1.4725914,1.2595673,-0.9127253,0.3593148,-1.2805171,1.1895355,-1.2275276,-2.7080169],[-0.602381,0.77669066,-0.91045237,0.6765315,1.5198331,0.98584676,-0.6646814,-3.0087254,1.3465527,-1.70341,0.2886211,-1.6427763,0.65770984,1.7254093,-1.2858292,1.6991309],[0.7220694,1.2202528,0.10777368,1.9406655,-1.220789,1.2494162,1.8096598,-1.8023076,1.2890683,-0.66988105,0.8938965,0.11598401,1.8390386,-0.87448055,-0.9062001,1.3228153],[-0.4695375,0.61746615,0.86073184,1.162937,2.2997434,-0.40255415,1.4652543,0.12586245,0.71676475,-0.2957893,0.5577596,-0.3819778,1.0152285,0.21837883,1.0579342,-1.3972099],[-1.8777071,0.2155044,-0.2284076,0.19383341,1.6172242,0.1602837,0.35020092,0.36284593,1.9580754,-0.494408,-1.7881852,0.29888794,-1.2268203,0.4650345,-0.93503106,0.50519854],[-2.2816277,-2.3652174,0.7032944,0.97289485,1.1262137,-0.83517325,0.17802557,0.4014706,-0.46639428,-0.029000035,0.92229146,0.21539159,1.6779217,-0.090065986,1.0800933,0.52010083],[3.3941636,-1.5397788,-1.5041008,0.6887333,-0.88837296,2.8354077,0.15820926,0.03745359,0.9928048,-2.1347356,0.039141133,1.4038074,1.6185874,-2.4398987,0.6491384,-0.2651996],[1.9864001,-0.52713925,1.1952665,1.1038971,0.1236031,-0.9605863311166,-0.82277703,0.2955112,1.3844801,-2.727543,-1.8007091,0.6908066,2.390155,0.016826525,0.20523676],[2.2651558,-1.4050428,3.4229817,-0.027962912,0.5889664,0.110130936,0.21203282,0.58769894,0.35887533,0.5469829,-0.05331134,-1.5222335,1.1779281,1.2774315,1.2428426,3.0681787],[-0.14355919,-1.2935635,-0.42545617,-0.6903682,0.2665867,1.6771916,-2.9186301,1.4051664,0.8108244,0.5615169,0.3715344,-0.96399593,1.6889501,3.129131,-1.8603277,1.7551509]])

    Layers[3].biases = np.array([[8.69753,6.765699,0.5852794,-0.41412368,-0.6293697,-0.724455,-1.7538221,-0.03453309,-0.42992353,0.5378669,-0.63958055,-0.7490098,0.06419784,-0.90417445,-0.021713246,-0.83141965]])
    
    
    for i in range(0,len(NeuronNum)):
        if(i==0):
            Layers[i].forward(X)
        else:
            Layers[i].forward(Activations[i-1].output)
        Activations[i].forward(Layers[i].output)



    output = np.argmax(Activations[len(Activations)-1].output,axis=1)

    i = 0
    right = 0
    wrong = 0
    for j in output:
        if j == y[i]:
            right +=1
        else:
            wrong +=1
        i+=1
    print(right)
    print(wrong)
    print("accuracy is " + str(right/i))

else:

    Loss_function = Loss_CategoricalCrossentropy()

    lowest_loss = 999999999
    LastLoss = 0
    LastLossChange = 1
    MaxLossChange = 0

    BestWeights = []
    BestBiases = []

    for w in Layers:
        BestWeights.append(w.weights.copy())
        BestBiases.append(w.biases.copy())


    for iteration in range (500000):

        for i in range(0,len(NeuronNum)):
            #if(MaxLossChange<)
            if(i==0):
                
                Layers[i].weights +=  np.random.randn(InputNum,NeuronNum[0])*0.05 #* (LastLossChange)*1000
                Layers[i].biases +=  np.random.randn(1,NeuronNum[0])*0.05 #* (LastLossChange)*1000
            else:
                Layers[i].weights +=  np.random.randn(NeuronNum[i-1],NeuronNum[i])*0.05 #* (LastLossChange)*1000
                Layers[i].biases +=  np.random.randn(1,NeuronNum[i])*0.05 #* (LastLossChange)*1000

        for i in range(0,len(NeuronNum)):
            if(i==0):
                
                Layers[i].forward(X)
                Activations[i].forward(Layers[i].output)
                tmp = RandArr(NeuronNum[i],0.05)
                #print(tmp)
                Activations[i].output = Activations[i].output * tmp
            else:
                Layers[i].forward(Activations[i-1].output)
                Activations[i].forward(Layers[i].output)
                tmp = RandArr(NeuronNum[i],0.05)
                Activations[i].output = Activations[i].output * tmp


        loss = Loss_function.calculate(Activations[-1].output,y)
        

        predictions = np.argmax(Activations[-1].output,axis = 1)
        accuracy = np.mean(predictions==y)

        if(loss < lowest_loss):
            print("new lowest loss ",loss, " accuracy ",accuracy)
            
            LastLossChange = abs(LastLoss - loss)
            #print(LastLossChange)
            LastLoss = loss
            i = 0
            for w in Layers:
                BestWeights[i] = w.weights.copy()
                BestBiases[i] = w.biases.copy()
                i+=1

            lowest_loss = loss
        else:
            i = 0
            for w in Layers:
                Layers[i].weights = BestWeights[i].copy()
                Layers[i].biases = BestBiases[i].copy()
                i+=1


    i = 0
    for t in BestWeights:
        out = f"Layers[{i}].weights = np.array(["
        for k in BestWeights[i]:
            tmp = "["
            for l in k:
                tmp += str(l) + ","
            tmp = tmp[:-1]
            tmp += "],"
            out += tmp
        out = out[:-1]
        out +="])"
        print(out)
        print()
    
        out = f"Layers[{i}].biases = np.array(["
        for k in BestBiases[i]:
            tmp = "["
            for l in k:
                tmp += str(l) + ","
            tmp = tmp[:-1]
            tmp += "],"
            out += tmp
        out = out[:-1]
        out +="])"
        print(out)
        print()
        i+=1


