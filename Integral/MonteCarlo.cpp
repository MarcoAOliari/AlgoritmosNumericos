#include <cstdio>
#include <random>
#include <math.h>
#define PI 4*atan(1)

double funcao(double r, double theta){
    return 2*(((4-pow(r, 2))*sqrt(3)*pow(r, 2)));
}

int main(){
    double lInferiorR = 0, lSuperiorR = 2, lInferiorTheta = 0, lSuperiorTheta = 2*PI, soma = 0;
    int n = 40000000;

    for(int i=0; i<n; i++){
        double aleatorioR = (double)(rand())/(double)(RAND_MAX)*(lSuperiorR-lInferiorR) + lInferiorR;
        double aleatorioTheta = (double)(rand())/(double)(RAND_MAX)*(lSuperiorTheta-lInferiorTheta) + lInferiorTheta;

        soma += funcao(aleatorioR, aleatorioTheta);
    }

    printf("%f", (lSuperiorTheta-lInferiorTheta)*(lSuperiorR - lInferiorR)*soma/n);
}