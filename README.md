# Simple-Logistic-Regression
  * This model is made without using any built-in functions
  * First I have calcualted hypothesis by using sigmoid function 
        
        
        Z = w(transpose).X + b
        A = sigmoid(Z)
  * Then for backward propogation I have calculated
        
        dZ = A-Y
        dB = 1/m*np.sum(dZ)
        dW = 1/m*(X.transpose(dZ)
  * Now updating the weights 
        
        w := w - learning_rate * dW
        b := b - learning_rate * dB
        
### After taking learning rate as 0.01 and 15000 iterations:

        Cost Function at iteration 15900: 0.631076901818312
        Cost Function at iteration 15901: 0.631076901818312
        Cost Function at iteration 15902: 0.6310769018183119
        Cost Function at iteration 15903: 0.631076901818312
        Cost Function at iteration 15904: 0.6310769018183118
        Cost Function at iteration 15905: 0.6310769018183119
        Cost Function at iteration 15906: 0.631076901818312
        Cost Function at iteration 15907: 0.6310769018183118
        Cost Function at iteration 15908: 0.6310769018183119
        Cost Function at iteration 15909: 0.6310769018183118
        Cost Function at iteration 15910: 0.6310769018183119
        Cost Function at iteration 15911: 0.6310769018183119
        Cost Function at iteration 15912: 0.6310769018183119
        Cost Function at iteration 15913: 0.6310769018183118
        Cost Function at iteration 15914: 0.6310769018183118
        Cost Function at iteration 15915: 0.6310769018183118
        Cost Function at iteration 15916: 0.6310769018183118
        Cost Function at iteration 15917: 0.6310769018183119
        Cost Function at iteration 15918: 0.6310769018183119
        Cost Function at iteration 15919: 0.6310769018183119
        Cost Function at iteration 15920: 0.6310769018183119
        Cost Function at iteration 15921: 0.631076901818312
        Cost Function at iteration 15922: 0.631076901818312
        Cost Function at iteration 15923: 0.631076901818312
        Cost Function at iteration 15924: 0.6310769018183118
        Cost Function at iteration 15925: 0.6310769018183119
        Cost Function at iteration 15926: 0.6310769018183119
        Cost Function at iteration 15927: 0.6310769018183119
        Cost Function at iteration 15928: 0.631076901818312
        Cost Function at iteration 15929: 0.631076901818312
        Cost Function at iteration 15930: 0.631076901818312
        Cost Function at iteration 15931: 0.6310769018183119
        Cost Function at iteration 15932: 0.631076901818312
        Cost Function at iteration 15933: 0.6310769018183119
        Cost Function at iteration 15934: 0.631076901818312
        Cost Function at iteration 15935: 0.6310769018183119
        Cost Function at iteration 15936: 0.6310769018183119
        Cost Function at iteration 15937: 0.6310769018183119
        Cost Function at iteration 15938: 0.6310769018183119
        Cost Function at iteration 15939: 0.6310769018183118
        Cost Function at iteration 15940: 0.6310769018183118
        Cost Function at iteration 15941: 0.6310769018183119
        Cost Function at iteration 15942: 0.6310769018183119
        Cost Function at iteration 15943: 0.6310769018183119
        Cost Function at iteration 15944: 0.6310769018183119
        Cost Function at iteration 15945: 0.6310769018183119
        Cost Function at iteration 15946: 0.631076901818312
        Cost Function at iteration 15947: 0.6310769018183118
        Cost Function at iteration 15948: 0.6310769018183118
        Cost Function at iteration 15949: 0.631076901818312
        Cost Function at iteration 15950: 0.6310769018183119
        Cost Function at iteration 15951: 0.6310769018183119
        Cost Function at iteration 15952: 0.6310769018183119
        Cost Function at iteration 15953: 0.6310769018183119
        Cost Function at iteration 15954: 0.6310769018183119
        Cost Function at iteration 15955: 0.6310769018183119
        Cost Function at iteration 15956: 0.6310769018183119
        Cost Function at iteration 15957: 0.6310769018183119
        Cost Function at iteration 15958: 0.6310769018183119
        Cost Function at iteration 15959: 0.6310769018183119
        Cost Function at iteration 15960: 0.6310769018183119
        Cost Function at iteration 15961: 0.6310769018183119
        Cost Function at iteration 15962: 0.6310769018183119
        Cost Function at iteration 15963: 0.6310769018183119
        Cost Function at iteration 15964: 0.6310769018183119
        Cost Function at iteration 15965: 0.6310769018183119
        Cost Function at iteration 15966: 0.631076901818312
        Cost Function at iteration 15967: 0.631076901818312
        Cost Function at iteration 15968: 0.6310769018183119
        Cost Function at iteration 15969: 0.6310769018183119
        Cost Function at iteration 15970: 0.631076901818312
        Cost Function at iteration 15971: 0.6310769018183119
        Cost Function at iteration 15972: 0.6310769018183119
        Cost Function at iteration 15973: 0.631076901818312
        Cost Function at iteration 15974: 0.6310769018183119
        Cost Function at iteration 15975: 0.631076901818312
        Cost Function at iteration 15976: 0.6310769018183119
        Cost Function at iteration 15977: 0.6310769018183119
        Cost Function at iteration 15978: 0.6310769018183119
        Cost Function at iteration 15979: 0.6310769018183119
        Cost Function at iteration 15980: 0.631076901818312
        Cost Function at iteration 15981: 0.631076901818312
        Cost Function at iteration 15982: 0.6310769018183119
        Cost Function at iteration 15983: 0.631076901818312
        Cost Function at iteration 15984: 0.6310769018183119
        Cost Function at iteration 15985: 0.631076901818312
        Cost Function at iteration 15986: 0.6310769018183118
        Cost Function at iteration 15987: 0.631076901818312
        Cost Function at iteration 15988: 0.6310769018183119
        Cost Function at iteration 15989: 0.6310769018183118
        Cost Function at iteration 15990: 0.6310769018183119
        Cost Function at iteration 15991: 0.6310769018183119
        Cost Function at iteration 15992: 0.6310769018183118
        Cost Function at iteration 15993: 0.6310769018183119
        Cost Function at iteration 15994: 0.6310769018183119
        Cost Function at iteration 15995: 0.6310769018183119
        Cost Function at iteration 15996: 0.6310769018183119
        Cost Function at iteration 15997: 0.6310769018183119
        Cost Function at iteration 15998: 0.6310769018183118
        Cost Function at iteration 15999: 0.6310769018183119
        ------------------------------------------------
         Number of test sets : 100
         Number of correct prediction : 80
         Accuracy : 80.0%
         
