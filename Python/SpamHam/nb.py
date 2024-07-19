# This skeleton code simply classifies every input as ham
#
# Here you can see there is a parameter k that is unused, the
# point is to show you how you could set up your own. You might
# also pass in extra data via a train method (also does nothing
# here). Modify this code as much as you like so long as the 
# accuracy test in the cell below runs.

class SpamClassifier:
    def __init__(self, k):
        self.k = k
        
    def train(self):
        pass
    
    
    def predict(self, new_data):
        log_class_conditional_likelihoods = np.array([[-3.83854747, -4.40050244, -3.37557787, -7.81822913, -3.56973388, -4.35249322,
  -5.94642695, -4.79780424, -4.52239226, -3.88640349, -4.87379015, -2.9354272,
  -4.11692715, -5.1791718,  -6.02646966, -4.40050244, -4.33698904, -4.11692715,
  -2.67073465, -5.94642695, -3.16426878, -6.71961684, -5.67816296, -5.94642695,
  -3.06463893, -3.36388183, -3.41150988, -3.94702811, -4.11692715, -4.0005168,
  -4.38424192, -4.6401753,  -4.2918686,  -4.61955601, -3.95749941, -3.87664732,
  -3.34089231,-6.02646966, -4.26288106, -4.40050244, -5.1791718,  -4.18064297,
  -4.33698904, -4.38424192, -3.31287927, -3.85741596, -6.02646966, -4.90045839,
  -3.78398849, -2.68243069, -4.01156664, -3.32959276, -4.35249322, -4.54108439],
 [-3.54302758, -3.73766962, -3.08672279, -6.58755001, -2.9961259,  -3.4520558,
  -3.47086513, -3.59181774, -3.77986997, -3.31852441, -3.77986997, -3.04039872,
  -3.70514643, -4.64163987, -4.52612698, -3.13529746, -3.39766173, -3.62080528,
  -2.68125768, -4.05612335, -2.78088753, -5.58902118, -3.68927308, -3.48360416,
  -6.04855351, -6.33623559, -7.84031298, -6.74170069, -6.92402225, -7.1471658,
  -7.84031298, -8.53346016, -5.96851081, -8.53346016, -5.76087144, -5.20125565,
  -5.35540633, -6.58755001, -5.70024682, -4.56316825, -8.53346016, -7.43484788,
  -5.31458434, -6.92402225, -3.86063133, -5.96851081, -6.74170069, -7.1471658,
  -4.37457708, -3.02407183, -4.94994123, -2.73134179, -3.03220195, -3.86063133]])
    
        log_class_priors = np.array( [-0.48939034, -0.94933059]) 
        class_predictions = np.zeros(len(new_data),dtype=float)
        i = 0
        for j in new_data:
            z = 0
            tmp0 = log_class_priors[0]
            tmp1 = log_class_priors[1]
            for k in j:
                #if(k == 1):
                tmp1 += k*log_class_conditional_likelihoods[1][z]
                #else:
                tmp0 += k*log_class_conditional_likelihoods[0][z]
                z+=1
            if(tmp0>tmp1):
                class_predictions[i] = 0
            else:
                class_predictions[i] = 1
            i+=1
        
    
        return class_predictions
    

def create_classifier():
    classifier = SpamClassifier(k=1)
    classifier.train()
    return classifier

classifier = create_classifier()